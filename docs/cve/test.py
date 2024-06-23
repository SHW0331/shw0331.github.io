from hpack import Decoder

# HPACK 인코딩된 데이터
encoded_data = b'\x82\x86\x41\x86\xa0\xe4\x1d\x13\x9d\x09\x84\x7a\x88\x25\xb6\x50\xc3\xcb\xb8\xb8\x3f\x53\x03\x2a\x2f\x2a'

# HPACK 디코더 초기화
decoder = Decoder()

# 데이터를 디코딩
decoded_headers = decoder.decode(encoded_data)

# 디코딩된 헤더 출력
for header in decoded_headers:
    print(header)
