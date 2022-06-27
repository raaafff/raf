import socket, struct

def int32_to_ip(int32):
    return socket.inet_ntoa(struct.pack("!L", int32))


assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"
