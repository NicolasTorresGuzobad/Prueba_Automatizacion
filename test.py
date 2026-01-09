from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

try:
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--incognito")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 5)

    driver.get("https://www.saucedemo.com/")
    print("Se ingreso a la pagina del login")

    campo_usuario = driver.find_element(By.ID,"user-name")
    campo_usuario.send_keys("standard_user")

    campo_contraseña = driver.find_element(By.ID,"password")
    campo_contraseña.send_keys("secret_sauce")

    boton_iniciar_sesion= wait.until(EC.element_to_be_clickable((By.ID,"login-button")))
    boton_iniciar_sesion.click()

    titulo_pagina = driver.find_element(By.CLASS_NAME,"app_logo")
    if titulo_pagina.text == "Swag Labs":
        print("Se ingreso a la pagina principal")

    popups = driver.find_elements(By.CLASS_NAME, "popup-close")
    if popups:
        popups[0].click()
        print("Popup cerrado")

    menu_desplegable = wait.until(EC.element_to_be_clickable((By.ID,"react-burger-menu-btn")))
    menu_desplegable.click()
    logout = wait.until(EC.element_to_be_clickable((By.ID,"logout_sidebar_link")))
    logout.click()

    titulo_login = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "login_logo")))
    if titulo_login.text == "Swag Labs":
        print("Se volvió al formulario de inicio")

finally:
    driver.quit()

