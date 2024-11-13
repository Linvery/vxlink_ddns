import socket
import psutil
import ipaddress

def get_public_ipv6_addresses():
    ipv6_addresses = {}
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET6:
                # 将字符串地址转换为 IPv6 对象
                ipv6_obj = ipaddress.IPv6Address(addr.address.split('%')[0])  # 去掉接口标识符部分
                if not (ipv6_obj.is_link_local or ipv6_obj.is_multicast or ipv6_obj.is_private):
                    ipv6_addresses[interface] = addr.address
    return ipv6_addresses


if __name__ == "__main__":
    public_ipv6_addresses = get_public_ipv6_addresses()
    for interface, ipv6 in public_ipv6_addresses.items():
        print(f"Interface: {interface}, Public IPv6 Address: {ipv6}")