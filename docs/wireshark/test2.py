import subprocess

def main():
    # tshark 명령어 설정
    tshark_cmd = [
        "tshark",           # tshark 실행
        "-i", "Wi-Fi",      # 네트워크 인터페이스 (필요시 변경)
        "-T", "fields",     # 필드 출력 형식 설정
        "-e", "ip.src",     # 출발지 IP
        "-e", "ip.dst"      # 목적지 IP
    ]
    
    try:
        # tshark 명령 실행
        process = subprocess.Popen(tshark_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Starting packet capture... (Press Ctrl+C to stop)")
        
        # 실시간으로 데이터 읽기
        for line in process.stdout:
            if line.strip():  # 빈 줄 제거
                # 필드가 탭으로 구분되어 있으므로 분리
                fields = line.strip().split('\t')
                if len(fields) == 2:
                    src_ip, dst_ip = fields
                    print(f"Source IP: {src_ip} -> Destination IP: {dst_ip}")
    
    except KeyboardInterrupt:
        print("\nStopping packet capture...")
        process.terminate()
    except FileNotFoundError:
        print("tshark 실행 파일을 찾을 수 없습니다. 환경 변수를 확인하세요.")
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    main()
