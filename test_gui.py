import pytest
from  selenium import webdriver
from selenium.webdriver.common.by import By


class TestSelenium:

    @pytest.mark.ui
    @pytest.mark.parametrize('username,password',[('standard_user','secret_sauce'),('problem_user','secret_sauce'),('performance_glitch_user','secret_sauce')])
    def test_tc1_valid_username(self,username,password):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://www.saucedemo.com/')
        driver.find_element(By.NAME,'user-name').send_keys(username)
        driver.find_element(By.NAME,'password').send_keys(password)
        driver.find_element(By.NAME,'login-button').click()
        print(driver.title)
        total_list_items=driver.find_elements(By.XPATH,"//div[@class='inventory_item']//div[@class='inventory_item_label']/a/div")
        assert len(total_list_items) ==6
        driver.close()

