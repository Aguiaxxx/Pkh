import asyncio
from playwright.async_api import async_playwright
from datetime import datetime
import time

# Função principal para capturar screenshots
async def capture_screenshots():
    async with async_playwright() as p:
        # Inicia o navegador em modo headless
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        # Acessa o site
        await page.goto('https://lightminer.co/7186484')
        print("Navegador iniciado. Captura de screenshots com clique no meio da tela a cada 1 minuto.")

        try:
            while True:
                # Obtém as dimensões da página
                viewport = page.viewport_size
                if viewport:
                    x = viewport['width'] // 2
                    y = viewport['height'] // 2

                    # Realiza o clique no meio da tela
                    await page.mouse.click(x, y)
                    print(f"Clique realizado no meio da tela: ({x}, {y})")

                # Nome do arquivo com timestamp
                timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                file_name = f'screenshot-{timestamp}.png'
                
                # Captura a screenshot
                await page.screenshot(path=file_name)
                print(f'Screenshot salva: {file_name}')

                # Espera 1 minuto antes da próxima captura
                time.sleep(60)
        except KeyboardInterrupt:
            print("Processo interrompido pelo usuário.")
        finally:
            # Fecha o navegador
            await browser.close()

# Executa a função no ambiente assíncrono
await capture_screenshots()
