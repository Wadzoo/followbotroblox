import undetected_chromedriver as webdriver
from selenium.webdriver.common.by import By
import os
import time
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QLineEdit,QPushButton
import sys
from PyQt5.QtCore import Qt
import subprocess as subproc
selected_profile = "Default" # change this to ur desire dprofile
home_dir = os.path.expanduser("~")
nec = []
folders = os.listdir(f"{home_dir}\\AppData\\Local\\Google\\Chrome\\User Data")

options = webdriver.ChromeOptions()
#options

def get_info(path):
    ls = []
    with open(path ,"r") as f:
        lines = f.readlines()
        
        ls = [line.strip() for line in lines]
        return ls
def nonhead(user_ids):
    
    users = get_info(user_ids)
    options.add_argument(f"--user-data-dir={home_dir}\\AppData\\Local\\Google\\Chrome\\User Data")
    options.add_argument(f"--profile-directory={selected_profile}") #can be found at userdata folder in APPdata
    driver = webdriver.Chrome(options=options)
    for users in user_ids:
        for user in users:
            driver.get(f"https://www.roblox.com/users/{user}/profile")
            time.sleep(1)
            
            el = driver.find_elements(By.CSS_SELECTOR,".MuiSvgIcon-root.MuiSvgIcon-fontSizeMedium.profile-header-more-icon.web-blox-css-mui-7ijiz4")
            
            try:
                
                if el:
                    perform = driver.find_element(By.CSS_SELECTOR,".MuiSvgIcon-root.MuiSvgIcon-fontSizeMedium.profile-header-more-icon.web-blox-css-mui-7ijiz4")
                    perform.click()
                    time.sleep(1)
                    follow = driver.find_element(By.CLASS_NAME, "profile-header-dropdown-label")
                    follow.click()
            except:
                
                pass
                
            time.sleep(1)
            

def head(user_ids):

    users = get_info(user_ids)
    options.add_argument(f"--user-data-dir={home_dir}\\AppData\\Local\\Google\\Chrome\\User Data")
    options.add_argument(f"--profile-directory={selected_profile}")
    options.add_argument(f"--headless=new")
    options.add_argument(f"--disable-gpu")
    options.add_argument(f"--no-sandbox")
    driver = webdriver.Chrome(options=options)
    for users in user_ids:
        for user in users:
            driver.get(f"{str(user)}")
            time.sleep(1)
            
            el = driver.find_elements(By.CSS_SELECTOR,".MuiSvgIcon-root.MuiSvgIcon-fontSizeMedium.profile-header-more-icon.web-blox-css-mui-7ijiz4")
            
            try:
                
                if el:
                    perform = driver.find_element(By.CSS_SELECTOR,".MuiSvgIcon-root.MuiSvgIcon-fontSizeMedium.profile-header-more-icon.web-blox-css-mui-7ijiz4")
                    perform.click()
                    time.sleep(1)
                    follow = driver.find_element(By.CLASS_NAME, "profile-header-dropdown-label")
                    follow.click()
            except:
                
                pass
                
            time.sleep(1)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(400,400,600,400)
        self.setStyleSheet("background: white;")
        self.label = QLabel("Roblox-Auto-Follower-Bot\n"
                            "Enter file Path(add txt at the end)", self)
        self.stpbtn = QPushButton("Stop Session", self)
        self.label.setGeometry(0,0,600,400)
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.label.setStyleSheet("font-size:" "30px;"
                                 "font-family:" "Inter;")
        self.stporstrlabel = QLabel(self)
        self.entry = QLineEdit(self)
        self.entry.setStyleSheet("font-size:" "20px;"
                                 "font-family:" "Inter;"
                                 "background-color:" "pink;"
                                 "border-radius:" "10px;")#set this later
        self.entry.setGeometry(200,100,200,40)
        
        self.btn = QPushButton("Start In headless-tab", self)
        self.btn1 = QPushButton("Start with UI/UX", self)
        self.stporstrlabel.setGeometry(225,250,150,150)
        self.btn.setGeometry(150,150,150,30)
        self.btn1.setGeometry(300,150,150,30)
        self.stpbtn.setGeometry(225,200,150,30)
        self.btn.setStyleSheet("""
    QPushButton {
        background-color: green; color: white; font-size: 15px; font-family: Inter; border-radius: 10px;
    }
    QPushButton:hover {
        background-color: grey;
    }
""")    
        self.btn1.setStyleSheet("""
    QPushButton {
        background-color: blue; color: white; font-size: 15px; font-family: Inter; border-radius: 10px;
    }
    QPushButton:hover {
        background-color: grey;
    }
""")
        self.stpbtn.setStyleSheet("""
    QPushButton {
        background-color: red; color: white; font-size: 15px; font-family: Inter; border-radius: 10px;
    }
    QPushButton:hover {
        background-color: grey;
    }
""")
        self.stpbtn.clicked.connect(self.stop_session)
        self.btn.clicked.connect(self.start_session1)
        self.btn1.clicked.connect(self.start_session2)    
    def stop_session(self):
        subproc.run("taskkill /f /im chromedriver.exe", shell=True)
        self.stporstrlabel.setText("stopped")
    def start_session1(self):
        head(self.entry.text())
        self.stporstrlabel.setStyleSheet("font-size:" "20px;")
        self.stporstrlabel.setText("Started!")
        
    
    def start_session2(self):
        nonhead(self.entry.text())
        self.stporstrlabel.setStyleSheet("font-size:" "20px;")
        self.stporstrlabel.setText("Started!")  
            

    
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
