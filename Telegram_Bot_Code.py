#Telegram Bot Code
import requests
import os

def telegram_bot_sendtext(message):
    '''Sends a message to Telegram Bot'''

    bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')
    bot_chatID = os.environ.get('TELEGRAM_CHAT_ID')
    URL = f'https://api.telegram.org/bot{bot_token}'
    tag_line = '<<< Python Script >>>'
    send_text = URL + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + message + '\n' + tag_line

    response = requests.get(send_text)

    if response:
        print(f'Message sent succesfully.')

'''Driver Code.'''
#msg = input('Enter your message: \n').strip()
#test = telegram_bot_sendtext(msg)

