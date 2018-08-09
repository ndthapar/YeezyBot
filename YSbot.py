
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
# ---- input already returns string 
# config file to store user inputs

def size_input():
    print('Enter size choices going from highest to lowest priority')
    ask_choices = ['first choice: ', 'second choice: ', 'third choice: ', 'fourth choice: ', 'fifth choice: ', 'sixth choice: ',
                        'seventh choice: ', 'eighth choice: ']
    saved_choices = []
    for i in range(7):
        print(ask_choices[i])
        choice = input()
        saved_choices.append(choice)


size_input()


# In[4]:


options = Select(driver.find_elements_by_tag_name('select')[0])


#following function could be handled in for loop running through the array of choices

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

#locate and click "purchase" option to move onto personal information

test = driver.find_elements_by_tag_name('input')


def purchase_click_test():
    for element in test:
        try:
            element.click()
        except: 
            continue
        return element


def use_purchase_click():
    use = purchase_click_test()
    if use is None:
        print("failed")
        return
    wait1 = WebDriverWait(driver, 1)
    cart = wait1.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="js-wrap"]/div[1]/div[2]/a/span[1]')))
    cart.click()
    
        



purchase_click()
wait2 = WebDriverWait(driver, 5000)
checkout = wait2.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="js-main"]/div/form/div/div[3]/input[2]')))
checkout.click()


# In[ ]:


wait3 = WebDriverWait(driver, 100)
wait3.until(EC.presence_of_element_located((By.XPATH, '//*[@id="checkout_email"]')))

#reinitiate driver for queue skip
skip_line_url = driver.current_url
link = skip_line_url
driver = webdriver.Chrome()
driver.get(link)

    
#personal info and captcha page
email = driver.find_element_by_xpath('//*[@id="checkout_email"]').send_keys('johndoe@gmail.com')
first_name = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_first_name"]').send_keys('john')
last_name = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_last_name"]').send_keys('doe')
address = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_address1"]').send_keys('1234 easy street')
city = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_city"]').send_keys('city')
zip_code = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_zip"]').send_keys('12345')
input("solve captcha and press enter")
phone = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_phone"]').send_keys('1234567892', Keys.RETURN)
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


# In[ ]:


time.sleep(5)
print(driver.page_source)


# In[ ]:


#Credit card number iframe located by partial ID then input passed
time.sleep(6)
iframe = driver.switch_to.frame(driver.find_element_by_xpath('//*[contains(@id,"card-fields-number")]'))
credit_card = driver.find_element_by_id('number')
card_number = credit_card.click()
card_number = credit_card.send_keys('6234234212345232')
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
card_expiry = credit_card.send_keys('0111')
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

