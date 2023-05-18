import nmap

target_host = input("Enter the target IP address or hostname: ")
target_ports = input("Enter the target ports (comma-separated): ").split(',')

nm = nmap.PortScanner()
nm.scan(target_host, ','.join(target_ports), arguments='-sV')

for host in nm.all_hosts():
    print(f"Host: {host}")
    print(f"State: {nm[host].state()}")
    for proto in nm[host].all_protocols():
        print(f"\nProtocol: {proto}")
        ports = nm[host][proto].keys()
        for port in ports:
            service = nm[host][proto][port]['name']
            product = nm[host][proto][port]['product']
            version = nm[host][proto][port]['version']
            print(f"Port: {port}\tService: {service}\tProduct: {product}\tVersion: {version}")
