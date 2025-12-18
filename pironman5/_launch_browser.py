#!/usr/bin/env python3
import subprocess
import sys
import os
from typing import List

def check_desktop_environment() -> bool:
    """
    Check if the current environment is a desktop environment (prevent failure in SSH/pure console environments)
    Return: True = desktop environment, False = non-desktop environment
    """
    # Core check 1: DISPLAY environment variable (required for X11/Wayland)
    if not os.getenv("DISPLAY"):
        print("Error: DISPLAY environment variable not detected. Current environment may be SSH/pure console.", file=sys.stderr)
        return False
    
    # Core check 2: Session type (distinguish desktop/console)
    session_type = os.getenv("XDG_SESSION_TYPE", "")
    if session_type not in ["x11", "wayland"]:
        print(f"Error: Current session type is {session_type}. Only x11/wayland desktop sessions are supported.", file=sys.stderr)
        return False
    
    # Optional check: Confirm desktop environment identifier (GNOME/KDE/XFCE etc.)
    desktop_env = os.getenv("XDG_CURRENT_DESKTOP", "")
    if not desktop_env:
        print("Warning: No explicit desktop environment identifier (e.g., GNOME/KDE) detected. Browser may not launch properly.", file=sys.stderr)
        # Only warn, not exit - some minimal desktops may lack this variable
    
    return True

def find_available_browsers() -> List[str]:
    """
    Detect installed browsers on the system and return a list of executable commands
    Priority: chromium > google-chrome > firefox
    """
    browsers = [
        "chromium-browser",  # Chromium for Debian/Ubuntu-based systems
        "chromium",          # Generic Chromium
        "google-chrome",     # Google Chrome
        "google-chrome-stable",  # Chrome Stable version
        "firefox"            # Firefox
    ]
    
    available = []
    for browser in browsers:
        # Use 'which' command to check if browser is installed
        try:
            subprocess.run(
                ["which", browser],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            available.append(browser)
        except subprocess.CalledProcessError:
            continue
    
    return available

def get_browser_fullscreen_args(browser: str) -> List[str]:
    """
    Return fullscreen arguments corresponding to different browsers
    """
    target_url = "http://127.0.0.1:34001"
    
    # Chrome/Chromium fullscreen arguments
    if "chrome" in browser or "chromium" in browser:
        return [
            browser,
            "--start-fullscreen",  # Launch in fullscreen mode
            "--kiosk",             # Kiosk mode (no address bar/menus)
            "--no-first-run",      # Skip first-run setup
            "--no-default-browser-check",  # Skip default browser check
            target_url
        ]
    # Firefox fullscreen arguments
    elif "firefox" in browser:
        return [
            browser,
            "-kiosk",              # Kiosk fullscreen mode
            "-new-window",         # Open in a new window
            target_url
        ]
    else:
        return [browser, target_url]

def launch_browser() -> bool:
    """
    Launch browser and open the specified URL in fullscreen mode
    Return: Whether launch was successful
    """
    # Find available browsers
    available_browsers = find_available_browsers()
    if not available_browsers:
        print("Error: No supported browsers detected (Chrome/Chromium/Firefox).", file=sys.stderr)
        return False
    
    # Use the first detected browser
    selected_browser = available_browsers[0]
    print(f"Detected available browser: {selected_browser}")
    
    # Build launch command
    cmd = get_browser_fullscreen_args(selected_browser)
    print(f"Executing command: {' '.join(cmd)}")
    
    try:
        # Launch browser in background (non-blocking, runs independently)
        subprocess.Popen(
            cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True
        )
        print(f"Successfully launched {selected_browser}, opened {cmd[-1]} in fullscreen mode.")
        return True
    except Exception as e:
        print(f"Failed to launch browser: {str(e)}", file=sys.stderr)
        return False

def run():
    """Main function"""
    # 1. Check if system is Linux
    if not sys.platform.startswith("linux"):
        print("Error: This script only supports Linux systems.", file=sys.stderr)
        sys.exit(1)
    
    # 2. New: Check if in desktop environment (core modification)
    if not check_desktop_environment():
        sys.exit(1)
    
    # 3. Warning: Avoid running with root privileges
    if os.geteuid() == 0:
        print("Warning: Running browsers as root is not recommended, may cause permission/security issues.", file=sys.stderr)
    
    # 4. Launch browser
    if not launch_browser():
        sys.exit(1)

if __name__ == "__main__":
    run()