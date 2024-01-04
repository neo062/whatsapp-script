from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Replace 'Your Phone Number' with the recipient's phone number (include country code but exclude any + or - symbols)
phone_number = "8250911714"  # For example: 1234567890
message = "Fuck You"

# Path to chromedriver.exe (you need to download this and specify its path)
chrome_driver_path = "/usr/local/bin/chromedriver"

# URL for opening WhatsApp Web
url = "https://web.whatsapp.com/"

# Function to send a message
def send_whatsapp_message():
    driver = webdriver.Chrome(chrome_driver_path)
    driver.get(url)
    input("Please scan the QR code and press any key after logging in to WhatsApp Web...")
    
    try:
        # Wait for WhatsApp Web to load
        time.sleep(10)
        
        # Locate the search box
        search_box = driver.find_element_by_xpath('//div[@class="_3FRCZ copyable-text selectable-text"]')
        search_box.click()
        search_box.send_keys(f"{phone_number}{Keys.ENTER}")
        time.sleep(2)
        
        # Locate the message box
        message_box = driver.find_element_by_xpath('//div[@class="_3uMse"]')
        message_box.click()
        time.sleep(2)
        
        # Send the message
        message_box.send_keys(message + Keys.ENTER)
        print("Message sent successfully!")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    finally:
        # Close the browser
        driver.quit()

# Call the function to send the message
send_whatsapp_message()
