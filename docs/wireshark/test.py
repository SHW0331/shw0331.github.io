import subprocess

tshark_cdm = None

def user_input():
    # tshark cmd list
    # -i <interface> : 캡처할 네트워크 인터페이스 지정.
    # -D : 사용 가능한 네트워크 인터페이스 목록 표시.
    # -f <BPF 필터> : 패킷 캡처 시 BPF 필터 적용(TCP/IP 레벨에서 작동).
    # -r <file> : 파일로부터 캡처한 데이터를 읽음.
    # -w <file> : 패킷 캡처 데이터를 파일로 저장.
    # -Y <filter> : 디스플레이 필터 적용(현재 버전).
    # -R <filter(old)> : 디스플레이 필터 적용(구버전).
    # -T <output format> : 출력 형식 지정(text, fields, json, pdml 중 선택).
    # -e <fields> : 특정 필드 값만 출력.
    # -V : 패킷 세부정보를 상세히 출력.
    # -z <statistics> : 통계 정보 출력(io,stat 또는 http,stat 등).
    # -c <packet count> : 캡처할 패킷 수를 제한.

    # 캡쳐할 네트워크 인터페이스 지정.
    result  = subprocess.run(
        ["tshark", "-D"],
        capture_output=True,
        check=True
    )
    output = result.stdout.decode('utf-8', errors='replace')
    print("Netwok Interfaces List : \n")
    print(output)
    interface = input("Specify the network interfaces to capture : ")

    # -i <interface>
    
    
    return

def process_packet():
    return

def process_tshark():
    return

def main():
    # data = process_tshark()
    user_input()
    return

if __name__ == "__main__":
    main()