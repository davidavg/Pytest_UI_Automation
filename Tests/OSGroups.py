'''
Created on Nov 1, 2018

@author: dguerra
'''

import pytest
from FrameworkLib.GeneralLib import Browser, AUTCommon, General, nDelay
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

general = General()
groupName = general.getRandName()

@pytest.fixture(scope="module")
def control():
    browser = Browser()
    control = browser.initBrowser()
    yield control
    browser.endBroswer(control)

def test_OSGroupsExist(control):
    common = AUTCommon()
    assert common.login(control)
    assert common.navigateOSGroups(control)    
      
def test_WidgetElementsVisibility(control):
    
    general = General()
    
    #validate pagination is present
    general.toVerifyElement(
        By.CSS_SELECTOR, 
        ".tile.os_groups.locked > div.widgetcontent > div > vne-grid > vne-grid-table > div.grid-record-count > div", 
        "Validate pagination is present on OS Groups Widget", 
        control
    )
    
    #filter is present
    general.toVerifyElement(
        By.CSS_SELECTOR, 
        ".tile.os_groups.locked > div.widgetcontent > div > vne-grid > div > input", 
        "Validate filter is present on OS Groups Widget", 
        control
    )
    
    #reload button exists
    general.toVerifyElement(
        By.CSS_SELECTOR, 
        ".tile.os_groups.locked .top-icons.ui-icon-container > span:nth-child(1) > a", 
        "Validate reload is present on OS Groups widget", 
        control
    )
    
    #Maximize button exists 
    general.toVerifyElement(
        By.CSS_SELECTOR, 
        ".tile.os_groups.locked .top-icons.ui-icon-container > span:nth-child(4) > a:nth-child(2)", 
        "Validate maximize button exists on OS Groups widget", 
        control
    )
    
    #Help button exists 
    general.toVerifyElement(
        By.CSS_SELECTOR, 
        ".tile.os_groups.locked .top-icons.ui-icon-container > span:nth-child(3) > a", 
        "Validate maximize button exists on OS Groups widget", 
        control
    )
    
    #Add button exists
    general.toVerifyElement(
        By.CSS_SELECTOR, 
        ".tile.os_groups.locked .widgetcontent > div > vne-grid > div.grid-actions.ui-button-container > span:nth-child(1) > button", 
        "Validate add button exists on OS Groups widget", 
        control
    )
    
    #Edit button exists
    general.toVerifyElement(
        By.CSS_SELECTOR, 
        ".tile.os_groups.locked .widgetcontent > div > vne-grid > div.grid-actions.ui-button-container > span:nth-child(2) > button", 
        "Validate add button exists on OS Groups widget", 
        control
    )
    
    #Delete button exists
    general.toVerifyElement(
        By.CSS_SELECTOR, 
        ".tile.os_groups.locked .widgetcontent > div > vne-grid > div.grid-actions.ui-button-container > span:nth-child(3) > button", 
        "Validate add button exists on OS Groups widget", 
        control
    )
    
    #validate items per page dropdown exists
    general.toVerifyElement(
        By.CSS_SELECTOR, 
        ".tile.os_groups.locked > div.widgetcontent > div > vne-grid > vne-grid-table :nth-child(6) > div.grid-pagination.ui-button-container.ng-scope > div > select", 
        "Validate items per page dropdown exists on OS Groups widget", 
        control
    )
    
    #Validate items per page label exists
    general.toVerifyElement(
        By.CSS_SELECTOR, 
        ".tile.os_groups.locked > div.widgetcontent > div > vne-grid > vne-grid-table :nth-child(6) > div.grid-pagination.ui-button-container.ng-scope > div > span", 
        "Validate items per page dropdown exists on OS Groups widget", 
        control
    )
    
    #validate selected page exists
    general.toVerifyElement(
        By.CSS_SELECTOR, 
        ".tile.os_groups.locked > div.widgetcontent > div > vne-grid > vne-grid-table :nth-child(6) > div.grid-pagination.ui-button-container.ng-scope > form > input", 
        "Validate page selection input exists on OS Groups widget", 
        control
    )
    
    #Validate selectAll checkbox exists
    general.toVerifyElement(
        By.XPATH, 
        "//div[@class='tile os_groups locked']/div[3]/div/vne-grid/vne-grid-table/div[2]/div/div/div/div/div/div/div/div/div/div/div/input", 
        "Validate 'Select all' checkbox exists on OS Groups widget", 
        control
    )

    assert general.verify()
    
def test_itemCount(control):
    
    general = General()
    
    try:
        itemCount = control.find_element_by_css_selector(".tile.os_groups.locked > div.widgetcontent > div > vne-grid > vne-grid-table > div.grid-record-count > div").get_attribute("innerHTML")
        OSGroupsList = control.find_elements_by_css_selector(".tile.os_groups.locked > div.widgetcontent > div > vne-grid > vne-grid-table :nth-child(6) > div > div .ui-grid-viewport.ng-isolate-scope > div > div")

        assert general.getItemCount(itemCount) == len(OSGroupsList)
        
    except:
        assert False

def test_reload(control):
    
    try:
        control.find_element_by_css_selector(".tile.os_groups.locked .top-icons.ui-icon-container > span:nth-child(1) > a").click()
        
        #Wait for item count to display
        WebDriverWait(control, nDelay).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".tile.os_groups.locked > div.widgetcontent > div > vne-grid > vne-grid-table > div.grid-record-count > div"))
        )
    except:
        assert False

def test_itemsPerPage(control):
    
    perPage = (20, 50 , 100, 200)
    wSelect = control.find_elements_by_css_selector(".tile.os_groups.locked > div.widgetcontent > div > vne-grid > vne-grid-table :nth-child(6) > div.grid-pagination.ui-button-container.ng-scope > div > select > option")
    
    for index in range(len(wSelect)):
        assert int(wSelect[index].get_attribute("label")) == perPage[index]                       

def test_validateDefaultOS(control):
    
    defaultOS = ("Tripwire: Cisco", "Tripwire: Linux", "Tripwire: Network Infrastructure", "Tripwire: Sun Microsystems","Tripwire: Unix Variant","Tripwire: Windows")
    wOSGroups = control.find_elements_by_css_selector(".tile.os_groups.locked > div.widgetcontent > div > vne-grid > vne-grid-table :nth-child(6) > div > div .ui-grid-viewport.ng-isolate-scope > div > div > div > div:nth-child(2) > div")
    OSgroupList = []
    
    for element in wOSGroups:
        OSgroupList.append(element.get_attribute("innerHTML"))
        
    for index in range(len(defaultOS)):
        assert defaultOS[index] in OSgroupList

def test_addOSGroup(control):
    
    actions = ActionChains(control)
    
    try:        
        control.find_element_by_css_selector(".tile.os_groups.locked .widgetcontent > div > vne-grid > div.grid-actions.ui-button-container > span:nth-child(1) > button").click()
        WebDriverWait(control, nDelay).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#node-tree-item-1882")))
        control.find_element_by_css_selector(
            "body > div.modal.modal-wizard.modal-wizard-os_groups.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.wizard-content > div > div > div > form > div > div:nth-child(1) > div > label > input"
            ).send_keys(groupName)
        actions.double_click(control.find_element_by_xpath("//form[@name='osgroups_form']/div/div[3]/div/div/ul/li[1]/div")).perform()
        actions.double_click(control.find_element_by_xpath("//form[@name='osgroups_form']/div/div[3]/div/div/ul/li[5]/div")).perform()
        control.find_element_by_css_selector("body > div.modal.modal-wizard.modal-wizard-os_groups.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.wizard-content > div > div > div > div > button.action").click()
        
        WebDriverWait(control, nDelay).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".tile.os_groups.locked > div.widgetcontent > div > vne-grid > vne-grid-table > div.grid-record-count > div"))
        )
        
        WebDriverWait(control, nDelay).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, ".tile.os_groups.locked > div.widgetcontent > div > vne-grid > vne-grid-table :nth-child(6) > div > div:nth-child(2) > div.grid-loading-overlay.ng-scope.ng-hide > div > span"))
        )
        
        WebDriverWait(control, nDelay).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), '"+groupName+"')]"))
        )
        
        wOSGroups = control.find_elements_by_css_selector(".tile.os_groups.locked > div.widgetcontent > div > vne-grid > vne-grid-table :nth-child(6) > div > div .ui-grid-viewport.ng-isolate-scope > div > div > div > div:nth-child(2) > div")
        OSgroupList = []
        
        for element in wOSGroups:
            OSgroupList.append(element.get_attribute("innerHTML"))
        
        assert groupName in OSgroupList
        
    except:
        assert False

def test_editOSGroup(control):
    try:
        wOSGroups = control.find_elements_by_css_selector(".tile.os_groups.locked > div.widgetcontent > div > vne-grid > vne-grid-table :nth-child(6) > div > div .ui-grid-viewport.ng-isolate-scope > div > div > div > div:nth-child(2) > div")
        checkBoxList = control.find_elements_by_css_selector(".tile.os_groups.locked > div.widgetcontent > div > vne-grid > vne-grid-table :nth-child(6) > div > div .ui-grid-viewport.ng-isolate-scope > div > div > div  > div > div > input")
        
        for index in range(len(wOSGroups)):
            if groupName == str(wOSGroups[index].get_attribute("innerHTML")):
                checkBoxList[index].click()
                checkBox = checkBoxList[index]
                OSGroup = wOSGroups[index]
                break
            
        control.find_element_by_css_selector(".tile.os_groups.locked .widgetcontent > div > vne-grid > div.grid-actions.ui-button-container > span:nth-child(2) > button").click()
        
        WebDriverWait(control, nDelay).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#node-tree-item-1882")))
        
        control.find_element_by_css_selector(
                "body > div.modal.modal-wizard.modal-wizard-os_groups.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.wizard-content > div > div > div > form > div > div:nth-child(1) > div > label > input"
                ).send_keys("_EDITED")
        control.find_element_by_css_selector("body > div.modal.modal-wizard.modal-wizard-os_groups.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.wizard-content > div > div > div > div > button.action").click()
        
        WebDriverWait(control, nDelay).until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), '"+groupName + "_EDITED"+"')]"))
            )
        
        assert groupName + "_EDITED" == str(OSGroup.get_attribute("innerHTML"))
        
        checkBox.click()

    except:
        assert False
        
def test_deleteOSGroup(control):
    
    general = General()
    
    try:
        wOSGroups = control.find_elements_by_css_selector(".tile.os_groups.locked > div.widgetcontent > div > vne-grid > vne-grid-table :nth-child(6) > div > div .ui-grid-viewport.ng-isolate-scope > div > div > div > div:nth-child(2) > div")
        checkBoxList = control.find_elements_by_css_selector(".tile.os_groups.locked > div.widgetcontent > div > vne-grid > vne-grid-table :nth-child(6) > div > div .ui-grid-viewport.ng-isolate-scope > div > div > div  > div > div > input")
        
        for index in range(len(wOSGroups)):
            if groupName + "_EDITED" == str(wOSGroups[index].get_attribute("innerHTML")):
                checkBoxList[index].click()
                break
    
        control.find_element_by_css_selector(".tile.os_groups.locked .widgetcontent > div > vne-grid > div.grid-actions.ui-button-container > span:nth-child(3) > button").click()

        time.sleep(2)      
        
        control.find_element_by_css_selector(".actions.ui-button-container > button:nth-child(2)").click()
        
        WebDriverWait(control, nDelay).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".tile.os_groups.locked > div.widgetcontent > div > vne-grid > vne-grid-table > div.grid-record-count > div"))
        )
        
        WebDriverWait(control, nDelay).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, ".tile.os_groups.locked > div.widgetcontent > div > vne-grid > vne-grid-table :nth-child(6) > div > div:nth-child(2) > div.grid-loading-overlay.ng-scope.ng-hide > div > span"))
        )
        
        time.sleep(2)   
        
        assert len(control.find_elements_by_xpath("//*[contains(text(), '"+groupName + "_EDITED"+"')]")) == 0
        
    except Exception as e:
        print(e)
        assert False

def test_selectedPage(control):
    wInputPage = control.find_element_by_css_selector(".tile.os_groups.locked > div.widgetcontent > div > vne-grid > vne-grid-table :nth-child(6) > div.grid-pagination.ui-button-container.ng-scope > form > input")
    nMinPage = int(wInputPage.get_attribute("min"))
    nMaxPage = int(wInputPage.get_attribute("max"))
    
    if nMinPage != nMaxPage:
        wInputPage.send_keys(nMaxPage)
        wOSGroupList = control.find_element_by_css_selector(".tile.os_groups.locked > div.widgetcontent > div > vne-grid > vne-grid-table :nth-child(6) > div > div .ui-grid-viewport.ng-isolate-scope > div > div")
        assert len(wOSGroupList) > 0
        

def test_checkAll(control):
    wCheckAll = control.find_element_by_xpath("//div[@class='tile os_groups locked focused']/div[3]/div/vne-grid/vne-grid-table/div[2]/div/div/div/div/div/div/div/div/div/div/div/input")
    
    wCheckAll.click()
    
    checkBoxList = control.find_elements_by_css_selector(".tile.os_groups.locked > div.widgetcontent > div > vne-grid > vne-grid-table :nth-child(6) > div > div .ui-grid-viewport.ng-isolate-scope > div > div > div  > div > div > input")
    
    assert bool(wCheckAll.get_attribute("checked"))
    
    for checkboxAttribute in checkBoxList:
        assert bool(checkboxAttribute.get_attribute("checked"))
        
def test_maximize(control):

    try:
        control.find_element_by_css_selector(".tile.os_groups.locked .top-icons.ui-icon-container > span:nth-child(4) > a:nth-child(2)").click()
        WebDriverWait(control, nDelay).until(EC.visibility_of_element_located((By.ID, "dash-sidebar")))
        
        WebDriverWait(control, nDelay).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='tile os_groups locked focused expanded']/div[2]/span[4]/a[1]")))
        
        minimizeButton = control.find_element_by_xpath("//div[@class='tile os_groups locked focused expanded']/div[2]/span[4]/a[1]")
        maximizeButton = control.find_element_by_xpath("//div[@class='tile os_groups locked focused expanded']/div[2]/span[4]/a[2]")
        
        assert str(maximizeButton.get_attribute("class")) == "ng-hide"
        
        minimizeButton.click()
        
        control.find_element_by_xpath("//div[@class='tile os_groups locked focused']/div[2]/span[4]/a[2]")
        assert str(control.find_element_by_xpath("//div[@class='tile os_groups locked focused']/div[2]/span[4]/a[1]").get_attribute("class")) == "ng-hide"
        assert control.find_elements_by_xpath("//div[@class='tile os_groups locked focused']/div[2]/span[4]/a[2]")
        #assert control.find_element_by_id("dash-sidebar")

    except:
        assert False

    