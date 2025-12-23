#!/bin/bash
# NTP Time Synchronization Service
# Course project for OS Security
# User: user-13-63

SERVICE_NAME="ntp-sync-service"
CURRENT_USER=$(whoami)
LOG_TAG="[$CURRENT_USER] $SERVICE_NAME"
CHECK_INTERVAL=60  # 1 минута для тестирования

log_message() {
    local level="$1"
    local msg="$2"
    echo "$LOG_TAG: $msg" | systemd-cat -p "$level" -t "$SERVICE_NAME"
}

check_ntp_status() {
    if timedatectl status | grep -q "System clock synchronized: yes"; then
        log_message "info" "Time is synchronized"
        return 0
    else
        log_message "warning" "Time is NOT synchronized"
        return 1
    fi
}

force_ntp_sync() {
    log_message "info" "Attempting time synchronization..."

    if sudo /usr/bin/chronyc -a makestep 1 1; then
        log_message "info" "Synchronization successful"
        return 0
    else
        log_message "err" "Synchronization failed"
        return 1
    fi
}

cleanup() {
    log_message "info" "Service stopping"
    exit 0
}

trap cleanup SIGTERM SIGINT

main() {
    log_message "info" "Service starting (PID: $$)"

    # Initial check
    if ! check_ntp_status; then
        force_ntp_sync
    fi

    # Main loop
    while true; do
        sleep $CHECK_INTERVAL
        if ! check_ntp_status; then
            force_ntp_sync
        fi
    done
}

main
