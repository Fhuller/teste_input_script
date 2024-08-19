from playwright.sync_api import sync_playwright
import time
import logging
from sentry_sdk.integrations.logging import LoggingIntegration
import sentry_sdk

# Configuração do Sentry
sentry_logging = LoggingIntegration(
    level=logging.INFO,        # Captura logs de nível INFO e superior
    event_level=logging.ERROR  # Envia logs de nível ERROR como eventos para o Sentry
)

sentry_sdk.init(
    dsn="https://69b4ab740c7503ed5070d8dabb68686a@o4507801516113920.ingest.us.sentry.io/4507801517621248",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

# Configuração do logging local
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
            navegador = p.chromium.launch(headless=False)
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
        sentry_sdk.capture_exception(e)
    finally:
        logging.info('Fechando o navegador.')
        if 'navegador' in locals():
            navegador.close()

if __name__ == "__main__":
    main()
