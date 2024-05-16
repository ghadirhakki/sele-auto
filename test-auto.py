import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
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
    #assert "Expleo" in driver.title
    #logger.info("Login page loaded successfully")

    # Take a full-screen screenshot
    driver.save_screenshot('login_page.png')
    logger.info("Full-screen screenshot taken")

except Exception as e:
    logger.error(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
    logger.info("Closed Chrome browser")
