# LAB 3 «ОЗНАКОМЛЕНИЕ С СУБД POSTGRESQL»

Создать и заполнить базу данных в PostgreSQL. Таблицы (минимум по 5 записей в каждой) связать между собой полями идентификаторов. С помощью команд интерактивного терминала `psql` просмотреть структуру базы данных, структуру таблиц, просмотреть данные в них, изменить структуру таблиц, добавить столбцы, добавить данные, создать столбцы с пользовательскими типами данных.
Создать и заполнить базу данных для учета работы продуктового магазина, состоящую из трех таблиц. Первая таблица должна содержать поля: наименование товара, количество товара на складе, стоимость покупки (за единицу измерения). Вторая: наименование производителя, адрес. Третья: цена продажи, проданное количество товара. На основании созданных таблиц создать таблицу, содержащую поля: Наименование товара, наименование производителя, стоимость покупки, цена продажи.
Коды команд
1. Создание базы данных:
```SQL
create database db2;
```
2. Вход в базу данных:
```sql
\c db2;
```
3. Создание нового типа данных — адрес.
```sql
create type adress as (street char(15), number int);
create type type_pay as enum('cash', 'card');
```
4. Создание первой таблицы (наименование товара, количество товара на складе, стоимость покупки (за единицу измерения)):
```sql
create table products(id int primary key, product char(15), count_of_store int, cost int);
```
5. Заполнение первой таблицы:
```sql
insert into products values (1, 'bread', 300, 14);
```
и т.д.
Просмотр результатов заполнения:
![image](https://github.com/user-attachments/assets/0ae250e8-8e98-40cf-9f56-587d0e08f450)

6. Создание второй таблицы (наименование производителя, адрес):
```sql
create table producers (id int primary key, creator char(15), 
creator_adress adress);
```
7. Заполнение второй таблицы:
```sql
insert into producers values (1, 'Selectel', ('Lomonosova', 535));
```
и т.д.
Просмотр результатов заполнения:
![image](https://github.com/user-attachments/assets/0f479a14-25f1-4f05-9b95-94bcc302e6e5)

8. Создание третьей таблицы (цена продажи, проданное количество товара):
```sql
create table sellers (id int primary key, id_product int, price int, count int, pay type_pay);
```
9. Заполнение третьей таблицы: 
```sql
insert into sellers values (0, 1, 100, 10, 'cash');
```
и т.д.
10. Создание новой таблицы на основании созданных ранее таблиц.
Новая таблица содержит поля: Наименование товара, наименование производителя, стоимость покупки, цена продажи.
```sql
create table prod_out as select products.product, producers.creator, 
products.cost, sellers.price from products inner join producers on 
products.id = producers.id inner join sellers on 
products.id=sellers.id_product;
```
![image](https://github.com/user-attachments/assets/d8dfc0f2-61cd-4c71-b30d-6df70914d043)

11.Изменение структуры таблицы (добавление нового столбца):
![image](https://github.com/user-attachments/assets/f9723943-cb0d-485c-b8ed-390f9321ce72)

12.Добавление, изменение и удаление записи в таблице:
![image](https://github.com/user-attachments/assets/8ae12d53-ea21-4ca4-bbb4-a13095c262d4)
