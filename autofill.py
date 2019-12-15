import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

"""
create folder for the selenium data related files
"""
if not os.path.exists('data'):
    os.makedirs('data')

# web driver
driver = webdriver.Chrome("./chromedriver.exe")

def website_url(url):
    """
    link to the website with forms
    """
    driver.get(url)
"""modal clicking function"""

def click_contact_us(modal_button="menu-item-49"):
    elem = driver.find_element_by_xpath("//li[@id='menu-item-49']/a")
    driver.execute_script("arguments[0].click();", elem)


def get_element(field_id, value):
    """gets an elament from a form and fills with the value"""
    element = driver.find_element_by_id(field_id)
    element.send_keys(value)
 

def select_all_that_apply_box(opt1="demo",opt2='info_park',opt3='call_back'):
    """checks the number of employee box"""
    elem = driver.find_element_by_xpath(
        "//div[@class='form-group select-services']/span[@class='wpcf7-form-control-wrap SelectType']/span[@class='wpcf7-form-control wpcf7-checkbox wpcf7-validates-as-required']/span[@class='wpcf7-list-item first']")
    elem2 = driver.find_element_by_xpath(
        "//div[@class='form-group select-services']/span[@class='wpcf7-form-control-wrap SelectType']/span[@class='wpcf7-form-control wpcf7-checkbox wpcf7-validates-as-required']/span[@class='wpcf7-list-item']")  
    elem3 = driver.find_element_by_xpath(
        "//div[@class='form-group select-services']/span[@class='wpcf7-form-control-wrap SelectType']/span[@class='wpcf7-form-control wpcf7-checkbox wpcf7-validates-as-required']/span[@class='wpcf7-list-item last']")
    if opt1:
        elem.click()
    if opt2:
        elem2.click()
    if opt3:
        elem3.click()

def click_add_message():
    """ add message to texterea"""
    driver.find_element_by_xpath("//div[@class='form-group msg-box']/h6").click()


def add_message(msg):
    """fill message textarea"""
    elem = driver.find_element_by_xpath("//div[@class='form-group msg-box']/textarea[@class='wpcf7-form-control wpcf7-textarea form-control']")
    elem.send_keys(msg)
   
def agree_to_terms_and_conditions():
    """chejcks the agree to terms and condition checkbox"""
    driver.find_element_by_name("acceptance").click()
    
def submit_form():
    """fiorm submiter"""
    elem = driver.find_element_by_xpath("//div[@class='form-group submit-btn']/input")
    elem.click()

    
def test_all_pages(url_resource=""):
    """responsible for testing the various pages. You pass the actual page identifier eg /products"""
    url  = "https://cascadehr.co.uk/{}".format(url_resource)
    return url

if __name__ == "__main__":

    urls = ["", "resources/"]
    for url in urls:
        url = test_all_pages(url_resource=url)
        website_url(url)
        click_contact_us()
        field_ids = ['firstname','lastname','email','companyName', 'phone']
        field_values = ['testfname',"testlname",'testemail@gmail.com','testcomapnyname','0700000000']
        field_ids_values = zip(field_ids, field_values)
        for i in field_ids_values:

            get_element(i[0],i[1])
        select_all_that_apply_box()
        msg = "Lorem ipsum is placeholder text commonly"
        click_add_message()
        add_message(msg=msg) 
        agree_to_terms_and_conditions()
        submit_form()
        time.sleep(2)