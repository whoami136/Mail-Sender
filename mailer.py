import sys
import time
import os
import resend

# ===== COLORS =====
G = '\033[1;32m'
B = '\033[1;34m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'
R = '\033[1;31m'

CONFIG_FILE = ".resend_config"

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
         MAIL TOOL(Creator:Nur)
             Bird Edition 🐦
=====================================
"""

print("\033[H\033[J")
print(banner)
slow_print(G + "[+] Bird Mail System Loaded via Resend API...\n")

# ===== SMART API KEY STORAGE SYSTEM =====
api_key = ""

if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, "r") as f:
        api_key = f.read().strip()
    
    print(G + f"[+] Automatically loaded your saved Resend API Key.")
    change_key = input(Y + "Do you want to change/reset this key? (y/N): " + W).lower()
    
    if change_key == "y":
        api_key = input(G + "Enter NEW Resend API Key (re_...): " + Y).replace(" ", "")
        if api_key:
            with open(CONFIG_FILE, "w") as f:
                f.write(api_key)
            slow_print(G + "[+] New API Key updated and saved permanently!")
        else:
            slow_print(R + "[ERROR] Key cannot be blank. Exiting.")
            sys.exit()
else:
    # First time configuration setup
    slow_print(Y + "[!] First-time setup detected.")
    api_key = input(G + "Enter your Resend API Key (re_...): " + Y).replace(" ", "")
    if api_key:
        with open(CONFIG_FILE, "w") as f:
            f.write(api_key)
        slow_print(G + "[+] API Key saved permanently! You won't have to type it next time.")
    else:
        slow_print(R + "[ERROR] API key cannot be blank. Exiting.")
        sys.exit()

# Configure the Resend Engine with the loaded/updated key
resend.api_key = api_key

# ===== USER INPUTS =====
to_email = input(G + "Send To: " + Y)
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
    <small>🐦 Sent via Bird Resend Mailer</small>

    </body>
    </html>
    """
    msg_subject = f"{warning_title} | {subject}"

# ===== ATTACHMENT SETUP =====
file_path = input(G + "Attach file path (ENTER to skip): " + Y)
attachments_list = []

if file_path:
    if os.path.exists(file_path):
        attachments_list.append({
            "filename": os.path.basename(file_path),
            "path": file_path
        })
        slow_print(C + "[+] File attached safely 🐦")
    else:
        slow_print(R + "[!] File not found, continuing without attachment.")

# ===== BUILD AND EXECUTE RESEND PARAMETERS =====
# "Whoami" is now hardcoded as requested
params = {
    "from": "Whoami <onboarding@resend.dev>",
    "to": [to_email],
    "subject": msg_subject,
    "html": html_body,
}

if attachments_list:
    params["attachments"] = attachments_list

try:
    slow_print(C + "\n[+] Connecting to Resend Cloud Infrastructure...")
    slow_print(C + "[+] Delivering message...")
    
    email_response = resend.Emails.send(params)
    
    print()
    slow_print(G + "[SUCCESS] Email dispatched safely via Resend! 🐦")
    print(G + f"Message ID: {email_response.get('id')}")

except Exception as e:
    print()
    slow_print(R + "[ERROR] Delivery through Resend failed")
    print(R + str(e))

print()
slow_print(W + "Process completed.")
