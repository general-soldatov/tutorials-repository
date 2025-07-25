# LAB 7 "Управление данными СУБД MуSQL средствами РНР"

## Цель работы
Приобретение навыков доступа к базам данных в сети Интернет, используя возможности PHP. Задачами лабораторной работы являются овладение навыками создания и заполнения таблиц баз данных, создания представлений, триггеров и хранимых процедур, освоение программных технологий доступа к базам данных MySQL с помощью серверных сценариев PHP.

## Теоретическое введение
Первоначально сервер MySQL разрабатывался для управления большими базами данных с целью обеспечить более высокую скорость работы по сравнению с существующими на тот момент аналогами. И вот уже в течение нескольких лет данный сервер успешно используется в условиях промышленной эксплуатации с высокими требованиями. Несмотря на то, что MySQL постоянно совершенствуется, он уже сегодня обеспечивает широкий спектр полезных функций. Благодаря своей доступности, скорости и безопасности MySQL очень хорошо подходит для доступа к базам данных по Интернету.  
MySQL – это программное обеспечение с открытым кодом. Это означает, что применять и модифицировать его может любой желающий. Такое ПО можно получать по Internet и использовать бесплатно. При этом каждый пользователь может изучить исходный код и изменить его в соответствии со своими потребностями. Использование программного обеспечения MySQL регламентируется лицензией GPL (GNU General Public License), вкоторой указано, что можно и чего нельзя делать с этим программным обеспечением в различных ситуациях. MySQL можно загрузить с веб-сайта http://www.mysql.com/
Важной особенностью (и недостатком) MySQL является отсутствие поддержки ограничений уровня столбцов таблиц (например, даже такое простое ограничение, как проверка принадлежности числа заданному диапазону). При этом реализация ограничений с помощью программного кода (запросов check) возможна, но не действенна: написанные запросы будут без проблем выполнены СУБД, но проигнорированы при работе с таблицами.  
Рассмотренные ранее СУБД Access и SQL Server решали задачу создания ограничений целостности с помощью соответствующих ограничений (типа Check), доступных как в графическом, так и программном (с помощью непосредственного ввода кода) режимах. Те же самые задачи в MySQL решаются намного сложнее и требуют написания соответствующих программных триггеров.
Рассмотрим основные функции PHP, применяемые для работы с MySQL сервером.Основной функцией для соединения с сервером MySQL является mysql_connect(), которая подключает скрипт к серверу баз данных MySQL и выполяет авторизацию пользователя базой данных. Синтаксис у данной функции такой:
```php
mysql_connect ([string $hostname] [, string $user] [, sting $password]);
```
word]);
Все параметры данной функции являются необязательными, поскольку значения по умолчанию можно прописать в конфигурационном файле php.ini. При желании можно указать другие имя MySQL-хоста, пользователя и пароль. Параметр $hostname может быть указан в виде: хост:порт.
Функция возвращает идентификатор (типа int) соединения, и вся дальнейшая работа осуществляется только через этот идентификатор. При следующем вызове функции mysql_connect() с теми же параметрами новое соединение не будет открыто, а функция возвратит идентификатор существующего соединения. 
Для закрытия соединения предназначена функция mysql_close(int $connection_id).
Вообще, соединение можно и не закрывать - оно будет закрыто автоматически при завершении работы PHP скрипта. Если используется более одного соединения, при вызове mysql_close() нужно указать идентификатор соединения, которое вы хотите закрыть. Вообще не закрывать соединения - плохой стиль, лучше закрывать соединения с MySQL самостоятельно, а не надеясь на автоматизм PHP. Если используется только одно соединение с базой данных MySQL за все время работы сценария, то можно не сохранять его идентификатор и не указывать идентификатор при вызове остальных функций.
Функция mysql_connect() устанавливает обыкновенное соединение с MySQL. Однако, PHP поддерживает постоянные соединения - для этого используется функция mysql_pconnect(). Аргументы этой функции такие же, как и у mysql_connect().
В чем разница между постоянным соединением и обыкновенным соединением с MySQL? Постоянное соединение не закрывается после завершения работы скрипта, даже если скрипт вызвал функцию mysql_close(). Соединение закрывается лишь тогда, когда удаляется процесс-владелец (например, при завершении работы или перезагрузке вебсервера Apache). 
PHP работает с постоянными соединениями следующим образом: при вызове функции mysql_pconnect() PHP проверяет, было ли ранее установлено соединение. Если да, то возвращается его идентификатор, а если нет, то открывается новое соединение и возвращается идентификатор.
Постоянные соединения позволяют значительно снизить нагрузку на сервер, а также повысить скорость работы PHP скриптов, использующих базы данных. При работе с постоянными соединениями нужно следить, чтобы максимальное число клиентов Apache не преывшало максимального числа клиентов MySQL, то есть параметр MaxClient (в конфигурационном файле Apache - httpd.conf) должен быть меньше или равен параметру max_user_connection (параметр MySQL).
Функция mysql_select_db (string $db [, int $id]) выбирает базу данных, с которой будет работать PHP скрипт. Если открыто не более одного соединения, можно не указывать параметр $id.
Все запросы к текущей базе данных отправляются функцией mysql_query(). Этой функции нужно передать один параметр - текст запроса. Текст запроса может содержать пробельные символы и символы новой строки (\n). Текст должен быть составлен по правилам синтаксиса SQL. Пример запроса:
```php
$q = mysql_query("SELECT * FROM mytable");
```
Приведенный запрос должен вернуть содержимое таблицы mytable. Результат запроса присваивается переменной $q. Результат - это набор данных, который после выполнения запроса нужно обработать определенным образом.
Есть возможность узнать значение каждого поля. Это можно сделать с помощью следующей функции:
```php
mysql_result (int $result, int $row, mixed $field);
```
Параметр функции $row задает номер записи, а параметр $field - имя или порядковый номер поля.

## Порядок выполнение
1. Зайдите в панель управления хостинга и создайте базу данных.
2. Перейдите в панель управления phpMyAdmin, раздел SQL и напишите запрос на создание таблицы:
```sql
CREATE TABLE students(
    id INT PRIMARY KEY AUTO_INCREMENT, 
    learn_book_id INT(6) UNIQUE,
    first_name varchar(20),
    name varchar(20),
    speciality varchar(7),
    birth_date date,
    course int(1),
    group_num int(2)
    );
```
3. Аналогичным образом создать структуру таблицы Subjects (справочник предметов):
```sql
CREATE TABLE subjects(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(10),
    cycle VARCHAR(10),
    hours INT,
    dep VARCHAR(20)
);
```
4. Аналогичным образом создать структуру таблицы scores (успеваемость студентов по предметам): 
```sql
CREATE TABLE scores(
	stud INT,
    discipline INT,
    score CHAR(1),
    date_of DATE,
    PRIMARY KEY (stud, discipline)
);
```
5. Задать ограничения для столбцов таблицы Students в форме триггера students_constraints, срабатывающего при попытке вставки новой записи в таблицу: 
```sql
-- удалим старый триггер
DROP TRIGGER IF EXISTS students_constraints_insert;

DELIMITER $ -- устанавливаем новый разделитель
CREATE TRIGGER students_constraints_insert 
BEFORE INSERT ON students 
FOR EACH ROW 
BEGIN
	IF NOT (NEW.course BETWEEN 1 AND 6) THEN -- курс в пределах 1...6
		SET NEW.course = 0;
	END IF; 
    
	IF NOT(NEW.speciality REGEXP '^[A-Z]$') THEN -- специальность A...z
		SET NEW.speciality = 0;
	END IF;
    
	IF NOT (NEW.group_num BETWEEN 1 AND 99) THEN
		SET NEW.group_num = 0;
	END IF;
END  $
DELIMITER ; -- меняем разделитель на ;
```
6. Аналогичным образом запрограммировать триггер students_constraints_update,
срабатывающий при попытке изменения записи в таблице.
7. Для таблиц Subjects и Uspev написать по два триггера, проверяющие целостность данных при вставке и изменении данных.
8. Установить связи между таблицами и указать правила ссылочной целостности:
```sql
ALTER TABLE `scores` ADD FOREIGN KEY (`stud`) REFERENCES `students`(`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE `scores` ADD FOREIGN KEY (`discipline`) REFERENCES `subjects`(`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;
```
8. Наполнить базу данных сведениями о студентах (не менее 5), предметах (не менее 3) и оценках (не менее 10):
Освоить приемы изменения и удаления полей и записей. Проверить работоспособность ограничений значений полей, уникальности и др., предусмотренные при задании структуры базы данных. Проверить работоспособность ссылочной целостности, удаляя, изменяя и вставляя данные.
9. Создать просмотр для вывода кратких сведений о студентах (идентификатор, номер зачетки, фамилия и инициалы, идентификатор группы):
```sql
SELECT id, learn_book_id, CONCAT(first_name, ' ', name) AS full_name, CONCAT(speciality,'-',course,'-',group_num) as group_data FROM students;
```
10. Сформировать представление по результатам запроса:
```sql
CREATE VIEW study AS SELECT id, learn_book_id, CONCAT(first_name, ' ', name) AS full_name, CONCAT(speciality,'-',course,'-',group_num) as group_data FROM students;
```
11. Аналогичным образом создать представление для вывода сведений об успеваемости студентов из таблицы успеваемости с указанием сведений о студенте из запроса Students_info и сведений о предмете из таблицы предметов. Результат должен содержать следующие поля: ФИО студента, Группа, Предмет, Дата, Оценка. Назвать представление как study_score.
Программный код запроса:
```sql

SELECT learn_book_id, full_name, group_data, score, subjects.name, date_of 
FROM study, scores, subjects 
WHERE study.id = scores.stud AND subjects.id = scores.discipline;
```
12. Создать хранимую процедуру для вывода сведений о студенте по номеру его зачетной книжки из представления:
```sql
DELIMITER $
CREATE PROCEDURE studs(IN LBID INT)
BEGIN
	SELECT * FROM study_score
	WHERE learn_book_id = LBID;
END;
$
DELIMITER ;
```
13. Проверить работоспособность хранимой процедуры:
```sql
CALL studs(243);
```
14. Создать и открыть файл index.php начальной страницы веб-приложения. Ввести HTML-разметку страницы index.php:
```html
<HTML>
<HEAD><TITLE>Лабораторная работа 3</TITLE></HEAD>
<BODY>
<H2>Информация о студентах</H2>
<FORM id="form" method="POST" action="index.php">
	<TABLE border="1" width="60%">
		<TR>
		<TH width="10%">Код</TH>
		<TH width="20%">Зачетная книжка</TH>
		<TH width="40%">ФИО</TH>
		<TH width="30%">Группа</TH>
		</TR>
		<TR align="center">
		<TD width="10%">Значение кода</TD>
		<TD width="20%">Значение зачетки</TD>
		<TD width="40%">Значение ФИО</TD>
		<TD width="30%">Значение группы</TD>
		</TR>
	</TABLE>
<BR/> Номер зачетной книжки: <input name="zk" type="text"/>
<input type="submit" value="Запрос"/>
</FORM>
</BODY>
</HTML>
```
15. Проверить работоспособность созданной страницы в веб-браузере.
16. Создать PHP-сценарий соединения с базой данных. Создать в виртуальной директории и открыть файл connection.php. Ввести программный код сценария для соединения с локальным сервером и сохранить:
```php
<?php
$link = @mysql_connect("localhost", "root") or die("Невозможно соединиться с сервером");
// ввести программный код соединения с базой данных Education:
$db=@mysql_select_db("Education") or die("Нет такой базы данных");
?>
```
17. Дополнить файл index.php PHP-инструкциями:
- поставить курсор
до первой строки <HTML> | ввести код:
```php
<?php
include("connection.php");
?>
```
- проверить работоспособность сценария, обновив в браузере страницу index.php.
- выполнить запрос к представлению study базы данных: поставить курсор после строки include("connection.php"); | ввести код:
```php
$sql = "SELECT * FROM `students_info`";
$query = mysql_query($sql);
$count = mysql_num_rows($query);
```
- организовать цикл по строкам таблицы: поставить курсор перед второй строкой <TR> и ввести код:
```php
<?php
for($i=0;$i<$count;$i++)
{
?>
```
- поставить курсор после второй строки </TR> и ввести код:
```php
<?php
}
?>
```
- выполнить подстановку результатов запроса в строки таблицы: поставить курсор перед второй строкой с текстом «Значение кода» и заменить текст «Значение кода» на:
```php
<?php echo mysql_result($query,$i,id);?>
```
- аналогичным образом заменить фрагменты текста «Значение зачетки», «Значение ФИО» и «Значение группы» на фрагменты кода:
```php
<?php echo mysql_result($query,$i,learn_book_id);?>
<?php echo mysql_result($query,$i,full_name);?>
<?php echo mysql_result($query,$i,group_data);?>
```
- сохранить файл index.php.
- проверить работоспособность сценария, обновив в браузере страницу index.php.
- добавить инструкции фильтрации данных по номеру зачетной книжки с условием, проверяющим, был ли запрос на фильтрацию: поставить курсор перед строкой с текстом «sql = "SELECT * FROM `students_info`";» и ввести код:
```php
if(!($_POST['zk']) or $_POST['zk']=='') {
```
- закрыть условный блок (если запроса не было, то будут показаны все записи): поставить курсор после строки с текстом «$count = mysql_num_rows($query);» | ввести «}».
- добавить код, выполняющий запрос на фильтрацию: поставить курсор после строки с текстом «};» и ввести код:
```php
else {
 $sql = "SELECT * FROM `students_info` where
 `no_zk`='".$_POST['zk']."'";
 $query = mysql_query($sql);
 $count = mysql_num_rows($query);
}
```
– сохранить файл index.php.
– проверить работоспособность сценария, обновив в браузере страницу index.php.

## Содержание отчёта
