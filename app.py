from config import url_api_base, product_url_base, bot_token, chat_id
from datetime import datetime
import requests
import json
import re

header = {'Content-Type': 'application/json'}

# Function to get api response
# to check product stock status
def check(product):
    product_url = product_url_base+product
    url_api = url_api_base+'?url='+product_url
    response = requests.get(url_api, headers=header)

    if response.status_code == 200:
        check_result = json.loads(response.content.decode('utf-8'))
        return get_product_info(check_result, product_url)
    else:
        return None

# Function to to send message to telegram bot
def get_product_info(check_result, product_url):
    if check_result is not None:
        if re.search('/yes/', product_url):
            message = 'SILAHKAN DIBUY SLURRRR!!!'
            send_message = requests.get(
                'https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text=Cron at : {2}\n{3} {4}'.format(bot_token, chat_id, datetime.now(), message, product_url))
            return print(product_url+' => AVAILABLE!!')
        """
        # to send message to telegram bot when 
        # product stock is not available/sold
        else:
            message = "SOLD"
            send_message = requests.get(
                'https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text=Cron at : {2}\n{3} {4}'.format(bot_token, chat_id, datetime.now(), message, product_url))
            return print(product_url+' => SOLD')
        """
# tuple of all sepatucompass's product
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

# loop to check availability one by one the product
for product in products:
    check(product)
