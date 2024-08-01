import boto3
from boto3.dynamodb.conditions import Key
from os import getenv
from dotenv import load_dotenv

class ListUsers:
    """Класс для управления записями в базе данных YDB, название класса не принципиально.
    """
    def __init__(self, dynamodb=None):
        """Инициализация базы данных и сервисного аккаунта, в целях безопасности используются 
           переменные окружения, либо указанные в файле .env
        """
        self.dynamodb = dynamodb
        self.table = 'List_Users'
        if not self.dynamodb:
            load_dotenv()
            self.dynamodb = boto3.resource(
                'dynamodb',
                endpoint_url=getenv('ENDPOINT'),
                region_name='ru-central1',
                aws_access_key_id=getenv('AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=getenv('AWS_SECRET_ACCESS_KEY')
                )

    def create_table(self):
        """Метод создания таблицы, инициализируются ключи и столбцы таблицы
        """
        table = self.dynamodb.create_table(
            TableName = self.table,
            KeySchema = [
                {
                    'AttributeName': 'user_id',
                    'KeyType': 'HASH'  # Ключ партицирования, можно добавить дополнительно ключ сортировки Range
                }
            ],
            AttributeDefinitions = [
                {
                "AttributeName": "user_id",
                "AttributeType": "N"
                },
                {
                "AttributeName": "name",
                "AttributeType": "S"
                },
                {
                "AttributeName": "group",
                "AttributeType": "S"
                }
            ]
        )
        return table

    def put_item(self, user_id, name, group):
        """Метод добавления записи в таблицу.
        """
        table = self.dynamodb.Table(self.table)
        tasks = {'S1': 0}
        response = table.put_item(
            Item = {
                    'user_id': user_id,
                    'name': name,
                    'group': group,
                    'tasks': tasks
            }
        )
        return response

    def update_task(self, user_id, task, ball):
        """Метод обновления записи.
        """
        table = self.dynamodb.Table(self.table)
        response = table.update_item(
            Key = {
                'user_id': user_id
            },
            UpdateExpression = f"set tasks.{task} = :t ",
            ExpressionAttributeValues = {
                ':t': ball
            },
            ReturnValues = "UPDATED_NEW"
        )
        return response

    def info_user(self, user_id):
        """Метод запроса информации по ключу партицирования
        """
        table = self.dynamodb.Table(self.table)
        response = table.query(
            ProjectionExpression = 'user_id, name, group, tasks',
            KeyConditionExpression = Key('user_id').eq(user_id)
        )
        return response['Items']

    def all_users(self):
        """Метод сканирования всех элементов таблицы.
        """
        table = self.dynamodb.Table(self.table)
        return table.scan()['Items']

    def for_mailer(self, group=None):
        """Метод выгрузки ключей таблицы для рассылки
        """
        table = self.dynamodb.Table(self.table)
        scan_kwargs = {
            'ProjectionExpression': "user_id, group"
        }
        response = table.scan(**scan_kwargs)
        if group:
            return [int(item['user_id']) for item in response['Items']
                    if int(item['active']) and item['group'] == group]

        return [int(item['user_id']) for item in response['Items'] if int(item['active'])]

    def delete_note(self, user_id):
        """Метод удаления записи из базы данных.
        """
        table = self.dynamodb.Table(self.table)
        try:
            response = table.delete_item(
                Key = {'user_id': user_id},
                )
            return response

        except Exception as e:
            print('Error', e)
        

    def delete_table(self):
        """Метод удаления таблицы из базы данных
        """
        table = self.dynamodb.Table(self.table)
        table.delete()
