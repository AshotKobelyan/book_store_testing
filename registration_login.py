import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
path_to_extension = r'C:\Пользователи\Ашот\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\4.46.2_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
driver = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
driver.create_options()
time.sleep(10)
driver.maximize_window()
driver.implicitly_wait(10)
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)
driver.get("http://practice.automationtesting.in/")
my_account_btn = driver.find_element_by_id("menu-item-50")
my_account_btn.click()
time.sleep(10)

### Registration_login: регистрация аккаунта ###
#register_email = driver.find_element_by_id("reg_email")
#register_email.send_keys("tkillgor2222e@gmail.com")
#register_password = driver.find_element_by_id("reg_password")
#register_password.send_keys("tacitueeees1tacitus2")
#register_btn = driver.find_element_by_css_selector('[name="register"]')
#register_btn.click()

### Registration_login: логин в систему ###
login_email = driver.find_element_by_id("username")
login_email.send_keys("tkillgore@gmail.com")
login_password = driver.find_element_by_id("password")
login_password.send_keys("tacitus1tacitus2")
login_btn = driver.find_element_by_css_selector('[name="login"]')
login_btn.click()
logout = driver.find_element_by_css_selector(".woocommerce-MyAccount-navigation-link:nth-child(6)")
logout_text = logout.text
assert logout_text == "Logout"
#time.sleep(3)
#driver.quit()

