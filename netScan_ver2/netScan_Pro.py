#Imports

import socket
from datetime import  datetime
from colorama import Fore,Style,init
import csv
import threading
from vuln_db import vuln_db

#initialize colorama
init()

#Banner,ASCII LOGO

print(Fore.MAGENTA+r'''
 ____  _____        _     ______                        
|_   \|_   _|      / |_ .' ____ \                       
  |   \ | |  .---.`| |-'| (___ \_|.---.  ,--.  _ .--.   
  | |\ \| | / /__\\| |   _.____`./ /'`\]`'_\ :[ `.-. |  
 _| |_\   |_| \__.,| |, | \____) | \__. // | |,| | | |  
|_____|\____|'.__.'\__/  \______.'.___.'\'-;__[___||__] 
                                                        
        NetScan Pro v1.5
     Author: Abdur Rahman
========================================
'''+Style.RESET_ALL)

# Disclaimer
print(Fore.YELLOW + "⚠ For educational and authorized use only!\n" + Style.RESET_ALL)

#target input
target=input("Enter Target IP or Hostname:")

#port range input
start_port=int(input("Enter Start Port: "))
end_port=int(input("Enter end Port: "))

print(f"\nScanning target:{target}")
print(f"Scan started at:{datetime.now()}")
print("=" * 50)

#store results

results=[]
threads=[]

#function to scan a single port
def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "UNKNOWN"
            vuln_info = vuln_db.get(port, "No known vulnerabilities in basic scan")
            print(Fore.GREEN + f"[+] Port {port} ({service}) is OPEN - {vuln_info}" + Style.RESET_ALL)
            results.append((port, service,"OPEN", vuln_info))
        s.close()
    except:
        pass

#multithreading for faster scanning

for port in range(start_port,end_port+1):
    t=threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

#save to CSV
with open('scan_results.csv', mode='w', newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["Port", "Service", "Status", "Vulnerability Info"])
    writer.writerows(results)


print("=" * 50)
print(f"Scan finished at: {datetime.now()}")
print(Fore.CYAN + "Results saved to scan_results.csv" + Style.RESET_ALL)