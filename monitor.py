# monitor.py
import psutil
import smtplib
import json
import os
from email.message import EmailMessage
from datetime import datetime

# Load threshold config
with open("config.json", "r") as f:
    config = json.load(f)

# Threshold values
CPU_THRESHOLD = config["cpu"]
RAM_THRESHOLD = config["ram"]
DISK_THRESHOLD = config["disk"]

# Email config
TO = config["to"]
FROM = config["from"]
SUBJECT = "🚨 System Alert: Resource Threshold Breached"
SMTP_SERVER = config["smtp_server"]
SMTP_PORT = config["smtp_port"]

def send_alert(subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = FROM
    msg["To"] = TO

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.send_message(msg)

def check_system():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    alert_triggered = False
    message = f"[{datetime.now()}] System Health Report:\n"
    message += f"CPU Usage: {cpu}%\n"
    message += f"RAM Usage: {ram}%\n"
    message += f"Disk Usage: {disk}%\n\n"

    if cpu > CPU_THRESHOLD or ram > RAM_THRESHOLD or disk > DISK_THRESHOLD:
        alert_triggered = True
        message += "⚠️ ALERT: One or more thresholds have been breached.\n"

    if alert_triggered:
        send_alert(SUBJECT, message)

    # Log to terminal or file
    print(message)

if __name__ == "__main__":
    check_system()
