import adp

# Список URL-адрес для сканування
URLS = [
    "https://ycombinator.com",
    "https://reddit.com",
    "https://github.com",
]

# Асинхронна функція для завантаження однієї сторінки
async def fetch_page(session: aiohttp.ClientSession, url: str) -> str:
    headers = {"Uda
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
    ad
        # Запускаємо всі завдання паралельно
        pages = await asyncio.gather(*tasks)
        
        print("\n--- Обробка отриманих даних ---")
        # Обробляємо результати
        for uad+ запускаємо головну асинхронну функцію
    asyncio.run(main())
