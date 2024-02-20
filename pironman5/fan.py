
import gpiozero # https://gpiozero.readthedocs.io/en/latest/installing.html

from utils import run_command, log
from system_status import set_pwm_fan_state, get_pwm_fan_state

TEMP_CONTROL_MAP = {
    '0': [50 , 0], # 'level': [min temp, level]
    '1': [50 , 1],
    '2': [60 , 2],
    '3': [67.5 , 3],
    '4': [75 , 4],
}
TEMP_HYSTERESIS = 5 # celsius

fan = None
enable_pwm_fan_control = False # for those systems that don't have pwm fan control
current_fan_level = 0

# fan control
# fan_pin: fan pin number in BCM
# =================================================================
def fan_init(fan_pin):
    global fan, enable_pwm_fan_control, current_fan_level
    _, os_id = run_command("lsb_release -a |grep ID | awk -F ':' '{print $2}'")
    os_id = os_id.strip()
    _, os_code_name = run_command("lsb_release -a |grep Codename | awk -F ':' '{print $2}'")
    os_code_name = os_code_name.strip()

    # Systems that need to replace system pwm fan control
    # Please use all lowercase
    TEMP_CONTROL_INTERVENE_OS = [
        'ubuntu',
    ]
    current_fan_level = 0
    enable_pwm_fan_control = False

    if os_id.lower() in TEMP_CONTROL_INTERVENE_OS or os_code_name.lower() in TEMP_CONTROL_INTERVENE_OS:
        log("System needs to replace system pwm fan control")
        enable_pwm_fan_control = True

    fan = gpiozero.OutputDevice(fan_pin)

# pwm fan control
# temp: cpu temp in celsius
# =================================================================
def pwm_fan_control(temp):
    global current_fan_level
    if temp < (TEMP_CONTROL_MAP[str(current_fan_level)][0] - 5):
        current_fan_level -= 1
        if current_fan_level < 0:
            current_fan_level = 0
        set_pwm_fan_state(current_fan_level)
    elif (current_fan_level < 4) and (temp > TEMP_CONTROL_MAP[str(current_fan_level+1)][0]):
        current_fan_level += 1
        set_pwm_fan_state(current_fan_level)

# fan control
# temp: cpu temp in celsius
# =================================================================
def fan_control(temp):
    global fan, enable_pwm_fan_control
    if enable_pwm_fan_control:
        pwm_fan_control(temp)

    # get fan1 state
    fan1_state = get_pwm_fan_state()
    if (fan1_state > 0):
        fan.on()
    else:
        fan.off()

# fan deinit
# =================================================================
def fan_deinit():
    global fan
    if fan:
        fan.off()
        fan.close()
        fan = None
        log("fan deinit done")