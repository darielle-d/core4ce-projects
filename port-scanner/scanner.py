import socket

from datetime import datetime

# common ports and what they do
common_ports = {
    20: "FTP Data",
    21: "FTP Control",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
}

# asking user to put in their IP address
target = input("Enter the target IP address ")

# log start time
print(f"\nStarting scan on {target} at {datetime.now()}")


# range of ports to scan 
start_port = 20 
end_port = 110

print(f"\nScanning ports {start_port} to {end_port}...\n")

# loop through each port in range
for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.1) # how long after no response

    result = sock.connect_ex((target, port))
    if result == 0:
        # get the service name from dictionary or default to UNKNOWN
        service = common_ports.get(port, "UNKNOWN SERVICE")
        print(f"Port {port} is OPEN ({service})")
        sock.close()
print(f"\nScan completed at {datetime.now()}")
