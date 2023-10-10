from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver (Chrome in this case)
driver = webdriver.Chrome()

# Set implicit wait to wait up to 10 seconds for elements to appear before raising an exception
driver.implicitly_wait(10)

# Navigate to LinkedIn
driver.get("https://www.linkedin.com")

try:
    # Wait for the login page to load by checking the page title
    WebDriverWait(driver, 20).until(EC.title_contains("LinkedIn Login"))
    print("Loaded login page")

    # Enter your username and password
    driver.find_element(By.ID, "username").send_keys("XXXXXX")
    driver.find_element(By.ID, "password").send_keys("XXXXXX")

    # Click the "Sign In" button
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Wait for the homepage to load
    WebDriverWait(driver, 20).until(EC.title_contains("LinkedIn"))

    # Print "Logged in" to indicate a successful login
    print("Logged in")

    # Navigate to the jobs page
    driver.get("https://www.linkedin.com/jobs/")

    # Wait for the search filters to be visible
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".jobs-search-box__container")))

    # Print "On jobs page" to indicate that the jobs page has loaded
    print("On jobs page")

    # Enter search keywords
    keyword = driver.find_element(By.CSS_SELECTOR, "input[aria-label='Search by title, skill, or company']")
    keyword.send_keys("Python Developer")

    # Enter location
    #location = driver.find_element(By.CSS_SELECTOR, "input[aria-label='Location']")
    location = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-label='Location']")))
    location.send_keys("New York")

    # Click the search button
    driver.find_element(By.CSS_SELECTOR, "button[aria-label='Search']").click()

    # Wait for the job results to load
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".jobs-search-results")))

    # Print "Results loaded" to indicate that job results have loaded
    print("Results loaded")

    # Print job results
    jobs = driver.find_elements(By.CSS_SELECTOR, ".job-card-container")

    for job in jobs:
        title = job.find_element(By.CSS_SELECTOR, ".job-card-title").text
        company = job.find_element(By.CSS_SELECTOR, ".job-card-company-name").text
        print(title, company)

finally:
    # Quit the WebDriver instance to close the browser
    driver.quit()
