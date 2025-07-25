# LAB 5 "РАЗРАБОТКА НЕЙРОНА НА PYTORCH"

## Target
изучение возможностей библиотеки PyTorch.

## Theory
Определим важнейшие аспекты, которые играют принципиальную роль в построении любой нейронной сети (все их исследователь задает явно):  
– непосредственно, сама архитектура нейросети (сюда входят типы функций активации у каждого нейрона);  
– начальная инициализация весов каждого слоя;  
– метод оптимизации нейросети (сюда ещё входит метод изменения learning_rate);  
– размер батчей (batch_size);  
– количество итераций обучения (num_epochs);  
– функция потерь (loss);  
– тип регуляризации нейросети (для каждого слоя можно свой).  
  
Кроме вышеуказанных аспектов, важное значение приобретают факторы, связанные с самой задачей и данными:  
– качество выборки (непротиворечивость, чистота, корректность постановки задачи);  
– размер выборки.  
  
## Practical
Пример построения классификатора с использованием одного нейрона (в задаче используется набор данных «Яблоки и груши»): 
```py
!wget https://raw.githubusercontent.com/denieryd/mipt-deep-learning/refs/heads/master/5.%20Neuron%2C%20OOP/seminar/data/apples_pears.csv
```

```py
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('apples_pears.csv')
```
Построим график:
```py
plt.figure(figsize=(10, 8))
plt.scatter(data['yellowness'], data['symmetry'], c=data['target'], cmap='rainbow')
plt.title('Apples & Pears', fontsize=15)
plt.xlabel('symmetry', fontsize=14)
plt.ylabel('yellowness', fontsize=14)
plt.show();
```
<img width="851" height="708" alt="image" src="https://github.com/user-attachments/assets/3fc398b3-70e8-4dba-a65b-0b2735d35714" />

```py
X = data.iloc[:, :2].values # матрица объекты-признаки
y = data['target'].values.reshape((-1, 1)) # классы (столбец из нулей и единиц)
```
В модуле torch.nn лежат все необходимые вещи для конструирования нейронок, а в модуле torch.optim лежат все необходимые вещи для выбора метода оптимизации нейросети: 
```py
import torch
from torch.nn import Linear, Sigmoid
```
Есть два пути объявления нейросетей в PyTorch:  
– функциональный (Functional);  
– последовательный (Sequential).  

Рассмотрим второй путь (он чуть более user-friendly), к первому потом ещё вернёмся, и построим таким способом один нейрон:
```py
num_features = X.shape[1]

neuron = torch.nn.Sequential(
    Linear(num_features, out_features=1),
    Sigmoid()
)
neuron
```
Пока что мы просто создали объект класса Sequential, который состоит из одного линейного слоя размерности (num_features, 1) и последующего применения сигмоиды. Но уже сейчас его можно применить к объекту (тензору), просто веса в начале инициализирутся случайно и при forward_pass мы получим какой-то ответ пока что необученного нейрона:  
```py
neuron(torch.autograd.Variable(torch.FloatTensor([1, 1])))
```
Реализуем предсказание с использованием необученного нейрона:
```py
proba_pred = neuron(torch.autograd.Variable(torch.FloatTensor(X)))
y_pred = proba_pred > 0.5
y_pred = y_pred.data.numpy().reshape(-1)

plt.figure(figsize=(10, 8))
plt.scatter(data['yellowness'], data['symmetry'], c=y_pred, cmap='spring')
plt.title('Apples & Pears', fontsize=15)
plt.xlabel('symmetry', fontsize=14)
plt.ylabel('yellowness', fontsize=14)
plt.show();
```
<img width="851" height="708" alt="image" src="https://github.com/user-attachments/assets/cd27265e-c27a-4d06-9e92-46fc1fe21b89" />

Как и ожидалось, ничего полезного. Давайте научим нейрон отличать груши от яблок по их симметричности и желтизне. Обернём данные в torch.Tensor, а тензоры в torch.Variable, чтобы можно было вычислять градиенты по весам:
```py
X = torch.autograd.Variable(torch.FloatTensor(X))
y = torch.autograd.Variable(torch.FloatTensor(y))
```
Код обучения одного нейрона на PyTorch:
```py

```
После обучения можно выполнить предсказание:
```py

```
