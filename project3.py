import requests
import json



token="5675259ef672fc42-5d02e46b003c6e4b-713ca0576474359b"
super_admin_id="4Ja8Dm63YNn5kUTiZGKosg=="
def set_web_hook():
    url = "https://chatapi.viber.com/pa/set_webhook"

    payload = {
        "url": "https://www.broadwayinfosys.com",
        "auth_token": token
    }

    r = requests.post(url=url, data=json.dumps(payload))

    print(r.json())

#set_web_hook()


def get_account_info():
    url = "https://chatapi.viber.com/pa/get_account_info"
    
    payload = {
        "auth_token": token
    }

    r = requests.post(url=url, data=json.dumps(payload))
    print(r.json())

#get_account_info()

def send_text_message(text):
    url = "https://chatapi.viber.com/pa/post"

    payload = {
        "auth_token": token,
        "from": super_admin_id,
        "type": "text",
        "text": text,
    }

    r = requests.post(url=url, data=json.dumps(payload))

    print(r.json())

#send_text_message()