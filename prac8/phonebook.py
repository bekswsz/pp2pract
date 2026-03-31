import psycopg2
from connect import get_connection

# 1. Поиск по паттерну (Функция)
def search_contacts(pattern):
    conn = get_connection()
    if conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM get_contacts_by_pattern(%s)", (pattern,))
        print(f"\n--- Результаты поиска по '{pattern}': ---")
        for row in cur.fetchall():
            print(row)
        cur.close()
        conn.close()

# 2. Добавление или обновление (Процедура Upsert)
def upsert_contact(name, phone):
    conn = get_connection()
    if conn:
        cur = conn.cursor()
        cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
        conn.commit()
        print(f"\nКонтакт {name} добавлен или обновлен.")
        cur.close()
        conn.close()

# 3. Пагинация (Функция)
def get_paged(limit, offset):
    conn = get_connection()
    if conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM get_paginated_contacts(%s, %s)", (limit, offset))
        print(f"\n--- Страница (лимит {limit}, отступ {offset}): ---")
        for row in cur.fetchall():
            print(row)
        cur.close()
        conn.close()

# 4. Удаление (Процедура)
def remove_contact(name):
    conn = get_connection()
    if conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
        conn.commit()
        print(f"\nКонтакт {name} удален.")
        cur.close()
        conn.close()

if __name__ == "__main__":
    # ТЕСТЫ:
    upsert_contact('Bekas', '87071112233') # Проверка вставки
    search_contacts('Bek')                 # Проверка поиска
    get_paged(5, 0)                        # Проверка пагинации (первые 5 штук)