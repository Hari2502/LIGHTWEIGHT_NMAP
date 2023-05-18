import nmap

target_host = input("Enter the target IP address or hostname: ")

nm = nmap.PortScanner()
nm.scan(target_host, arguments='-O')

for host in nm.all_hosts():
    print(f"Host: {host}")
    print(f"State: {nm[host].state()}")
    if 'osmatch' in nm[host]:
        for match in nm[host]['osmatch']:
            print(f"OS Name: {match['name']}\tAccuracy: {match['accuracy']}")
    else:
        print("OS information not available.")
