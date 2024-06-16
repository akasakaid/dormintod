import os
import sys
import json
import time
import requests
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)
merah = Fore.LIGHTRED_EX
kuning = Fore.LIGHTYELLOW_EX
hijau = Fore.LIGHTGREEN_EX
biru = Fore.LIGHTBLUE_EX
putih = Fore.LIGHTWHITE_EX
hitam = Fore.LIGHTBLACK_EX
reset = Style.RESET_ALL


class Dormintod:
    def __init__(self):
        self.base_headers = {
            "host": "api.dormint.io",
            "connection": "keep-alive",
            "accept": "application/json, text/plain, */*",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 4A / 5A Build/QQ3A.200805.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36",
            "content-type": "application/json",
            "origin": "https://web.dormint.io",
            "x-requested-with": "tw.nekomimi.nekogram",
            "sec-fetch-site": "same-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://web.dormint.io/",
            "accept-language": "en,en-US;q=0.9",
        }
        self.line = putih + "~" * 50

    def load_data(self):
        datas = open("data.txt", "r").read().splitlines()
        self.log(f"{hijau}total account : {putih}{len(datas)}")
        if len(datas) <= 0:
            self.log(f"input you token account in data.txt first !")
            sys.exit()

        return datas

    def start_farming(self, token):
        url = "https://api.dormint.io/tg/farming/start"
        headers = self.base_headers.copy()
        data = json.dumps({"auth_token": token})
        res = self.http(url, headers, data)
        if "ok" in res.text.lower():
            self.log(f"{hijau}start farming successfully !")
            return True

        self.log(f"{merah}start farming failure !")
        return False

    def claim_farming(self, token):
        url = "https://api.dormint.io/tg/farming/claimed"
        data = json.dumps({"auth_token": token})
        headers = self.base_headers.copy()
        res = self.http(url, headers, data)
        if "ok" in res.text.lower():
            self.log(f"{hijau}claim farming successfully !")
            return True

        self.log(f"{merah}claim farming failure !")
        return False

    def status_farming(self, token):
        url = "https://api.dormint.io/tg/farming/status"
        headers = self.base_headers.copy()
        data = json.dumps({"auth_token": token})
        while True:
            res = self.http(url, headers, data)
            farming_status = res.json()["farming_status"]
            farming_left = res.json()["farming_left"]
            if farming_status == "farming_status_not_started":
                self.log(f"{kuning}farming not started !")
                result = self.start_farming(token)
                continue

            if farming_status == "farming_status_started":
                self.log(f"{putih}farming is started !")
                farming_amount = res.json()["farming_value"]
                self.log(f"{hijau}farming balance : {putih}{farming_amount}")
                self.log(f'{putih}next claim in : {hijau}{self.secto(round(farming_left))}')
                return round(farming_left) + 5

            if farming_status == "farming_status_finished":
                self.log(f"{hijau}farming is finished !")
                result = self.claim_farming(token)
                continue

    def user_info(self, token):
        url = "https://api.dormint.io/user/info"
        headers = self.base_headers.copy()
        data = json.dumps({"auth_token": token})
        res = self.http(url, headers, data)
        if '"ok"' not in res.text.lower():
            self.log(f"{merah}something wrong !, check http log for more information !")
            return False

        balance = res.json()["sleepcoin_balance"]
        self.log(f"{hijau}balance : {putih}{balance}")

    def main(self):
        banner = f"""
    {hijau}Auto Claim {biru}Dormint {hijau}/ {biru}sleepcoin {hijau}on Telegram 
    
    {hijau}By: {putih}t.me/AkasakaID
    {hijau}Github: {putih}@AkasakaID
    
    {hijau}Message: {putih}dont't forget to 'git pull' maybe i update the repo !
        """
        arg = sys.argv
        if "marinkitagawa" not in arg:
            os.system("cls" if os.name == "nt" else "clear")
        print(banner)
        
        accounts = self.load_data()
        print(self.line)
        while True:
            list_countdown = []
            _start = int(time.time())
            for no,account in enumerate(accounts):
                self.log(f'{hijau}account number : {putih}{no + 1}{hijau}/{putih}{len(accounts)}')
                self.user_info(account)
                result = self.status_farming(account)
                list_countdown.append(result)
                print(self.line)

            _end = int(time.time())
            _tot = _end - _start
            _min = min(list_countdown) - _tot
            if _min <= 0:
                continue

            self.countdown(_min)
    
    def secto(self,t):
            menit, detik = divmod(t, 60)
            jam, menit = divmod(menit, 60)
            jam = str(jam).zfill(2)
            menit = str(menit).zfill(2)
            detik = str(detik).zfill(2)
            return f"{jam}:{menit}:{detik}"

    def countdown(self, t):
        while t:
            menit, detik = divmod(t, 60)
            jam, menit = divmod(menit, 60)
            jam = str(jam).zfill(2)
            menit = str(menit).zfill(2)
            detik = str(detik).zfill(2)
            print(f"waiting until {jam}:{menit}:{detik} ", flush=True, end="\r")
            t -= 1
            time.sleep(1)
        print("                          ", flush=True, end="\r")

    def log(self, msg):
        now = datetime.now().isoformat(" ").split(".")[0]
        print(f"{hitam}[{now}] {reset}{msg}")

    def http(self, url, headers, data=None):
        while True:
            try:
                if data is None:
                    res = requests.get(url, headers=headers)
                    open("http.log", "a", encoding="utf-8").write(f"{res.text}\n")
                    if "<html>" in res.text:
                        self.log("failed get json response !")
                        time.sleep(2)
                        continue

                    return res

                if data == "":
                    res = requests.post(url, headers=headers)
                    open("http.log", "a", encoding="utf-8").write(f"{res.text}\n")
                    if "<html>" in res.text:
                        self.log(f"failed get json response !")
                        time.sleep(2)
                        continue

                    return res

                res = requests.post(url, headers=headers, data=data)
                open("http.log", "a", encoding="utf-8").write(f"{res.text}\n")
                if "<html>" in res.text:
                    self.log(f"failed get json response !")
                    time.sleep(2)
                    continue

                return res

            except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
                self.log("connection timeout / connection error !")
                continue


if __name__ == "__main__":
    try:
        app = Dormintod()
        app.main()
    except KeyboardInterrupt:
        sys.exit()
