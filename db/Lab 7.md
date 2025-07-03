# LAB 7 «ПОДГОТОВКА ПЕЧАТНЫХ ДОКУМЕНТОВ ИЗ СУБД POSTGRESQL»

1. Убедитесь, что PostgreSQL установлен и правильно настроен на вашем компьютере. Если вы используете Linux, то необходимо перейти к пользователю, который имеет право работать с БД:
```bash
sudo -i -u postgres
```
Также установите необходимые библиотеки для Python:
```bash
pip install sqlalchemy psycopg2 reportlab
```
2. Создайте новую базу данных orders_db в PostgreSQL:
```sql
CREATE DATABASE orders_db;
```
4. Создайте таблицы clients и orders с соответствующими ограничениями целостности:
```sql
CREATE TABLE clients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    client_id INT REFERENCES clients(id) ON DELETE CASCADE,
    order_date DATE NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL
);
```
4. Добавьте несколько клиентов и заказов в таблицы:
```sql
INSERT INTO clients (name, email) VALUES 
('Иван Иванов', 'ivan@example.com'),
('Мария Петрова', 'maria@example.com');

INSERT INTO orders (client_id, order_date, total_amount) VALUES 
(1, '2023-10-01', 1500.00),
(2, '2023-10-02', 2500.00);
```
5. Извлеките данные о клиентах и их заказах с помощью SQL-запроса:
```sql
SELECT c.name, c.email, o.order_date, o.total_amount 
FROM clients c 
JOIN orders o ON c.id = o.client_id;
```
Поскольку мы будем использовать тестового пользователя для приложения, то сначала создадим его:
```sql
CREATE USER test WITH PASSWORD '1234';
```
Дадим ему права для работы с базой данных:
```sql
GRANT ALL PRIVILEGES ON DATABASE orders_db TO test;
```
Если нам нужно выдать права только для определённой таблицы:
```sql
GRANT ALL PRIVILEGES ON TABLE clients TO test;
```
6. Перейдём к разработке приложения на Python с использованием SQLAlchemy и ReportLab. Создайте файл generate_report.py и добавьте следующий код:
```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Numeric
from sqlalchemy.orm import sessionmaker, declarative_base
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Настройка подключения к базе данных
DATABASE_URL = "postgresql+psycopg2://test:1234@localhost/orders_db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Определение моделей
class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('clients.id'))
    order_date = Column(Date)
    total_amount = Column(Numeric)

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# Извлечение данных о клиентах и заказах
results = session.query(Client.name, Client.email, Order.order_date, Order.total_amount).join(Order).all()

# Генерация PDF-документа
pdf_file = "report.pdf"
c = canvas.Canvas(pdf_file, pagesize=letter)

# Регистрация шрифта с поддержкой кириллицы
pdfmetrics.registerFont(TTFont('Arial', '/usr/share/fonts/truetype/ubuntu/UbuntuMono-BI.ttf'))  # Убедитесь, что файл Arial.ttf доступен
c.setFont('Arial', 12)

c.drawString(100, 750, "Отчет о заказах")

y_position = 730
for name, email, order_date, total_amount in results:
    c.drawString(50, y_position, f"Клиент: {name}, Email: {email}, Дата заказа: {order_date}, Сумма заказа: {total_amount}")
    y_position -= 20

c.save()
print(f"Отчет успешно сохранен в файл {pdf_file}")

# Закрытие сессии
session.close()
```
7. Запустите приложение через консоль:
```bash
python generate_report.py
```
После выполнения скрипта будет создан PDF-документ report.pdf, содержащий информацию о клиентах и их заказах.
