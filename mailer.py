import smtplib
import sys
import time
from email.mime.text import MIMEText

# ===== COLORS =====
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'

def slow_print(text):
    for c in text + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

# ===== 3 TRIANGLE ASCII LOGO =====
logo = f"""
{C}        /\           /\           /\ 
{C}       /  \         /  \         /  \ 
{G}      / /\ \       / /\ \       / /\ \ 
{G}     / /  \ \     / /  \ \     / /  \ \ 
{Y}    / /----\ \   / /----\ \   / /----\ \ 
{Y}   /_/      \_\ /_/      \_\ /_/      \_\ 

{W}   =====================================
{C}          SMTP MAIL SENDER TOOL
{G}               Created by Nur
{W}   =====================================
"""

def banner():
    print("\033[H\033[J")
    print(logo)
    slow_print(G + "[+] Starting SMTP Mail System...\n")

banner()

# ===== SMTP SETTINGS =====
smtp_server = input(G + "SMTP Server (smtp.gmail.com): " + Y)
if not smtp_server:
    smtp_server = "smtp.gmail.com"

smtp_port_input = input(G + "SMTP Port (587): " + Y)
smtp_port = int(smtp_port_input) if smtp_port_input else 587

email = input(G + "Your Email: " + Y)
password = input(G + "App Password: " + Y).replace(" ", "")

print()
to = input(G + "Send To: " + Y)
subject = input(G + "Subject: " + Y)
message = input(G + "Message: " + Y)

# ===== EMAIL BUILD =====
msg = MIMEText(message)
msg["From"] = email
msg["To"] = to
msg["Subject"] = subject

try:
    slow_print(C + "\n[+] Connecting to SMTP server...")
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    slow_print(C + "[+] Logging in...")
    server.login(email, password)

    slow_print(C + "[+] Sending email...")
    server.send_message(msg)
    server.quit()

    print()
    slow_print(G + "[SUCCESS] Email sent successfully!")

except Exception as e:
    print()
    slow_print(R + "[ERROR] Failed to send email")
    print(R + str(e))

print()
slow_print(W + "Process completed.")

