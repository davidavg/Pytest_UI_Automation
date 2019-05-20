'''
Created on Nov 1, 2018

@author: dguerra
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from random import randint

sURL = "https://10.248.250.35/"
sUser = "ip360@tripwire.com"
sPassword = "ip360@tripwire.com"
nDelay = 5

class Browser:
    
    def initBrowser(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(sURL)
        
        WebDriverWait(driver, nDelay).until(
                EC.visibility_of_element_located((By.ID, "login"))
            )
        
        WebDriverWait(driver, nDelay).until(
                EC.visibility_of_element_located((By.ID, "password"))
            )
        
        WebDriverWait(driver, nDelay).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id='layout']/form/div/div[2]/button"))
            )
        
        return driver
        
    def endBroswer(self, driver):
        driver.close()
    
class AUTCommon:
    
    def privacyError(self):
        #in case we need to handle the privacy error window
        pass
    
    def login(self, driver):
        try:
            driver.find_element_by_xpath("//input[@id='login']").send_keys(sUser)
            driver.find_element_by_xpath("//input[@id='password']").send_keys(sPassword)
            driver.find_element_by_xpath("//*[@id='layout']/form/div/div[2]/button").click()
            
            #Wait for the IP360 logo to appears
            WebDriverWait(driver, nDelay).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo"))
            )
            
            #Wait for pagination of scan profiles widget to appear
            WebDriverWait(driver, nDelay).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".tile.scan_profiles.locked .widgetcontent :nth-child(3) div:nth-child(5) > div.grid-record-count > div"))
            )
        except:
            return False
        else:
            return True
        
    def navigateOSGroups(self, driver):
        try:
            driver.find_element_by_xpath("//li[@id='dash-tab-3']/a").click()
                       
            #Wait for hardware status widget to load because it is the one that takes longer
            WebDriverWait(driver, nDelay).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, ".inner-circle"))
                )
            
            #Wait for item count to display
            WebDriverWait(driver, nDelay).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, ".tile.os_groups.locked > div.widgetcontent > div > vne-grid > vne-grid-table > div.grid-record-count > div"))
                )
        except:
            return False
        else:
            return True
        
    def installLicence(self, strLicencePath):
        #Function to install a licence in case it is not installed yet
        pass
    
class General():
    
    def __init__(self):
        self.__TestList = []
        self.__bVerify = True
    
    def toVerify(self, bCondition, strTest):
        
        if isinstance(bCondition, bool):
            self.__TestList.append((bCondition, strTest))
        else:
            self.__TestList.append((False, strTest + " : Invalid data type for bCondition"))
    
    '''
    toVerifyElement - It's a function that sends information to a list that will be validated later
    bCondition - It's a boolean calculated from a test operation
    strTest - Is the string specifying what is evaluated
    '''
    def toVerifyElement(self, locator, strQuery, strTest, driver):
        
        try:
            driver.find_element(locator, strQuery).is_displayed()
            self.__TestList.append((True, strTest))
        except:
            self.__TestList.append((False, strTest))
           
    def verify(self):
        
        for testTuple in self.__TestList:
            if not testTuple[0]:
                self.__bVerify = False
                print("\nFAIL: " + testTuple[1])
        
        return self.__bVerify 
    
    def getItemCount(self, strItemCount):
        nItemCount = ""
        
        for character in strItemCount[::-1]:
            if character == ' ':
                break
            
            nItemCount = character + nItemCount
            
        return int(nItemCount)
    
    def getRandName(self):
        return "AUT_" + str(datetime.now().year) + str(datetime.now().month) + str(datetime.now().day) + str(randint(1,1000))
    
