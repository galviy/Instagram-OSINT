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
- [x] get photo (mendapatkan semua link foto dan disave di <id>.json)
- [x] get save (simpan semua foto yang ada dari current <id> saat memilih target)

![Login](https://github.com/galviy/Instagram-OSINT/raw/main/show%20case/ll.png)


![Commands](https://github.com/galviy/Instagram-OSINT/raw/main/show%20case/ll2.png)

![Commands](https://github.com/galviy/Instagram-OSINT/raw/main/show%20case/ll3.png)

![Downloads photo](https://media.discordapp.net/attachments/1467508535591174480/1486589684778926223/image.png?ex=69c60e08&is=69c4bc88&hm=08d19d5aef6dde2f22cbe100061fb7a5324c4ccec2a6f793400c1b66023ed819&=&format=webp&quality=lossless&width=1630&height=876)
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

