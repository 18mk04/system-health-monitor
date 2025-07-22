#!/bin/bash

echo "*/5 * * * * /home/mk/System_Health/system-health-monitor/monitor.sh" | crontab -
echo "✅ Cron job scheduled to run every 5 minutes."
