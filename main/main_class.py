import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

username = "Admin"
password = "admin123"
wait_time = 10
name = "random_ShiftName"
assigned_emmployees = "Odis Adalwin"
button_login_xpath = '//button[@type="submit"]'
menu_Admin_xpath = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a"
menu_job_xpath = "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span"
work_xpath = "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[5]/a"
button_add_xpath = "/html/body/div/div[1]/div[2]/div[2]/div/div/div[1]/div/button"
shift_name_xpath = "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input"
clock1_xpath = "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div/i"
clock2_xpath = "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div/i"
assigned_employees_xpath = "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/div/div[1]/input"
button_save_xpath = "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[4]/button[2]"
bin_xpath = "/html/body/div/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[2]/div/div[6]/div/button[1]/i"
yes_xpath = "/html/body/div/div[3]/div/div/div/div[3]/button[2]"
check_xpath = f"//div[contains(., '{name}') and contains(., '06:00') and contains(., '18:00') and contains(., '12.00')]"


class TestWebPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    def log_page(self):
        WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located((By.NAME, 'username'))).send_keys(
            username)
        self.driver.find_element(By.NAME, 'password').send_keys(password)
        self.driver.find_element(By.XPATH, button_login_xpath).click()

    def add_page(self):
        WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located((By.XPATH, menu_Admin_xpath))).click()
        WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located((By.XPATH, menu_job_xpath))).click()
        self.driver.find_element(By.XPATH, work_xpath).click()

    def set_clock(self):
        self.driver.find_element(By.XPATH, clock1_xpath).click()
        for i in range(3):
            self.driver.find_element(By.XPATH,
                                     "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div[1]/i[2]").click()
        self.driver.find_element(By.XPATH, clock2_xpath).click()
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/i[1]").click()
        self.driver.find_element(By.XPATH, clock2_xpath).click()

    def add_record(self):
        WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located((By.XPATH, button_add_xpath))).click()
        WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located((By.XPATH, shift_name_xpath))).send_keys(name)

    def save_record(self):
        self.driver.find_element(By.XPATH, assigned_employees_xpath).send_keys(assigned_emmployees)
        self.driver.find_element(By.XPATH, button_save_xpath).click()


    def check_record(self):
        WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located(
                (By.XPATH, check_xpath)))


    def del_record(self):
        row_del = self.driver.find_element(By.XPATH, check_xpath)
        row_del.find_element(By.XPATH, bin_xpath).click()
        self.driver.find_element(By.XPATH, yes_xpath).click()

    def check_record_after(self):
        try:
            WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located(
                (By.XPATH, check_xpath)))
        except Exception as ex:
            return None
        assert False, 'Element is found'
    def close_page(self):
        self.driver.close()
