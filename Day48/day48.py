# Day 48 - Intermediate+ Selenium Webdriver Browser and Game Playing Bot

from selenium import webdriver

chrome_driver_path = "/Users/luis/Code/ChromeDevelopment/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# # driver.get("https://www.amazon.com")
#
# driver.get("https://www.amazon.com/Willz-Multi-Use-Programmable-Pressure-Stainless/dp/B08WRQ3K2H/ref=sr_1_1_sspa?crid=3553RIN7LRFJW&keywords=instant+pot&qid=1653308901&sprefix=instant+p%2Caps%2C341&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzOTdRQkdaUU84QUNRJmVuY3J5cHRlZElkPUEwMjA0ODYyQUFSVVE2T1U1QTVXJmVuY3J5cHRlZEFkSWQ9QTA4NjMwMzMyQk83NzNRUFhaQ1cxJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==")
#
# price = driver.find_element("priceblock-ourrprice")
# print(price.text)
#

driver.get("https://www.python.org")

documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
print(documentation_link.text)

driver.findelementbyxbp


# driver.close()  # Closes a single tab, active tab
driver.quit()  # This will actually quit the entire browser.
