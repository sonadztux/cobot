from config import url_api_base, product_url_base, bot_token, chat_id
from datetime import datetime
import requests
import json
import re

header = {'Content-Type': 'application/json'}


def check(product):
    product_url = product_url_base+product
    url_api = url_api_base+'?url='+product_url
    response = requests.get(url_api, headers=header)

    if response.status_code == 200:
        check_result = json.loads(response.content.decode('utf-8'))
        return get_product_info(check_result, product_url)
    else:
        return None


def get_product_info(check_result, product_url):
    if check_result is not None:
        if re.search('/yes/', product_url):
            message = 'SILAHKAN DIBUY SLURRRR!!!\nlink :', product_url
            send_message = requests.get(
                'https://api.telegram.org/bot'+bot_token+'/sendMessage?chat_id='+chat_id+'&text='+message)
            return product_url+' => AVAILABLE!!'
        else:
            print('masuk sini')
            message = "SOLD"
            send_message = requests.get(
                'https://api.telegram.org/bot'+bot_token+'/sendMessage?chat_id='+chat_id+'&text='+message)
            return print(product_url+' => SOLD')


products = (
    'gazelle-hi-cappuccino',
    'gazelle-hi-red',
    'gazelle-hi-white',
    'gazelle-hi-blue-sky',
    'gazelle-low-black-black',
    'gazelle-low-blue-sky',
    'gazelle-low-cappuccino',
    'gazelle-low-grey',
    'gazelle-low-white',
    'gazelle-low-pink',
    'gazelle-low-red',
    'gazelle-low-red-indonesia-bersatu',
    'gazelle-low-navy',
    'gazelle-low-white-indonesia-bersatu',
    'rd-low',
    'rd-hi'
)

for product in products:
    check(product)
