import time
import telegram
from bs4 import BeautifulSoup
import requests


# send message
def bot(message):
    bot = telegram.Bot(token='here telegram token')
    chat_id = chat_id = 01234567890 #your chat id
    message = str(message)
    print(bot.send_message(text=message, chat_id=01234567890)) #your chat id


# bot("Reboot done") #nur bei Bedarf


def webSearch(known_list):
    url = "https://..." # site to check
    page = requests.get(url)
    inhalt = BeautifulSoup(page.content, 'html.parser')  # complete .html -page
    lists = inhalt.find_all('... html ...', class_="... html ...")  # checks for specific content in html code
    new_whg_list = []
    for new_whg in lists:
        str_element = str(new_whg)
        new_whg_list.append(str_element)

    bot_starter = False
    for new_whg in new_whg_list:
        if not new_whg in known_list:
            known_list.append(new_whg)
            bot_starter = True

    if bot_starter:
        bot("New message you want to send...")

    return known_list


known_list_list = []

while True:
    try:
        known_list_list = webSearch(known_list_list)
    except:
        print("irgendwas passt nicht")
    time.sleep(120)
