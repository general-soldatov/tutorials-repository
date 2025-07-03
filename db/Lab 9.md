# LAB 9 «РАБОТА С БАЗОЙ ДАННЫХ PostgreSQL (повторение)»


1. Убедитесь, что PostgreSQL установлен на вашем компьютере. Вы можете ска-чать его с официального сайта. Также установите DBeaver для удобного взаимодействия с базой данных.
2. Откройте консоль PostgreSQL и выполните следующие команды для создания базы данных:
CREATE DATABASE test_db;

3. Подключение к базе данных через DBeaver:
1) Откройте DBeaver.
2) Создайте новое подключение к базе данных PostgreSQL.
3) Введите имя базы данных test_db, имя пользователя и пароль.
4) После подключения создайте таблицу employees:
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    position VARCHAR(50),
    salary DECIMAL(10, 2)
);

4. Добавьте несколько записей в таблицу employees:
INSERT INTO employees (name, position, salary) VALUES 
('Иван Иванов', 'Разработчик', 60000),
('Мария Петрова', 'Менеджер', 75000),
('Сергей Смирнов', 'Аналитик', 50000);

5. Извлеките данные из таблицы employees:
SELECT * FROM employees;

6. Работа с базой данных через Python и SQLAlchemy. Создайте файл db_operations.py и добавьте следующий код:
from sqlalchemy import create_engine, Column, Integer, String, Numeric
from sqlalchemy.orm import sessionmaker, declarative_base

# Настройка подключения к базе данных
DATABASE_URL = "postgresql+psycopg2://test:1234@localhost/test_db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Определение модели Employee
class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    position = Column(String)
    salary = Column(Numeric)

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# Извлечение данных о сотрудниках
employees = session.query(Employee).all()
for employee in employees:    
    print(f"ID: {employee.id}, Name: {employee.name}, Position: {em-ployee.position}, Salary: {employee.salary}")

# Закрытие сессии
session.close()

7. Запустите приложение через консоль:
python db_operations.py

После выполнения скрипта вы увидите список сотрудников из таблицы employees.
