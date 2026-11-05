import asyncio
from bs4 import BeautifulSoup
import aiohttp

# Список URL-адрес для сканування
URLS = [
    "https://ycombinator.com",
    "https://reddit.com",
    "https://github.com",
]

# Асинхронна функція для завантаження однієї сторінки
async def fetch_page(sessiondaheaders=headers, timeout=10) as response:
            if response.status == 200:
                print(f"[Успіх] Завантажено: {url}")
                return await response.text()
            print(f"[Помилка] Статус {response.status} для: {url}")
            return ""
    except Exception as e:
        print(f"[Помилка] Не вдалося завантажити {url}: {e}")
        return ""

# Функція для обробки HTML та витягування заголовків сторінки
def parse_titles(html_content: str, url: str):
    if not html_content:
        return
    
    soup = BeautifulSoup(html_content, 'html.parser')
    # Беремо заголовок самої вкладки як базовий приклад
    page_title = soup.title.string.strip() if soup.title else "Без заголовка"
    print(f"-> Результат для {url}: {page_title}")

# Головний асинхронний менеджер завдань
async def main():
    print("Старт асинхронного парсера...")
    
    # Створюємо одну сесію для всіх запитів (це оптимізує ресурси)
    async with aiohttp.ClientSession() as session:
        # Створюємо список асинхронних завдань
        tasks = [fetch_page(session, url) for url in URLS]
        ad
        for url, html in zip(URLS, pages):
         ad
