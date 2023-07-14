import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class select_certificade:
    print ('Bem vindos ao Sid')
    print ('Versão 1.0.2')
    def __init__(self):
        self.data_final = ""
        self.procuracao = ""
    

    def obter_data_final(self):
        self.data_final = input("Insira a data final no formato dd/mm/yyyy: ")
    def obter_procuracao(self):
        self.procuracao = input("Insira o CNPJ do procuração: ")

    def executar(self):
        # Configuração do chromedriver
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=chrome_options)
        ## Acesso à página desejada

        driver.get("https://login.esocial.gov.br/login.aspx")

        # Aguarda 3 segundos antes de clicar na opção do certificado digital
        time.sleep(3)

        # Clica na opção do certificado digital
        certificado_digital = driver.find_element(By.XPATH, '//*[@id="login-acoes"]/div[2]/p/button')
        certificado_digital.click()

        # Aguarda 3 segundos antes de clicar na opção do certificado digital
        time.sleep(3)

        # Clica na opção do certificado digital
        certificado_digital = driver.find_element(By.XPATH, '//*[@id="cert-digital"]/button')
        certificado_digital.click()


        # Aguarda mais 3 segundos antes de abrir o site do eSocial referente ao certificado
        time.sleep(5)

        #acessar procuração

        driver.get("https://www.esocial.gov.br/portal/Home/Index?trocarPerfil=true")

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="perfilAcesso"]/option[3]').click()

        time.sleep(3)

        # Seleciona o campo de Procuração CNPJ
        procuracao = driver.find_element(By.XPATH, '//*[@id="procuradorCnpj"]')
        procuracao.click()


        # Define a o CNPJ
        cnpj = self.procuracao

        # Executa um script em JavaScript para preencher o campo com CPNJ
        driver.execute_script(f"arguments[0].value = '{cnpj}';", procuracao)

        time.sleep(3)

        #Acessar a geral
        certificado_digital = driver.find_element(By.XPATH, '//*[@id="btn-verificar-procuracao-cnpj"]')
        certificado_digital.click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="geral"]').click()

        time.sleep(5)

        #solicitação

        #Proxima solicitação 06/2023

        time.sleep(3)

        # Acessa a página de solicitação
        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        # Aguarda o carregamento da página
        time.sleep(2)

        # Seleciona a opção de solicitação desejada
        solicitar_opcao = driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]')
        solicitar_opcao.click()

        # Aguarda o carregamento do campo de data inicial
        time.sleep(2)

        # Preenche o campo de data inicial
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/06/2023')


        verificar = driver.find_element(By.XPATH, '//*[@id="DataFinal"]')
        verificar.click()
        # Aguarda o carregamento do campo de data final
        time.sleep(2)

        # Executa um script em JavaScript para preencher o campo de data final
        campo_data_final = driver.find_element(By.XPATH, '//*[@id="DataFinal"]')
        data_final = self.data_final.replace("/", "\\/")  # Escapar a barra para o JavaScript
        script = f"arguments[0].value = '{data_final}';"
        driver.execute_script(script, campo_data_final)

        time.sleep(5)

        # Clica no botão "Salvar"
        solicitar_opcao = driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()
        # Fecha o navegador
        driver.quit()

# Criar uma instância da classe select_certificade
app = select_certificade()

# Obter a data final do usuário
app.obter_data_final()
app.obter_procuracao()
# Executar o código
app.executar()