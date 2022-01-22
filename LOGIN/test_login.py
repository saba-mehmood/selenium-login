import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager import driver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.mark.usefixtures("init__driver")
class BaseTest:
    pass


class TestHubSpot(BaseTest):

    @pytest.mark.parametrize( 
                         "email",
                         [
                             ("xyz@yopmail.com"),
                             ("bsc-01@yopmail.com")
                         ]
                         )
    def test_login(self,email):
        
        self.driver.get("https://bscdev.akru.co/")
        self.driver.maximize_window()

        """ ASSIGNING INDEX 0 TO AKRU WINDOW"""
        window_before = self.driver.window_handles[0]


        """ RUNNING SCRIPT TO THE CURRENT WINDOW"""
        self.driver.execute_script("window.open()")


        """ PERFORM ACTIONS ON ELEMENTS"""

        self.driver.find_element(By.XPATH,'//*[@id="very-specific-design"]/div/div[2]/div[1]/button[1]').click()
        self.driver.find_element(By.ID,'navbar-header-sticky-login').click()
        self.driver.find_element(By.XPATH,'//*[@id="navbar-header-sticky-login"]/div/div/div/div/button').click()
        self.driver.find_element(By.CLASS_NAME,'donwload-btn').click()
        self.driver.find_element(By.ID,'navbar-magic-email').send_keys(email)
        self.driver.find_element(By.XPATH,'//*[@id="navbar-magic-next"]').click() 
        time.sleep(60)
      

        ################ YOPMAIL WINDOW ############


        """ ASSIGNING INDEX 1 TO YOPMAIL WINDOW"""
        self.driver.switch_to.window(self.driver.window_handles[1])    
        self.driver.get("https://yopmail.com/en/wm")


        """ PERFORM ACTIONS ON ELEMENTS"""
        self.driver.find_element(By.CLASS_NAME,'ycptinput').send_keys(email)
        self.driver.find_element(By.XPATH,'//*[@id="refreshbut"]/button/i').click()
        self.driver.switch_to.frame(self.driver.find_element(By.ID,'ifmail'))
        self.driver.find_element(By.XPATH,'//*[@id="mail"]/div/table/tbody/tr/td/div[2]/div/div/div/div/div/div[4]').click()
        time.sleep(2)
        self.driver.close()

        """ AFTER CLOSING WINDOW 1 YOPMAIL, NOW MAGIC LINK WILL BE OPEN ON INDEX 1"""
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(8)
        self.driver.close()

        """ SWITCHING BACK TO WINDOW 0"""
        self.driver.switch_to.window(window_before)
        time.sleep(10)


          
                