import socket
from datetime import datetime

target_ip=input("Enter target IP::: ")
common_port=[21,22,23,25,53,80,110,443,20]

print(f"\nScanning target: {target_ip}")
print(f"Scan started at: {datetime.now()}")
print("=" * 50)


for port in common_port:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result=sock.connect_ex((target_ip, port))
        if result==0:
            print(f"[+] Port {port} is open")
        else:
            print(f"[-] Port {port} is closed")
        sock.close()
    except KeyboardInterrupt:
        print("\nScan stopped by user.")
        break
    except socket.gaierror:
        print("❌ Hostname could not be resolved.")
        break
    except socket.error:
        print("❌ Could not connect to server.")
        break
    print("=" * 50)
    print(f"Scan finished at: {datetime.now()}")
