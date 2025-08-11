import requests 
import threading

domain = input('Enter the domain (e.g., youtube.com): ')

# with open('subdomains.txt', 'w' ) as file:
#     file.write('www\nmail\nblog\napi\ndev\ntest\nshop\nnews\nftp\ncpanel\n')
# subdomain_enum.py
with open('subdomains.txt') as file:
    subdomains = file.read().splitlines()

discovered_subdomains = []

lock = threading.Lock()

def check_subdomain(subdomain):
    for protocol in ["http", "https"]:
        url = f"{protocol}://{subdomain}.{domain}"
        try:
            requests.get(url, timeout=3)
        except requests.ConnectionError:
            pass
        else:
            print(f"Discovered subdomain: {url}")
            with lock:
                discovered_subdomains.append(url)


threads = []
# Create and start threads for each subdomain
# Wait for all threads to complete
for subdomain in subdomains:
    thread = threading.Thread(target=check_subdomain, args=(subdomain,))
    thread.start()
    threads.append(thread)
    

for thread in threads:
    thread.join()

with open('discovered_subdomains.txt', 'w') as file:
    for subdomain in discovered_subdomains:
        print(subdomain, file=file)