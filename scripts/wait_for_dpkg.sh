#!/bin/bash

# Ensure output buffering is turned off for immediate display
shopt -s checkwinsize

# Get current script PID to exclude self from process checks
SCRIPT_PID=$$

# Function to clear the current line
clear_line() {
    printf "\r%*s\r" "${COLUMNS:-80}" ""
}

# Function to check if dpkg is locked
# Returns: 0=locked, 1=unlocked
# Also outputs lock information to stdout
is_dpkg_locked() {
    local lock_files=()
    local processes=()
    
    # Check dpkg lock files - this is the most accurate way to detect actual locks
    for lock_file in "/var/lib/dpkg/lock" "/var/lib/dpkg/lock-frontend" "/var/lib/apt/lists/lock"; do
        if [ -f "$lock_file" ]; then
            # Check if the lock file is actually being held by a process
            local pid=$(fuser "$lock_file" 2>/dev/null)
            if [ -n "$pid" ] && [ "$pid" != "$SCRIPT_PID" ]; then
                # Get process details
                local proc_info=$(ps -o cmd= -p "$pid" 2>/dev/null)
                if [ -n "$proc_info" ]; then
                    # Extract process name (first part of command)
                    local proc_name=$(basename "$(echo "$proc_info" | awk '{print $1}')")
                    processes+=("Lock: $lock_file (PID: $pid, Process: $proc_name)")
                else
                    processes+=("Lock: $lock_file (PID: $pid)")
                fi
            fi
        fi
    done
    
    # Only consider the process as locked if we found actual lock holders
    # Avoid false positives from process name matching
    if [ ${#processes[@]} -gt 0 ]; then
        printf "%s" "${processes[*]}"
        return 0  # locked
    fi
    
    return 1  # not locked
}

# Configuration
WAIT_INTERVAL=1
MAX_WAIT=3600  # 1 hour timeout
start_time=$(date +%s)

if ! is_dpkg_locked; then
    exit 0
fi

# Main loop to wait for dpkg to become available
while true; do
    # Get lock information
    lock_info=$(is_dpkg_locked)
    is_locked=$?
    
    # Exit loop if dpkg is available
    if [ $is_locked -ne 0 ]; then
        break
    fi
    
    # Calculate elapsed time
    current_time=$(date +%s)
    elapsed=$((current_time - start_time))
    minutes=$((elapsed / 60))
    seconds=$((elapsed % 60))
    
    # Check for timeout
    if [ $elapsed -ge $MAX_WAIT ]; then
        clear_line
        echo "Error: Timeout waiting for dpkg to become available!"
        echo "Lock details: $lock_info"
        exit 1
    fi
    
    # Clear line and extract process information
    clear_line
    app_name="unknown"
    pid="-"
    
    if [ -n "$lock_info" ]; then
        # Try to extract application name and PID
        if echo "$lock_info" | grep -q "Process: [^)]*" && echo "$lock_info" | grep -q "(PID: [0-9]\+"; then
            app_name=$(echo "$lock_info" | head -n 1 | grep -o "Process: [^)]*" | cut -d' ' -f2)
            pid=$(echo "$lock_info" | head -n 1 | grep -o "PID: [0-9]\+" | cut -d' ' -f2)
        elif echo "$lock_info" | grep -q "(PID: [0-9]\+"; then
            pid=$(echo "$lock_info" | head -n 1 | grep -o "PID: [0-9]\+" | cut -d' ' -f2)
        fi
    fi
    
    # Display status
    printf "dpkg currently locked by \"%s\"(%s), waiting... (%d minutes%02d seconds elapsed)" "$app_name" "$pid" "$minutes" "$seconds"
    sleep $WAIT_INTERVAL
done

# Final cleanup and message
clear_line
echo "dpkg is now available, proceeding with operations."

exit 0