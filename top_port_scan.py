import nmap

target_host = input("Enter the target IP address or hostname: ")

nm = nmap.PortScanner()
nm.scan(target_host, arguments='-F')

for host in nm.all_hosts():
    print(f"Host: {host}")
    print(f"State: {nm[host].state()}")
    for proto in nm[host].all_protocols():
        print(f"\nProtocol: {proto}")
        ports = nm[host][proto].keys()
        for port in ports:
            print(f"Port: {port}\tState: {nm[host][proto][port]['state']}")
