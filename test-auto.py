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

    # Navigate to LinkedIn
    logger.info("Navigating to LinkedIn")
    driver.get("https://www.linkedin.com")

    # Wait for a few seconds to allow page to load
    time.sleep(5)

    # Verify page title
    assert "LinkedIn" in driver.title
    logger.info("LinkedIn page loaded successfully")

    # Take a screenshot
    driver.save_screenshot('linkedin_homepage.png')
    logger.info("Screenshot taken")

except Exception as e:
    logger.error(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
    logger.info("Closed Chrome browser")
