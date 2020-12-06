from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

import csv

# Path Of Exe
PATH = "C:\Program Files (x86)\chromedriver.exe"

#Create Driver Instance
driver = webdriver.Chrome(PATH)

## WebSite Name
driver.get("https://www.jumia.com.ng/")

# Get Search Name
search = driver.find_element_by_name("q")

## Input MacBook
search.send_keys("MacBook")

## Click Enter Key
search.send_keys(Keys.RETURN)

## Create CSV File
csv_file = open("jumia-macbooks.csv", "w", newline='',  encoding='utf-8')

## Create Writer Object
csv_writer = csv.writer(csv_file)

## Create Table Columns / Headings
csv_writer.writerow(["Product Title", "Product Price", "Product Link"])

## Get All Cards On The Page
for card in driver.find_elements_by_class_name("c-prd")[1:]:
	## Get Product Title
	title = card.find_element_by_class_name("name").text
	# print(title)

	## Get Product Price
	price = card.find_element_by_class_name("prc").text
	# print(price)

	## Get Link Of Product
	link = card.find_element_by_class_name("core").get_attribute("href")
	# print(link)
	# print("----")

	## Add To CSV File
	csv_writer.writerow([title, price, link])

csv_file.close()

print("Done")

# Close D
driver.quit()