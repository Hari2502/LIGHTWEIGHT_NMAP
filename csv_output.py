import csv
import nmap

target_host = input("Enter the target IP address or hostname: ")
target_ports = input("Enter the target ports (comma-separated): ").split(',')

nm = nmap.PortScanner()
nm.scan(target_host, ','.join(target_ports))

output_file = 'scan_results.csv'

with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Host', 'Protocol', 'Port', 'State'])
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            ports = nm[host][proto].keys()
            for port in ports:
                writer.writerow([host, proto, port, nm[host][proto][port]['state']])

print(f"Scan results saved to {output_file} file.")
