
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time

import os

def calculate():
    driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"))
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver.get("https://azure.microsoft.com/en-in/pricing/calculator/#virtual-machines4904e425-8d44-4a9a-9083-4ef1fd5993fb")
    try:
        # vm click
        sel_vm = WebDriverWait(driver, 30000).until(
            EC.presence_of_element_located((By.XPATH, "//button[@title='Virtual Machines']"))
        )
        # time setting
        sel_vm.click()
        hours = WebDriverWait(driver, 30000).until(
            EC.presence_of_element_located((By.NAME, "hours"))
        )
        hours.clear()
        hours.send_keys('1')
        # OS setting
        select_os = WebDriverWait(driver, 30000).until(
            EC.presence_of_element_located((By.NAME, "operatingSystem"))
        )
        select_os_options = Select( driver.find_element_by_name("operatingSystem") )
        select_os_options.select_by_index(0)
        # Resource setting
        size_select = WebDriverWait(driver, 30000).until(
            EC.presence_of_element_located((By.NAME, "size"))
        )
        select_size_options = Select( driver.find_element_by_name("size") )
        for size_i in range(len(select_size_options.options)):
            print("resource size")
            print(size_i)
            select_size_options = Select( driver.find_element_by_name("size") )
            select_size_options.select_by_index(size_i)
            # pay per hour
            radio_payg = WebDriverWait(driver, 30000).until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='radio' and @value='payg']"))
            )
            radio_payg.click()
            # region setting
            region_select = WebDriverWait(driver, 30000).until(
                EC.presence_of_element_located((By.NAME, "region"))
            )
            region_select_options = Select( driver.find_element_by_name("region") )
            for region_i in range(len(region_select_options.options)):
                print("payg region number")
                print(region_i)
                region_select_options.select_by_index(region_i)
                clone_button = WebDriverWait(driver, 30000).until(
                    EC.presence_of_element_located((By.XPATH, "//button[@title='Clone']"))
                )    
                clone_button.click()
            # two year setting
            radio_one_year = WebDriverWait(driver, 30000).until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='radio' and @value='one-year']"))
            )                         
            radio_one_year.click()
            region_select_options = Select( driver.find_element_by_name("region") )
            for region_i in range(len(region_select_options.options)):
                print("one-year region number")
                print(region_i)
                region_select_options.select_by_index(region_i)
                clone_button = WebDriverWait(driver, 30000).until(
                    EC.presence_of_element_located((By.XPATH, "//button[@title='Clone']"))
                )    
                clone_button.click()
            # three year setting
            radio_three_year = WebDriverWait(driver, 30000).until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='radio' and @value='three-year']"))
            )                                         
            radio_three_year.click()
            region_select_options = Select( driver.find_element_by_name("region") )
            for region_i in range(len(region_select_options.options)):
                print("third-year region number")
                print(region_i)
                region_select_options.select_by_index(region_i)
                clone_button = WebDriverWait(driver, 30000).until(
                    EC.presence_of_element_located((By.XPATH, "//button[@title='Clone']"))
                )    
                clone_button.click()

        export_button = WebDriverWait(driver, 30000).until(
            EC.presence_of_element_located((By.CLASS_NAME, "export-button"))
        )
        export_button.click()
        time.sleep(30)
    finally:
        print('end')

calculate()
