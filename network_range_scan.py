import nmap

target_network = input("Enter the target network range (CIDR notation): ")

nm = nmap.PortScanner()
nm.scan(target_network, arguments='-sn')

for host in nm.all_hosts():
    print(f"Host: {host}")
    print(f"State: {nm[host].state()}")
