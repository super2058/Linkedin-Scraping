import time
import json
import argparse
import datetime

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from restricted_input import r_input

from setting import *
from config import *
from functions import *
import tkinter as tk
import time

email = 'superMark2058@gmail.com'
password = 'ToTo20000508'

def getText(driver, xpath)->str:
    return fnGetElementXpath(driver, False, xpath).__getattribute__('text')

def setText(driver, xpath, val)->bool:
    #Set up text
    try:
        ele = fnGetElementXpath(driver, False, xpath)
        actions = ActionChains(driver)
        actions.click(on_element = ele)
        actions.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)            
        actions.send_keys(f'{val}')
        actions.perform()
        return True
    except:
        return False

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description="Make an account in Upwork")
    parser.add_argument('-in', '--index_number', help = "Pass --index_number to the mail and the name of octo profile", type = int, default = 1, required = True)
    args = parser.parse_args()

    with open('elements.json') as fp:
        elements = json.loads(fp.read())
    
    profile_id = ''

    # Delete Profile
    try:
        profile_id = fnGetUUID(f'{OCTO_ID}_{args.index_number - MIN_NUMBER}')
        stop_profile(profile_id)
        deleteProfile(profile_id)
        print(f'Success to delete {OCTO_ID} profile!')
    except:
        print(f'There does not exist with profile name {OCTO_ID}')
    
    # # Create Profile
    try:
        profile_id = fnGetUUID(f'{OCTO_ID}_{args.index_number}')
    except:
        print(f'Create Octo Profile with {OCTO_ID}.')
        profile_id = createProfile(f'{OCTO_ID}_{args.index_number}')
    # profile_id = fnGetUUID(f'{OCTO_ID}')

    port = get_debug_port(profile_id)
    driver = get_webdriver(port)
    driver.get('https://www.linkedin.com/checkpoint/lg/sign-in-another-account')
    input_email = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="username"]'))).send_keys(email)
    input_password = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys(password)
    signin = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="organic-div"]/form/div[3]/button'))).click()
    time.sleep(1)



    
    driver.get('https://www.linkedin.com/posts/thomasdussud_please-explain-your-motivations-for-applying-activity-7100144420817129472-vl2A/?utm_source=share&utm_medium=member_desktop')
    time.sleep(3)
    # write search windows
    # WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="global-nav-typeahead"]/input'))).send_keys(keyword)
    # press enter
    # WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="global-nav-typeahead"]/input'))).send_keys(Keys.ENTER)

    # WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, f"//div[@class='scaffold-finite-scroll__content']/div[{lump}]/div/ul/li[{k}]/div/div/div/div[2]/a/div[3]/span[1]/span[1]/span[1]"))).text
    for i in range(0, 100):
        WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH, '/html/body'))).send_keys(Keys.END)
        try:
            button_text = "Load more comments"  # Replace with the text of the button you want to find
            xpath_expression = f"//span[text()='{button_text}']"
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath_expression))).click()
            print("pressed")
        except:
            print("cant find load more button")
        time.sleep(1)
    
    js_script = '''
        name_list=[]
        elements=document.querySelectorAll('[class*="comments-post-meta__name-text"]');
        elements.forEach(element=>{
            name_list.push(element.innerText);
        });
        return name_list;
    '''
    all_name_list = driver.execute_script(js_script)
    # Define the data-attribute-index value you want to match
    js_script = '''
        mail_list=[]
        elements=document.querySelectorAll('a[href^="mailto:"]');
        elements.forEach(element=>{
            mail_list.push(element.textContent);
        });
        return mail_list;
    '''
    all_email_list = driver.execute_script(js_script)
    print(len(all_name_list))
    print(len(all_email_list))
    print(all_name_list)
    print(all_email_list)
    
    for i in range(0, len(all_email_list)):
        temp_email = ''
        temp_email = all_email_list[i]
        print(temp_email)
        with open("result.txt", "a") as fp:
            fp.write(temp_email)
            fp.write("\n")