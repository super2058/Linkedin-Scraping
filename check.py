import time
from setting import *

if __name__ == '__main__':
    
    profile_id = "22bdce8311134d54939ad24caeb477cc"
    port = get_debug_port(profile_id)
    driver = get_webdriver(port)
    driver.get("https://www.upwork.com/nx/find-work/most-recent")
    while True:
        driver.refresh()
        time.sleep(60)
