import json
import os

class Cookies:
    def __init__(self, sessionid, csrftoken, ds_user_id):
        self.sessionid = sessionid
        self.csrftoken = csrftoken
        self.ds_user_id = ds_user_id

    def headers(self): 
        return {
            "User-Agent": "Instagram 123.1.0.26.115 Android (30/3.0; 320dpi; 720x1280; Xiaomi; Redmi Note 7; lavender; qcom; en_US)",
            "X-IG-App-ID": "936619743392459",
            "Cookie": f"sessionid={self.sessionid}; csrftoken={self.csrftoken}; ds_user_id={self.ds_user_id}"
        }
    
    @staticmethod
    def input_credentials(filepath):
        sessionid = input("Session iD -> ")
        csrftoken = input("csrftoken -> ")
        ds_user_id = input("ds_user_id -> ")
        try:
            with open(filepath, "w") as f:
                json.dump({
                    "sessionid" : sessionid,
                    "csrftoken" : csrftoken,
                    "ds_user_id": ds_user_id
                },f,indent = 2)
                print("Please re-open the program.")
                os.system("PAUSE")
        except Exception as e:
            print("Gagal save token:", e)

    @staticmethod

    def from_file(filepath):
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
                return Cookies(**data)
        except Exception as e:
            print("Gagal load token:", e)
            return Cookies("", "", "")


my_cookies = Cookies.from_file("token.json")
