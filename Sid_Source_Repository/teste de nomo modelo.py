import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

class select_certificade:
    print ('=======Download SID=======')
    def __init__(self): 
        self.procuracao = ""
        self.localarquivo = ""
    
    def obter_procuracao(self):
        self.procuracao = input("Insira o CNPJ do procuração: ")
    def obter_localarquivo(self):
        self.localarquivo = input("Insira o nome da pasta: ")

    def executar(self):
        #Criar pasta
        import os
        import shutil

        destino = "C:\\" # O caminho do destino
        nome = self.localarquivo # O nome da pasta
        pasta = os.path.join (destino, nome) # O caminho completo da pasta
        if os.path.exists (pasta):
            shutil.rmtree(pasta)
            print("Já existe uma pasta com o nome definido, a mesma será substituída.")
            time.sleep(5)
        os.mkdir (pasta) # Criar a pasta

        # Configuração do chromedriver
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-infobars")  # Desativar a barra de informações para manipular configurações do Chrome
        chrome_options.add_argument("--disable-extensions")  # Desativar extensões
        chrome_options.add_argument("--disable-gpu")  # Desativar aceleração de GPU (não funciona em algumas plataformas)
        chrome_options.add_argument("--disable-dev-shm-usage")  # Prevenir problemas de memória compartilhada
        chrome_options.add_argument("--no-sandbox")  # Necessário em ambientes não privilegiados
        chrome_options.add_argument("--disable-popup-blocking")  # Desativar bloqueio de pop-ups
        chrome_options.add_argument("--disable-impl-side-painting")  # Melhorar a renderização em algumas páginas

        # Definir o zoom para 50%
        chrome_options.add_argument("--width=1920")
        chrome_options.add_argument("--height=1080")
        chrome_options.add_argument("--force-device-scale-factor=0.5")

        # Definir as preferências de download
        prefs = {}
        prefs["profile.default_content_settings.popups"] = 0 # Desabilitar popups
        prefs["download.default_directory"] = f"C:\\{nome}" # Definir o diretório de destino
        prefs["download.prompt_for_download"] = False # Desabilitar a janela de confirmação
        prefs["download.directory_upgrade"] = True 
        prefs["safebrowsing.enabled"] = True
        chrome_options.add_experimental_option("prefs", prefs) # Adicionar as preferências ao webdriver
        driver = webdriver.Chrome(options=chrome_options) # Iniciar o webdriver

        driver.get("https://login.esocial.gov.br/login.aspx")

        # Aguarda 3 segundos antes de clicar na opção do certificado digital
        time.sleep(3)

        # Clica na opção do certificado digital
        driver.find_element(By.XPATH, '//*[@id="login-acoes"]/div[2]/p/button').click()

        # Aguarda 3 segundos antes de clicar na opção do certificado digital
        time.sleep(3)

        # Clica na opção do certificado digital
        driver.find_element(By.XPATH, '//*[@id="cert-digital"]/button').click()


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
        driver.find_element(By.XPATH, '//*[@id="btn-verificar-procuracao-cnpj"]').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="geral"]').click()

        time.sleep(3)
       
        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Consulta")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div/div[4]/input').click()
        time.sleep(3)
        codigos_disponiveis = []

        for i in range(51, 0, -1):
            xpath_situacao = f'//*[@id="DataTables_Table_0"]/tbody/tr[{i}]/td[5]'
            try:
                elemento_situacao = driver.find_element(By.XPATH, xpath_situacao)
                if elemento_situacao.text == "disponível para baixar":
                    contagem += 1
                            
                    # Obtém o código do elemento
                    xpath_codigo = f'//*[@id="DataTables_Table_0"]/tbody/tr[{i}]/td[1]'
                    elemento_codigo = driver.find_element(By.XPATH, xpath_codigo)
                    codigo = elemento_codigo.text
                    
                    # Adiciona o código à lista
                    codigos_disponiveis.append(codigo)
                    
                    # Clica no link de download
                    xpath_download = f'//*[@id="DataTables_Table_0"]/tbody/tr[{i}]/td[8]/a'
                    driver.find_element(By.XPATH, xpath_download).click()
                    
                    # Aguarde o download
                    time.sleep(5)  # Você pode ajustar o tempo de espera conforme necessário
            except NoSuchElementException:
                print(f"Elemento não encontrado no índice {i}")
                
        # Constrói o caminho completo para a pasta "data"
        pasta_data = os.path.join(os.getcwd(), "data")
        # Salva os códigos dos elementos "disponível para baixar" em um arquivo
        nome_arquivo = os.path.join(pasta_data, f"{self.localarquivo}_codigos_disponiveis.txt")
        with open(nome_arquivo, "w") as arquivo:
         arquivo.write("\n".join(codigos_disponiveis))
       

# Criar uma instância da classe select_certificade
app = select_certificade()
# Obter a data final do usuário

app = select_certificade()
# Obter a data final do usuário
app.obter_procuracao()
app.obter_localarquivo()
# Executar o código
app.executar()


