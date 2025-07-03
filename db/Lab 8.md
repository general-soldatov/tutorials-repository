# LAB 8 «РАБОТА С PostgreSQL ЧЕРЕЗ ТЕРМИНАЛ LINUX»

В этой работе мы будем взаимодействовать с СУБД PostgreSQL через терминал Ubuntu Linux. Если на вашем компьютере установлена Windows 10 или 11, то можно воспользоваться WSL.
Для этого перейдите в терминал и наберите команду 
```cmd
> wsl
```
Теперь мы перешли в терминал OS Ubuntu. Для подключения к базе данных PostgreSQL понадобится установленный PostgreSQL клиент:
```bash
sudo apt install postgresql-client-<VERSION>
```
Для установки PostgreSQL сервера:
```bash
sudo apt install postgresql
```
Проверим, можем ли мы подключиться к базе данных PostgreSQL:
```bash
sudo -u postgres psql -c "SELECT version();"
```
Вывод команды должен быть примерно таким:
![image](https://github.com/user-attachments/assets/958bd9de-aa1d-46f8-96a6-292500949b35)

Логин в только что установленный postgreSQL сервер нужно производить под именем пользователя postgres:
```bash
sudo -i -u postgres
psql
```
Выйти из клиента PostgreSQL: `\q`
Для подключения к базе данных PostgreSQL можно использовать команду:
```bash
psql -U<USERNAME> -h<HOSTNAME> -d<DB_NAME>
```
Если такая команда не просит ввести пароль пользователя, то можно еще добавить опцию -W.
Создать новую роль c именем tester (указывайте нужное имя):
```sql
CREATE USER tester;
```
Дать права роли на базу данных:
```sql
GRANT ALL PRIVILEGES ON DATABASE orders_db TO tester;
```
Дать права роли на таблицу:
```sql
GRANT ALL PRIVILEGES ON TABLE clients TO tester;
```
Дать пользователю право вставки в таблицу:
```sql
GRANT INSERT ON TABLE clients TO tester;
```
Если текущий пользователь не имеет права на изменение последовательности, необходимой для генерации новых значений полей типа автоинкремента. Чтобы назначить нужные права своему пользователю:
```sql
GRANT USAGE, UPDATE ON SEQUENCE authors_id_seq TO tester;
```
Показать список баз данных PostgreSQL: `\l`
![image](https://github.com/user-attachments/assets/8a7866db-5d96-4014-a1d3-bc374c220e83)

Показать список таблиц: 
![image](https://github.com/user-attachments/assets/d5caa8ab-2080-4821-aca1-9b8cb5b76224)

Показать список пользователей (ролей): 
![image](https://github.com/user-attachments/assets/ac1c9f6e-2951-49b3-b680-4192de2bb121)

Показать структуру таблицы:

 ![image](https://github.com/user-attachments/assets/4c425a7b-3b21-425f-9112-c275cd65e511)

Переименовать базу данных:
```sql
ALTER DATABASE db2 RENAME TO newdb;
```
Удалить базу данных:
```sql
drop database db_name;
```
Изменить текущую базу данных в PostgreSQL (вы не сможете переименовать или удалить текущую базу данных): \connect db_name или более короткий alias: \c db_name

 ![image](https://github.com/user-attachments/assets/54b75d0b-286a-4dcb-bc61-f41486e63c7c)

Удалить роль (пользователя):
```sql
DROP ROLE user_name;
```
