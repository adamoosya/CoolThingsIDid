# Import the webdriver
from selenium import webdriver
# Import the chrome client
from webdriver_manager.chrome import ChromeDriverManager
# Import pandas for data analysis
import pandas as pd
import datetime
from datetime import datetime
import csv

pd.set_option('display.max_columns', None)

def getDataPoint():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://safe.density.io/#/displays/dsp_956223069054042646?token=shr_o69HxjQ0BYrY2FPD9HxdirhJYcFDCeRolEd744Uj88e")
    driver.implicitly_wait(10)    
    html_table = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/div/span")
    dataPoint = int(html_table.text.split('%')[0])
    driver.close()
    return dataPoint

def createCSV():
    df = pd. DataFrame(list())
    df.to_csv('RSFData.csv')
    f = open('RSFData.csv', 'w')
    writer = csv.writer(f) 
    header = [""]
    for i in range(7,13):
        for j in range(0,6):
            header.append(str(i) + ":" + str(j) + "0" + " AM")
    for i in range(1,10):
        for j in range(0,6):
            header.append(str(i) + ":" + str(j) + "0" + " PM")
    writer.writerow(header)
    days = [["M"], ["T"], ["W"], ["Th"], ["F"], ["S"], ["Su"]]
    #for i in range(len(days)):
    writer.writerows(days)
    f.close()

def insertDataPoint():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    day = datetime.today().weekday()
    data_list = []
    with open("RSFData.csv") as clone:
        data = csv.reader(clone)
        for row in data:
            data_list.append(row)
    hm = current_time.split(':')
    h = int(hm[0])
    m = int(hm[1])
    index = 6 * (h - 7) + m//10 + 1 
    data_point = getDataPoint()
    if (len(data_list[day + 1]) >= index):
        if data_list[day + 1][index].equals(""):
            data_list[day + 1][index] = data_point
    else:
        while (len(data_list[day + 1]) < index):
            data_list[day + 1].append("")
        data_list[day + 1].append(data_point)
    with open("RSFData.csv", 'w') as write:
        writer = csv.writer(write)
        for row in data_list:
            writer.writerow(row)

insertDataPoint()


