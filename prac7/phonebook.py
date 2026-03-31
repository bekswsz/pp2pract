import csv
from connect import get_connection

# 1. Функция для ввода данных вручную
def insert_user_manually():
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    
    conn = get_connection()
    if conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO phonebook (first_name, phone_number) VALUES (%s, %s)", (name, phone))
        conn.commit()
        print("Готово! Контакт сохранен.")
        cur.close()
        conn.close()

# 2. Функция для загрузки из CSV
def upload_from_csv(file_path):
    conn = get_connection()
    if conn:
        cur = conn.cursor()
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                cur.execute("INSERT INTO phonebook (first_name, phone_number) VALUES (%s, %s)", (row[0], row[1]))
        conn.commit()
        print("Все контакты из CSV загружены!")
        cur.close()
        conn.close()

# Запуск для проверки:
# insert_user_manually()
# upload_from_csv('contacts.csv')