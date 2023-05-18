# Nmap Port Scanner

A simple port scanning tool implemented in Python using the Nmap library. This tool allows you to scan a target IP address or hostname for open ports.

## Prerequisites

- Python 3.x
- python-nmap package

## Installation

1. Clone the repository or download the project files:

   ```bash
   git clone https://github.com/your-username/nmap-port-scanner.git

2. Install the required dependencies using pip:

pip install -r requirements.txt

Usage
Run the port_scanner.py script:

python port_scanner.py

Enter the target IP address or hostname when prompted.

Enter the target ports to scan, separated by commas.

The program will perform the port scan and display the results, including the host, protocol, port, and its state (open, closed, filtered, etc.).

Example

Enter the target IP address or hostname: 127.0.0.1
Enter the target ports (comma-separated): 22,80,443

Host: 127.0.0.1
State: up

Protocol: tcp
Port: 22	State: open
Port: 80	State: closed
Port: 443	State: closed


License
MIT License

Disclaimer
This tool is meant for educational and authorized testing purposes only. The author and the organization are not responsible for any unauthorized or illegal use of this program. Use it at your own risk and ensure you have proper authorization before scanning any network or system.


Feel free to customize the content as per your requirements. Don't forget to include the appropriate license file (e.g., LICENSE) in your repository.
