import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from UtilityScripts.excel_methods import ExcelMethods
    
class TestLogin:    
    @pytest.mark.parametrize('s_num, username, password', ExcelMethods('Sheet').get_parametrize_list())
    def test_001(self, s_num, username, password):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get('http://127.0.0.1:8000/login')
        self.driver.find_element(By.ID, 'id_username').send_keys(username)
        self.driver.find_element(By.ID, 'id_password').send_keys(password)
        self.driver.find_element(By.ID, 'login_button').click()
        time.sleep(2)    
        if 'Logged in successfully' in self.driver.find_element(By.ID, 'notice').text:
            status = True
        else:
            status = False
        ExcelMethods('Sheet').update_result_in_excel(s_num, status)
        self.driver.quit()