markdown
Copy code
# Nmap Python Programs

This repository contains a collection of Python programs for network scanning and port enumeration using the Nmap library. Each program focuses on different aspects of network reconnaissance and can be used for various purposes, including port scanning, service version detection, OS fingerprinting, script scanning, and more.

## Prerequisites

- Python 3.x
- python-nmap package

## Installation

1. Clone the repository or download the project files:

   ```bash
   git clone https://github.com/your-username/nmap-python-programs.git
Install the required dependencies using pip:

bash
Copy code
pip install -r requirements.txt
Programs
Below is an overview of the programs available in this repository:

Basic Port Scanner: Perform a basic port scan on a target IP address or hostname. [View Program]

Service Version Detection: Scan for open ports and determine the service version running on each port. [View Program]

OS Fingerprinting: Conduct OS fingerprinting to identify the operating system of the target host. [View Program]

Script Scanning: Perform script scanning using default scripts available in Nmap. [View Program]

UDP Port Scanning: Perform port scanning for UDP protocols instead of TCP. [View Program]

IPv6 Port Scanning: Perform port scanning on IPv6 addresses or hostnames. [View Program]

Aggressive Scan: Perform an aggressive scan with more comprehensive scanning options. [View Program]

Output to XML File: Save the scan results to an XML file for further analysis. [View Program]

Output to CSV File: Save the scan results to a CSV file for easy data manipulation. [View Program]

Scan Multiple Hosts: Scan multiple target hosts in a single run. [View Program]

Scan Top Ports: Perform a scan on the top common ports instead of scanning all ports. [View Program]

Scan Network Range: Scan a range of IP addresses within a network using CIDR notation. [View Program]

Scan Using a Specific Nmap Script: Execute a specific Nmap script during the scan for advanced analysis. [View Program]

Scan Target from a File: Read a list of target IP addresses or hostnames from a file and perform the scan. [View Program]

Scan Using a Configuration File: Perform a scan using a pre-defined Nmap configuration file. [View Program]

Usage
Choose the desired program based on the specific scanning requirements.

Run the program using the following command:

bash
Copy code
python program_name.py
Follow the instructions prompted by the program to enter the target information, such as IP addresses, hostnames, or ports.

The program will perform the network scanning based on the specified options and display the scan results accordingly.

License
MIT License

Disclaimer
These programs are meant for educational and authorized testing purposes only. The author and the organization are not responsible
