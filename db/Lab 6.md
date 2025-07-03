# LAB 6 «РАЗРАБОТКА ПРИЛОЖЕНИЯ БАЗ ДАННЫХ С ПОМОЩЬЮ ФРЕЙМВОРКА SQLAlchemy»

1. Убедитесь, что PostgreSQL установлен на вашем компьютере. Также активируйте виртуальное окружение и установите необходимые библиотеки для Python :
```bash
pip install sqlalchemy psycopg2
```
2. Создайте новую базу данных library_db в PostgreSQL:
```sql
CREATE DATABASE library_db;
```
3. Создайте таблицы authors и books с соответствующими ограничениями целостности:
```sql
CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author_id INT REFERENCES authors(id) ON DELETE CASCADE
);
```
4. Добавьте несколько авторов и книг в таблицы:
```sql
INSERT INTO authors (name) VALUES ('George Orwell'), ('J.K. Rowling');

INSERT INTO books (title, author_id) VALUES 
('1984', 1),
('Harry Potter and the Philosopher's Stone', 2);
```
5. Выполнение операций CRUD с помощью SQL:
1) Чтение данных:
```sql
SELECT * FROM books;
```
2) Обновление данных:
```sq;
UPDATE books SET title = '1984 (Updated Edition)' WHERE id = 1;
```
3) Удаление данных:
```sql
DELETE FROM books WHERE id = 1;
```
6. Разработка приложения на Python с использованием SQLAlchemy: создайте файл app.py и добавьте следующий код:
```python
from sqlalchemy import create_engine, Column, Integer, String, For-eignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Настройка подключения к базе данных
DATABASE_URL = "postgresql+psycopg2://test:1234@localhost/library_db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Определение моделей
class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship("Author")

# Создание таблиц
Base.metadata.create_all(engine)

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# Добавление нового автора и книги
new_author = Author(name='F. Scott Fitzgerald')
session.add(new_author)
session.commit()

new_book = Book(title='The Great Gatsby', author_id=new_author.id)
session.add(new_book)
session.commit()

# Чтение книг
books = session.query(Book).all()
for book in books:
    print(f'Title: {book.title}, Author: {book.author.name}')

# Закрытие сессии
session.close()
```
7. Запустите приложение через консоль:
```bash
python app.py
```
