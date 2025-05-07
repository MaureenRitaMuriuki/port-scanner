import socket
from datetime import datetime

# Define a function to scan ports
def scan_ports(target):
    print(f"Scanning target: {target}")
    
    # Start time
    start_time = datetime.now()
    print(f"Scan started at: {start_time}")

    # Try connecting to the first 1000 ports
    for port in range(1, 1001):
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        # Try to connect to the target on each port
        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"Port {port} is open")
        sock.close()

    # End time
    end_time = datetime.now()
    print(f"Scan finished at: {end_time}")
    print(f"Scan duration: {end_time - start_time}")

if __name__ == "__main__":
    target = input("Enter target IP or hostname: ")
    scan_ports(target)
