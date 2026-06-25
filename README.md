# Subdomain Enumerator

A fast, multi-threaded subdomain enumeration tool written in Python. Accepts any custom wordlist, making it flexible for different reconnaissance scenarios.

---

## Features

- Multi-threaded scanning for fast enumeration
- Custom wordlist support — bring your own wordlist
- Clean, minimal output showing only discovered subdomains
- Lightweight — single script, one dependency

---

## Requirements

- Python 3.x
- requests

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

```bash
python3 sub-domainenum.py <domain> <wordlist>
```

**Example:**

```bash
python3 sub-domainenum.py google.com wordlist.txt
```

---

## Sample Output

```
[*] Scanning google.com | 6 subdomains

[+] Found: admin.google.com

[*] Done. 6 subdomains checked.
```

## Author 
Abin Watson | eJPT 

Date: June 2026

