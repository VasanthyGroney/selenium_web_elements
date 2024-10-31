from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Initialize the WebDriver
driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH

try:
    # 1. Launch browser and maximize window
    driver.maximize_window()

    # 2. Navigate to URL 'http://automationexercise.com'
    driver.get("http://automationexercise.com")

    # 3. Verify that the home page is visible successfully
    WebDriverWait(driver, 10).until(EC.title_contains("Automation Exercise"))
    print("Home page is visible successfully")

    # 4. Click on 'Signup / Login' button
    signup_login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Signup / Login"))
    )
    signup_login_button.click()

    # 5. Verify 'New User Signup!' is visible
    new_user_signup = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'New User Signup!')]"))
    )
    print("'New User Signup!' is visible successfully")

    # 6. Enter name and email address
    driver.find_element(By.NAME, "name").send_keys("John Doe")
    driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("johndoe@example.com")

    # 7. Click 'Signup' button
    signup_button = driver.find_element(By.XPATH, "//button[@data-qa='signup-button']")
    signup_button.click()

    # 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
    enter_account_info = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//b[contains(text(), 'Enter Account Information')]"))
    )
    print("'ENTER ACCOUNT INFORMATION' is visible successfully")

    # 9. Fill details: Title, Name, Email, Password, Date of Birth
    driver.find_element(By.ID, "id_gender1").click()  # Select 'Mr' as title
    driver.find_element(By.ID, "password").send_keys("TestPassword123")
    Select(driver.find_element(By.ID, "days")).select_by_value("1")  # Day
    Select(driver.find_element(By.ID, "months")).select_by_value("1")  # Month
    Select(driver.find_element(By.ID, "years")).select_by_value("1990")  # Year

    # 10. Select checkbox 'Sign up for our newsletter!'
    driver.find_element(By.ID, "newsletter").click()

    # 11. Select checkbox 'Receive special offers from our partners!'
    driver.find_element(By.ID, "optin").click()

    # 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
    driver.find_element(By.ID, "first_name").send_keys("John")
    driver.find_element(By.ID, "last_name").send_keys("Doe")
    driver.find_element(By.ID, "company").send_keys("OpenAI")
    driver.find_element(By.ID, "address1").send_keys("123 AI Lane")
    driver.find_element(By.ID, "address2").send_keys("Suite 100")
    Select(driver.find_element(By.ID, "country")).select_by_visible_text("United States")
    driver.find_element(By.ID, "state").send_keys("California")
    driver.find_element(By.ID, "city").send_keys("San Francisco")
    driver.find_element(By.ID, "zipcode").send_keys("94107")
    driver.find_element(By.ID, "mobile_number").send_keys("+1234567890")

    # 13. Click 'Create Account' button
    create_account_button = driver.find_element(By.XPATH, "//button[@data-qa='create-account']")
    create_account_button.click()

    # 14. Verify that 'ACCOUNT CREATED!' is visible
    account_created_msg = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//b[contains(text(), 'Account Created!')]"))
    )
    print("'ACCOUNT CREATED!' is visible successfully")

    # 15. Click 'Continue' button
    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@data-qa='continue-button']"))
    )
    continue_button.click()

    # 16. Verify that 'Logged in as username' is visible
    logged_in_as = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//li[contains(text(), 'Logged in as John Doe')]"))
    )
    print("'Logged in as username' is visible successfully")

    # 17. Click 'Delete Account' button
    delete_account_button = driver.find_element(By.LINK_TEXT, "Delete Account")
    delete_account_button.click()

    # 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    account_deleted_msg = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//b[contains(text(), 'Account Deleted!')]"))
    )
    print("'ACCOUNT DELETED!' is visible successfully")

    # Click 'Continue' button after deletion
    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@data-qa='continue-button']"))
    )
    continue_button.click()

finally:
    # Close the browser
    driver.quit()
