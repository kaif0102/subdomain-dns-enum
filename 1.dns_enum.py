# dns_enum.py
import dns.resolver

target_domain = input("Enter the domain to enumerate DNS records: ")
records_type = ['A', 'AAAA', 'CNAME', 'MX', 'TXT', 'SOA', 'NS']

resolver = dns.resolver.Resolver()
for record_type in records_type:
    try:
        answer = resolver.resolve(target_domain, record_type)
    except dns.resolver.NoAnswer:
        print(f"No {record_type} records found for {target_domain}.")
        continue
    print(f"{record_type} records for {target_domain}:")
    for data in answer:
        print(f" {data}")