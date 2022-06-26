def int32_to_ip(int32):
    n1 = int(int32 / 16777216) % 256
    n2 = int(int32 / 65536) % 256
    n3 = int(int32 / 256) % 256
    n4 = int(int32) % 256
    return f'{n1}.{n2}.{n3}.{n4}'


assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"