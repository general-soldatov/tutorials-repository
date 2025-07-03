# LAB 8 «РАБОТА С PostgreSQL ЧЕРЕЗ ТЕРМИНАЛ LINUX»

В этой работе мы будем взаимодействовать с СУБД PostgreSQL через терминал Ubuntu Linux. Если на вашем компьютере установлена Windows 10 или 11, то можно вос-пользоваться WSL.
Для этого перейдите в терминал и наберите команду > wsl. 
Теперь мы перешли в терминал OS Ubuntu. Для подключения к базе данных PostgreSQL понадобится установленный PostgreSQL клиент:
sudo apt install postgresql-client-<VERSION>
Для установки PostgreSQL сервера:
sudo apt install postgresql
Проверим, можем ли мы подключиться к базе данных PostgreSQL:
sudo -u postgres psql -c "SELECT version();"
Вывод команды должен быть примерно таким:
 
Логин в только что установленный postgreSQL сервер нужно производить под именем пользователя postgres:
sudo -i -u postgres
psql
Выйти из клиента PostgreSQL: \q
Для подключения к базе данных PostgreSQL можно использовать команду:
psql -U<USERNAME> -h<HOSTNAME> -d<DB_NAME>
Если такая команда не просит ввести пароль пользователя, то можно еще добавить опцию -W.
Создать новую роль c именем tester (указывайте нужное имя):
CREATE USER tester;
Дать права роли на базу данных:
GRANT ALL PRIVILEGES ON DATABASE orders_db TO tester;
Дать права роли на таблицу:
GRANT ALL PRIVILEGES ON TABLE clients TO tester;
Дать пользователю право вставки в таблицу:
GRANT INSERT ON TABLE clients TO tester;
Если текущий пользователь не имеет права на изменение последовательности, не-обходимой для генерации новых значений полей типа автоинкремента. Чтобы назначить нужные права своему пользователю:
GRANT USAGE, UPDATE ON SEQUENCE authors_id_seq TO tester;
Показать список баз данных PostgreSQL: \l
 
Показать список таблиц: 
 
Показать список пользователей (ролей): 
 
Показать структуру таблицы:
 
Переименовать базу данных:
ALTER DATABASE db2 RENAME TO newdb;
Удалить базу данных:
drop database db_name;
Изменить текущую базу данных в PostgreSQL (вы не сможете переименовать или удалить текущую базу данных): \connect db_name или более короткий alias: \c db_name
 
Удалить роль (пользователя):
DROP ROLE user_name;

