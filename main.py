from login import LoginInstagram
from credentials import Cookies
from menu import BuildMenu

def main():
    masuk = LoginInstagram.login()
    if masuk:
        print("Masuk ke bagian Menu!")
        menu = BuildMenu()
        menu.menuu()
    else:
        print("Gagal login!")
        Cookies.input_credentials("./token.json")
        
if __name__ == "__main__":
    main()
