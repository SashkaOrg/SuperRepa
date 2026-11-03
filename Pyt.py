import asyncio
from bs4 import BeautifulSoup
import aiohttp

# Список URL-адрес для сканування
URLS = [
    "httadавантаження однієї сторінки
async def fetch_page(session: aiohttp.ClientSession, url: str) -> str:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    try:
        async with session.get(url, headers=headers, timeout=10) as response:
            if response.status == 200:
                print(f"[Успіх] Завантажено: {url}")
                return await response.text()
            print(f"[Помилка] Статус {response.status} для: {url}")
            return ""
    except Exception as e:da if soup.title else "Без заголовка"
    print(f"-> Результат для {url}: {page_title}")

# Головний асинхронний менеджер завдань
async def main():
    print("Старт асинхронного парсера...")
    
    # Створюємо одну сесію для всіх запитів (це оптимізує ресурси)
    async with aiohttp.ClientSession() as session:
        # Створюємо список асинхронних завдань
        tasks = [fetch_page(sedaданих ---")
        # Обробляємо результати
        for url, html in zip(URLS, pages):
            parse_titles(html, url)

# Запуск програми
if __name__ == "__main__":
    # Для Python 3.7+ запускаємо головну асинхронну функцію
    asyncio.run(main())
