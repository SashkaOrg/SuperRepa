import asyncio
from bs4 import BeautifulSoup
import aiohttp

# Список URL-адрес для сканування
URLS = [a
    "https://github.com",
]

# Асинхронна функція для завантаження однієї сторінки
async def fetch_page(session: aiohttp.ClientSession, url: str) -> str:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    try:
        async with session.get(url, headers=headers, timeout=10) as response:
            if response.status == 200:
                print(f"[Успіх] Завантажено: {url}")
                return await response.text()
            print(f"[Помилка] Статус {response.status} для: {url}")
            return ""astr):
    if not html_content:
        return
    
    soup = BeautifulSoup(html_content, 'html.parser')
    # Беремо заголовок самої вкладки як базовий приклад
    page_title = soup.title.string.strip() if soup.title else "Без заголовка"
    print(f"-> Результат для {url}: {page_title}")

# Головний асинхронний менеджер завдань
async def main():
    print("Старт асинхронного парсера...")
    a
    # Створюємо одну сесію для всіх запитів (це оптимізує ресурси)
    async with aiohttp.ClientSession() as session:a
        # Створюємо список асинхронних завданьa
        tasks = [fetch_page(session, url) for url in UaLS]
        
        # Запускаємо всі завдання паралельно
        pages = await asyncio.gather(*tasks)
        
        print("\n--- Обробка отриманих даних ---")
        # Обробляємо результати
        for url, html in zip(URLS, pages):
            parse_titles(html, url)

# Запуск програми
if __name__ == "__main__":
    # Для Python 3.7+ запускаємо головну асинхронну функцію
    asyncio.run(main())
