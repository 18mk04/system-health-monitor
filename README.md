
# 🖥️ System Health Monitor (Linux)

A lightweight system health monitoring tool using **Python** and **Bash** that tracks CPU, RAM, disk usage, and active processes on Linux systems. Sends email alerts when thresholds are breached.

---

## 🚀 Features

- ✅ Monitors CPU, RAM, and Disk usage in real time  
- ✅ Alerts sent via email when thresholds are exceeded  
- ✅ Scheduled using `cron` to run automatically  
- ✅ Configurable settings through a `config.json` file  
- ✅ Lightweight and easy to set up  


---

## 🛠️ Tech Stack

- **Python 3**
  - `psutil`
  - `smtplib`, `email`
  - `os`, `subprocess`
- **Bash**
- **Linux Cron Jobs**
- **Sendmail / SMTP**

---

## ⚙️ Configuration (`config.json`)

\`\`\`json
{
  "cpu": 75,
  "ram": 80,
  "disk": 85,
  "to": "your_email@example.com",
  "from": "monitor@example.com",
  "smtp_server": "localhost",
  "smtp_port": 25
}
\`\`\`

> Adjust thresholds and email settings as needed.

---

## 📦 Installation & Setup

1. **Clone this repo**
   \`\`\`bash
   git clone https://github.com/yourusername/system-health-monitor.git
   cd system-health-monitor
   \`\`\`

2. **Install dependencies**
   \`\`\`bash
   pip install psutil
   \`\`\`

3. **Make scripts executable**
   \`\`\`bash
   chmod +x monitor.sh setup_cron.sh
   \`\`\`

4. **Run the monitor manually**
   \`\`\`bash
   ./monitor.sh
   \`\`\`

---

## ⏱️ Set Up Cron Job

Schedule the monitor to run every 5 minutes:

\`\`\`bash
./setup_cron.sh
\`\`\`

This script adds the following entry to your crontab:
\`\`\`
*/5 * * * * /full/path/to/monitor.sh
\`\`\`

---

## ✉️ Email Alert

When thresholds (e.g., CPU > 75%) are crossed, an email is sent with the system status. You can use:
- `sendmail` for localhost
- `smtp.gmail.com` with port 587 (with additional setup)

---

## 📌 Example Alert

> ⚠️ High CPU Usage Detected  
> CPU Usage: 82%  
> RAM Usage: 78%  
> Disk Usage: 68%

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Marikannan P**  
[GitHub](https://github.com/18mk04) • [LinkedIn](https://linkedin.com/in/marik1804)

---

## 🙌 Contributions

Feel free to fork this repo, suggest features, or report issues via pull requests or GitHub Issues.

