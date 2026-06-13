import sys
import requests
import threading
from concurrent.futures import ThreadPoolExecutor
# ---Argument---
if len(sys.argv) !=3:
    print(f"usage: {sys.argv[0]} <domain> <wordlist>")
    exit()
domain = sys.argv[1]
wordlist = sys.argv[2]
# print(domain)

# ---Loading Wordlist---
try:
    with open(wordlist,"r") as file:
        subdomains = [line.strip() for line in file if line.strip()]
except:
    print(f"[!] Wordlist not found: {wordlist}")
    exit()

    total = len(subdomains)
    checked = 0
    checked_lock = threading.Lock()

    # ---Prograss Listener---
    def progress_watcher():
        while True:
            input()
            with checked_lock:
                print(f"\n[*] Prograss: {checked}/{total} checked")
    
    watcher = threading.Thread(target=progress_watcher, daemon=True)
    watcher.start()

    # ---Core Function---
    def check_subdomain(sub):
        global checked
        full_domain = f"{sub}.{domain}"
        url = f"https://{full_domain}"
        try:
            response = requests.get (url, timeout=3)
            print(f"[+] found: {full_domain} (Status: {response.status_code})")
        except requests.ConnectionError:
            pass
        except requests.Timeout:
            pass
        finally:
            with checked_lock:
                checked += 1
    
    # ---Run with threading---
    print(f"[*] starting enumeration on {domain} | {total} subdomains | press Enter for progress\n")
    with ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(check_subdomain, subdomains)

    print(f"\n[*] Done. {total} subdomains checked.") 
