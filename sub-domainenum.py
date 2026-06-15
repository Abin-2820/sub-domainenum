import sys
import requests
import threading

# ---Argument---
if len(sys.argv)!=3:
    print(f"usage: python3 {sys.argv[0]} <domain> <wordlist>")
    exit()
domain = sys.argv[1]
wordlist = sys.argv[2]

# ---Wordlist---
try:
    subdomains = []
    with open(wordlist, "r") as file:
        for line in file:
            if line.strip():
                subdomains.append(line.strip())
        # for i in subdomains :
        #     print(i)
except FileNotFoundError:
    print(f"[!] wordlist not found: {wordlist}")
    exit()

# ---Core function---
total = len(subdomains)
lock = threading.Lock()

def check(sub):
    fullDomain = f"{sub}.{domain}"
    url = f"https://{fullDomain}"
    try:    
        requests.get(url, timeout=3)
        print(f"[+] found: {fullDomain}")
    except:
        pass
threads = []
print(f"[*] scanning {domain} | {total} subdomains\n")

for sub in subdomains:
    t = threading.Thread(target=check, args=(sub, ))
    threads.append(t)
    t.start()

    for t in threads:
        t.join()

print(f"\n[*] Done. {total} subdomains checked.")




