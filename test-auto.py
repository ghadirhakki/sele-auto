import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode for automation

try:
    # Create a new Chrome session
    logger.info("Starting Chrome browser")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)

    # Set window size to full screen
    driver.set_window_size(1920, 1080)
    logger.info("Set browser window to full screen")

    # Navigate to Login page
    logger.info("Navigating to Login page")
    driver.get("https://portail-oab.expleo.suez.com/mydashboard")

    # Wait for a few seconds to allow page to load
    time.sleep(5)
    
    # Print and log the page title
    page_title = driver.title
    print("Page title:", page_title)
    logger.info(f"Page title: {page_title}")

    # Verify page title
    assert "Sign in to your account" in driver.title
    logger.info("Login page loaded successfully")

    # Take a full-screen screenshot
    driver.save_screenshot('1_login_page.png')
    logger.info("Full-screen screenshot taken")


    # Find and fill email input field
    email_input =driver.find_element(By.ID, "i0116")
    email_input.send_keys("expleo.admin@suezenv.onmicrosoft.com")
    logger.info("Entered email")

    driver.save_screenshot('2_enter_email_page.png')
    logger.info("entered email screenshot taken")

    # Find and click "Next" button
    next_button = driver.find_element(By.ID,"idSIButton9")
    next_button.click()
    logger.info("Clicked on 'Next' button")

    driver.save_screenshot('3_next_button_clicked.png')
    logger.info("Next butotn clicked screenshot taken")

    time.sleep(15)
    driver.save_screenshot('4_next_button_clicked_page_shown.png')
    logger.info("Next page of next button clicked screenshot taken ")

    # Find and fill pwd input field
    email_input =driver.find_element(By.ID, "i0118")
    email_input.send_keys("1@BSu3z!#")
    logger.info("Entered pwd")

    time.sleep(10)
    driver.save_screenshot('5_enter_pwd_page.png')
    logger.info("entered pwd screenshot taken")

    # Find and click "Sign in" button
    signIn_button = driver.find_element(By.ID,"idSIButton9")
    signIn_button.click()
    logger.info("Clicked on 'Sign in' button")


    time.sleep(10)
    driver.save_screenshot('6_signed_in_page.png')
    logger.info("signed in screenshot taken")


    #pop up avant de continuer 
    # Find and click "OK" button by class name
    ok_button = driver.find_element(By.CLASS_NAME, "v-btn__content")
    ok_button.click()
    logger.info("Clicked on 'OK' button")

    time.sleep(10)
    driver.save_screenshot('7_pop_up_off.png')
    logger.info("pop_up_off screenshot taken")


    #open the left menu
    menu = driver.find_element(By.CLASS_NAME, "menu.burger-menu.float-left")
    menu.click()
    logger.info("menu opened")


    time.sleep(10)
    driver.save_screenshot('8_menu_opened.png')
    logger.info("menu opened screenshot")

    #click on mes tournées 
    tours = driver.find_element(By.ID,"smTours.sous-menu")
    tours.click
    logger.info("sous_menu_tours opened")

    time.sleep(10)
    driver.save_screenshot('9_sous_menu_tours.png')
    logger.info("sous_menu_tours opened screenshot")
    
    

except Exception as e:
    logger.error(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
    logger.info("Closed Chrome browser")
