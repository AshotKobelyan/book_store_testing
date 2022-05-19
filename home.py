import time
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
### Home: добавление комментария ###
driver.execute_script("window.scrollBy(0, 600);")
selenium_ruby_btn = driver.find_element_by_css_selector('[title="Selenium Ruby"]')
selenium_ruby_btn.click()
driver.execute_script("window.scrollBy(0, 600);")
SR_reviews_btn = driver.find_element_by_css_selector('[href="#tab-reviews"]')
SR_reviews_btn.click()
driver.execute_script("window.scrollBy(0, 300);")
rating_five = driver.find_element_by_css_selector('[class="star-5"]')
rating_five.click()
review_textarea = driver.find_element_by_id("comment")
review_textarea.send_keys("Nice book!")
name_textarea = driver.find_element_by_id("author")
name_textarea.send_keys("Tacitus")
email_textarea = driver.find_element_by_id("email")
email_textarea.send_keys("tkillgore@gmail.com")
submit_btn = driver.find_element_by_id("submit")
submit_btn.click()
time.sleep(3)
driver.quit()

