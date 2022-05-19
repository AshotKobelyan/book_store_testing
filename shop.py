import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
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

### Логин в системе ###
#my_account_btn = driver.find_element_by_id("menu-item-50")
#my_account_btn.click()
#time.sleep(10)
#login_email = driver.find_element_by_id("username")
#login_email.send_keys("tkillgore@gmail.com")
#login_password = driver.find_element_by_id("password")
#login_password.send_keys("tacitus1tacitus2")
#login_btn = driver.find_element_by_css_selector('[name="login"]')
#login_btn.click()

shop_btn = driver.find_element_by_id("menu-item-40")
shop_btn.click()
driver.execute_script("window.scrollBy(0, 300);")

### Shop: отображение страницы товара ###
#HTML_5_forms = driver.find_element_by_css_selector('[title="Mastering HTML5 Forms"]')
#HTML_5_forms.click()
#title = driver.find_element_by_css_selector('[itemprop="name"]')
#title_text = title.text
#assert title_text == "HTML5 Forms"

### Shop: количество товаров в категории ###
#HTML_btn = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/product-category/html/"]')
#HTML_btn.click()
#products = driver.find_elements_by_class_name("product")
#assert len(products) == 3

### Shop: сортировка товаров ###
#selector_orderby = driver.find_element_by_css_selector('[name="orderby"]')
#selector_orderby_default = selector_orderby.get_attribute("value")
#assert selector_orderby_default == "menu_order"
#select = Select(selector_orderby)
#select.select_by_value("price-desc")
#selector_orderby = driver.find_element_by_css_selector('[name="orderby"]')
#selector_orderby_default = selector_orderby.get_attribute("value")
#assert selector_orderby_default == "price-desc"

### Shop: отображение, скидка товара ###
#Android = driver.find_element_by_css_selector('[title="Android Quick Start Guide"]')
#Android.click()
#book_old_price = driver.find_element_by_css_selector(".price>del>span")
#book_old_price_text = book_old_price.text
#book_new_price = driver.find_element_by_css_selector(".price>ins>span")
#book_new_price_text = book_new_price.text
#assert book_old_price_text == "₹600.00"
#assert book_new_price_text == "₹450.00"
#wait = WebDriverWait(driver, 10)
#book_cover = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
#book_cover.click()
#exit_book_cover = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
#exit_book_cover.click()

### Shop: проверка цены в корзине ###
#HTML5_WebApp_Development_add_btn = driver.find_element_by_css_selector('[data-product_id="182"]')
#HTML5_WebApp_Development_add_btn.click()
#time.sleep(5)
#cart_item = driver.find_element_by_css_selector(".cartcontents")
#cart_item_text = cart_item.text
#cart_price = driver.find_element_by_css_selector(".amount")
#cart_price_text = cart_price.text
#assert cart_item_text == "1 Item"
#assert cart_price_text == "₹180.00"
#cart_btn = driver.find_element_by_css_selector('[class="wpmenucart-contents"]')
#cart_btn.click()
#wait = WebDriverWait(driver, 10)
#subtotal = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[data-title="Subtotal"]'), "₹180.00"))
#total = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[data-title="Total"]:nth-child(2)'), "₹189.00"))

### Shop: работа в корзине ###
#HTML5_WebApp_Development_add_btn = driver.find_element_by_css_selector('[data-product_id="182"]')
#HTML5_WebApp_Development_add_btn.click()
#time.sleep(30)
#JS_Data_Structures_and_Algorithm_add_btn = driver.find_element_by_css_selector('[data-product_id="180"]')
#JS_Data_Structures_and_Algorithm_add_btn.click()
#cart_btn = driver.find_element_by_css_selector('[class="wpmenucart-contents"]')
#cart_btn.click()
#time.sleep(5)
#HTML5_WebApp_Development_remove_btn = driver.find_element_by_css_selector('[class="cart_item"]>[class="product-remove"]:nth-child(1) [data-product_id="182"]')
#HTML5_WebApp_Development_remove_btn.click()
#time.sleep(5)
#undo_btn = driver.find_element_by_link_text("Undo?")
#undo_btn.click()
#JS_Data_Structures_and_Algorithm_input = driver.find_element_by_css_selector('[name="cart[045117b0e0a11a242b9765e79cbf113f][qty]"]')
#JS_Data_Structures_and_Algorithm_input.clear()
#JS_Data_Structures_and_Algorithm_input.send_keys("3")
#time.sleep(10)
#update_cart_btn = driver.find_element_by_css_selector('[name="update_cart"]')
#update_cart_btn.click()
#time.sleep(10)
#JS_Data_Structures_and_Algorithm_quantity = driver.find_element_by_css_selector('[name="cart[045117b0e0a11a242b9765e79cbf113f][qty]"]')
#JS_Data_Structures_and_Algorithm_quantity_3 = JS_Data_Structures_and_Algorithm_quantity.get_attribute("value")
#assert JS_Data_Structures_and_Algorithm_quantity_3 == "3"
#time.sleep(10)
#apply_coupon_btn = driver.find_element_by_css_selector('[name="apply_coupon"]')
#apply_coupon_btn.click()
#coupon = driver.find_element_by_css_selector(".woocommerce-error")
#coupon_text = coupon.text
#assert coupon_text == "Please enter a coupon code."

### Shop: покупка товара ###
HTML5_WebApp_Development_add_btn = driver.find_element_by_css_selector('[data-product_id="182"]')
HTML5_WebApp_Development_add_btn.click()
cart_btn = driver.find_element_by_css_selector('[class="wpmenucart-contents"]')
cart_btn.click()
checkout_btn = driver.find_element_by_css_selector(".checkout-button")
checkout_btn.click()
wait = WebDriverWait(driver, 10)
first_name = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[for="billing_first_name"]'), "First Name"))
first_name_textarea = driver.find_element_by_id("billing_first_name")
first_name_textarea.send_keys("Tacitus")
last_name_textarea = driver.find_element_by_id("billing_last_name")
last_name_textarea.send_keys("Killgore")
email_textarea = driver.find_element_by_id("billing_email")
email_textarea.send_keys("tkillgore@gmail.com")
phone_textarea = driver.find_element_by_id("billing_phone")
phone_textarea.send_keys("+79998765511")
country_selector = driver.find_element_by_class_name("select2-choice")
country_selector.click()
country_selector_textarea = driver.find_element_by_class_name("select2-input")
country_selector_textarea.send_keys("Russia")
selector_btn = driver.find_element_by_css_selector(".select2-result-label")
selector_btn.click()
address_1 = driver.find_element_by_css_selector('[name="billing_address_1"]')
address_1.send_keys("Solnechnaya")
address_2 = driver.find_element_by_css_selector('[name="billing_address_2"]')
address_2.send_keys("999")
city = driver.find_element_by_css_selector('[name="billing_city"]')
city.send_keys("Grad Kitezh")
state = driver.find_element_by_css_selector('[name="billing_state"]')
state.send_keys("Grad Kitezh")
postcode = driver.find_element_by_css_selector('[name="billing_postcode"]')
postcode.send_keys("90210")
driver.execute_script("window.scrollBy(0, 600);")
payment_checkbox = driver.find_element_by_id("payment_method_cheque")
payment_checkbox.click()
place_order = driver.find_element_by_id("place_order")
place_order.click()
thank_you = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
payment_method = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".method"), "Check Payments"))
#time.sleep(3)
#driver.quit()
