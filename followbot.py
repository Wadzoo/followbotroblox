from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import colorama
from colorama import Fore, Back, Style
ids = []
colorama.init()
MAX_DELAY = 300
MIN_DELAY = 20
txt_art = Fore.GREEN + """ ____    _____   __       __       _____   __      __  ____    ____        ____     ____    ______   
/\  _`\ /\  __`\/\ \     /\ \     /\  __`\/\ \  __/\ \/\  _`\ /\  _`\     /\  _`\  /\  _`\ /\__  _\  
\ \ \L\_\ \ \/\ \ \ \    \ \ \    \ \ \/\ \ \ \/\ \ \ \ \ \L\_\ \ \L\ \   \ \ \L\ \\ \ \L\ \/_/\ \/  
 \ \  _\/\ \ \ \ \ \ \  __\ \ \  __\ \ \ \ \ \ \ \ \ \ \ \  _\L\ \ ,  /    \ \  _ <'\ \  _ <' \ \ \  
  \ \ \/  \ \ \_\ \ \ \L\ \\ \ \L\ \\ \ \_\ \ \ \_/ \_\ \ \ \L\ \ \ \\ \    \ \ \L\ \\ \ \L\ \ \ \ \ 
   \ \_\   \ \_____\ \____/ \ \____/ \ \_____\ `\___x___/\ \____/\ \_\ \_\   \ \____/ \ \____/  \ \_/
    \/_/    \/_____/\/___/   \/___/   \/_____/'\/__//__/  \/___/  \/_/\/ /    \/___/   \/___/    \/_/
                                                                                                     
                                                                                                     """
     
print(txt_art)    
choice = int(input(Fore.RED +"Enter the mode(ui/ux = 1/headless=2): "))
path = input(Fore.RED + "Enter Your User id path(add file extension at the end): ")

#add your cookies here
Roblo_sec = []

def remove(path,n):
    try:
        with open(path, "r") as f:
            cont = f.read()
            
        removed = cont[n:]
        
        with open(path,"w") as w:
            w.writelines(removed)
    
    except Exception as e:
        print(f"Error Occured While removing ID: {e}")
        
def format_list(path):
    with open(path, "r") as f:
        lines = f.read()
        lines = lines.strip().split("\n")
        for line in lines:
            ids.append(line)
            
    
def start(choice,path):
    format_list(path)
    num_of_times = 0
    if choice == 2:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
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
                    
                    num_of_times += 1
                    with open(path,"r") as f:
                        lin = f.read()
                        if lin[0] == "\n":
                            remove(path,1)
                            remove(path,len(user))
                        else:
                            remove(path,len(user))
                            
                    time.sleep(10)
                else:
                    print(f"{Fore.RED}Error Following {user}"
                    f"{Fore.RED}ERR:User is banned or you are rate limited")
                    time.sleep(15)
                
                if num_of_times == 30:
                    print("Users Followed:", num_of_times)
                    print("Total followers:")
                    print(Fore.RED + f"You Now Have Been Rate Limited, Delaying for 3 minutes")
                    time.sleep(MAX_DELAY)
                    num_of_times = 0
                    
                
    except Exception as e:
        print(Fore.RED + f"ERROR: {e}")
    
    finally:
        driver.quit()
        print(Fore.LIGHTBLUE_EX + f"Successfully followed {len(ids)}")

start(choice,path)

#Author: WadzooTheZomb
