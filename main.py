import tools
import vxlink

username = "a@qq.com"
password = "test123@"

if __name__ == "__main__":
    # get ipv6
    public_ipv6_addresses = tools.get_public_ipv6_addresses()
    if len(public_ipv6_addresses) == 0:
        print("No public IPv6 address found")
        exit()
    else:
        ipv6 = list(public_ipv6_addresses.values())[0]


    group_list = [
        {
            "vxtrans_id": 12345,
            "to_ip": ipv6,
            "to_port": "8096"
        },
        {
            "vxtrans_id": 12346,
            "to_ip": ipv6,
            "to_port": "3000"
        }
    ]

    # login
    vx = vxlink.VxLink(username,password)
    for group in group_list:
        vx.edit_vxtrans_ipv6(group["vxtrans_id"],group["to_ip"],group["to_port"])
        print(vx.get_vxtrans_list())