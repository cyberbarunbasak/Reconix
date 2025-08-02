# 🔎 Reconix – Terminal Recon Tool in Python

**Reconix** is a fast, terminal-based reconnaissance and port scanning tool developed for ethical hacking, CTFs, and cybersecurity enthusiasts.

> ⚠ For educational use only. Unauthorized scanning is illegal.

---

## 🚀 Features

- ⚡ Multi-threaded TCP port scanner (1–1024)
- 🔍 Service detection (with banner grabbing)
- 🌐 Exploit-DB link suggestions based on service
- 📄 Auto-generates detailed `<ip>.txt` scan report
- 🖥 Simple terminal usage with no external dependencies
- 🧑‍💻 100% Python – no login, no API keys

---


## 🛠 Installation

```bash
git clone https://github.com/cyberbarunbasak/Reconix.git
cd Reconix
pip3 install requests
python3 scanner.py

## 🧪 Usage

```bash
python3 scanner.py <target>
```

Example:

```bash
python3 scanner.py example.com
```

## 📝 Output
📄 Scan Report for 192.168.xx.xx

[+] Port 22/tcp OPEN | Service: ssh | Version: OpenSSH 8.2
↪ Possible exploits: https://www.exploit-db.com/search?cve=&description=ssh

[+] Port 80/tcp OPEN | Service: http | Version: Apache 2.4.41
↪ Possible exploits: https://www.exploit-db.com/search?cve=&description=http

```

## 📌 Legal Disclaimer
This tool is intended for educational purposes only.
Unauthorized scanning or recon on systems you do not own is strictly illegal.


🙌 Support & Connect
If you found Reconix useful, please consider:


⭐ Starring this repository

👤 Following me on GitHub
