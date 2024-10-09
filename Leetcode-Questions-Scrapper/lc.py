# Importing Required Packages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Import Service class
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Specify the path to your installed ChromeDriver
chrome_driver_path = r"C:\Users\pende\Downloads\chromedriver-win64\chromedriver.exe"

# Set up the Selenium WebDriver
# define the chromedriver service
s = Service(chrome_driver_path)
# Instantiate the webdriver
driver = webdriver.Chrome(service = s)

# Open a webpage with Selenium
page_URL = "https://leetcode.com/problemset/?page="  # Replace with the URL you want to visit

def get_a_tags(url):
    # Load the URL in the browser
    driver.get(url)
    # Wait for 7 seconds to ensure page is fully loaded
    time.sleep(7)
    # Find all the 'a' elements on page
    links = driver.find_elements(By.TAG_NAME, "a")
    ans = []
    pattern = "/problems"
    # Iterate over each 'a' element
    for i in links:
        href = i.get_attribute("href")
        if href is not None and pattern in href: # because some a type atrributes don't have href so returns NULL which cause error if we don't check
            ans.append(i.get_attribute("href"))
    ans = list(set(ans)) # To avoide duplicate elements
    return ans


# List to store final list of links
my_ans = []

# Going through all pages and geiing links
for i in range(1, 55):
    my_ans += get_a_tags(page_URL + str(i))

# Remove any duplicates that might have been introduced in the process
my_ans = list(set(my_ans))

# Open a file to write the results to
with open('lc.txt', 'a') as f:
    # Iterate over each link in your final list
    for j in my_ans:
        # Write each link to the file, followed by a newline
        f.write(j+'\n')

# Print the total number of unique links found
print(len(my_ans))

# Close the browser
driver.quit()