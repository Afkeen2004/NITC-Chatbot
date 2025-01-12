from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
import time
import csv
import pandas
import pdfplumber

options = Options()
options.headless = False  
options.add_argument("--window-size=1920,1200")

# URL = "https://nitc.ac.in/news-and-events"  
URL = "https://nitc.ac.in/hostels/overview"

DRIVER_PATH = "C:\\Users\\sride\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

driver = webdriver.Chrome(options=options)

driver.get(URL)


# titles = driver.find_elements(By.CLASS_NAME, 'xc-title')
# dates = driver.find_elements(By.CLASS_NAME, 'xc-date')

# title_text = []
# dates_text = []

# for i in titles:
#     print(i.text)
#     title_text.append(i.text)
    
# for i in dates:
#     print(i.text)
#     dates_text.append(i.text)

# data = list(zip(title_text, dates_text))
# with open("news_events.csv", "w", newline="", encoding="utf-8") as file:
#         writer = csv.writer(file)
#         writer.writerow(["Title", "Date"]) 
#         writer.writerows(data)  

# links = driver.find_elements(By.CLASS_NAME, 'xc-footer-links')
# departments = []
# for i in links:
#     print(i.text)
#     departments.append(i.text)

# departments = [item.replace(",", "") for item in departments]
# departments = [item.replace("\"", "") for item in departments]
# with open("depts.csv", "w", newline="", encoding="utf-8") as file:
#         writer = csv.writer(file)
#         writer.writerow(["Title"])  
#         for item in departments:
#             writer.writerow([item])
# cse = driver.find_elements(By.XPATH, "//div[@class='xc-department-content']//p")
# cse_content = []
# for i in cse:
#     print(i.text)
#     cse_content.append(i.text)
# with open("cse.csv", "w", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Description of the CSE Department"])  
#     for item in cse_content:
#         writer.writerow([item])

# eee = driver.find_elements(By.XPATH, "//div[@class='xc-department-content']//p")
# eee_content = []
# for i in eee:
#     print(i.text)
#     eee_content.append(i.text)
# with open("eee.csv", "w", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Description of the EEE Department"])  
#     for item in eee_content:
#         writer.writerow([item])

# faculty_names = []
# faculty_positions = []
# faculty = driver.find_elements(By.CLASS_NAME, "faculty-name")
# for i in faculty:
#     print(i.text)
#     faculty_names.append(i.text)
# faculty = driver.find_elements(By.CLASS_NAME, "faculty-position")
# for i in faculty:
#     print(i.text)
#     faculty_positions.append(i.text)
# faculty_data = list(zip(faculty_names, faculty_positions))
# with open("eee_faculty.csv", "w", newline="", encoding="utf-8") as file:
#         writer = csv.writer(file)
#         writer.writerow(["Name", "Position"])  
#         writer.writerows(faculty_data)

# contact = []
# content = []
# data = driver.find_elements(By.CLASS_NAME, "xc-department-content")
# for i in data:
#      print(i.text)
#      c = i.text
#      c = c.replace(",", "") 
#      content.append(c)
# #content = [item.replace(",", "") for item in content]
# data = driver.find_elements(By.CLASS_NAME, "xc-hostel-contact-box")
# for i in data:
#      print(i.text)
#      contact.append(i.text)
# print(contact)
# del contact[0]
# drata = list(zip(content, contact))
# with open("hostel.csv", "w", newline="", encoding="utf-8") as file:
#         writer = csv.writer(file)
#         writer.writerow(["Info", "Contact"])  
#         writer.writerows(drata)
# driver.quit()

with pdfplumber.open("academic-calendar.pdf") as pdf:
    # Get the first page of the PDF
    page = pdf.pages[0]
    
    # Extract the table(s) from the page
    table = page.extract_table()

# If the PDF contains tables, `table` will be a list of rows (list of lists)
# Now, let's print the extracted table to see its structure
for row in table:
    print(row)
    
# Assuming you have extracted the 'table' list from the PDF
with open('academic_calendar.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the rows of the table to the CSV file
    for row in table:
        writer.writerow(row)
