import socket

def scan_target(ip, ports):
    print(f"\n[+] starting scanning on  target : {ip}")
    print("=" * 40)

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        else:
            print(f"[-] Port {port} is closed")

        s.close()

    print("=" * 40)
    print(f"[+] scanning completed on target : {ip}\n")

print("Welcome to the Port Scanner")
target_user = input("Enter the target IP address: ")

main_ports = [21, 22, 23, 25, 53, 80, 110, 443, 8080]
scan_target(target_user, main_ports)