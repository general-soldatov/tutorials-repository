# LAB 2 "РЕКОМЕНДАТЕЛЬНЫЕ СИСТЕМЫ"

## Target
применение идей коллаборативной фильтрации и фильтрации, основанной на контенте, для формирования рекомендаций фильмов пользователям.  

## Theory
В лабораторной работе необходимо выполнить 3 задания на исследование данных о фильмах с сайта MovieLens и применение двух подходов к построению рекомендаций фильмов – на основе предпочтений похожих пользователей и на основе предпочтений пользователя, для которого генерируется рекомендация.  
Данные: набор данных ml-25m включает в себя описание 5-звездного рейтинга фильмов с сайта [MovieLens](http://movielens.org/) – одного из старейших сервисов по рекомендации фильмов. Набор данных содержит 25 000 095 оценок и 1 093 360 применений тегов к 62 423 фильмам. Эти данные были созданы 162 541 пользователями в период с 9 января 1995 года по 21 ноября 2019 года – именно в этот день был сгенерирован датасет. Пользователи были выбраны случайным образом при условии, что пользователь оценил как минимум 20 фильмов. Демографическая информация в набор данных не включена. Каждый пользователь представлен только id. В папке Data/lab4 расположено несколько таблиц с характеристиками фильмов. Также эти данные доступны для скачивания по ссылке https://grouplens.org/datasets/movielens/25m/. Все задания лабораторной работы необходимо выполнять по этим данным.  
## tags.csv
Таблица tags.csv содержит все теги фильмов. Теги - это сгенерированные пользователями метаданные о фильмах. Каждый тег обычно представляет собой слово или короткую фразу. Значение, ценность и цель каждого тега определяется каждым пользователем.  
### Формат данных:
userId,movieId,tag,timestamp  
3,260,classic,1439472355  
3,260,sci-fi,1439472256  
4,1732,dark,comedy,1573943598  
...  
  
### Описание полей:  
● userId – идентификатор пользователя;  
● movieId – идентификатор фильма;  
● tag – название тега;  
● timestamp – количество секунд, прошедших с 1 января 1970.  

## ratings.csv
В таблице ratings.csv представлены оценки пользователей за фильмы. Рейтинги представляют собой шкалу из 5 звезд с использованием половинки звезды (от 0.5 звёзд до 5.0 звезд). 
### Формат данных:  
userId,movieId,rating,timestamp  
1,296,5.0,1147880044  
1,306,3.5,1147868817  
1,307,5.0,1147868828  
...  

### Описание полей:  
● userId – идентификатор пользователя;  
● movieId – идентификатор фильма;  
● rating – оценка, которую пользователь поставил фильму;  
● timestamp – количество секунд, прошедших с 1 января 1970.  
  
Строки упорядочены по userId, а затем по movieId.  

## movies.csv
Таблица movies.csv содержит информацию о фильмах. Каждая строка представляет информацию об одном фильме. Названия фильмов вводились вручную или были импортированы с сайта https://www.themoviedb.org/.   
### Формат данных:
movieId,title,genres  
1,Toy Story (1995),Adventure|Animation|Children|Comedy|Fantasy  
2,Jumanji (1995),Adventure|Children|Fantasy  
3,Grumpier Old Men (1995),Comedy|Romance  
...  

### Описание полей:  
● movieId – идентификатор фильма;  
● title – название фильма и год выпуска в скобках после названия;  
● genres – список жанров фильма, все жанры записываются в одном поле через разделитель “|”.   

Допустимые жанры:  
1. Action  
2. Adventure  
3. Animation  
4. Children's  
5. Comedy  
6. Crime  
7. Documentary  
8. Drama  
9. Fantasy  
11. Horror  
12. Musical  
13. Mystery  
14. Romance  
15. Sci-Fi  
16. Thriller  
17. War  
18. Western  
19. (no genres listed)

## genome-tags.csv
Таблица genome-tags.csv содержит tag genome – структуру данных, которая описывает релевантность тегов по отношению к фильму. Заданы 1128 тэгов, и по каждому фильму указаны значения релевантности для каждого тега. Tag genome был рассчитан с помощью алгоритма на основе пользовательского контента, включая теги, рейтинги и текстовые описания. Таблица содержит описания тегов.
### Формат данных:
tagId,tag  
2,007 (series)  
4,1920s  
11,3d  
22,adapted from:book  
...

### Описание полей:
● tagId – идентификатор тега, значения сгенерированы в тот момент, когда экспортировался весь набор данных, так что могут быть не такими, как в других версиях датасетов от MovieLens (например, 1М и 20M).;  
● tag – название тега.  

## genome-scores.csv
Таблица genome-scores.csv содержит релевантность тегов по отношению к фильмам.
### Формат данных:
movieId,tagId,relevance  
1,3,0.0625  
1,5,0.14075  
1,8,0.20375  
...  

### Описание полей:
● movieId – идентификатор фильма;  
● tagId – идентификатор тега;  
● relevance – релевантность тега фильму.  

## links.csv
Таблица links.csv содержит идентификаторы фильмов с других ресурсов. В каждой строке находятся ссылки на один фильм.  
### Формат данных:  
movieId,imdbId,tmdbId  
1,114709,862  
2,113497,8844  
3,113228,15602  
...  

### Описание полей:
● movieId – идентификатор фильма на https://movielens.org. Например, фильм "Toy Story" имеет ссылку https://movielens.org/movies/1;  
● imdbId – идентификатор фильма на http://www.imdb.com. Например, фильм Toy Story имеет ссылку http://www.imdb.com/title/tt0114709/;  
● tmdbId – идентификатор фильма на https://www.themoviedb.org.  Например, фильм Toy Story имеет ссылку https://www.themoviedb.org/movie/862.  

## Понимание данных
В таблице movies.csv представление жанров не очень хорошее: не очень понятно, что с ними можно делать. Очень часто для подобных данных используется следующий подход: под каждый жанр создается новый столбец, в соответствующем жанру столбце у фильма записывается 1, если в перечне был такой жанр, и 0 – если не было. Этот подход чем-то похож на one-hot encoding.  
Вторая проблема с данными – наличие в столбце title года выпуска фильма. Лучше всего под год выпуска выделить отдельный столбец.

## Practical
Скачаем в Google Colab архив с данными:  
```bash
!wget https://files.grouplens.org/datasets/movielens/ml-25m.zip
```
Распакуем архив:
```bash
!unzip ml-25m.zip
```
Создадим датафрейм тегов фильма:
```py
import pandas as pd

tag = pd.read_csv('ml-25m/tags.csv')
tag.sample(3)
tag_counts = tag['tag'].value_counts()
tag_counts[:10].sort_values().plot(kind='barh', figsize=(8, 4), colormap='Accent');
```
<img width="795" height="351" alt="image" src="https://github.com/user-attachments/assets/df53d3d1-1b3c-40d3-be7a-0cee4e1e8c9f" />
  
Загрузим данные о рейтингах  

```py
import numpy as np

rating = pd.read_csv('ml-25m/ratings.csv')
rating.sample(3)

rating["rating"].plot(kind='hist', figsize=(8, 4), colormap='Paired', 
                      xticks=np.arange(0.5, 5.5, 0.5));
```

<img width="678" height="366" alt="image" src="https://github.com/user-attachments/assets/4a4d6c8a-45fb-49bf-a72d-75040a0e56e1" />


Загрузим данные о фильмах и tag genome  
```py
movies = pd.read_csv('ml-25m/movies.csv')
genome_scores = pd.read_csv('ml-25m/genome-scores.csv')
genome_tag = pd.read_csv('ml-25m/genome-tags.csv')

genome_tag[genome_tag.tag == 'dragon']
top5_dragon_genom = genome_scores.query("tagId == 321").nlargest(5, "relevance")
movies[movies.movieId.isin(top5_dragon_genom.movieId)]
```
<img width="1071" height="301" alt="image" src="https://github.com/user-attachments/assets/4ad51fa8-366d-4d8d-ba09-74b0f3e40061" />
  
Объединим таблицы с описаниями фильмов и их рейтингами в одну
```py
data = pd.merge(movies, rating)
data.sample(5)
```

<img width="1477" height="301" alt="image" src="https://github.com/user-attachments/assets/1f37a5a8-54d0-4fc3-bd5b-105d0edfc58b" />

В таблицу number_rating будем хранить общее количество оценок фильму
```py
number_rating = data.groupby('title')['rating'].count().rename(
    "rated_by_users").reset_index()
number_rating.sample(5)
```

<img width="586" height="292" alt="image" src="https://github.com/user-attachments/assets/2c01e94d-686d-4623-b2bd-bbc50bad80c9" />

  
Поскольку обработка всей таблицы с рейтингами фильмов от пользователей перегружает RAM, то для примера возьмём случайные 10К строк из неё и составим сводную таблицу рейтингов, которые каждый пользователь ставил каждому фильму:
```py
data_train = data.sample(10000)
movie_pivot = data_train.pivot_table(index=['userId'], 
                                     columns=["title"],
                                     values="rating")
movie_pivot.head().T
```

<img width="686" height="628" alt="image" src="https://github.com/user-attachments/assets/2cc6d949-7bd9-47cd-a25e-0d12605df60d" />

Матрица предпочтений, полученная с помощью кода выше, состоит практически из одних нулей. В такой матрице маловероятно найти хоть что-то. Например, поищем похожий фильм.
```py
watched_movie = movie_pivot["How to Train Your Dragon (2010)"]
similar_movies = movie_pivot.corrwith(watched_movie)
similar_movies = similar_movies.sort_values(ascending=False)
similar_movies.head()
```
Судя по результату, фильм похож только сам на себя.  
<img width="435" height="399" alt="image" src="https://github.com/user-attachments/assets/7b7eb4f0-d7cd-41ae-a749-7033d894e2a6" />

Выход из ситуации с неудачным поиском похожих фильмов такой: будем делать рекомендации не всем и сразу, а конкретному пользователю. Формировать movie_pivot будем только для этого конкретного пользователя.  
1. Возьмем все оценки, которые поставил пользователь U.  
2. По фильмам, которые он оценил, получим всех пользователей, которые ставили этим фильмам оценки.  
3. Скорее всего, на этом этапе список получится большим (для случайного пользователя может получиться около 2 миллионов строк). Например, оставить только пользователей, у которых много общих фильмов.  
4. Для каждого пользователя посчитаем похожесть (например, корреляцию).  
5. Отсортируем пользователей по похожести.  
6. Оставим только k самых похожих пользователей.

Выбираем случайного пользователя, получаем фильмы, которые он смотрел, а затем находим пользователей, которые смотрели те же фильмы, что и тот, для которого делается рекомендация и выводим 10 рекомендуемых фильмов:

```py
all_users = rating['userId'].value_counts()
user = all_users.sample(1).index

user_movies = data[data.userId == user[0]]
user_movies = user_movies.drop(['genres', 'timestamp', 'userId'], axis=1)

new_data = data[data.movieId.isin(user_movies.movieId)]
new_data = new_data.drop(['genres', 'timestamp'], axis=1)
new_data.sample(10)
```
<img width="830" height="524" alt="image" src="https://github.com/user-attachments/assets/5049e490-6916-4504-8c30-c00bf39fe20f" />

Получим список фильма пользователя по его ID:
```py
user_group = new_data.groupby(['userId'])
```
Найдём фильмы трёх пользователей, оценивших больше всего фильмов в выборке:
```py
sorted_users_group = sorted(user_group, key=lambda x: len(x[1]), reverse=True)
```
Найдём ID пользователя, у которого больше всего похожих фильмов:
```py
similar_movies_user = sorted_users_group[1][0]
# скорее всего в sorted_users_group[0][0] будет сам пользователь
person2 = user_group.get_group(similar_movies_user).sort_values(by='movieId')
```
Получим список одинаковых фильмов для двух пользователей с оценками
```py
temp = user_movies[user_movies['movieId'].isin(user_group.get_group(similar_movies_user)['movieId'])]
person1 = temp.sort_values(by='movieId')
person1.head()
```
Далее посчитаем коэффициент корреляции Пирсона для этих двух пользователей.  
```py
from scipy.stats import pearsonr
pearsonr(person1.rating, person2.rating)[0] #0.36139189423020873
```
Таким образом, мы посчитали коэффициент корреляции, который показывает, насколько у пользователей совпадают списки просмотренных фильмов.
