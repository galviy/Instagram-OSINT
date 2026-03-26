import os
from commands import command
from colorama import Fore, Style, init
init(autoreset=True)


class BuildMenu:

    def print_ascii_welcome(self):
        print(r'''
                .-"      "-.  
               /            \ 
              |     v33n     | 
              |,  .-.  .-.  ,| 
              | )(__/  \__)( | 
              |/     /\     \| 
    (@_       (_     ^^     _) 
_     ) \_______\__|IIIIII|__/__________________________ 
(_)@8@8{}<________|-\IIIIII/-|__________________________-_> 
     )_/        \          / 
    (@            -------- instagram OSINT! 

         [---]   by:> galv1n   [---]
''')

    def menuu(self):
        self.print_ascii_welcome()
        target = input(Fore.MAGENTA + "Username target: ")
        user_id = command.get_user_id(target);
        if not user_id:
            print("Invalid username " + target + " not found!\nUse set username <username> to add new username")
            #target = ""
        while True:
            cmd = input(Fore.LIGHTBLUE_EX + "\ncommand > ").strip().lower()
            if cmd == "exit":
                 print(Fore.LIGHTYELLOW_EX + "Bye!")
                 break
            elif cmd == "get info":
                command.get_user_info(target)
            elif cmd == "get following":
                print("anjir")
                p = command.get_following(user_id)
                print(p)
            elif cmd == "get highlight":
                highlights = command.get_highlights(user_id)
                print("\nAvailable Highlights:")
                for i, h in enumerate(highlights):
                    print(f"{i + 1}. {h['title']} (ID: {h['id']})")
                for i, highlight in enumerate(highlights):
                    highlight_id = highlight["id"]
                    title = highlight.get("title", f"highlight_{i+1}")
                    print(f"\nIsi dari highlight '{title}':")
                    try:
                        items = command.get_highlight_items(highlight_id)
                        if items:
                            command.show_highlight_media(items)
                        else:
                            print("Tidak ada item di highlight ini.")
                    except Exception as e:
                        print(f"!!! Gagal mengambil highlight '{title}': {e}")

            elif cmd == "help":
                print("-> Perintah tersedia:")
                print("- get highlight (mendapatkan semua link didalam highlight)")
                print("- get following (mendapatkan array following user instagram)")
                print("- get following name (mendapatkan array following user instagram beserta username instagram mereka)")
                print("- get info (mendapatkan informasi seperti; followers,following)")
                print("- get followers (mendapatkan array followers )")
                print("- get photo (mendapatkan semua link foto) ")
                print("- get save (simpan semua foto yang ada dari <id>.json)")
                print("- exit")
            elif cmd == "get photo":
                command.get_all_photos(user_id)
            elif cmd == "get save":
                command.downloadAll(user_id)

