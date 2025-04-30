from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Abrir o navegador
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://site.fastshop.com.br/iphone-16-apple--128gb--ultramarino--tela-de-6-1---5g-e-camera-de-48mp-aemyec3braazl_prd-66788/p")

# Esperar o botão estar presente e visível
wait = WebDriverWait(driver, 5)
botao = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-fs-prime-benefits-checkbox="true"]')))

# Scroll até o botão
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", botao)

# Esperar até estar clicável
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-fs-prime-benefits-checkbox="true"]')))
botao.click()
time.sleep(5)
