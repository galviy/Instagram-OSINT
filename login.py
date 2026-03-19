import requests
from credentials import my_cookies

class LoginInstagram:

    def login():
        url = "https://i.instagram.com/api/v1/accounts/current_user/"
        try:
            response = requests.get(url, headers=my_cookies.headers())
            response.raise_for_status()
            data = response.json()
            if(data["user"]["username"] != None):
                print("successfully logged in to " + data["user"]["username"])
                return True
            else:
                return False
        except requests.RequestException as e:
            print("Login gagal:")
            print(e)
            return False
        

