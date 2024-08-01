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
```bash
yc iam service-account create \
  --name service-account-for-cf \
  --description "service account for cloud functions"
```
