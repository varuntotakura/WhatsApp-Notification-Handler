from selenium import webdriver
from time import sleep
import winsound

duration = 200  # millisecond
freq = 900  # Hz
browser = webdriver.Chrome(executable_path='C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe')
browser.get('https://web.whatsapp.com/')

input('Enter anything after scanning QR code:')

intros = ['hi', 'der', 'hello', 'varun']
postives = ['yes', 'ok', 'urgent', 'yeah']
negatives = ['no', 'not important', 'nothing']

while True:
    unread = browser.find_elements_by_class_name("P6z4j") # The green dot tells us that the message is new
    if len(unread) > 0:
        ele = unread[-1]
        action = webdriver.common.action_chains.ActionChains(browser)
        action.move_to_element_with_offset(ele, 0, -20) # move a bit to the left from the green dot

        # Clicking couple of times because sometimes whatsapp web responds after two clicks
        try:
            action.click()
            action.perform()
            action.click()
            action.perform()
        except Exception as e:
            pass
        try:
            name = browser.find_element_by_class_name("_19vo_").text  # Contact name
            text_box = browser.find_element_by_class_name("_3u328")
            resp = browser.find_elements_by_class_name("-N6Gq")[-1].text
            tex = resp.split('\n')[0].lower()
            if tex in intros:
                text = "Hi "+name+". VARUN's Bot here :)\n Now I am activated for you.\nMr. VARUN is busy now.\n"
                text_box.send_keys(text)
                text = "Is it Very Urgent to talk with Mr. VARUN?\n"
                text_box.send_keys(text)
            elif tex in postives:
                text = "Ok. I'll notify him.\nPlease wait for sometime, Mr. VARUN will see you.\nHave a nice day.\n"
                text_box.send_keys(text)
                winsound.Beep(freq, duration)
                winsound.Beep(freq, duration)
                winsound.Beep(freq, duration)
            elif tex in negatives:
                text = "Okay, then Mr. VARUN will talk to you later.\nHave a nice day.\n"
                text_box.send_keys(text)
            else:
                text = "Hi "+name+". VARUN's Bot here.\n I couldn't understand that.\n"
                text_box.send_keys(text)

        except Exception as e:
            print(e)
            pass
        sleep(3)
