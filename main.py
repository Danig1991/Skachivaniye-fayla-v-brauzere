import glob
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# базовый url
base_url = 'https://www.lambdatest.com/selenium-playground/download-file-demo'

# путь до директории
path_download = "C:\\!!!путь до директории!!!\\"

# добавить опции
options = webdriver.ChromeOptions()
# оставить браузер открытым
options.add_experimental_option("detach", True)
# путь по умолчанию для скачивания
prefs = {'download.default_directory': path_download}
options.add_experimental_option('prefs', prefs)

# автоматическая загрузка драйвера
service = ChromeService(ChromeDriverManager().install())

# открытие браузера с параметрами
driver_chrome = webdriver.Chrome(
    options=options,
    service=service
)

# переход по url в браузере/развернуть на весь экран
driver_chrome.get(base_url)
driver_chrome.maximize_window()

# нажатие на кнопку Download File
driver_chrome.find_element(By.LINK_TEXT, "Download File").click()
time.sleep(5)
print("Скачивание файла.")

# проверка наличия файла в директории
file_name = "LambdaTest.pdf"
file_path = path_download + file_name

assert os.access(file_path, os.F_OK) is True, \
    "Ошибка: Файл должен присутствовать в директории."
print("Файл в директории.")

# проверка, что файл не пуст
files = glob.glob(os.path.join(path_download, "*.*"))
for file in files:
    file_size = os.path.getsize(file)
    if file_size > 4000:
        print(f"Файл \"{file.replace(path_download, "")}\" не пуст.")
    else:
        print(f"Файл \"{file.replace(path_download, "")}\" пуст.")

# закрытие браузера
driver_chrome.quit()
print("Браузер закрыт.")

# пауза
time.sleep(2)

# удаление файлов из директории
files = glob.glob(os.path.join(path_download, "*.*"))
for file in files:
    os.remove(file)
    print(f"Файл \"{file.replace(path_download, "")}\" удален из директории.")
