
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# In[2]:


#initiate driver
link = "https://yeezysupply.com/"
driver = webdriver.Chrome()
driver.get(link)


# In[3]:


# add selection to fill size choice variables here
print('Enter size choices in order of priority')
first_choice = str(input('first choice:'))
second_choice = str(input('second choice:'))
third_choice = str(input('third choice:'))
fourth_choice = str(input('fourth choice:'))
fifth_choice = str(input('fifth choice:'))
sixth_choice = str(input('sixth choice:'))
seventh_choice = str(input('seventh choice:'))
eighth_choice = str(input('eighth choice:'))


# In[4]:


options = Select(driver.find_elements_by_tag_name('select')[0])



def select_size(first_choice,second_choice,third_choice,fourth_choice,fifth_choice, sixth_choice, seventh_choice, eighth_choice):     
        try:
            options.select_by_visible_text(first_choice)
        except: 
            try:
                options.select_by_visible_text(second_choice)
            except:     
                try:
                    options.select_by_visible_text(third_choice)    
                except:
                    try:
                        options.select_by_visible_text(fourth_choice)
                    except:
                        try:
                            options.select_by_visible_text(fifth_choice)
                        except:
                            try:
                                options.select_by_visible_text(sixth_choice)
                            except:
                                try:
                                    options.select_by_visible_text(seventh_choice)
                                except:
                                    try:
                                        options.select_by_visible_text(eighth_choice)
                                    except:
                                        print('size selection error')
                                        pass
                                    


select_size(first_choice,second_choice,third_choice,fourth_choice,fifth_choice, sixth_choice, seventh_choice, eighth_choice)

#run through purchase clicks

test = driver.find_elements_by_tag_name('input')

def purchase_click():
    try:
        test[0].click()
        wait1 = WebDriverWait(driver, 1)
        cart = wait1.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="js-wrap"]/div[1]/div[2]/a/span[1]')))
        cart.click()
    except:
        try:
            test[1].click()
            wait1 = WebDriverWait(driver, 1)
            cart = wait1.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="js-wrap"]/div[1]/div[2]/a/span[1]')))
            cart.click()

        except:
            try:
                test[2].click()
                wait1 = WebDriverWait(driver, 1)
                cart = wait1.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="js-wrap"]/div[1]/div[2]/a/span[1]')))
                cart.click()
            except:
                try:
                    test[3].click()
                    wait1 = WebDriverWait(driver, 1)
                    cart = wait1.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="js-wrap"]/div[1]/div[2]/a/span[1]')))
                    cart.click()
                except:
                    try:
                        test[4].click()
                        wait1 = WebDriverWait(driver, 1)
                        cart = wait1.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="js-wrap"]/div[1]/div[2]/a/span[1]')))
                        cart.click()
                    except:
                        pass
                        try:
                            test[5].click()
                            wait1 = WebDriverWait(driver, 1)
                            cart = wait1.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="js-wrap"]/div[1]/div[2]/a/span[1]')))
                            cart.click()
                        except:
                            try:
                                test[6].click()
                                wait1 = WebDriverWait(driver, 1)
                                cart = wait1.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="js-wrap"]/div[1]/div[2]/a/span[1]')))
                                cart.click()
                            except:
                                try:
                                    test[7].click()
                                    wait1 = WebDriverWait(driver, 1)
                                    cart = wait1.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="js-wrap"]/div[1]/div[2]/a/span[1]')))
                                    cart.click()
                                except:
                                    try:
                                        test[8].click()
                                        wait1 = WebDriverWait(driver, 1)
                                        cart = wait1.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="js-wrap"]/div[1]/div[2]/a/span[1]')))
                                        cart.click()
                                    except:
                                        try:
                                            test[9].click()
                                            wait1 = WebDriverWait(driver, 1)
                                            cart = wait1.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="js-wrap"]/div[1]/div[2]/a/span[1]')))
                                            cart.click()
                                        except:
                                            print('purchase button selection error')
                                            pass
                    

purchase_click()
wait2 = WebDriverWait(driver, 5000)
checkout = wait2.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="js-main"]/div/form/div/div[3]/input[2]')))
checkout.click()


# In[5]:


wait3 = WebDriverWait(driver, 5000)
wait4 = WebDriverWait(driver, 20)
wait3.until(EC.presence_of_element_located((By.XPATH, '//*[@id="checkout_email"]')))

#reinitiate driver for queue skip
skip_line_url = driver.current_url
link = skip_line_url
driver = webdriver.Chrome()
driver.get(link)


#personal info and captcha page
email = driver.find_element_by_xpath('//*[@id="checkout_email"]').send_keys('ndthapar@gmail.com')
first_name = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_first_name"]').send_keys('Ken')
last_name = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_last_name"]').send_keys('Bone')
address = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_address1"]').send_keys('1234 Somewhere St.')
city = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_city"]').send_keys('Seattle')
zip_code = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_zip"]').send_keys('98144')
input("solve captcha and press enter")
phone = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_phone"]').send_keys('3052341234', Keys.RETURN)
driver.find_element(By.ID, 'salesFinal').click()
driver.find_element_by_xpath('//*[@id="checkout_shipping_address_phone"]').send_keys(Keys.RETURN)


#Continue to payment method button click --- NOTE: Expand this method to all page transitions 
##so program doesnt falter due to page load times --- Try not to rely on selenium until()

verification_link = str(driver.current_url)

if 'shipping_method' in verification_link:
    time.sleep(3)
    driver.find_element_by_name('button').click()
else:
    print('shipping failed')
    
print(verification_link)


# In[6]:


time.sleep(5)
print(driver.page_source)


# In[7]:


#Credit card number iframe located by partial ID then input passed
time.sleep(6)
iframe = driver.switch_to.frame(driver.find_element_by_xpath('//*[contains(@id,"card-fields-number")]'))
credit_card = driver.find_element_by_id('number')
card_number = credit_card.click()
card_number = credit_card.send_keys('6330228399123456')
driver.switch_to.default_content()

#Credit card name iframe located by partial ID then input passed
iframe = driver.switch_to.frame(driver.find_element_by_xpath('//*[contains(@id,"card-fields-name")]'))
credit_card = driver.find_element_by_id('name')
card_name = credit_card.click()
card_name = credit_card.send_keys('Ken Bone')
driver.switch_to.default_content()

#Credit card expiration date iframe located by partial ID then input passed
iframe = driver.switch_to.frame(driver.find_element_by_xpath('//*[contains(@id,"card-fields-expiry")]'))
credit_card = driver.find_element_by_id('expiry')
card_expiry = credit_card.click()
card_expiry = credit_card.send_keys('1234')
driver.switch_to.default_content()

#Credit card cvv iframe located by partial ID then input passed
iframe = driver.switch_to.frame(driver.find_element_by_xpath('//*[contains(@id,"card-fields-verification_value")]'))
credit_card = driver.find_element_by_id('verification_value')
card_cvv = credit_card.click()
card_cvv = credit_card.send_keys('123')
driver.switch_to.default_content()

#Same billing address as shipping address click: 
billing_address = driver.find_element_by_xpath('//*[contains(@id,"checkout_different_billing_address")]')
billing_address.click()


#complete order click
billing_address.send_keys(Keys.RETURN)


# Thinks to add for those interested:
# 
# 1. GUI allowing input for size choices, pauses at captcha so user can do it manually, different credit cards and IP's
# 2. Captcha harvester
# 3. Refresh script that monitors the drop through some sort of WebElement identification
# 4. URL verification for each page transition so the script doesnt stop -- expansion of method already used
# 5. Input setup to allow for several credit card entries -- expanded
