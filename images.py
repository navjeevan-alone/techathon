from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import urllib

# Initialize Chrome options
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Initialize the Chrome WebDriver with the correct keyword argument
driver = webdriver.Chrome('chromedriver')

url = "https://www.google.com/search?q={s}&tbm=isch&tbs=sur:fc&hl=en&ved=0CAIQpwVqFwoTCKCa1c6s4-oCFQAAAAAdAAAAABAC&biw=1251&bih=568"
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(5)  # Consider using WebDriverWait here for better reliability
driver.get(url.format(s='Pets'))

# Find image elements
imgResults = driver.find_elements(By.XPATH, "//img[contains(@class,'Q4LuWd')]")

# Extract image sources
src = [img.get_attribute('src') for img in imgResults]

# Download the first 10 images
for i in range(min(10, len(src))):
    urllib.request.urlretrieve(src[i], f"sample_data/pets{i}.jpg")

driver.quit()  # Don't forget to close the driver
