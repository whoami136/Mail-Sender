cat << 'EOF' > README.md
# 🐦 Bird Mailer (SMTP Edition)

<p align="center">
  <img src="https://github.com" width="100%" alt="SMTP Mail Sender Tool Interface">
</p>

An interactive, color-coded terminal CLI tool engineered for custom HTML email generation, priority warning styling, and secure file dispatch via SMTP.

## 📝 Description

### Short Description
An interactive, color-coded terminal CLI tool engineered for custom HTML email generation, priority warning styling, and secure file dispatch via SMTP.

### Long Description
Bird Mailer is a lightweight, responsive Command Line Interface (CLI) utility built entirely in Python. It modernizes manual email testing workflows by enabling developers to assemble visually styled multipart HTML notifications straight from the console. By abstracting core `smtplib` and `MIME` libraries, it delivers robust message architecture packaging. 

The application implements a unique five-tier visual priority envelope system that applies customized CSS background-color wrappers, border accents, and high-visibility header emblems based on urgency. It handles stream processing for robust Base64 binary attachment encoding natively, ensuring that verification payloads, documents, or data captures pass through mail relay infrastructure safely to any target inbox.

---

## ⚙️ Requirements & Installation

Run these setup commands inside your terminal to install prerequisites and prepare the framework:

```bash
# Update local packages and install Python core binaries
sudo apt update && sudo apt install -y python3 python3-pip

# Clone your synchronized repository
git clone git@github.com:whoami136/Mail-Sender.git
cd Mail-Sender

# Run the utility natively from any directory path
python3 mailer.py
```

---

## 🌟 Key Features

* **Visual Priorities:** Render 5 separate CSS high-priority responsive container alerts dynamically.
* **Streamlined UI:** Full ANSI terminal color coding with an animated introductory ASCII banner layout.
* **Masked Identity:** Hardcoded custom display signature masking your email transport routing information.
* **Safe Input Boundaries:** Automatic string cleaning parameters tracking formatting inputs or accidental white spaces.
* **Binary Processing:** Automated Base64 attachment packaging natively supporting arbitrary extension types.

---
Created By Nur (Whoami)  
Released under the MIT License.
EOF
