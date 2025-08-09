# 📡 NetScanner Suite – Python Network Scanner Collection


A growing collection of Python-based **network scanning tools** I am building to deepen my understanding of networking, port scanning, and vulnerability research.  
Each version is a step forward in complexity, speed, and professional reporting.

#### ⚠ **Disclaimer:** Use these tools **only** on systems you own or have explicit permission to test. Unauthorized scanning is illegal.

---

## 📂 Projects in This Suite

### 1️⃣ Basic Port Scanner – `netScan_ver1(beginner)/netScan.py`
**Purpose:** Learn Python socket programming & the basics of TCP port scanning.  
**Features:**
- Scans a fixed list of common ports
- Single-threaded
- Simple, readable output  
🔗 [View Basic Port Scanner](netScan_ver1(beginner)/README.md)

---

### 2️⃣ NetScan Pro – `netScan_ver2/netscan_Pro.py`
**Purpose:** Add professional features & speed improvements.  
**Features:**
- Custom port range scanning
- Service detection (e.g., 80 → HTTP)
- Built-in vulnerability database
- Multithreading for performance
- Color-coded results
- CSV export for reporting
- ASCII hacker-style banner  
🔗 [View NetScan Pro](netScan_ver2/README.md)

---


## 🛠 Installation
```bash
git clone https://github.com/abdurrahmanador/NetScanner.git
cd NetScanner
pip install colorama
```


---

## 📊 Feature Comparison

| Feature                          | Basic Port Scanner | NetScan Pro |
|----------------------------------|:-----------------:|:-----------:|
| Fixed Port List                  |        ✅         |     ❌      |
| Custom Port Range                |        ❌         |     ✅      |
| Service Detection                |        ❌         |     ✅      |
| Vulnerability Database           |        ❌         |     ✅      |
| Multithreading                   |        ❌         |     ✅      |
| CSV Export                       |        ❌         |     ✅      |
| Colorized Output                 |        ❌         |     ✅      |

---

## 🧠 Why This Suite Exists

- Documenting my learning progression from **beginner → advanced** network scanning
- Experimenting with different scanning techniques (single-threaded, multi-threaded, async)
- Practicing **secure coding** for networking tools
- Building **portfolio-ready, professional tools** for future cybersecurity work

---

## 🔋 Dependencies

- Python 3.8+
- colorama
- csv (built-in)
- socket (built-in)
- threading (built-in)

---

## 🎯 Next in Development

### NetScan Ultra 
- Asynchronous scanner with live progress bar & HTML report

### Vulnerability API Integration 
- Pull real-time CVEs from online sources

---

## 📜 License

MIT License

---

> *Contributions and feedback are welcome! Feel free to open issues or submit pull requests as you follow along in my network security journey.*

