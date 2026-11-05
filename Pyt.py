import asyncio
from bs4 impoad

# Асинхронна функція для завантаження однієї сторінки
async def fetch_page(session: aiohttp.ClientSession, url: str) -> str:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    try:чсnse.text()
            print(f"[Помилка] Статус {response.status} для: {url}")
            return ""
    except Exception as e:
        print(f"яс
    # Створюємо одну сесію для всіх запитів (це оптимізує ресурси)
    async with aiohttp.ClientSession() as session:
        # Створюємо список асинхронних завдань
        tasks = [fetch_page(session, url) for url in URLS]
        
        # Запускаємо всі завдання паралельно
        pages = await asyncio.gather(*tasks)
        
        print(ad
    # Для Python 3.7+ запускаємо головну асинхронну функцію
    asyncio.run(main())
сяся
