# Dormintod

Auto Claim for dormint / sleepcoin on Telegram

# Table of Contents

- [Dormintod](#dormintod)
- [Table of Contents](#table-of-contents)
- [Features](#features)
- [Register](#register)
- [How to Use](#how-to-use)
  - [Windows](#windows)
  - [Linux](#linux)
  - [Termux](#termux)
- [How to Find Account Token](#how-to-find-account-token)
- [Discussion](#discussion)
- [Support](#support)
- [Thank you \< 3](#thank-you--3)

# Features

- [x] Auto Claim
- [x] Multi Account Support

# Register

Click the followling link to register : [https://t.me/dormint_bot?start=629438076](https://t.me/dormint_bot?start=629438076)

# How to Use

## Windows 

1. Make sure you computer was installed python and git.
   
   python site : [https://python.org](https://python.org)
   
   git site : [https://git-scm.com/](https://git-scm.com/)

2. Clone this repository
   ```shell
   git clone https://github.com/akasakaid/dormintod.git
   ```

3. goto dormintod directory
   ```
   cd dormintod
   ```

4. install the require library
   ```
   python -m pip install -r requirements.txt
   ```

5. Edit `data.txt`, input you data token in `data.txt`, find you token in [How to Find Account Token](#how-to-find-account-token). One line for one data account, if you want add you second account add in new line!

6. execute the main program 
   ```
   python bot.py
   ```

## Linux

1. Make sure you computer was installed python and git.
   
   python
   ```shell
   sudo apt install python3 python3-pip
   ```
   git
   ```shell
   sudo apt install git
   ```

2. Clone this repository
   
   ```shell
   git clone https://github.com/akasakaid/dormintod.git
   ```

3. goto dormintod directory

   ```shell
   cd dormintod
   ```

4. Install the require library
   
   ```
   python3 -m pip install -r requirements.txt
   ```

5. Edit `data.txt`, input you data token in `data.txt`, find you token in [How to Find Account Token](#how-to-find-account-token). One line for one data account, if you want add you second account add in new line!

6. execute the main program 
   ```
   python bot.py
   ```

## Termux

1. Make sure you termux was installed python and git.
   
   python
   ```
   pkg install python
   ```

   git
   ```
   pkg install git
   ```

2. Clone this repository
   ```shell
   git clone https://github.com/akasakaid/dormintod.git
   ```

3. goto dormintod directory
   ```
   cd dormintod
   ```

4. install the require library
   ```
   python -m pip install -r requirements.txt
   ```

5. Edit `data.txt`, input you data token in `data.txt`, find you token in [How to Find Account Token](#how-to-find-account-token). One line for one data account, if you want add you second account add in new line!

6. execute the main program 
   ```
   python bot.py
   ```

# How to Find Account Token

How to find you account token

1. Active dev tool first [https://youtu.be/NYxHmck_GjE](https://youtu.be/NYxHmck_GjE)
2. Open bot and open dev tool
3. Go to network tab
4. Select `Fetch/XHR` for type (below  filter box)
5. Choose one of visible urls (`info`,`status`,`or etc`)
6. Click and switch to payload tab
7. Copy token in auth_token value on payload tab, example token:
   
   Payload tab content :
   
   ```
   {"auth_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjAyMzgxMTksInRnX2lkIjoiNjI5NDM4MDc2In0.SE6QqkY18-mGBEkzwnXq2-kZJSgZ8hE4qB8A3Fmemek"}
   ```

   Copy into like example in below and paste on `data.txt`

   ```
   eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjAyMzgxMTksInRnX2lkIjoiNjI5NDM4MDc2In0.SE6QqkY18-mGBEkzwnXq2-kZJSgZ8hE4qB8A3Fmemek
   ```

# Discussion

If you have an question or something you can ask in here : [@sdsproject_chat](https://t.me/sdsproject_chat)

# Support

To support me you can buy me a coffee via website in below

- Send IDR directly via QRIS : [https://s.id/nusanqr](https://s.id/nusanqr)
- https://trakteer.id/fawwazthoerif/tip
- https://sociabuzz.com/fawwazthoerif/tribe

# Thank you < 3