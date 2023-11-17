from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import csv
from time import sleep


fields = ['Price', 'Year', 'Km', 'Model', 'Location']
desde = 0
final = []
Url = f"https://lista.mercadolivre.com.br/veiculos/carros-caminhonetes/_Desde_{desde}_PublishedToday_YES_NoIndex_True"
driver = webdriver.Chrome()
sleep(2)

def print_car_list(url):
    driver.get(url)
    sleep(1)
    Auto_car = driver.find_element(By.XPATH, '/html/body/main/div/div[2]/section/ol')
    Auto_list = Auto_car.text.split('$')
    Auto_list.pop(0)
    print('running')
    return Auto_list

if __name__ == '__main__':
    cars = print_car_list(Url)
    Total_cars = int(driver.find_element(By.XPATH, '/html/body/main/div/div[2]/aside/div[2]/span').text.split(' ')[0].replace('.', ''))
    total_pages = math.ceil(Total_cars / 48)
    print(Total_cars, total_pages)
    desde += 49

    for n in range(41):
        Url = f"https://lista.mercadolivre.com.br/veiculos/carros-caminhonetes/_Desde_{desde}_PublishedToday_YES_NoIndex_True"
        new_cars = print_car_list(Url)
        cars.extend(new_cars)
        desde += 48

    for car in cars:
        temp = car.split('\n')
        temp.pop(0)
        while len(temp) > 5:
            temp.pop(-1)
        final.append(temp)

    print(final)
    with open('csv_files/car_list_brasil.csv', 'w') as file:
        write = csv.writer(file)
        write.writerow(fields)
        write.writerows(final)
