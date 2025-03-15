from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import colorama
from colorama import Fore, Back, Style
ids = []
colorama.init()

txt_art = Fore.GREEN + """___________    .__  .__                  __________ __   
\_   _____/___ |  | |  |   ______  _  __ \______   \ _____/  |_ 
 |    __)/  _ \|  | |  |  /  _ \ \/ \/ /  |    |  _//  _ \   __/
 |     \(  <_> )  |_|  |_(  <_> )     /   |    |   (  <_> )  |  
 \___  / \____/|____/____/\____/ \/\_/    |______  /\____/|__|  
     \/                                          \/"""   
     
print(txt_art)    
choice = input(Fore.RED +"Enter the mode(ui/ux = 1/headless=2): ")
path = input(Fore.RED + "Enter Your User id path(add file extension at the end): ")

#add your cookies here
Roblo_sec = []


def format_list(path):
    with open(path, "r") as f:
        lines = f.read()
        lines = lines.strip().split("\n")
        for line in lines:
            ids.append(line)
            
    
    
def start(choice,path):
    format_list(path)
    if choice == 2:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        
    else:
        driver = webdriver.Chrome()
    
    try:
        for cookie in Roblo_sec:
            driver.get("https://roblox.com/login")
            time.sleep(3)
            driver.add_cookie({
            "name": ".ROBLOSECURITY",
            "value": cookie,
            "domain": ".roblox.com"
    })
            for user in ids:
                driver.get(f"https://roblox.com/users/{user}/profile")
                time.sleep(3)
                checker_element = driver.find_elements(By.CSS_SELECTOR, ".MuiSvgIcon-root.MuiSvgIcon-fontSizeMedium.profile-header-more-icon.web-blox-css-mui-7ijiz4")
                if checker_element:
                    
                    btn = driver.find_element(By.CSS_SELECTOR, ".MuiSvgIcon-root.MuiSvgIcon-fontSizeMedium.profile-header-more-icon.web-blox-css-mui-7ijiz4")
                    btn.click()
                    time.sleep(1)
                    follow = driver.find_element(By.CLASS_NAME, "profile-header-dropdown-label")
                    follow.click()
                    print(F"{Fore.GREEN}Sucessfully Followed {user}")
                    time.sleep(20)
                    
                else:
                    print(f"{Fore.RED}Error Following {user}"
                        f"{Fore.RED}ERR:User is banned or you are rate limited")
                    time.sleep(20)
                
    except Exception as e:
        print(Fore.RED + f"ERROR: {e}")
    
    finally:
        driver.quit()
        print(Fore.LIGHTBLUE_EX + f"Successfully followed {len(ids)}")

start(choice,path)

#Author: WadzooTheZombot
