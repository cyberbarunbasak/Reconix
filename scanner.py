
import socket
import threading
import requests

# Fancy banner
banner = """
██████╗ ███████╗ ██████╗ ██████╗ ██████╗ ██╗  ██╗██╗  ██╗
██╔══██╗██╔════╝██╔════╝ ██╔══██╗██╔══██╗██║ ██╔╝╚██╗██╔╝
██████╔╝█████╗  ██║  ███╗██████╔╝██████╔╝█████╔╝  ╚███╔╝ 
██╔═══╝ ██╔══╝  ██║   ██║██╔═══╝ ██╔═══╝ ██╔═██╗  ██╔██╗ 
██║     ███████╗╚██████╔╝██║     ██║     ██║  ██╗██╔╝ ██╗
╚═╝     ╚══════╝ ╚═════╝ ╚═╝     ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝
            Terminal Reconnaissance Tool
"""
print(banner)
print("🔧 Developed by Barun Basak")
print("⚠️  WARNING: This tool is intended for EDUCATIONAL PURPOSES ONLY. Unauthorized scanning is illegal.\n")

# Get user input for IP address
target = input("📍 Enter target IP address: ").strip()
print(f"📡 Scanning target: {target} (this may take a while...)\n")

# Output file based on IP
output_file = f"{target}.txt"

ports = range(1, 1025)
open_ports = []
detailed_results = []

def get_version_banner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((ip, port))
        s.send(b"\r\n")
        banner = s.recv(1024).decode(errors="ignore").strip()
        return banner if banner else "Unknown version"
    except:
        return "Unknown version"

def check_exploit_db(service_name):
    try:
        url = f"https://www.exploit-db.com/search?cve=&description={service_name}"
        return url  # Placeholder link
    except:
        return None

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "unknown"
            banner = get_version_banner(target, port)
            exploit_link = check_exploit_db(service)
            report = f"[+] Port {port}/tcp OPEN | Service: {service} | Version: {banner}"
            if exploit_link:
                report += f"\n    ↪ Possible exploits: {exploit_link}"
            print(report)
            open_ports.append(port)
            detailed_results.append(report)
        s.close()
    except Exception:
        pass

threads = []
for port in ports:
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

with open(output_file, "w") as f:
    f.write(f"📄 Scan Report for {target}\n")
    f.write(f"Developed by Barun Basak | For educational use only\n\n")
    f.write("\n".join(detailed_results))
    f.write("\n\n✔️ Thanks For Using , Have a Good Day\n")

print(f"✅ Scan complete. Report saved to {output_file}")
print("✔️ Thanks For Using , Have a Good Day")
