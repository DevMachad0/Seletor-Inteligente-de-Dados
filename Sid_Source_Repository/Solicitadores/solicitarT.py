import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class select_certificade:

    def executar(self):   

        # Configuração do chromedriver
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=chrome_options)
        
        # Acesso à página desejada
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
        time.sleep(3)
        try:
            #Acessar a geral
            driver.get("https://www.esocial.gov.br/portal/Home/Index?trocarPerfil=true")
        except NoSuchElementException:
            driver.quit()
            print ("========================ERRO===========================")
            print ("Erro no processo, verifique o portal ou tente novamente.")
            print ("=======================================================")
            time.sleep(999)

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="geral"]/div').click()

        time.sleep(2)
        #solicitação
        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/07/2018)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/07/2018')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (31/07/2018)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[6]/td[2]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        time.sleep(3)

        #Proxima solicitação 08/2018


        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/08/2018)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/08/2018')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (31/08/2018)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[5]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        #Proxima solicitação 09/2018

        time.sleep(3)

        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/09/2018)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/09/2018')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (30/09/2018)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[7]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        #Proxima solicitação 10/2018

        time.sleep(3)

        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/10/2018)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/10/2018')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (31/10/2018)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[3]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        #Proxima solicitação 11/2018

        time.sleep(3)

        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/11/2018)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/11/2018')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (30/11/2018)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[5]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        #Proxima solicitação 12/2018

        time.sleep(3)

        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/12/2018)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/12/2018')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (31/12/2018)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[6]/td[1]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        #Proxima solicitação 01/2019

        time.sleep(3)

        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/01/2019)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/01/2019')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (31/01/2019)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[4]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        #Proxima solicitação 02/2019

        time.sleep(3)

        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/02/2019)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/02/2019')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (28/02/2019)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[4]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        #Proxima solicitação 03/2019

        time.sleep(3)

        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/03/2019)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/03/2019')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (31/03/2019)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[7]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        #Proxima solicitação 04/2019

        time.sleep(3)

        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/04/2019)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/04/2019')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (30/04/2019)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[2]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        #Proxima solicitação 05/2019

        time.sleep(3)

        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/05/2019)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/05/2019')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (31/05/2019)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[5]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        #Proxima solicitação 06/2019

        time.sleep(3)

        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/06/2019)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/06/2019')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (30/06/2019)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[7]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        #Proxima solicitação 07/2019

        time.sleep(3)

        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/07/2019)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/07/2019')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (31/07/2019)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[3]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        #Proxima solicitação 08/2019

        time.sleep(3)

        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/08/2019)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/08/2019')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (31/08/2019)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[6]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        #Proxima solicitação 09/2019

        time.sleep(3)

        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/09/2019)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/09/2019')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (30/09/2019)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[6]/td[1]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        #Proxima solicitação 10/2019

        time.sleep(3)

        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/10/2019)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/10/2019')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (31/10/2019)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[4]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        #Proxima solicitação 11/2019

        time.sleep(3)

        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/11/2019)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/11/2019')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (30/11/2019)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[6]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        #Proxima solicitação 12/2019

        time.sleep(3)

        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/12/2019)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/12/2019')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (31/12/2019)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[6]/td[2]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        #Proxima solicitação 01/2020

        time.sleep(3)

        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/01/2020)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/01/2020')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (31/01/2020)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[5]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        #Proxima solicitação 02/2020

        time.sleep(3)

        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/02/2020)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/02/2020')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (29/02/2020)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[6]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        #Proxima solicitação 03/2020

        time.sleep(3)

        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/03/2020)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/03/2020')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (31/03/2020)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[6]/td[2]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        #Proxima solicitação 04/2020

        time.sleep(3)

        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/04/2020)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/04/2020')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (30/04/2020)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[4]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        #Proxima solicitação 05/2020

        time.sleep(3)

        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/05/2020)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/05/2020')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (31/05/2020)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[7]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        #Proxima solicitação 06/2020

        time.sleep(3)

        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/06/2020)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/06/2020')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (30/06/2020)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[2]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        #Proxima solicitação 07/2020

        time.sleep(3)

        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/07/2020)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/07/2020')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (31/07/2020)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[5]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        #Proxima solicitação 08/2020

        time.sleep(3)

        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/08/2020)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/08/2020')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (31/08/2020)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[6]/td[1]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        #Proxima solicitação 09/2020

        time.sleep(3)

        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/09/2020)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/09/2020')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (30/09/2020)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[3]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        #Proxima solicitação 10/2020

        time.sleep(3)

        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/10/2020)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/10/2020')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (31/10/2020)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[6]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        #Proxima solicitação 11/2020

        time.sleep(3)

        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/11/2020)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/11/2020')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (30/11/2020)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[6]/td[1]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        #Proxima solicitação 12/2020

        time.sleep(3)

        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/12/2020)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/12/2020')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (31/12/2020)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[4]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        #Proxima solicitação 01/2021

        time.sleep(3)

        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/01/2021)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/01/2021')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (31/01/2021)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[7]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        #Proxima solicitação 02/2021

        time.sleep(3)

        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/02/2021)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/02/2021')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data 28/02/2021)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[4]/td[7]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        #Proxima solicitação 03/2021

        time.sleep(3)

        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/03/2021)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/03/2021')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data 31/03/2021)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[3]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        #Proxima solicitação 04/2021

        time.sleep(3)

        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/04/2021)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/04/2021')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data 30/04/2021)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[5]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        #Proxima solicitação 05/2021

        time.sleep(3)

        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/05/2021)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/05/2021')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data 31/05/2021)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[6]/td[1]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        #Proxima solicitação 06/2021

        time.sleep(3)

        driver.get("https://www.esocial.gov.br/portal/download/Pedido/Solicitacao")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="TipoPedido"]/option[2]').click()

        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data (01/06/2021)
        data_inicial = driver.find_element(By.XPATH, '//*[@id="DataInicial"]')
        data_inicial.send_keys('01/06/2021')

        # Aguarda mais 5 segundos antes de clicar no campo de data final
        time.sleep(2)

        # Seleciona o campo de data inicial e envia a data 30/06/2021)
        driver.find_element(By.XPATH, '//*[@id="conteudo-pagina"]/form/section/div[2]/div[2]/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[3]').click()

        # Salvar

        driver.find_element(By.XPATH, '//*[@id="btnSalvar"]').click()

        # Fecha o navegador
        driver.quit()
        print("Solicitação do dia 1 foi finalizada")
# Criar uma instância da classe select_certificade
app = select_certificade()
# Executar o código
app.executar()