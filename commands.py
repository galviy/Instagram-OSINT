import requests
import time
import random
from credentials import my_cookies
from colorama import Fore, Style, init
import json
from pathlib import Path
import os

class command:

    @staticmethod
    def get_user_id(username):
        url = f"https://www.instagram.com/web/search/topsearch/?query={username}"
        try:
            response = requests.get(url, headers=my_cookies.headers())
            response.raise_for_status()
            data = response.json()
            if not data["users"]:
                print(Fore.RED + f"Username '{username}' tidak ditemukan!")
                return None
            user = data["users"][0]["user"]
            print(Fore.CYAN + f"Username ditemukan: {user['username']} ({user['full_name']})")
            print(f"ID -> {user["pk"]}")     
            return user["pk"]   
        except Exception as e:
             print(Fore.RED + f"Error get_user_id: {e}")
             return None
    @staticmethod
    def get_user_info(username):
        url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"
        try:
            res = requests.get(url, headers=my_cookies.headers())
            res.raise_for_status()
            user = res.json()["data"]["user"]
            print(Fore.CYAN + f"\nInfo akun {user['username']}")
            print("Nama:", user["full_name"])
            print("Bio:", user["biography"])
            print("Followers:", user["edge_followed_by"]["count"])
            print("Following:", user["edge_follow"]["count"])
            print("Posts:", user["edge_owner_to_timeline_media"]["count"])
            print("Private:", user["is_private"])
            print("Verified:", user["is_verified"])
            print("Foto Profil:", user["profile_pic_url_hd"])
        except Exception as e:
            print(Fore.RED + f"Gagal mengambil info user: {e}")

    @staticmethod
    def get_following(user_id):
        base_url = f"https://i.instagram.com/api/v1/friendships/{user_id}/following/"
        following_names = []
        next_max_id = None
        while True:
            if next_max_id:
                url = f"{base_url}?max_id={next_max_id}"
            else: 
                url = base_url
            try:
                response = requests.get(url, headers=my_cookies.headers())
                response.raise_for_status()
                data = response.json()
                users = data.get("users", [])
                following_names += [user["username"] for user in users]
                print(f"Fetched {len(users)} following. Total so far: {len(following_names)}")
                delay = random.uniform(1, 2)
                print(f"Sleeping for {delay:.2f} seconds to avoid rate-limiting...")
                time.sleep(delay)
                next_max_id = data.get("next_max_id")
                if not next_max_id:
                    break
            except requests.RequestException as e:
                print(f"Error fetching following names: {e}. Sleeping 60s before retry...")
                time.sleep(60)
                continue

        return following_names
    
    @staticmethod
    def get_highlights(user_id):
        url = f"https://i.instagram.com/api/v1/highlights/{user_id}/highlights_tray/"
        try:
            res = requests.get(url, headers=my_cookies.headers())
            res.raise_for_status()
            return res.json().get("tray", [])
        except:
            return []
        
    @staticmethod
    def get_highlight_items(highlight_id):
        url = f"https://i.instagram.com/api/v1/feed/reels_media/?reel_ids={highlight_id}"
        try:
            res = requests.get(url, headers=my_cookies.headers())
            res.raise_for_status()
            return res.json()["reels"][highlight_id]["items"]
        except:
            return []
        
    @staticmethod
    def show_highlight_media(items):
        for i, item in enumerate(items):
            print(Fore.YELLOW + f"\nStory {i + 1}:")
            if item["media_type"] == 1:
                url = item["image_versions2"]["candidates"][0]["url"]
                print("Type: Photo\n URL:", url)
            elif item["media_type"] == 2:
                url = item["video_versions"][0]["url"]
                print("Type: Video\n URL:", url)
            else:
                print("Unknown media type")
    @staticmethod
    def downloadAll(user_id):
        filename = os.path.join("json", f"{user_id}.json")
        folder_user = os.path.join("json", user_id)
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                os.makedirs(folder_user, exist_ok=True)
                counter = 0
                for item in data:
                    counter += 1
                    url = item['url']
                    
                   
                    save_path = os.path.join(folder_user, f"{counter}.jpg")
                    
                    print(f"Downloading {counter}: {url}")
 
                    r = requests.get(url)
                    with open(save_path, 'wb') as f:
                        f.write(r.content)
                        
                print(f"Total {counter} file didownload.")
    
        except FileNotFoundError:
            print(f"unable to find {filename}\nDo >get photo to download all links first")
        except json.JSONDecodeError:
            print(f"{filename} is corrupted")
            
    @staticmethod
    def get_all_photos(user_id):
        base_url = f"https://i.instagram.com/api/v1/feed/user/{user_id}/"
        headers = my_cookies.headers()
        all_photos = []
        max_id = None

        while True:
            url = f"{base_url}?max_id={max_id}" if max_id else base_url

            try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()
                data = response.json()

                items = data.get("items", [])
                print(Fore.CYAN + f"Fetched {len(items)} posts")

                for item in items:
                    location_name = item.get("location", {}).get("name") if item.get("location") else None
                    if location_name:
                        print(Fore.MAGENTA + f"Lokasi: {location_name}")

                    if "carousel_media" in item:
                        print(Fore.BLUE + "Carousel:")
                        for media in item["carousel_media"]:
                            if media["media_type"] == 1:
                                url = media["image_versions2"]["candidates"][0]["url"]
                                all_photos.append({
                                    "url": url,
                                    "location": location_name,
                                    "is_carousel": True
                                })
                                print("Image", url)
                            elif media["media_type"] == 2:
                                print(" Video detected (skipped)")

                    else:
                        media_type = item.get("media_type")
                        if media_type == 1 and "image_versions2" in item:
                            url = item["image_versions2"]["candidates"][0]["url"]
                            all_photos.append({
                                "url": url,
                                "location": location_name,
                                "is_carousel": False
                            })
                            print("Image url", url)
                        elif media_type == 2:
                            print("Video detected (skipped)")

                delay = random.uniform(1, 2)
                print(Fore.YELLOW + f"Sleeping for {delay:.2f} seconds...")
                time.sleep(delay)

                max_id = data.get("next_max_id")
                if not max_id:
                    print(Fore.GREEN + "Semua foto berhasil diambil.")
                    break

            except Exception as e:
                print(Fore.RED + f"Error fetching posts: {e}. Tidur 60 detik sebelum lanjut...")
                time.sleep(60)
                continue


        #filename = f"{user_id}.json"
        filename = os.path.join("json", f"{user_id}.json")
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(all_photos, f, ensure_ascii=False, indent=2)
            print(Fore.GREEN + f"Disimpan ke file {filename} ({len(all_photos)} foto).")
        except Exception as e:
            print(Fore.RED + f"Gagal menyimpan ke file JSON: {e}")

        return all_photos
