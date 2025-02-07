from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

class TestOnlineBanking:
    
    @pytest.fixture(scope="class")
    def setup(self):
        """เตรียม WebDriver และเปิดเว็บ"""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://example-bank.com")  # แก้เป็น URL จริง
        yield
        self.driver.quit()

    def test_user_registration(self, setup):
        """ทดสอบการสมัครสมาชิก"""
        driver = self.driver
        driver.find_element(By.ID, "register").click()
        driver.find_element(By.NAME, "username").send_keys("testuser")
        driver.find_element(By.NAME, "password").send_keys("Password123")
        driver.find_element(By.NAME, "confirm_password").send_keys("Password123")
        driver.find_element(By.NAME, "email").send_keys("testuser@example.com")
        driver.find_element(By.ID, "register_submit").click()
        assert "Registration Successful" in driver.page_source

    def test_check_account_balance(self, setup):
        """ทดสอบการล็อกอิน และเช็กยอดเงิน"""
        driver = self.driver
        driver.find_element(By.NAME, "username").send_keys("testuser")
        driver.find_element(By.NAME, "password").send_keys("Password123")
        driver.find_element(By.ID, "login_submit").click()
        balance = driver.find_element(By.ID, "account_balance").text
        assert "$1000.00" in balance  # ตรวจสอบว่ายอดเงินตรงกับที่คาดไว้

    def test_transfer_money(self, setup):
        """ทดสอบการโอนเงิน"""
        driver = self.driver
        driver.find_element(By.ID, "transfer_money").click()
        driver.find_element(By.NAME, "recipient").send_keys("receiver123")
        driver.find_element(By.NAME, "amount").send_keys("100")
        driver.find_element(By.ID, "transfer_submit").click()
        assert "Transfer Successful" in driver.page_source
