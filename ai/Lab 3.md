# LAB 3 "РАЗРАБОТКА МОДЕЛИ ДЛЯ КЛАСТЕРИЗАЦИИ МНОЖЕСТВА НЕПОМЕЧЕННЫХ ОБЪЕКТОВ"

## Target
получить навыки подготовки данных для машинного обучения и решения задач «без учителя» на примере кластеризации (разделения на кластеры) непомеченных объектов (объектов без меток).

## Theory
Сущность машинного обучения «без учителя» заключается в том, что алгоритму до начала обучения не демонстрируются примеры и не предъявляются правильные ответы, так как их попросту нет. Например, имеется множество изображений объектов, которые потенциально могут быть разделены на несколько классов. Однако, в отличие от задачи классификации, объекты не помечены, то есть заранее неизвестно, к какому классу принадлежит то или иное изображение. Соответственно, мы не можем обучить модель на правильных примерах и показать ей, к какому классу относится каждое изображение.  
На практике с непомеченными объектами приходится работать гораздо чаще, чем с помеченными, что подчеркивает актуальность машинного обучения «без учителя».  
Одной из самых популярных задач машинного обучения «без учителя» является кластеризация.  
Кластеризация – это процесс разделения множества непомеченных объектов на подмножества. Каждое подмножество называется кластером. Внутри одного кластера объекты должны быть относительно похожи друг на друга, но при этом отличаться от объектов в других кластерах.  
Основой кластеризации является гипотеза компактности или непрерывности: близкие объекты схожи и принадлежат одному кластеру. Близость объектов определяется расстоянием между ними: схожесть или различие объектов зависят от того, насколько они удалены друг от друга. Таким образом, задача кластеризации заключается в том, чтобы распределить объекты по кластерам так, чтобы каждый кластер содержал близко расположенные объекты, а объекты из разных кластеров находились далеко друг от друга.
После разделения объектов на кластеры каждому объекту присваивается метка того кластера, к которому он принадлежит. Новый объект будет относиться к тому кластеру, в котором находятся ближайшие к нему объекты выборки.  
Для выполнения кластеризации множество непомеченных объектов преобразуется в матрицу «объекты – признаки» размерностью k строк на n столбцов, где k – количество объектов в выборке, а n – число признаков, описывающих каждый объект.

## Practics
Загрузить датасет по ссылке: https://archive.ics.uci.edu/ml/datasets/iris .
Данные представлены в виде data файла. Данные представляют собой информацию о трех классах цветов
Создать Python скрипт. Загрузить данные в датафрейм
```py
import pandas as pd
import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
data = pd.read_csv(url, header=None)

data.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
data.head()
```
## K-means
Проведем кластеризацию методов k-средних
```py
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

no_labeled_data = data.iloc[:, :-1]

k_means = KMeans(init='k-means++', n_clusters=3, 
                 n_init=15, random_state=42)
k_means.fit(no_labeled_data)

centers = k_means.cluster_centers_
predicted_labels = k_means.labels_

print("Centers of cluster", centers, 'Predicted labels', predicted_labels, sep='\n')
```
Получим центры кластеров и определим, какие наблюдения в какой кластер попали.
```py
data['cluster'] = predicted_labels
print(data[['class', 'cluster']].head(10))
```
Построим результаты классификации для признаков попарно (1 и 2, 2 и 3, 3 и 4).
```py
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.scatter(data['sepal_length'], data['sepal_width'], c=data['cluster'], cmap='viridis')
plt.title('K-Means: Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')

plt.subplot(2, 2, 2)
plt.scatter(data['sepal_width'], data['petal_length'], c=data['cluster'], cmap='viridis')
plt.title('K-Means: Sepal Width vs Petal Length')
plt.xlabel('Sepal Width')
plt.ylabel('Petal Length')

plt.subplot(2, 2, 3)
plt.scatter(data['petal_length'], data['petal_width'], c=data['cluster'], cmap='viridis')
plt.title('K-Means: Petal Length vs Petal Width')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')

plt.tight_layout()
plt.show()
```
Результат можем наблюдать на графике
![image](https://github.com/user-attachments/assets/23d6eab7-2eb6-4676-a348-c386c515dab5)

## Иерархическая кластеризация:

Теперь рассмотрим метод иерархической кластеризации.

Импортируем необходимые библиотеки и выполним кластеризацию.
```py
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

hierarchical = AgglomerativeClustering(n_clusters=3)
hierarchical_labels = hierarchical.fit_predict(no_labeled_data)

data['hierarchical_cluster'] = hierarchical_labels

data[['class', 'hierarchical_cluster']].head(10)
```
Построим дендрограмму для визуализации иерархической кластеризации.
```py
linked = linkage(no_labeled_data, method='ward')

plt.figure(figsize=(15, 7))
dendrogram(linked, orientation='top',
           labels=data['class'].values,
           distance_sort='descending',
           show_leaf_counts=True)
plt.title("Dendrogrm for Hierarchical Clustering")
plt.xlabel('Samples')
plt.ylabel('Distance')
plt.show()
```
Результом является представленный график:
![image](https://github.com/user-attachments/assets/0665e18a-130f-4ad4-95bc-535b1b505c5e)


Сохраните блокнот через меню «Файл / Сохранить».
Переименуйте файл на Google Диске, используя шаблон «Лабораторная работа № 3 студента группы … Фамилия Имя», указав свой номер группы, фамилию и имя.
