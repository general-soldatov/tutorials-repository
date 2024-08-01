# YandexDataBases
## Методы
Для работы с таблицами в Document API поддерживаются следующие методы:  
CreateTable — создаёт таблицу.  
DeleteTable — удаляет таблицу.  
DescribeTable — возвращает информацию о таблице.  
DescribeTimeToLive — возвращает информацию о состоянии времени жизни (TTL) в указанной таблице.  
ListTables — возвращает список таблиц.  
UpdateTimeToLive — включает или отключает время жизни (TTL) для указанной таблицы.  
Для работы с элементами таблиц поддерживаются следующие методы:  
BatchGetItem — возвращает атрибуты элементов из нескольких таблиц.  
BatchWriteItem — записывает или удаляет элементы из таблиц.  
DeleteItem — удаляет элемент в таблице.  
GetItem — возвращает атрибуты элемента из одной таблицы.  
PutItem — перезаписывает элементы в таблице.  
Query — возвращает элементы из таблиц.  
Scan — возвращает элементы и атрибуты из таблицы.  
TransactGetItems — извлекает несколько элементов из таблиц.  
TransactWriteItems — синхронная операция записи.  
UpdateItem — обновляет элементы в таблице.  
## Настройка сервисного аккаунта
Создаём сервисный аккаунт
```bash
yc iam service-account create \
  --name service-account-for-cf \
  --description "service account for cloud functions"
```
Проверяем текущий список сервисных аккаунтов. А также добавляем идентификатор аккаунта в переменную окружения.
```bash
yc iam service-account list
echo "export SERVICE_ACCOUNT_ID=<идентификатор_сервисного_аккаунта>" >> ~/.bashrc && . ~/.bashrc
echo $SERVICE_ACCOUNT_ID 
```
Запрос идентификатора папки облака и его запись в переменную окружения.
```bash
echo "export FOLDER_ID=$(yc config get folder-id)" >> ~/.bashrc && . ~/.bashrc 
echo $FOLDER_ID
```
Назначение роли сервисному аккаунту
```bash
yc resource-manager folder add-access-binding $FOLDER_ID \
  --subject serviceAccount:$SERVICE_ACCOUNT_ID \
  --role editor 
```
Создание статического ключа доступа
```bash
yc iam access-key create --service-account-name <name_account>
```
Записываем в переменую окружения необходимые нам значения из JSON:
```env
AWS_ACCESS_KEY_ID='< access_key.key_id >'
AWS_SECRET_ACCESS_KEY='< secret >'
```
## Управление базой данных
Основные операции управления базой данных описаны в классе файла `ydb_manage.py` с аннотациями.
