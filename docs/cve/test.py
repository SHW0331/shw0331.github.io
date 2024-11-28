import socket

def check_ports(host, ports):
    results = {}
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(2)  # 2초 타임아웃
                result = s.connect_ex((host, port))
                if result == 0:
                    results[port] = "Open"
                else:
                    results[port] = "Closed"
        except Exception as e:
            results[port] = f"Error: {e}"
    return results

if __name__ == "__main__":
    # 테스트할 호스트 (IP 주소 또는 도메인)
    host = "103.224.182.208"  # 로컬호스트로 설정 (변경 가능)
    # 테스트할 포트 목록
    ports = [80, 8080, 443, 8443]
    
    results = check_ports(host, ports)
    for port, status in results.items():
        print(f"Port {port}: {status}")
