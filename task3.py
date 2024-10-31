from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Chrome()  # Make sure the ChromeDriver is in your PATH

try:
    # 1. Launch browser and maximize window
    driver.maximize_window()

    # 2. Navigate to URL 'http://automationexercise.com'
    driver.get("http://automationexercise.com")

    # 3. Verify that the home page is visible successfully
    WebDriverWait(driver, 10).until(EC.title_contains("Automation Exercise"))
    print("Home page is visible successfully")

    # 4. Click on 'Products' button
    products_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Products"))
    )
    products_button.click()

    # 5. Verify user is navigated to ALL PRODUCTS page successfully
    all_products_page = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'All Products')]"))
    )
    print("User is navigated to ALL PRODUCTS page successfully")

    # 6. Enter product name in search input and click search button
    search_input = driver.find_element(By.ID, "search_product")
    search_input.send_keys("Dress")  # Example search term
    search_button = driver.find_element(By.ID, "submit_search")
    search_button.click()

    # 7. Verify 'SEARCHED PRODUCTS' is visible
    searched_products = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Searched Products')]"))
    )
    print("'SEARCHED PRODUCTS' is visible successfully")

    # 8. Verify all the products related to search are visible
    product_list = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='productinfo text-center']/p"))
    )
    if product_list:
        print("All products related to search are visible")
    else:
        print("No products related to the search are visible")

finally:
    # Close the browser
    driver.quit()
