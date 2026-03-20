# instagram osint
Another level instagram scrapper using mobile API


# Warning
Using a self-bot or modified client could lead to your account being banned. Use this tool only if you understand the risks.


# Requirements & library
- colorama
- requests

# Project To DO
- [ ] idk what next?
- [x] get highlight (mendapatkan semua link didalam highlight
- [x] get following (mendapatkan array following user instagram)
- [x] get following name (mendapatkan array following user instagram beserta username instagram mereka)
- [x] get info (mendapatkan informasi seperti; followers,following)
- [x] get followers (mendapatkan array followers )
- [x] get photo (mendapatkan semua link foto)  

![Login](https://github.com/galviy/Instagram-OSINT/raw/main/show%20case/ll.png)


![Commands](https://github.com/galviy/Instagram-OSINT/raw/main/show%20case/ll2.png)

![Commands](https://github.com/galviy/Instagram-OSINT/raw/main/show%20case/ll3.png)


# Setting up cookies
you can modify the `token.json` to your information details, SHARING THIS DETAILS COULD LEAD UR ACCOUNT GETTING STOLEN!
```json
{
  "sessionid": "",
  "csrftoken": "",
  "ds_user_id": ""
}
```

# how to get api?

debug instagram network by ur self lol, use frida to bypass ssl pinning 
example -> https://engineering.beeper.com/2025/11/24/reverse-engineering-instagram-video-uploads/

