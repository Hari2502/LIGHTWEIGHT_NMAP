import nmap

target_hosts = input("Enter the target IP addresses or hostnames (comma-separated): ").split(',')
target_ports = input("Enter the target ports (comma-separated): ").split(',')

nm = nmap.PortScanner()

for target_host in target_hosts:
    nm.scan(target_host, ','.join(target_ports))
    for host in nm.all_hosts():
        print(f"Host: {host}")
        print(f"State: {nm[host].state()}")
        for proto in nm[host].all_protocols():
            print(f"\nProtocol: {proto}")
            ports = nm[host][proto].keys()
            for port in ports:
                print(f"Port: {port}\tState: {nm[host][proto][port]['state']}")
        print()
