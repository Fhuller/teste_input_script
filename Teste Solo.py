from playwright.sync_api import sync_playwright
import time
import logging

# Configuração do logging
logging.basicConfig(
    filename='app_certo.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    try:
        logging.info('Iniciando o script de Playwright.')

        with sync_playwright() as p:
            logging.info('Iniciando o navegador Chromium.')
            navegador = p.chromium.launch(headless=False)  # Defina headless=True se não precisar ver o navegador
            pagina = navegador.new_page()
            pagina.goto("https://www.hashtagtreinamentos.com/curso-python")
            logging.info('Navegou para a URL.')

            logging.info('Preenchendo o formulário.')
            pagina.fill('xpath=//*[@id="_form_1919_"]/div[1]/div[1]/div/input', "Lira")
            pagina.fill('xpath=//*[@id="_form_1919_"]/div[1]/div[2]/div/input', 'pythonimpressionador@gmail.com')
            logging.info('Campos preenchidos.')

            pagina.locator('xpath=//*[@id="_form_1919_submit"]').click()
            logging.info('Formulário enviado.')

            logging.info('Aguardando 10 segundos.')
            time.sleep(10)
            logging.info('Finalizando o script.')

    except Exception as e:
        logging.error(f'Ocorreu um erro: {e}')
    finally:
        logging.info('Fechando o navegador.')
        if 'navegador' in locals():
            navegador.close()

if __name__ == "__main__":
    main()
