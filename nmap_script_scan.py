import nmap

target_host = input("Enter the target IP address or hostname: ")
target_ports = input("Enter the target ports (comma-separated): ").split(',')
script_name = input("Enter the name of the Nmap script to execute: ")

nm = nmap.PortScanner()
nm.scan(target_host, ','.join(target_ports), arguments=f'--script={script_name}')

for host in nm.all_hosts():
    print(f"Host: {host}")
    print(f"State: {nm[host].state()}")
    if 'script' in nm[host]:
        for script in nm[host]['script']:
            print(f"Script ID: {script}\tResult: {nm[host]['script'][script]}")
    else:
        print("No scripts found.")
