# LAB 4 «СЕРВЕРНОЕ АДМИНИСТРИРОВАНИЕ НА ПРИМЕРЕ POSTGRESQL»

Убедитесь, что PostgreSQL установлен на вашем компьютере. Для работы с базой данных используйте консоль или программу DBeaver.
Создадим базу данных командой:
```sql
CREATE DATABASE db2;
```
Создадим таблицу для подразделений компании:
```sql
CREATE TABLE departments (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);
```
Создадим таблицу employees, которая будет содержать информацию о сотрудниках с ограничениями.
```sql
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    department_id INT REFERENCES departments(id) ON DELETE CASCADE
);
```
Вставим данные в представленные таблицы:
```sql
INSERT INTO departments (name) VALUES ('HR'), ('IT'), ('Sales');

INSERT INTO employees (name, email, department_id) VALUES 
('John Doe', 'john@example.com', 1),
('Jane Smith', 'jane@example.com', 2);
```
Ознакомимся с результатами заполнения базы данных:
![image](https://github.com/user-attachments/assets/08b36c47-19e1-4f0a-aa3a-7be916943129)
  
Для создания резервной копии используйте команду pg_dump в консоли:
```bash
pg_dump db2 > db_backup.sql
```
Удалите таблицы из базы данных:
```sql
DROP TABLE employees;
DROP TABLE departments;
```
Чтобы восстановить базу данных из резервной копии, воспользуемся следующей командой:
```bash
psql db2 < lab_db_backup.sql
```
Создайте нового пользователя и предоставьте ему права на использование базы данных.
```sql
CREATE USER new_user WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE db2 TO new_user;
```
