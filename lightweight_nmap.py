import nmap

def scan_ports(target_host, target_ports):
    nm = nmap.PortScanner()
    nm.scan(target_host, ','.join(target_ports))

    for host in nm.all_hosts():
        print(f"Host: {host}")
        print(f"State: {nm[host].state()}")
        for proto in nm[host].all_protocols():
            print(f"\nProtocol: {proto}")
            ports = nm[host][proto].keys()
            for port in ports:
                print(f"Port: {port}\tState: {nm[host][proto][port]['state']}")

# User input
target_host = input("Enter the target IP address or hostname: ")
target_ports = input("Enter the target ports (comma-separated): ").split(',')

scan_ports(target_host, target_ports)
