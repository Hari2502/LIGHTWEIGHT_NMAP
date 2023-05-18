import nmap

target_host = input("Enter the target IP address or hostname: ")
target_ports = input("Enter the target ports (comma-separated): ").split(',')

nm = nmap.PortScanner()
nm.scan(target_host, ','.join(target_ports), arguments='-oX scan_results.xml')

print(f"Scan results saved to scan_results.xml file.")
