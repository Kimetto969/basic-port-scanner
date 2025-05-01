import socket
from datetime import datetime

def scan_ports(target_ip, start_port, end_port):
    print(f"\n[+] Scanning {target_ip} from port {start_port} to {end_port}...")
    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target_ip, port))  # 0 if port is open
            if result == 0:
                open_ports.append(port)
            s.close()
        except KeyboardInterrupt:
            print("\n[!] Scan interrupted by user.")
            break
        except socket.gaierror:
            print("[!] Invalid hostname or IP.")
            break
        except socket.error:
            print("[!] Could not connect to server.")
            break

    return open_ports

def main():
    print("=== Basic Port Scanner ===")
    target = input("Enter target IP address: ")

    try:
        socket.inet_aton(target)  # Validate IP
    except socket.error:
        print("[!] Invalid IP format.")
        return

    try:
        start_port = int(input("Enter starting port (e.g., 20): "))
        end_port = int(input("Enter ending port (e.g., 100): "))
        if start_port < 0 or end_port > 65535 or start_port > end_port:
            raise ValueError
    except ValueError:
        print("[!] Invalid port range.")
        return

    start_time = datetime.now()
    open_ports = scan_ports(target, start_port, end_port)
    duration = datetime.now() - start_time

    if open_ports:
        print(f"\n[+] Open ports on {target}: {open_ports}")
    else:
        print(f"\n[-] No open ports found on {target} in that range.")
    print(f"[i] Scan completed in {duration}")

if __name__ == "__main__":
    main()
