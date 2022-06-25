import ipaddress


def int32_to_ip(int32):
    if int32 < 0:
        return None
    ret = ""
    buff: int
    for i in range(4):
        buff = int32 >> (3 - i) * 8
        ret += str(buff) + ("." if i < 3 else "")
        int32 -= buff << (3 - i) * 8
    return ret


# Another variant, using ipaddress module
def std_int32_to_ip(int32):
    return str(ipaddress.ip_address(int32))


# for num in (2154959208, 0, 2149583361, 4294967295,
#         4278255360, 167772687, 536870912, 32,
#         16777216, 1, 4278190080, 255,
#         16843009):
#     print(num, "=>", int32_to_ip(num))

# assert int32_to_ip(2154959208) == "128.114.17.104"
# assert int32_to_ip(0) == "0.0.0.0"
# assert int32_to_ip(2149583361) == "128.32.10.1"

# assert int32_to_ip(4294967295) == "255.255.255.255"
# assert int32_to_ip(4278255360) == "255.0.255.0"
# assert int32_to_ip(167772687) == "10.0.2.15"
# assert int32_to_ip(536870912) == "32.0.0.0"
# assert int32_to_ip(32) == "0.0.0.32"
# assert int32_to_ip(16777216) == "1.0.0.0"
# assert int32_to_ip(1) == "0.0.0.1"
# assert int32_to_ip(4278190080) == "255.0.0.0"
# assert int32_to_ip(255) == "0.0.0.255"
# assert int32_to_ip(16843009) == "1.1.1.1"
# assert int32_to_ip(-10) == None