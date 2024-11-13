from pyclbr import Class

import requests

base_url = "https://vx.link"
base_UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI"
req = requests.Session()
req.headers.update({'User-Agent': base_UA})

class VxLink:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.token = self.get_login_token()
        self.do_login()

    def get_login_token(self):
        res = req.post(f"{base_url}/openapi/v1/token")
        if res.status_code == 200:
            return res.text
        else:
            Exception("Failed to get token")

    def do_login(self):
        data={
            "action":"login",
            "username":self.username,
            "password":self.password,
            "token":self.token
        }
        res = req.post(f"{base_url}/openapi/v1/user",data=data)
        if res.json()["status"] == 1:
            return True
        else:
            Exception("Failed to login")

    def get_vxtrans_list(self):
        data = {
            "action":"list",
            "token":self.token
        }
        res = req.post(f"{base_url}/openapi/v1/vxtrans",data=data)
        if res.status_code == 200:
            return res.json()
        else:
            Exception("Failed to get vxtrans list")

    def edit_vxtrans_ipv6(self,vxtrans_id,to_ip,to_port):
        data = {
            "action":"edit",
            "token":self.token,
            "id":vxtrans_id,
            "to_ip":to_ip,
            "to_port":to_port
        }
        res = req.post(f"{base_url}/openapi/v1/vxtrans",data=data)
        if res.json()["status"] == 1:
            return True
        else:
            Exception("Failed to change vxtrans ipv6")

if __name__ == "__main__":
    vx = VxLink("test@a.com","test")
    print(vx.get_vxtrans_list())
    vx.edit_vxtrans_ipv6(0,"2408::0","3000")


