import socket

common_services = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    135: "RPC",
    139: "NetBIOS",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP"
}

target = input("Enter target IP: ")
start_port = int(input("Start port: "))
end_port = int(input("End port: "))

print(f"\nScanning {target}...\n")

open_ports = []

for port in range(start_port, end_port + 1):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(0.5)

    result = scanner.connect_ex((target, port))

    if result == 0:
        service = common_services.get(port, "Unknown Service")
        print(f"[OPEN] Port {port} → {service}")
        open_ports.append(port)

    scanner.close()

print("\nScan complete.")

print(f"\nTotal Open Ports Found: {len(open_ports)}")
