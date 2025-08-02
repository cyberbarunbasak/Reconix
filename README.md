<h1 align="center">🔎 Reconix</h1>
<p align="center">A blazing-fast terminal reconnaissance tool for ethical hackers, CTF players, and cybersecurity analysts.</p>

<p align="center">
  <img src="https://img.shields.io/badge/Made%20With-Python3-blue?style=flat-square">
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square">
  <img src="https://img.shields.io/github/last-commit/cyberbarunbasak/Reconix?style=flat-square">
</p>

---

## 🚀 Features

* ⚡ Multi-threaded TCP port scanner (ports 1–1024)
* 🔍 Service detection with banner grabbing
* 🌐 Suggests relevant exploits via Exploit-DB
* 📜 Auto-generates detailed `<ip>.txt` report
* 🖥️ Simple terminal interface (no GUI)
* 🧑‍💻 100% Python – no logins, no API keys, no external binaries

---

## 📸 Demo

Below are real usage screenshots of Reconix in action:

### 🖥 Terminal Scan Interface

![Screenshot](assets/screenshots/Screenshot%202025-08-02%20101821.png)

### 🧾 Output with Exploit Links

![Screenshot](assets/screenshots/Screenshot%202025-08-02%20102012.png)

📁 View folder: [assets/screenshots](https://github.com/cyberbarunbasak/Reconix/tree/main/assets/screenshots)

---

## 🛠️ Installation

```bash
git clone https://github.com/cyberbarunbasak/Reconix.git
cd Reconix
pip3 install requests
python3 scanner.py
```

---

## 🧪 Usage

```bash
python3 scanner.py <target>
```

**Example:**

```bash
python3 scanner.py 192.168.50.129
```

---

## 📄 Sample Output

```bash
📄 Scan Report for 192.168.xxx.xx

[+] Port 22/tcp OPEN | Service: ssh | Version: OpenSSH 8.2
    ↪ Possible exploits: https://www.exploit-db.com/search?cve=&description=ssh

[+] Port 80/tcp OPEN | Service: http | Version: Apache 2.4.41
    ↪ Possible exploits: https://www.exploit-db.com/search?cve=&description=http

✔ Thanks For Using , Have a Good Day
```

A file like `192.168.xxx.xx.txt` will be saved in your project folder.

---

## ⚖️ Legal Disclaimer

> **Reconix is intended for educational and ethical use only.**
> Unauthorized scanning or reconnaissance on systems you do not own is illegal and punishable under law.

---

## 🙌 Support & Connect

If you found **Reconix** useful:

* ⭐ Star this repository to support the project
* 👤 [Follow me on GitHub](https://github.com/cyberbarunbasak)
* 🔁 Share with your cybersecurity friends and CTF teams

---

## 📄 License

This project is licensed under the [MIT License](https://github.com/cyberbarunbasak/Reconix/blob/main/LICENSE).
