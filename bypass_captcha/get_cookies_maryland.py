import json
import time
import requests
from twocaptcha import TwoCaptcha

try:
    print("here 1")

    proxy = ""  # indicate your proxy parameters
    my_key = ""  #insert api key
    url = "https://casesearch.courts.state.md.us/casesearch/"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

    with open(r"C:\Users\Chicken Parmesean\Downloads\bypass_captcha\cookies_datadome.json", 'r') as json_file:
        content = json_file.read().strip()
        cookie_value = json.loads(content) if content else "DEFAULT_COOKIE_VALUE"


    cookies = {'datadome': cookie_value}

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US',
        'content-type': 'text/plain;charset=UTF-8',
        'origin': url,
        'referer': url,
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': user_agent,
    }

    res = requests.get(
        url,
        proxies={'http': 'http://' + proxy},
        cookies=cookies,
        headers=headers,
        verify=False  # Optional: disable SSL verification if necessary
    )
    print("here 2")
    if res.status_code == 403:
        print("here 2")
        # Fetching DataDome lock information
        dd = res.text.split('dd=')[1].split('</script')[0]
        dd = json.loads(dd.replace("'", '"'))
        cid = res.headers.get('Set-Cookie').split('datadome=')[1].split(';')[0]

        captcha_url = (
            f"https://geo.captcha-delivery.com/captcha/?"
            f"initialCid={dd['cid']}&hash={dd['hsh']}&"
            f"cid={cid}&t={dd['t']}&referer={url}&"
            f"s={dd['s']}&e={dd['e']}"
        )

        data = {
            "key": my_key,
            "method": "datadome",
            "captcha_url": captcha_url,
            "pageurl": url,
            "json": 1,
            "userAgent": user_agent,
            "proxy": proxy,
            "proxytype": "http",
        }

        response = requests.post("https://2captcha.com/in.php?", data=data)
        request_id = response.json()["request"]
        print("here 3")

        while True:
            print("here 4 - getting bypass")
            solu = requests.get(f"https://2captcha.com/res.php?key={my_key}&action=get&json=1&id={request_id}").json()
            if solu["request"] == "CAPCHA_NOT_READY":
                time.sleep(5)
            elif "ERROR" in solu["request"]:
                print(f"Error: {solu['request']}")
                exit(0)
            else:
                break

        # Extract and update the datadome cookie
        print("here 5")
        cookie_value = solu["request"].split(";")[0].split("=")[1]
        with open(r"C:\Users\Chicken Parmesean\Downloads\bypass_captcha\cookies_datadome.json", 'w') as json_file:
            json.dump(cookie_value, json_file)
        print("here 6")
        print("Captcha solved successfully and cookie updated.")
    else:
        print("Request did not trigger captcha. Proceeding without solving captcha.")

except:
    print("ERROR")