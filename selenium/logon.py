from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# URL da página de login
login_url = "https://login.salesforce.com"

# Credenciais de login
usuario = "seu_usuario"
senha = "sua_senha"

# Inicializa o driver do navegador (certifique-se de ter o driver correto instalado: https://sites.google.com/chromium.org/driver/)
driver = webdriver.Chrome()

try:
    # Abre a página de login
    driver.get(login_url)

    # Aguarda até que o campo de usuário esteja presente na página
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "campo-usuario"))
    )

    # Insere o usuário e a senha nos campos de login
    driver.find_element(By.ID, "campo-usuario").send_keys(usuario)
    driver.find_element(By.ID, "campo-senha").send_keys(senha)

    # Submete o formulário de login
    driver.find_element(By.ID, "botao-login").click()

    # Aguarda até que o botão desejado esteja presente na página após o login
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "botao-desejado"))
    )

    # Clica no botão desejado após o login
    driver.find_element(By.ID, "botao-desejado").click()

finally:
    # Fecha o navegador ao finalizar
    driver.quit()
