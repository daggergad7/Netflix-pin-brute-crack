import pickle
import requests
import json
from selenium import webdriver
with open('cookie.json',"r") as f:
    data = json.load(f)
json_string = json.dumps(data)


# print(json_string)
pickle.dump( data , open("cookies.pkl","wb"))
browser = webdriver.Chrome('chromedriver.exe')

browser.get('https://www.netflix.com')
# print(browser.get_cookies())
browser.delete_all_cookies()
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    if 'sameSite' in cookie:
         del cookie['sameSite']
    browser.add_cookie(cookie)

# print(browser.get_cookies())
browser.get('https://www.netflix.com/browse')

# pickle.dump( browser.get_cookies() , open("cookiestest.json","wb"))