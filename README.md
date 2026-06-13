# Subdomain Enumerator

> A custom-built Python tool for subdomain enumeration — developed as part of my penetration testing toolkit.

---

## Built With

- Python 3
- Custom wordlist-based enumeration

---

## Usage

```bash
python subdomain_enum.py <domain> <wordlist.txt>
```

**Example:**
```bash
python subdomain_enum.py example.com rockyou.txt
```

---

## How It Works

The tool takes a target domain as input, iterates through a wordlist of common subdomain names, and attempts to resolve each one — reporting valid subdomains that exist.

---

## Disclaimer

This tool is intended for **authorized penetration testing and educational use only**. Do not use against systems you do not have permission to test.

---

## Author

**Abin Watson**  
Penetration Tester | eJPT Certified  
Specialising in Networks, Hosts, Endpoints & Web Applications
