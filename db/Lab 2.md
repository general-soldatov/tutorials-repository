# LAB 2 «РАБОТА С БАЗОЙ ДАННЫХ SQLITE В СУБД DBEAVER»

Для работы с нашей базой данных воспользуемся GUI приложением DBeaver. DBeaver — это приложение для управления базами данных (СУБД). Его используют в сферах мобильной и веб-разработки, администрирования баз данных и бизнес-аналитики. DBeaver доступен в бесплатной (на англ. Community Edition) и платной (на англ. Enterprise Edition) версиях. В платной версии есть техническая поддержка и доступны расширенные функции, например интеграция с Git для работы с файловыми данными в репозитории.
Для учебных целей достаточно бесплатной версии, которую можно скачать с сай-та https://dbeaver.io/download/. После установки приложения с помощью мастера откроем приложение. В строке меню выберите Файл > Новый > DBeaver > Database Project > Да-лее. Затем назовём проект и нажимаем кнопку Готово. Затем в разделе проекты найдём пункт Connection, нажмём правой кнопкой мыши и выберем Создать > Соединение. 
![image](https://github.com/user-attachments/assets/a71a1f24-c722-403d-9685-e98941675105)
  
В новом окне выбираем SQLite, выбираем базу sample.db и нажимаем Готово.
Теперь нам необходимо скачать данные, с которыми будем работать по ссылке: https://github.com/nalgeon/sqliter/blob/main/city.csv. Откроем терминал и запустим нашу базу данных в консольном режиме. Для импорта данных из csv в таблицу воспользуемся следующей командой:
```sql
.import --csv city.csv city 
select count(*) from city;
```
Таким образом мы импортировали данные и посчитали количество строк в нашей таблице. Чтобы просмотреть первые строки таблицы, воспользуемся следующим запро-сом:
```sql
SELECT * FROM city LIMIT 5;
```
Просмотрим необходимые нам столбцы:
```sql
SELECT federal_district, city, population FROM city LIMIT 10;
```
Выполним запрос на количество символов города с самым длинным названием:
```sql
SELECT MAX(LENGTH(city)) FROM city 
```  
Теперь наша задача определить количество городов в каждом из федеральных округов и отсортировать их по убыванию количества:
```sql
SELECT 
	federal_district as district,
	COUNT(*) as city_count
FROM city 
GROUP BY federal_district
ORDER BY city_count DESC;
```
С помощью команды GROUP BY мы сгруппировали данные по столбцу feder-al_district, а сортировку данных провели с помощью команды ORDER BY. Ключевое слово DESC указывает, что сортировка идёт по убыванию.
Теперь проведём фильтрацию данных:
```sql
SELECT address FROM city 
WHERE city LIKE '%Красный%'; 
```
С помощью этого запроса мы получим данные по столбцу address, в ячейках ко-торого встречается слово «Красный». Ответим теперь на вопрос, какие города были ос-нованы в период 1990 – 2020 гг.?
```sql
SELECT region, city, foundation_year
FROM city 
WHERE foundation_year BETWEEN 1990 AND 2020;
Если мы хотим ознакомиться с городами, которые были основаны в последние 40 лет, с сортировкой по убыванию:
SELECT region, city, foundation_year
FROM city 
WHERE foundation_year BETWEEN DATE('now', '-40 years') AND DATE('now')
ORDER BY foundation_year DESC;
```
Найдём количество городов в Приволожском и Уральском ФО:
```sql
SELECT count(*)
FROM city 
WHERE federal_district in ('Приволжский', 'Уральский');
```
Теперь посмотрим количество городов, основанных в каждом веке. Для этого мы можем воспользоваться подзапросами:
```sql
WITH history AS (
	SELECT 
		city,
		(foundation_year/100)+1 as century
	FROM city 
)
SELECT 
	century || '-й век' as dates,
	count(*) as city_count
FROM history
GROUP BY century
ORDER BY century DESC;
```
Итак, мы сделали подзапрос создания таблицы history посредством синтаксиса WITH … AS, к которой обращаемся во втором запросе.

Определим количество городов в Сибирском и Приволжском ФО для каждого часового пояса:
```sql
SELECT timezone, count(*) AS city_count
FROM city 
WHERE federal_district in ('Сибирский', 'Приволжский')
GROUP BY timezone
ORDER BY timezone;
```
А теперь интересное задание: найдём три ближайших города к Самаре, не считая саму Самару:
```sql
WITH samara AS (
	SELECT 
		geo_lat AS samara_lat,
		geo_lon AS samara_lon
	FROM city 
	WHERE city = 'Самара'
)
SELECT 
	city,
	(geo_lat - samara_lat)*(geo_lat - samara_lat) +
		(geo_lon - samara_lon)*(geo_lon - samara_lon) as distance
FROM city, samara
WHERE city <> 'Самара'
ORDER BY distance
LIMIT 3;
```
