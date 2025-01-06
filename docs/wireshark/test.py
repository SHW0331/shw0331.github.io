import subprocess

def process_packet():
    return

def process_tshark():
    # tshark cmd
    tshark_cmd = [
        "tshark",
        "-i", "Wi-Fi",
        "-T", "fields",
        "-e", "ip.src",
        "-e", "ip.dst",
    ]
    
    # tshark start
    # process = subprocess.Popen(tshark_cmd, stdout=subprocess.PIPE, text=True)
    process = subprocess.Popen(tshark_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    for line in process.stdout:
        if line.strip():  # 빈 줄 제거
            # 필드가 탭으로 구분되어 있으므로 분리
            fields = line.strip().split('\t')
            if len(fields) == 2:
                src_ip, dst_ip = fields
                print(f"Source IP: {src_ip} -> Destination IP: {dst_ip}")
                if src_ip == '172.26.80.68':
                    print("find source ip : 172.26.80.68")
        

def main():
    data = process_tshark()
    return

if __name__ == "__main__":
    main()