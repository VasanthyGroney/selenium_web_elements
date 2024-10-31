from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

# Define the search term
search_term = "ISTQB"

# Initialize the Chrome driver
driver = webdriver.Chrome()

try:
    # Step 1: Launch the browser and navigate to Google
    driver.get("https://www.google.com")

    # Step 2: Wait for the search bar to become visible
    search_bar = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "q"))
    )

    # Step 3: Scroll to the search bar and use JavaScript to enter text to avoid interception
    driver.execute_script("arguments[0].scrollIntoView();", search_bar)
    driver.execute_script(f"arguments[0].value = '{search_term}';", search_bar)

    # Step 4: Wait for the dynamic dropdown to appear and click the first suggestion
    first_suggestion = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//ul[@role='listbox']//li[1]"))
    )
    driver.execute_script("arguments[0].click();", first_suggestion)

    # Step 5: Verify that a new page has opened
    WebDriverWait(driver, 10).until(
        EC.title_contains(search_term)
    )
    print("Test passed: First suggestion selected, and new page opened successfully.")

except TimeoutException:
    print("Test failed: Operation timed out.")
except ElementClickInterceptedException:
    print("Test failed: Element click intercepted.")
finally:
    # Close the browser
    driver.quit()
