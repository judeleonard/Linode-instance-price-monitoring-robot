from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import smtplib
import imghdr
import requests
from bs4 import BeautifulSoup
from email.message import EmailMessage
#from config.auth import (SENDER, PASSWORD, TARGET_WEBSITE)

import os
import time


class Robot:

    def grab_element(self):
        url = os.environ['TARGET_WEBSITE']
        chromeOptions = Options()
        # choose to headless chrome browser here since the robot will run in production mode
        chromeOptions.headless = True
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chromeOptions) 
        driver.get(url)
        time.sleep(3)
        file_data = driver.find_element(By.ID, "compute-high-memory")
        file_data.screenshot(f"{os.getcwd()}/screenshots/linode_price_summary.png")

        driver.quit()


    def send_latest_price(self):
        sender = os.environ['SENDER']
        recipient = "judeleonard86@gmail.com"
        password = os.environ['PASSWORD']

        incoming_message = EmailMessage()   # create an object email message class
        incoming_message['Subject'] = "Latest AWS Prices for Linode Services"
        incoming_message['From'] = sender
        incoming_message['To'] = recipient
        incoming_message.set_content('Checkout the latest pricing for Linode!')

        filename=f"{os.getcwd()}/screenshots/AWS_price_summary.png"   # directory to saved screenshot
        with open(filename, 'rb') as file:  # identify the kind of data we wish to attach using imghdr module
            image_data = file.read()
            image_type = imghdr.what(file.name)
            image_name = file.name

        incoming_message.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(incoming_message)



def monitor_updates():
    # agent for making html requests to avoid connection exception error
    config = {
        'Accept-Language': 'en-US,en;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    }
    url = TARGET_WEBSITE
    response = requests.get(url, headers=config)
    if response.status_code != 200:
	    print("Error getting page")
	    exit()
    else:
        webpage = response.text
        soup = BeautifulSoup(webpage, 'html.parser')
        tables = soup.find_all('table')
        target_table = soup.find('div', id ="compute-high-memory")
        # grab the price in a text format and convert to integer
        # here current price represents our current plan for linode service
        linode_current_price = int(target_table.find('td', class_='row--linode-150-gb').getText().split('$')[1])
        # grab the price of linode per month for 150gb ram
        # our robot will send us a message once the price exceeds or equals $500
        if linode_current_price >= 500:
            my_robot = Robot()  # initialize out robot class
            my_robot.grab_element()
            my_robot.send_latest_price()

        else:
            exit()








if __name__ == "__main__":
    monitor_updates()
