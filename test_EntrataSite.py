from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.select import Select


@pytest.fixture(scope="module")
def driver():
    # Webdriver set up
    driver = webdriver.Chrome()  # We can also use Firefox(), Edge(), etc.
    yield driver
    driver.quit()


    """
    Test Case 1- Verify the page the title
    """


def test_title(driver):
    driver.get("https://www.entrata.com/")
    expected_title = "Property Management Software | Entrata"
    actual_title = driver.title
    assert actual_title == expected_title
    print("if title matches assert is true else throw an error")


    """
    Test Case 2- Verify the login functionality by navigating and entering the credentials
    """


def test_login(driver):
    try:
        # Navigate to the login page
        driver.get("https://www.entrata.com/")

        # Locate the username, password fields, and login button
        login_button = driver.find_element(By.XPATH, "//a[@href='/sign-in']")
        property_manager_login = driver.find_element(By.XPATH, "//a[@href='https://sso.entrata.com/entrata/login']")
        username_field = driver.find_element(By.ID, "entrata-username")
        password_field = driver.find_element(By.ID, "entrata-password")
      # signin_button = driver.find_element(By.ID, "//li[@class='form-item submit']")

        login_button.click()
        property_manager_login.click()
        username_field.send_keys("waghsandeep9552@testmail.com")
        password_field.send_keys("!@#WER")
      #  signin_button.click()

        # Wait for the login to complete and the next page to load
        # Optionally, use WebDriverWait for better handling of dynamic content
        driver.implicitly_wait(10)  # waits up to 10 seconds for elements to appear

    except Exception as e:
        pytest.fail(f"An error occurred during the test: {e}")


    """
    Test Case 3- Verify the schedule demo functionality by filling the form
    """


def test_scheduledemo(driver):
    try:
        # Navigate entrata website
        driver.get("https://www.entrata.com/")

# Locators store
        scheduledemo_button = driver.find_element(By.XPATH, "//a[@href='https://go.entrata.com/schedule-demo.html']")
        firstname_field = driver.find_element(By.ID, "FirstName")
        lastname_field = driver.find_element(By.ID, "LastName")
        email_field = driver.find_element(By.ID, "Email")
        company_field = driver.find_element(By.ID, "Company")
        phone_field = driver.find_element(By.ID, "Phone")
        jobtitle_field = driver.find_element((By.ID, "Title"))


# Event calling
        scheduledemo_button.click()
        firstname_field.send_keys("Sandeep ")
        lastname_field.send_keys("Wagh")
        email_field.send_keys("waghsandeep9552@testmail.com")
        company_field.send_keys("Entrata")
        phone_field.send_keys("0000955231")

#   Dropdown handling

        unitcount_dropdown = driver.find_element_by_id("Unit_Count__c")
        select = Select(unitcount_dropdown)
        # Select an option by visible text, for example "101 - 200"
        select.select_by_visible_text("101 - 200")
        # Optionally, you can verify the selection
        selected_option = select.first_selected_option
        assert selected_option.text == "101 - 200", "The expected option was not selected."
        jobtitle_field.send_keys("Full stack QA")
        iam_dropdown = driver.find_element_by_id("demoRequest")
        select = Select(iam_dropdown)
        # Select an option by visible text, for example "a Resident"
        select.select_by_visible_text("a Resident")
        # Optionally, you can verify the selection
        selected_option = select.first_selected_option
        assert selected_option.text == "a Resident", "The expected option was not selected."

# Wait applied for page loading

        driver.implicitly_wait(10)

    except Exception as e:
        pytest.fail(f"An error occurred during the test: {e}")

    """
    Test Case 4- Verify the solution tab , Extract all the text from the solution and click on "Multifamily"
    """


def test_solution(driver):
    driver.get("https://www.entrata.com/")
    elements = driver.find_elements_by_xpath("//a[contains(@class, 'fat-nav-links')]")
    # Iterate through elements and print the text
    for element in elements:
        print(element.text)  # print the values from solution tab

    # Click on the "Multifamily" tab if matches with text
    for element in elements:
        if element.text == "Multifamily":
            element.click()
            break

    assert "multifamily" in driver.current_url.lower(), "The Multifamily page was not opened."

