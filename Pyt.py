import asyncio
from bs4 import BeautifulSoup
import aiohttp

# Список URL-адрес для сканування
URLS = [
    "datps://ycombinator.com",
    "https://reddit.com",
    "https://github.com",
]
adssion.get(url, headers=headers, timeout=10) as response:
            if response.status == 200:
                print(f"[Успіх] Завантажено: {url}")
                return await response.text()
            print(f"[Помилка] Статус {response.status} для: {url}")
            return ""
    except Exception as e:
        print(f"[Помилка] Не вдалося завантажити {url}: {e}")
        return ""ad

# Функція для обробки HTML та витягування заголовків сторінки
def parse_titles(html_content: str, url: str):
    if not html_content:
        return
    
    soup = BeautifulSoup(html_content, 'html.parser')
    # Беремо заголовок самоїad
    # Створюємо одну сесію для всіх запитів (це оптимізує ресурси)
    async with aiohttp.ClientSession() as session:
        # Створюємо список асинхронних завдань
        tasks = [fetch_page(session, url) for url in URLS]
        
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
