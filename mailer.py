import smtplib
import sys
import time
import os
import getpass

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# ===== COLORS =====
G = '\033[1;32m'
B = '\033[1;34m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'
R = '\033[1;31m'

def slow_print(text):
    for c in text + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

# ===== BIRD ASCII BANNER =====
banner = rf"""
{G}
                   _.:._
                 ."\ | /".
{B}.,__            "=.\:/.="            __,.
{Y} "=.`"=._          /^\          _.="`.="
{C}   ".'.'."=.=.=.=.     .'.'.'.'.'.'."
{G}     `~.`.`.`.`.`.`.   .'.'.'.'.'.~`
{B}        `~.` ` `.`.`   .'.'.'.'.~`
{C}            `=.-~~-._ ) ( _.-~~-.=`
{Y}                    \ /
{G}                     ( )
{B}                      Y

=====================================
        SMTP MAIL SENDER TOOL
             Bird Edition 🐦
=====================================
"""

print("\033[H\033[J")
print(banner)
slow_print(G + "[+] Bird Mail System Loaded...\n")

# ===== INPUTS =====
smtp_server = input(G + "SMTP Server (smtp.gmail.com): " + Y)
if not smtp_server:
    smtp_server = " smtp.gmail.com"

smtp_port_input = input(G + "SMTP Port (587): " + Y)
smtp_port = int(smtp_port_input) if smtp_port_input else 587

email = input(G + "Your Email: " + Y)
password = getpass.getpass(G + "App Password: " + Y).replace(" ", "")

to = input(G + "Send To: " + Y)
subject = input(G + "Subject: " + Y)
message = input(G + "Message: " + Y)

# ===== PRIORITY SYSTEM =====
priority = input(G + "Make HIGH PRIORITY? (y/n): " + Y).lower()

msg_subject = subject
html_body = f"""
<html>
<body style="font-family:Arial;padding:20px;">
    <h3>🐦 {subject}</h3>
    <p>{message}</p>
</body>
</html>
"""

if priority == "y":
    print("\nChoose Warning Type:")
    print("1) ⚠️ BE CAREFUL WITH THIS MESSAGE")
    print("2) 📢 IMPORTANT MESSAGE")
    print("3) 🚨 URGENT MESSAGE")
    print("4) 🔒 CONFIDENTIAL MESSAGE")
    print("5) ⚡ ACTION REQUIRED")

    choice = input(G + "Select (1-5): " + Y)

    warning_title = "⚠️ BE CAREFUL WITH THIS MESSAGE"
    warning_color = "#ffcc00"
    warning_bg = "#fff7b2"

    if choice == "2":
        warning_title = "📢 IMPORTANT MESSAGE"
        warning_color = "#0066cc"
        warning_bg = "#e6f2ff"
    elif choice == "3":
        warning_title = "🚨 URGENT MESSAGE"
        warning_color = "#d60000"
        warning_bg = "#ffd6d6"
    elif choice == "4":
        warning_title = "🔒 CONFIDENTIAL MESSAGE"
        warning_color = "#333333"
        warning_bg = "#f0f0f0"
    elif choice == "5":
        warning_title = "⚡ ACTION REQUIRED"
        warning_color = "#ff6600"
        warning_bg = "#fff0e6"

    html_body = f"""
    <html>
    <body style="font-family:Arial;background-color:{warning_bg};padding:20px;">

    <div style="background:{warning_color};
                color:white;
                padding:15px;
                border-left:10px solid orange;
                font-size:18px;
                font-weight:bold;">
        {warning_title}
    </div>

    <br>

    <div style="background:white;padding:15px;border:1px solid #ddd;">
        <h2>{warning_title}</h2>
        <p>{message}</p>
    </div>

    <br>
    <small>🐦 Sent via Bird SMTP Mailer</small>

    </body>
    </html>
    """

    msg_subject = f"{warning_title} | {subject}"

# ===== BUILD EMAIL =====
msg = MIMEMultipart("alternative")
msg["From"] = f"Whoami <{email}>"
msg["To"] = to
msg["Subject"] = msg_subject

msg.attach(MIMEText(html_body, "html"))

# ===== ATTACHMENT =====
file_path = input(G + "Attach file (ENTER to skip): " + Y)

if file_path:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(f.read())

        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={os.path.basename(file_path)}"
        )

        msg.attach(part)
        slow_print(C + "[+] File attached 🐦")
    else:
        slow_print(R + "[!] File not found")

# ===== SEND EMAIL =====
try:
    slow_print(C + "\n[+] Connecting SMTP...")
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.ehlo()
    server.starttls()

    slow_print(C + "[+] Logging in...")
    server.login(email, password)

    slow_print(C + "[+] Sending email...")
    server.send_message(msg)
    server.quit()

    slow_print(G + "[SUCCESS] Email sent 🐦")

except Exception as e:
    slow_print(R + "[ERROR] Failed")
    print(R + str(e))

slow_print(W + "Done.")
