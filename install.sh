#!/bin/bash
# ============================================================
# Pironman 5 Installer
# Supports: Pironman 5, Pironman 5 Mini, Pironman 5 Max, Pironman 5 Pro Max, Pironman 5 NAS, Pironman 5 UPS
#
# Usage:
#   curl -sSL https://raw.githubusercontent.com/sunfounder/pironman5/1.3.x/install.sh | sudo bash
#   curl -sSL https://raw.githubusercontent.com/sunfounder/pironman5/1.3.x/install.sh | sudo bash -s -- --pipower5
#   curl -sSL https://raw.githubusercontent.com/sunfounder/pironman5/1.3.x/install.sh | sudo bash -s -- --variant base --pipower5 --container
#   # China mirror (Gitee):
#   curl -sSL https://gitee.com/sunfounder/pironman5/raw/1.3.x/install.sh | sudo bash -s -- --cn
#   curl -sSL https://gitee.com/sunfounder/pironman5/raw/1.3.x/install.sh | sudo bash -s -- --cn --variant base
# (Safe to run directly — interactive prompts read from /dev/tty)
# ============================================================

# Pre-scan args for --cn (mirror) before downloading the framework,
# since the framework URL itself needs to use the correct source.
USE_CN_MIRROR=false
for _arg in "$@"; do
    if [ "$_arg" = "--cn" ]; then
        USE_CN_MIRROR=true
        break
    fi
done

# Source Installer framework — use local path when available (e.g. Docker build),
# otherwise curl from GitHub (or Gitee mirror with --cn).
FRAMEWORK_DIR="/tmp/installer-tools"
if [ -d "$FRAMEWORK_DIR" ]; then
    source "$FRAMEWORK_DIR/installer_1.1.0.sh"
else
    if [ "$USE_CN_MIRROR" = true ]; then
        INSTALLER_URL="https://gitee.com/sunfounder/sunfounder-installer-scripts/raw/main/tools/installer_1.1.0.sh"
    else
        INSTALLER_URL="https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/refs/heads/main/tools/installer_1.1.0.sh"
    fi
    curl -fsSL "$INSTALLER_URL?$(date +%s)" -o installer.sh
    if [ $? -ne 0 ]; then
        echo "Network error, please check your internet connection."
        exit 1
    fi
    source installer.sh
    rm installer.sh
fi

installer_check_root_privileges

# ============================================================
# Banner
# ============================================================
echo -e "\033[34m"
cat <<BANNER

██████╗ ██╗██████╗  ██████╗ ███╗   ██╗███╗   ███╗ █████╗ ███╗   ██╗    ███████╗
██╔══██╗██║██╔══██╗██╔═══██╗████╗  ██║████╗ ████║██╔══██╗████╗  ██║    ██╔════╝
██████╔╝██║██████╔╝██║   ██║██╔██╗ ██║██╔████╔██║███████║██╔██╗ ██║    ███████╗
██╔═══╝ ██║██╔══██╗██║   ██║██║╚██╗██║██║╚██╔╝██║██╔══██║██║╚██╗██║    ╚════██║
██║     ██║██║  ██║╚██████╔╝██║ ╚████║██║ ╚═╝ ██║██║  ██║██║ ╚████║    ███████║
╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝    ╚══════╝

Pironman 5 Installer
BANNER
echo -e "\033[0m"

# ============================================================
# Parse CLI Arguments
# ============================================================
INSTALL_PIPOWER5=false
IS_CONTAINER=false
IS_PLAIN_TEXT=false
ARG_VARIANT=""
INSTALL_PLUGIN=""
NO_AUTOLOGIN=false
PIPOWER5_BRANCH_ARG=""
BRANCH_OVERRIDE=""
# USE_CN_MIRROR already pre-scanned above (before framework download)
while [ $# -gt 0 ]; do
    case "$1" in
        --pipower5) INSTALL_PIPOWER5=true; INSTALL_PLUGIN="pipower5"; SKIP_MENU=false ;;
        --container) IS_CONTAINER=true; IS_PLAIN_TEXT=true ;;
        --plain-text) IS_PLAIN_TEXT=true ;;
        --no-autologin) NO_AUTOLOGIN=true ;;
        --cn) USE_CN_MIRROR=true ;;
        --variant=*) ARG_VARIANT="${1#*=}" ;;
        --variant) shift; ARG_VARIANT="$1" ;;
        --plugin) shift; INSTALL_PLUGIN="$1"; INSTALL_PIPOWER5=true; INSTALL_PLUGIN="pipower5" ;;
        --pipower5-branch) shift; PIPOWER5_BRANCH_ARG="$1" ;;
        --pironman5-branch) shift; BRANCH_OVERRIDE="$1" ;;
    esac
    shift
done

# --plugin mode: skip variant menu, detect from existing install
# --pipower5 flag also sets INSTALL_PLUGIN but should still show menu
_PLUGIN_ONLY=false
if [ -n "$INSTALL_PLUGIN" ] && [ "$SKIP_MENU" != "false" ]; then
    if [ -z "$ARG_VARIANT" ]; then
        _PLUGIN_ONLY=true
        if [ -f /opt/pironman5/.variant ]; then
            ARG_VARIANT=$(cat /opt/pironman5/.variant)
        else
            ARG_VARIANT="base"
        fi
    fi
fi

# Validate --variant
if [ -n "$ARG_VARIANT" ]; then
    case "$ARG_VARIANT" in
        base|mini|max|pro-max|pro_max)
            # Normalize pro-max to pro_max for internal key
            [ "$ARG_VARIANT" = "pro-max" ] && ARG_VARIANT="pro_max" ;;
        *) echo "Invalid variant: $ARG_VARIANT. Valid: base, mini, max, pro-max"; exit 1 ;;
    esac
fi

# Branch override via environment variable
# Usage: PIRONMAN5_BRANCH=fix/promax curl ... | bash -s -- --variant pro-max
# BRANCH_OVERRIDE set via --pironman5-branch, or env, or empty
BRANCH_OVERRIDE="${BRANCH_OVERRIDE:-${PIRONMAN5_BRANCH:-}}"



# ============================================================
# Product Configuration
# ============================================================

# --- Product list (shown in menu) ---
# Format: "Display Name|variant|branch"
PRODUCTS=(
    "Pironman 5|base|1.3.x"
    "Pironman 5 Max|max|1.3.x"
    "Pironman 5 Pro Max|pro_max|1.3.x"
    "Pironman 5 Mini|mini|1.3.x"
)

# --- Peripherals per variant ---
declare -A PM5_PERIPHERALS
PM5_PERIPHERALS[base]="storage cpu network memory history log cpu_temperature gpu_temperature temperature_unit oled oled_sleep ws2812 pwm_fan_speed gpio_fan_state gpio_fan_mode pi5_power_button"
PM5_PERIPHERALS[mini]="storage cpu network memory history log cpu_temperature gpu_temperature temperature_unit ws2812 pwm_fan_speed gpio_fan_state gpio_fan_mode gpio_fan_led"
PM5_PERIPHERALS[max]="storage cpu network memory history log cpu_temperature gpu_temperature temperature_unit oled ws2812 pwm_fan_speed gpio_fan_state gpio_fan_mode gpio_fan_led pi5_power_button oled_sleep"
PM5_PERIPHERALS[pro_max]="storage cpu network memory history log cpu_temperature gpu_temperature temperature_unit ip_address mac_address oled oled_sleep ws2812 pi5_power_button"

# --- DT overlays per variant ---
declare -A PM5_OVERLAYS
PM5_OVERLAYS[base]="sunfounder-pironman5.dtbo"
PM5_OVERLAYS[mini]="sunfounder-pironman5mini.dtbo"
PM5_OVERLAYS[max]="sunfounder-pironman5.dtbo"
PM5_OVERLAYS[pro_max]="sunfounder-pironman5promax.dtbo"

# ============================================================
if [ -n "$ARG_VARIANT" ]; then
    # --variant mode: skip interactive menu
    for prod in "${PRODUCTS[@]}"; do
        IFS='|' read -r p_name p_variant p_branch <<< "$prod"
        if [ "$p_variant" = "$ARG_VARIANT" ]; then
            product_name="$p_name"
            variant="$p_variant"
            branch="$p_branch"
            break
        fi
    done
    if [ -z "$variant" ]; then
        echo "Variant not found: $ARG_VARIANT"
        exit 1
    fi
else
    # Interactive menu mode
    n=${#PRODUCTS[@]}
    echo "Please select your product model:"
    for i in $(seq 0 $((n - 1))); do
        name="${PRODUCTS[$i]%%|*}"
        echo "  $((i + 1))) $name"
    done
    echo ""
    while true; do
        printf "Enter number [1-%d]: " $n
        read -r choice < /dev/tty || {
            echo ""
            echo "Input/output error (pipe + sudo on Ubuntu/Debian)."
            echo "Download the script first:"
            echo "  curl -o install.sh URL && sudo bash install.sh"
            echo "Or skip the menu:"
            echo "  sudo bash install.sh --variant <model>"
            exit 1
        }
        if [ "$choice" -ge 1 ] 2>/dev/null && [ "$choice" -le "$n" ] 2>/dev/null; then
            selected=$((choice - 1))
            break
        fi
        echo "Invalid choice, please try again."
    done

    IFS='|' read -r product_name variant branch <<< "${PRODUCTS[$selected]}"
fi

# ============================================================
# Package Versions
# ============================================================
# Fetch pironman5 version from GitHub/Gitee
PIRONMAN5_VERSION="unknown"
_fetch_version() {
    local _vurl="${GIT_RAW_BASE}pironman5${GIT_RAW_SEP}${1}/pironman5/version.py"
    local _vraw=$(curl -fsSL "$_vurl" 2>/dev/null) || return 1
    PIRONMAN5_VERSION=$(echo "$_vraw" | awk '/__version__/ { gsub(/[^0-9.]/, ""); print }')
}
_fetch_version "$branch"

# Apply branch override from environment variable
if [ -n "$BRANCH_OVERRIDE" ]; then
    branch="$BRANCH_OVERRIDE"
    _fetch_version "$branch"
fi

PM_AUTO_BRANCH="v2"
DASHBOARD_BRANCH="v2"
SF_RPI_STATUS_BRANCH="main"

# Source base URLs — switch to Gitee mirror with --cn
# Note: Gitee raw URL format differs from GitHub: needs a /raw/ segment.
if [ "$USE_CN_MIRROR" = true ]; then
    GIT_REPO="https://gitee.com/sunfounder/"
    GIT_RAW_BASE="https://gitee.com/sunfounder/"
    GIT_RAW_SEP="/raw/"
    PIPOWER5_DTBO_URL="https://gitee.com/sunfounder/pipower5/raw/main/sunfounder-pipower5.dtbo"
else
    GIT_REPO="https://github.com/sunfounder/"
    GIT_RAW_BASE="https://raw.githubusercontent.com/sunfounder/"
    GIT_RAW_SEP="/"
    PIPOWER5_DTBO_URL="https://github.com/sunfounder/pipower5/raw/refs/heads/main/sunfounder-pipower5.dtbo"
fi



# Unified install: all dependencies pre-installed
# All overlays copied below

# UPS and pipower5 variants have pipower5 as a built-in module
if [ "$variant" = "ups" ]; then
    INSTALL_PIPOWER5=true
fi

# Helper: check if a peripheral is present
has() { return 0; }

# ============================================================
# Install Report
# ============================================================
echo ""
# Detect git source (uses framework function, idempotent)
installer_detect_git_source
# With --cn, downloads already forced to Gitee — fix the report label
if [ "$USE_CN_MIRROR" = true ]; then
    INSTALLER_GIT_SOURCE="Gitee (--cn)"
fi

echo "========================================="
echo "  ${product_name}  v${PIRONMAN5_VERSION}"
echo "  Branch: ${branch}"
echo "  Source: ${INSTALLER_GIT_SOURCE}"
echo "  ---------------------------------------"
# Fetch component versions from GitHub/Gitee
_fetch_comp_version() {
    local _url="${GIT_RAW_BASE}${1}${GIT_RAW_SEP}${2}/$(echo ${1} | sed 's/-/_/g')/version.py"
    local _raw=$(curl -fsSL "$_url" 2>/dev/null) || { echo "unknown"; return; }
    echo "$_raw" | awk '/__version__/ { gsub(/[^0-9.]/, ""); print }'
}
PM_AUTO_VER=$(_fetch_comp_version "pm_auto" "$PM_AUTO_BRANCH")
DASHBOARD_VER=$(_fetch_comp_version "pm_dashboard" "$DASHBOARD_BRANCH")
SF_RPI_STATUS_VER=$(_fetch_comp_version "sf_rpi_status" "$SF_RPI_STATUS_BRANCH")

echo "  pm_auto          ${PM_AUTO_BRANCH}  (v${PM_AUTO_VER})"
echo "  pm_dashboard     ${DASHBOARD_BRANCH}  (v${DASHBOARD_VER})"
echo "  sf_rpi_status    ${SF_RPI_STATUS_BRANCH}  (v${SF_RPI_STATUS_VER})"
if [ "$INSTALL_PIPOWER5" = true ]; then
    _pipower5_display_branch="${PIPOWER5_BRANCH:-${PIPOWER5_BRANCH_ARG:-v2}}"
    PIPOWER5_VER=$(_fetch_comp_version "pipower5" "${_pipower5_display_branch}")
    echo "  pipower5         ${_pipower5_display_branch}  (v${PIPOWER5_VER})"
fi
echo "========================================="
echo ""

# ============================================================
# Build Dependency Sets (deduplicated)
# ============================================================

# -- Pre-install scripts --
if [ "$IS_CONTAINER" = true ]; then
    PRE_SCRIPTS="install_influxdb.sh"
else
    PRE_SCRIPTS="umbrel_patch.sh"
    if has "ws2812" || has "gpio_fan_state" || has "vibration_switch"; then
        PRE_SCRIPTS="$PRE_SCRIPTS install_lgpio.sh fix_kali_gpio_spi.sh"
    fi
    PRE_SCRIPTS="$PRE_SCRIPTS install_influxdb.sh"
fi
# Deduplicate
PRE_SCRIPTS=$(echo "$PRE_SCRIPTS" | tr ' ' '\n' | awk 'NF' | sort -u | tr '\n' ' ')

# -- APT dependencies --
APT_DEPS="python3-dev influxdb"
if has "oled"; then
    APT_DEPS="$APT_DEPS libjpeg-dev libfreetype6-dev libopenjp2-7 kmod i2c-tools"
fi
if has "pi5_power_button"; then
    APT_DEPS="$APT_DEPS build-essential gcc g++"
fi
if has "gpio_fan_state" || has "vibration_switch"; then
    APT_DEPS="$APT_DEPS python3-gpiozero"
fi
APT_DEPS=$(echo "$APT_DEPS" | tr ' ' '\n' | awk 'NF' | sort -u | tr '\n' ' ')

# -- Pip dependencies (installed into venv) --
PIP_DEPS="pip setuptools build requests psutil"
if has "ws2812"; then
    PIP_DEPS="$PIP_DEPS adafruit-circuitpython-neopixel-spi adafruit_platformdetect Adafruit-Blinka==8.59.0 rpi.lgpio adafruit-circuitpython-typing 'Adafruit-PureIO>=1.1.7' 'pyftdi>=0.40.0'"
fi
if has "oled"; then
    PIP_DEPS="$PIP_DEPS Pillow smbus2"
fi
if has "gpio_fan_state" || has "vibration_switch"; then
    PIP_DEPS="$PIP_DEPS rpi.lgpio"
fi
if has "pi5_power_button"; then
    PIP_DEPS="$PIP_DEPS evdev"
fi
PIP_DEPS=$(echo "$PIP_DEPS" | tr ' ' '\n' | awk 'NF' | sort -u | tr '\n' ' ')

# -- Groups --
GROUP_LIST="video influxdb"
if has "ws2812"; then
    GROUP_LIST="$GROUP_LIST spi gpio"
fi
if has "oled"; then
    GROUP_LIST="$GROUP_LIST i2c"
fi
if has "gpio_fan_state" || has "vibration_switch"; then
    GROUP_LIST="$GROUP_LIST gpio"
fi
if has "pi5_power_button"; then
    GROUP_LIST="$GROUP_LIST input"
fi
if [ "$INSTALL_PIPOWER5" = true ]; then
    GROUP_LIST="$GROUP_LIST i2c pipower5"
fi
GROUP_LIST=$(echo "$GROUP_LIST" | tr ' ' '\n' | awk 'NF' | sort -u | tr '\n' ' ')

# -- Kernel modules --
MODULES=""
if has "oled"; then
    MODULES="i2c-dev"
fi

# ============================================================
# Build Declarative Install Commands (DSL)
# ============================================================

# --- Plugin-only install (incremental, only when no --variant given) ---
if [ "$_PLUGIN_ONLY" = true ]; then
    VENV_PIP="/opt/pironman5/venv/bin/pip3"
    # GIT_REPO already set to mirror source above (with --cn)
    branch="${BRANCH_OVERRIDE:-1.3.x}"

    if [ "$INSTALL_PLUGIN" = "pipower5" ]; then
        TITLE "Clone PiPower 5 source"
        PIPOWER5_BRANCH="${PIPOWER5_BRANCH:-${PIPOWER5_BRANCH_ARG:-v2}}"
        PIPOWER5_SRC="${HOME}/pipower5"
        if [ -d "${PIPOWER5_SRC}" ]; then
            RUN "cd ${PIPOWER5_SRC} && git fetch origin && git checkout ${PIPOWER5_BRANCH} && git pull origin ${PIPOWER5_BRANCH}" "Update PiPower 5 source"
        else
            RUN "git clone -b ${PIPOWER5_BRANCH} ${GIT_REPO}pipower5.git ${PIPOWER5_SRC}" "Clone PiPower 5 source"
        fi

        TITLE "Build and install kernel driver"
        RUN "apt-get install -y dkms 2>&1 || { printf 'Types: deb\nURIs: http://deb.debian.org/debian/\nSuites: trixie trixie-updates\nComponents: main contrib non-free non-free-firmware\nSigned-By: /usr/share/keyrings/debian-archive-keyring.pgp\n' > /etc/apt/sources.list.d/debian-trixie.sources && apt-get update && apt-get install -y dkms 2>&1; }" "Install DKMS"
        RUN "apt-get install -y linux-headers-raspi linux-headers-\$(uname -r)" "Install kernel headers"
        RUN "cd ${PIPOWER5_SRC}/driver && make clean && make module && make dkms_install && make dtbo && modprobe pipower5 || true" "Build and install pipower5.ko"

        if [ -f "${VENV_PIP}" ]; then
            TITLE "Install PiPower5 Python package"
            RUN "${VENV_PIP} install ${PIPOWER5_SRC}" "Install pipower5 from local source"

            TITLE "Copy email templates"
            RUN "mkdir -p /opt/pironman5/email_templates" "Create email template dir"
            RUN "cp -r ${PIPOWER5_SRC}/email_templates/* /opt/pironman5/email_templates/" "Copy email templates"

            TITLE "Create symlinks"
            RUN "ln -sf /opt/pironman5/venv/bin/pipower5 /usr/local/bin/pipower5" "Create pipower5 symlink"
        fi

        TITLE "Setup PiPower5 groups"
        RUN "getent group pipower5 > /dev/null 2>&1 || groupadd -r pipower5" "Create pipower5 group"
        RUN "usermod -aG i2c pironman5 2>/dev/null; usermod -aG pipower5 pironman5 2>/dev/null; true" "Add pironman5 to i2c+pipower5"

        TITLE "Copy udev rules"
    RUN "cp ${PIPOWER5_SRC}/rules/99-pipower5.rules /etc/udev/rules.d/" "Copy udev rules"
    RUN "udevadm control --reload-rules" "Reload udev"

    TITLE "Copy device tree overlay"
        OVERLAY_SEARCH_PATHS="/boot/firmware/current/overlays /boot/firmware/overlays /boot/overlays"
        OVERLAY_PATH=""
        for p in $OVERLAY_SEARCH_PATHS; do
            if [ -d "$p" ]; then OVERLAY_PATH="$p"; break; fi
        done
        if [ -n "$OVERLAY_PATH" ]; then
            RUN "cp ${PIPOWER5_SRC}/driver/sunfounder-pipower5.dtbo ${OVERLAY_PATH}/" "Copy DT overlay"
            DTOVERLAY_ADD "sunfounder-pipower5.dtbo"
        fi

        TITLE "Persist device tree overlay"
        RUN "mkdir -p /usr/local/share/sunfounder/overlays" "Create persistent overlay directory"
        RUN "if [ -f ${PIPOWER5_SRC}/driver/sunfounder-pipower5.dtbo ]; then cp ${PIPOWER5_SRC}/driver/sunfounder-pipower5.dtbo /usr/local/share/sunfounder/overlays/; elif [ -f ${PIPOWER5_SRC}/sunfounder-pipower5.dtbo ]; then cp ${PIPOWER5_SRC}/sunfounder-pipower5.dtbo /usr/local/share/sunfounder/overlays/; else curl -fsSL $PIPOWER5_DTBO_URL -o /usr/local/share/sunfounder/overlays/sunfounder-pipower5.dtbo; fi" "Persist PiPower5 device tree overlay"
        if [ "$IS_CONTAINER" = false ]; then
        RUN "mkdir -p /etc/kernel/postinst.d" "Create postinst.d directory"
        RUN "cp ${PIPOWER5_SRC}/bin/sunfounder-dtbos-hook /etc/kernel/postinst.d/sunfounder-dtbos && chmod +x /etc/kernel/postinst.d/sunfounder-dtbos" "Install kernel postinst hook"
        RUN "/etc/kernel/postinst.d/sunfounder-dtbos" "Run postinst hook now for existing overlay dirs"
        fi

        TITLE "Enable PiPower5 plugin"
        RUN "echo pipower5 >> /opt/pironman5/.custom_module" "Write custom module"
        echo "========================================="
        echo ""
    fi

    if [ "$IS_PLAIN_TEXT" = true ]; then
        installer_install --plain-text
    else
        installer_install
    fi
    exit 0
fi

# PiPower5 standalone uses standard pironman5 flow + pipower5 plugin
if [ "$variant" = "pipower5" ]; then
    INSTALL_PIPOWER5=true
    INSTALL_PLUGIN="pipower5"

    TITLE "PiPower 5"
    # Check for old standalone installation
    if [ -d /opt/pipower5 ] || [ -f /etc/systemd/system/pipower5.service ]; then
        RUN "true" "Detected old PiPower 5 — will remove before new install"
        RUN "systemctl stop pipower5 2>/dev/null; systemctl disable pipower5 2>/dev/null; rm -f /etc/systemd/system/pipower5.service" "Remove old pipower5 service"
        RUN "rm -rf /opt/pipower5 /var/log/pipower5 /root/.config/pipower5" "Remove old /opt/pipower5"
        RUN "rm -f /usr/local/bin/pipower5" "Remove old pipower5 symlink"
        RUN "rmmod pipower5_driver 2>/dev/null; rmmod pipower5 2>/dev/null; dkms remove -m pipower5 --all 2>/dev/null; dkms remove -m pipower5_driver --all 2>/dev/null; find /lib/modules -name 'pipower5*.ko*' -delete 2>/dev/null; rm -f /etc/modules-load.d/pipower5*.conf; depmod -a" "Remove old kernel driver"
        RUN "systemctl daemon-reload" "Reload systemd"
    fi
fi

# --- Clone repository ---
TITLE "Install build dependencies"
RUN "DEBIAN_FRONTEND=noninteractive apt-get update" "Update package list"
RUN "DEBIAN_FRONTEND=noninteractive apt-get install -y python3-pip python3-venv git curl" "Install build dependencies"

TITLE "Clone pironman5 repository"
RUN "rm -rf ${HOME}/pironman5" "Remove existing pironman5 directory"
RUN "git clone -b ${branch} --depth=1 ${GIT_REPO}pironman5 ${HOME}/pironman5" "Clone pironman5"
if [ "$IS_CONTAINER" = false ]; then
    RUN "chown -R ${USERNAME}:${USERNAME} ${HOME}/pironman5" "Set repo ownership"
fi
CD "${HOME}/pironman5"

# --- Pre-install scripts ---
if [ -n "$PRE_SCRIPTS" ]; then
    TITLE "Run pre-install scripts"
    for script in $PRE_SCRIPTS; do
        RUN "bash scripts/${script}" "Run ${script}"
    done
fi

# --- APT dependencies ---
TITLE "Install APT dependencies"
RUN "DEBIAN_FRONTEND=noninteractive apt-get install -y ${APT_DEPS}" "Install APT dependencies"

# --- User and group setup ---
if [ "$IS_CONTAINER" = false ]; then
    TITLE "Setup system user"
    RUN "getent group pironman5 > /dev/null || groupadd -r pironman5" "Create pironman5 group"
    RUN "getent passwd pironman5 > /dev/null || useradd -r -g pironman5 -s /sbin/nologin -d /opt/pironman5 -m pironman5" "Create pironman5 user"
    RUN "usermod -aG pironman5 ${USERNAME}" "Add ${USERNAME} to pironman5 group"

    TITLE "Setup sudo permissions"
    RUN "echo 'pironman5 ALL=(ALL) NOPASSWD: /usr/sbin/shutdown, /usr/sbin/reboot, /usr/sbin/poweroff, /usr/sbin/halt, /usr/bin/systemctl, /usr/bin/lsblk' | tee /etc/sudoers.d/pironman5 > /dev/null" "Create sudoers file"
    RUN "chmod 0440 /etc/sudoers.d/pironman5" "Set sudoers permissions"

    if [ -n "$GROUP_LIST" ]; then
        TITLE "Add user to groups"
        for group in $GROUP_LIST; do
            RUN "getent group ${group} > /dev/null 2>&1 || groupadd -r ${group}; usermod -aG ${group} pironman5" "Setup ${group} group"
        done
    fi
fi

# --- Working directory and venv ---
TITLE "Create working directory"
RUN "mkdir -p /opt/pironman5 /var/log/pironman5" "Create directories"
RUN "touch /var/log/pironman5/pironman5.log" "Create log file"
if [ "$IS_CONTAINER" = false ]; then
    RUN "chmod 775 /opt/pironman5" "Set work directory permissions"
    RUN "chown -R pironman5:pironman5 /opt/pironman5" "Set work directory owner"
    RUN "chmod 775 /var/log/pironman5" "Set log directory permissions"
    RUN "chown -R pironman5:pironman5 /var/log/pironman5" "Set log directory owner"
    RUN "chmod 664 /var/log/pironman5/pironman5.log" "Set log file permissions"
    RUN "chown pironman5:pironman5 /var/log/pironman5/pironman5.log" "Set log file owner"
fi
RUN "rm -rf /opt/pironman5/venv" "Remove old virtual environment"
RUN "python3 -m venv /opt/pironman5/venv --system-site-packages" "Create virtual environment"

VENV_PIP="/opt/pironman5/venv/bin/pip3"

# --- Uninstall conflicting packages ---
if has "gpio_fan_state" || has "vibration_switch"; then
    TITLE "Remove conflicting packages"
    RUN "${VENV_PIP} uninstall -y RPi.GPIO 2>/dev/null; true" "Uninstall RPi.GPIO"
fi

# --- Install pip dependencies ---
TITLE "Install Python dependencies"
RUN "${VENV_PIP} install --upgrade ${PIP_DEPS}" "Install Python packages"

# --- Install Python source packages ---
TITLE "Install Python packages from source"
RUN "${VENV_PIP} install ./ " "Install pironman5"
RUN "${VENV_PIP} install git+${GIT_REPO}pm_auto.git@${PM_AUTO_BRANCH}" "Install pm_auto"
RUN "${VENV_PIP} install git+${GIT_REPO}sf_rpi_status.git@${SF_RPI_STATUS_BRANCH}" "Install sf_rpi_status"
RUN "${VENV_PIP} install git+${GIT_REPO}pm_dashboard.git@${DASHBOARD_BRANCH}" "Install pm_dashboard"

# --- Install PiPower5 ---
if [ "$INSTALL_PIPOWER5" = true ]; then
    PIPOWER5_BRANCH="${PIPOWER5_BRANCH:-${PIPOWER5_BRANCH_ARG:-v2}}"
    PIPOWER5_SRC="${HOME}/pipower5"

    TITLE "Clone PiPower5 source"
    if [ -d "${PIPOWER5_SRC}" ]; then
        RUN "cd ${PIPOWER5_SRC} && git fetch origin && git checkout ${PIPOWER5_BRANCH} && git pull origin ${PIPOWER5_BRANCH}" "Update PiPower5 source"
    else
        RUN "git clone -b ${PIPOWER5_BRANCH} ${GIT_REPO}pipower5.git ${PIPOWER5_SRC}" "Clone PiPower5 source"
    fi

    TITLE "Install PiPower5 build dependencies"
    RUN "apt-get install -y dkms 2>&1 || { printf 'Types: deb\nURIs: http://deb.debian.org/debian/\nSuites: trixie trixie-updates\nComponents: main contrib non-free non-free-firmware\nSigned-By: /usr/share/keyrings/debian-archive-keyring.pgp\n' > /etc/apt/sources.list.d/debian-trixie.sources && apt-get update && apt-get install -y dkms 2>&1; }" "Install DKMS"
    RUN "apt-get install -y linux-headers-raspi linux-headers-\$(uname -r)" "Install kernel headers"

    TITLE "Build and install PiPower5 kernel driver"
    RUN "cd ${PIPOWER5_SRC}/driver && make clean && make module && make dkms_install && make dtbo && make install-overlay && modprobe pipower5 || true" "Build and install pipower5.ko"

    TITLE "Install PiPower5 Python package"
    RUN "${VENV_PIP} install git+${GIT_REPO}pipower5.git@${PIPOWER5_BRANCH}" "Install pipower5"
    RUN "ln -sf /opt/pironman5/venv/bin/pipower5 /usr/local/bin/pipower5" "Create pipower5 symlink"

    if [ "$IS_CONTAINER" = false ]; then
        TITLE "Setup PiPower5 udev rules"
        RUN "cp ${PIPOWER5_SRC}/rules/99-pipower5.rules /etc/udev/rules.d/" "Copy udev rules"
        RUN "udevadm control --reload-rules" "Reload udev"
    fi

    TITLE "Copy PiPower5 email templates"
    RUN "mkdir -p /opt/pironman5/email_templates" "Create email template dir"
    RUN "cp -r ${PIPOWER5_SRC}/email_templates/* /opt/pironman5/email_templates/" "Copy email templates"
fi

# --- Symlinks ---
TITLE "Create symlinks"
RUN "ln -sf /opt/pironman5/venv/bin/pironman5 /usr/local/bin/pironman5" "Create pironman5 symlink"

# --- Shell completion ---
TITLE "Setup shell completion"
RUN "${VENV_PIP} install --ignore-installed argcomplete" "Install argcomplete"
RUN "/opt/pironman5/venv/bin/register-python-argcomplete pironman5 > /etc/bash_completion.d/pironman5" "Register bash completion"

# --- Systemd auto-start ---
if [ "$IS_CONTAINER" = false ]; then
    TITLE "Setup auto-start"
    RUN "cp bin/pironman5.service /etc/systemd/system/" "Install service file"
    RUN "systemctl enable pironman5.service" "Enable pironman5 service"
    RUN "systemctl daemon-reload" "Reload systemd"
fi

# --- Kernel modules ---
if [ "$IS_CONTAINER" = false ] && [ -n "$MODULES" ]; then
    TITLE "Configure kernel modules"
    for module in $MODULES; do
        RUN "echo ${module} >> /etc/modules-load.d/modules.conf" "Add module ${module}"
    done
fi

# --- Device tree overlays ---
if [ "$IS_CONTAINER" = false ]; then
    TITLE "Copy device tree overlays"
    OVERLAY_SEARCH_PATHS="/boot/firmware/current/overlays /boot/firmware/overlays /boot/overlays"
    OVERLAY_PATH=""
    for p in $OVERLAY_SEARCH_PATHS; do
        if [ -d "$p" ]; then
            OVERLAY_PATH="$p"
            break
        fi
    done
    if [ -z "$OVERLAY_PATH" ]; then
        installer_log_failed "Device tree overlay directory not found. Checked: ${OVERLAY_SEARCH_PATHS}"
    else
        if [ -n "${PM5_OVERLAYS[$variant]}" ] && [ "${PM5_OVERLAYS[$variant]}" != "" ]; then
            RUN "cp ${HOME}/pironman5/overlays/${PM5_OVERLAYS[$variant]} ${OVERLAY_PATH}/" "Copy ${PM5_OVERLAYS[$variant]}"
        fi
        if [ "$INSTALL_PIPOWER5" = true ]; then
            # Copy pipower5 DT overlay at runtime (after make dtbo has built it)
            RUN "if [ -f ${PIPOWER5_SRC}/driver/sunfounder-pipower5.dtbo ]; then cp ${PIPOWER5_SRC}/driver/sunfounder-pipower5.dtbo ${OVERLAY_PATH}/; elif [ -f ${PIPOWER5_SRC}/sunfounder-pipower5.dtbo ]; then cp ${PIPOWER5_SRC}/sunfounder-pipower5.dtbo ${OVERLAY_PATH}/; else curl -fsSL $PIPOWER5_DTBO_URL -o ${OVERLAY_PATH}/sunfounder-pipower5.dtbo; fi" "Copy PiPower5 device tree overlay"
        fi
    fi
fi

# --- Persist device tree overlays ---
# On Ubuntu, flash-kernel rotates overlay directories (current/ <-> old/)
# on kernel updates, stranding custom dtbos. Store dtbos in a persistent
# location + install a kernel postinst.d hook to re-copy after updates.
TITLE "Persist device tree overlays"
RUN "mkdir -p /usr/local/share/sunfounder/overlays" "Create persistent overlay directory"
if [ -n "${PM5_OVERLAYS[$variant]}" ] && [ "${PM5_OVERLAYS[$variant]}" != "" ]; then
    RUN "cp ${HOME}/pironman5/overlays/${PM5_OVERLAYS[$variant]} /usr/local/share/sunfounder/overlays/" "Persist ${PM5_OVERLAYS[$variant]}"
fi
if [ "$INSTALL_PIPOWER5" = true ]; then
    RUN "if [ -f ${PIPOWER5_SRC}/driver/sunfounder-pipower5.dtbo ]; then cp ${PIPOWER5_SRC}/driver/sunfounder-pipower5.dtbo /usr/local/share/sunfounder/overlays/; elif [ -f ${PIPOWER5_SRC}/sunfounder-pipower5.dtbo ]; then cp ${PIPOWER5_SRC}/sunfounder-pipower5.dtbo /usr/local/share/sunfounder/overlays/; else curl -fsSL $PIPOWER5_DTBO_URL -o /usr/local/share/sunfounder/overlays/sunfounder-pipower5.dtbo; fi" "Persist PiPower5 device tree overlay"
fi

if [ "$IS_CONTAINER" = false ]; then
TITLE "Install kernel postinst hook"
RUN "mkdir -p /etc/kernel/postinst.d" "Create postinst.d directory"
RUN "cp ${HOME}/pironman5/bin/sunfounder-dtbos-hook /etc/kernel/postinst.d/sunfounder-dtbos && chmod +x /etc/kernel/postinst.d/sunfounder-dtbos" "Install kernel postinst hook"
RUN "/etc/kernel/postinst.d/sunfounder-dtbos" "Run postinst hook now for existing overlay dirs"
fi

# --- Post-install scripts ---
if [ "$IS_CONTAINER" = false ]; then
    if has "gpio_fan_state" || has "vibration_switch"; then
        TITLE "Run post-install scripts"
        RUN "bash scripts/change_rpi.gpio_to_rpi.lgpio.sh" "Migrate RPi.GPIO to rpi.lgpio"
    fi
fi

# --- Fix permissions ---
if [ "$IS_CONTAINER" = false ]; then
    TITLE "Finalize permissions"
    RUN "chmod +x /opt/pironman5" "Set execution permission on work dir"
    RUN "chown -R pironman5:pironman5 /opt/pironman5" "Set final ownership"
fi

# --- Write variant file ---
TITLE "Write product variant"
RUN "mkdir -p /opt/pironman5" "Ensure work directory exists"
RUN "echo -n '${variant}' > /opt/pironman5/.variant" "Write variant identifier"
if [ "$INSTALL_PIPOWER5" = true ]; then
    RUN "echo -n 'pipower5' > /opt/pironman5/.custom_module" "Write custom module"
fi

if [ "$IS_CONTAINER" = false ] && [ "$variant" = "pro_max" ]; then
    _hdmi_url="${GIT_REPO}pi-hdmi-edid/raw/main/install.sh"
    RUN "curl -fsSL \"$_hdmi_url\" | bash" "Install HDMI EDID plugin"
fi

# --- Write dtoverlay to config.txt ---
if [ "$IS_CONTAINER" = false ]; then
    TITLE "Configure device tree overlays"
    if [ -n "${PM5_OVERLAYS[$variant]}" ] && [ "${PM5_OVERLAYS[$variant]}" != "" ]; then
        DTOVERLAY_ADD "${PM5_OVERLAYS[$variant]}"
    fi
    if [ "$INSTALL_PIPOWER5" = true ]; then
        DTOVERLAY_ADD "sunfounder-pipower5.dtbo"
    fi
fi

# Auto-detect non-TTY output (pipe, container); keep colors for interactive terminals
if [ ! -t 1 ]; then
    IS_PLAIN_TEXT=true
fi
# Suppress tput errors when TERM is unset
export TERM="${TERM:-xterm-256color}"

# ============================================================
# Execute Installation
# ============================================================
if [ "$IS_PLAIN_TEXT" = true ]; then
    installer_install --plain-text
else
    installer_install
fi

# ============================================================
# Pro Max: Auto-launch browser
# ============================================================
if [ "$IS_CONTAINER" = false ] && [ "$variant" = "pro_max" ]; then
    echo ""
    read -p "Auto-launch dashboard on 4.3\" screen at startup? [Y/n]: " install_browser < /dev/tty
    if [[ "$install_browser" =~ ^[Yy]?$ ]]; then
        LAUNCH_CMD='/opt/pironman5/venv/bin/python3 -c "from pironman5._launch_browser import run; run()"'
        # XDG autostart (GNOME/KDE/XFCE)
        AUTOSTART_DIR="${HOME}/.config/autostart"
        mkdir -p "$AUTOSTART_DIR"
        cat > "${AUTOSTART_DIR}/pironman5-dashboard.desktop" << EOF
[Desktop Entry]
Type=Application
Name=Pironman 5 Dashboard
Comment=Auto-launch Pironman 5 dashboard on the 4.3" screen
Exec=${LAUNCH_CMD}
X-GNOME-Autostart-enabled=true
EOF
        chown "${USERNAME}:${USERNAME}" "${AUTOSTART_DIR}/pironman5-dashboard.desktop"
        # labwc autostart (Raspberry Pi OS Wayland)
        LABWC_DIR="${HOME}/.config/labwc"
        mkdir -p "$LABWC_DIR"
        grep -q 'pironman5' "${LABWC_DIR}/autostart" 2>/dev/null || \
            echo "${LAUNCH_CMD} &" >> "${LABWC_DIR}/autostart"
        chown "${USERNAME}:${USERNAME}" "${LABWC_DIR}/autostart" 2>/dev/null || true
        echo "Autostart entry created. Dashboard will launch on next desktop login."

        # --- Configure auto-login on non-Pi systems (Pi OS has it by default) ---
        if [ "$NO_AUTOLOGIN" = false ] && [ ! -f /usr/bin/raspi-config ]; then
            echo ""
            read -p "Enable auto-login so dashboard starts without password? [Y/n]: " setup_autologin < /dev/tty
            if [[ "$setup_autologin" =~ ^[Yy]?$ ]]; then
                if [ -f /etc/gdm3/custom.conf ]; then
                    if ! grep -q 'AutomaticLoginEnable\s*=\s*[Tt]rue' /etc/gdm3/custom.conf 2>/dev/null; then
                        cp /etc/gdm3/custom.conf /etc/gdm3/custom.conf.bak 2>/dev/null
                        sed -i '/^\[daemon\]/a AutomaticLoginEnable=True\nAutomaticLogin='"${USERNAME}" /etc/gdm3/custom.conf
                        echo "  ✓ Auto-login configured for ${USERNAME} (GDM3)"
                    else
                        echo "  - Auto-login already enabled (GDM3)"
                    fi
                elif command -v lightdm >/dev/null 2>&1 || [ -d /etc/lightdm ]; then
                    LIGHTDM_CONF="/etc/lightdm/lightdm.conf"
                    mkdir -p /etc/lightdm
                    if ! grep -q "autologin-user=${USERNAME}" "$LIGHTDM_CONF" 2>/dev/null; then
                        cp "$LIGHTDM_CONF" "${LIGHTDM_CONF}.bak" 2>/dev/null || true
                        if grep -q '\[Seat:\*\]' "$LIGHTDM_CONF" 2>/dev/null; then
                            sed -i '/^\[Seat:\*\]/a autologin-user='"${USERNAME}" "$LIGHTDM_CONF"
                        else
                            echo -e "\n[Seat:*]\nautologin-user=${USERNAME}" >> "$LIGHTDM_CONF"
                        fi
                        echo "  ✓ Auto-login configured for ${USERNAME} (LightDM)"
                    else
                        echo "  - Auto-login already enabled (LightDM)"
                    fi
                else
                    echo "  ⚠ Display manager not detected. Please configure auto-login in system settings."
                fi
            fi
        fi

        # Try to launch immediately if desktop is available
        if [ -n "$DISPLAY" ] || [ -n "$WAYLAND_DISPLAY" ] || [ -S /run/user/1000/wayland-0 ]; then
            /opt/pironman5/venv/bin/python3 -c "from pironman5._launch_browser import run; run()" 2>/dev/null || true
        fi
    fi
fi

# ============================================================
# Complete
# ============================================================
if [ "$IS_CONTAINER" = false ]; then
    installer_prompt_reboot
fi
