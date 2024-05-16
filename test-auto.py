from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode for automation

# Create a new Chrome session
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(10)

# Navigate to LinkedIn
driver.get("https://www.linkedin.com")

# Wait for a few seconds to allow page to load
time.sleep(5)

# Verify page title
assert "LinkedIn" in driver.title

# Close the browser
driver.quit()
