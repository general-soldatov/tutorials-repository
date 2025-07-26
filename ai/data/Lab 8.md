# LAB 8 "СВЕРТОЧНАЯ НЕЙРОННАЯ СЕТЬ"

## Target
получение практических навыков по реализации пайплайна для решения задачи машинного обучения с использованием сверточной нейросетевой модели.

## Theory
Для проектирования и разработки нейронной сети в рамках данной работы будет использоваться нейросетевой фреймворк PyTorch. На современном этапе развития инструментальных средств машинного обучения исследователю на рынке доступны следующие варианты программных средств:  
1. TensorFlow. Фреймворк машинного обучения от компании Google (свободно распространяемое решение). TensorFlow предназначен для поддержки реализации всех стадий жизненного цикла нейросетевых моделей. TensorFlow представляет собой библиотеку крупномасштабного машинного обучения и численных расчетов. В качестве языка обращения к библиотеке используется Python, но само ядро библиотеки написано на C++. Библиотека позволяет проектировать, обучать и развертывать глубокие модели; именного deep learning является основным преимуществом TensorFlow. Библиотека представляет модели в виде вычислительного графа. Узлы графа (тензоры) соответствуют обрабатываемым данным, а ребра графа – операциям над этими данными. Библиотека TensorFlow позволяет создавать модели глубокого обучения, которые могут быть развернуты на различных платформах: персональных компьютерах, смартфонах iOS и Android, CPU, GPU или TPU, облачные сервисы Google, Amazon или Microsoft. В настоящее время доступна версия библиотеки 2.0, которая сильно отличается от версий 1.x.  
2. PyTorch. Фреймворк машинного обучения от компании Facebook, разработанный для языка Python. PyTorch во многом схож с TensorFlow: простое аппаратное ускорение с использованием GPU; простая система прототипирования моделей глубокого обучения; множество стандартных блоков вычислений, слоев ИНС, содержащихся в составе библиотеки. PyTorch рекомендуется использовать для небольших проектов, которые необходимо запустить в качестве узкоспециализированного веб-сервиса, тогда как TensorFlow предпочтительнее при обучении больших моделей, которые требуют использования больших вычислительных мощностей в виде облачных сервисов и кластеров. TensorFlow и PyTorch – это наиболее популярные библиотеки в сфере машинного обучения. Работа с каждой из них возможна без непосредственной установки данных библиотек (что является достаточно трудоемким процессом): можно использовать бесплатный сервис Google Colab для обучения глубоких моделей. Но рассмотренные библиотеки не являются единственными на рынке.  

CNTK (Microsoft Cognitive Toolkit) – библиотека машинного обучения от Microsoft. Как и TensorFlow данный программный продукт использует граф для представления потока вычислений, но CNTK является более специализированной на моделях глубокого обучения. CNTK отличается более высокой скоростью выполнения операций в рамках манипулирования данными при обучении нейронных сетей и предлагает различные языки в качестве клиентских (Python, C++, C#, Java). Основной недостаток CNTK – малое количество целевых платформ для развертывания.  
Apache MXNet – фреймворк машинного обучения, используемый компанией Amazon в качестве библиотеки машинного обучения в рамках облака AWS. Отличается высокой степенью масштабируемости по отдельным GPU и компьютерам. Поддерживает большое количество различных языков разработки: Python, C++, Scala, R, JavaScript, Julia, Perl, Go. При этом API MXNet считается менее дружественным чем TensorFlow.  
В рамках данной работы в качестве рабочего фреймворка рекомендуется использование PyTorch или TensorFlow. Основное преимущество TensorFlow – масштабируемость. При этом у PyTorch существует преимущество в виде удобного API и используемой идеи близости библиотеки к концепции языка Python (Python-like стиль).

## Practical
Нас необходимо решить задачу классификации цветов. Рассмотрим Датасет содержащий 4242 изображения цветов размеченных по 5 видам (тюльпан, ромашка, подсолнух, роза, одуванчик). Подключаем google drive чтобы хранить на нем папку с изображениями:
```py
from google.colab import drive
drive.mount('/content/drive/', force_remount=True)
```
Скачиваем архив по ссылке, распаковываем и сохраняем в google drive в папку flowers
```py
import os
if not os.path.exists('flowers.zip'):
  !wget https://www.dropbox.com/s/qmfzqc056oiwy8c/flowers.zip
if not os.path.exists('drive/MyDrive/flowers'):
  !unzip flowers.zip -d drive/MyDrive/
if os.path.exists('drive/MyDrive/flowers/.ipynb_checkpoints'):
  !rm drive/MyDrive/flowers/.ipynb_checkpoints
```
Загружаем библиотеки. Фиксируем random.seed для воспроизводимости
```py
import numpy as np # linear algebra
import os
import torch
import torchvision
from torchvision.datasets.utils import download_url
from torch.utils.data import random_split
from torchvision.datasets import ImageFolder
from torchvision import transforms
from torchvision.transforms import ToTensor
from torch.utils.data.dataloader import DataLoader
import torch.nn as nn
import torch.nn.functional as F
import random
from tqdm import tqdm

random.seed(0)
torch.manual_seed(0)
```
Выбираем на чем будем делать вычисления - CPU или GPU (cuda)
```py
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(device)
```
Проведём нормализацию изображений и упакуем их в тензор
```py
prepare_imgs = torchvision.transforms.Compose(
    [
        torchvision.transforms.Resize((224, 224)), #приводим картинки к одному размеру
        torchvision.transforms.ToTensor(), # упаковываем их в тензор
        torchvision.transforms.Normalize(
            mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225] # нормализуем картинки по каналам
        ),
    ]
)
# задаем датасет. Лейблы - имена папок:
dataset = ImageFolder('drive/MyDrive/flowers', transform=prepare_imgs)
```
Создадим вспомогательный класс для отслеживания метрик и Loss:
```py
class ValueMeter(object):
    """
    Вспомогательный класс, чтобы отслеживать loss и метрику
    """
    def __init__(self):
        self.sum = 0
        self.total = 0
  
    def add(self, value, n):
        self.sum += value*n
        self.total += n
  
    def value(self):
        return self.sum/self.total

def log(mode, epoch, loss_meter, accuracy_meter, best_perf=None):
  """
  Вспомогательная функция, чтобы
  """
  print(
      f"[{mode}] Epoch: {epoch:0.2f}. "
      f"Loss: {loss_meter.value():.2f}. "
      f"Accuracy: {100*accuracy_meter.value():.2f}% ", end="\n")

  if best_perf:
      print(f"[best: {best_perf:0.2f}]%", end="")
```
Создадим свёрточную сеть с нуля - бейзлайн, пропишем вручную слои:
```py
model = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2), # output: 64 x 16 x 16

            nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.Conv2d(128, 128, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2), # output: 128 x 8 x 8

            nn.Conv2d(128, 256, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.Conv2d(256, 256, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2), # output: 256 x 4 x 4

            nn.Flatten(),
            nn.Linear(256*28*28, 1024),
            nn.ReLU(),
            nn.Linear(1024, 512),
            nn.ReLU(),
            nn.Linear(512, 5))
model.to(device) # отправляем модель на девайс (GPU)
```
Задаем гиперпараметры для обучения.
```py
batch_size = 32 # размер батча
optimizer = torch.optim.Adam(params = model.parameters()) # алгоритм оптимизации
lr = 0.001 # learning rate
```
Разбиваем датасет на train/validation. Задаем dataloader'ы - объекты для итеративной загрузки данных и лейблов для обучения и валидации:
```py
train_set, val_set = torch.utils.data.random_split(dataset, [len(dataset)-1000, 1000])
print('Размер обучающего и валидационного датасета: ', len(train_set), len(val_set))
loaders = {'training': DataLoader(train_set, batch_size, pin_memory=True,num_workers=2, shuffle=True),
           'validation':DataLoader(val_set, batch_size, pin_memory=True,num_workers=2, shuffle=False)}
```
Функция для подсчета Accuracy
```py
def accuracy(outputs, labels):
    _, preds = torch.max(outputs, dim=1)
    return torch.tensor(torch.sum(preds == labels).item() / len(preds))
```
Функция для обучения и валидации модели
```py
def trainval(model, loaders, optimizer, epochs=10):
    """
    model: модель, которую собираемся обучать
    loaders: dict с dataloader'ами для обучения и валидации
    optimizer: оптимизатор
    epochs: число обучающих эпох (сколько раз пройдемся по всему датасету)
    """
    loss_meter = {'training': ValueMeter(), 'validation': ValueMeter()}
    accuracy_meter = {'training': ValueMeter(), 'validation': ValueMeter()}

    loss_track = {'training': [], 'validation': []}
    accuracy_track = {'training': [], 'validation': []}

    for epoch in range(epochs): # итерации по эпохам
        for mode in ['training', 'validation']: # обучение - валидация
            # считаем градиент только при обучении:
            with torch.set_grad_enabled(mode == 'training'):
                # в зависимоти от фазы переводим модель в нужный ружим:
                model.train() if mode == 'training' else model.eval()
                for imgs, labels in tqdm(loaders[mode]):
                    imgs = imgs.to(device) # отправляем тензор на GPU
                    labels = labels.to(device)
                    bs = labels.shape[0]  # размер батча (отличается для последнего батча в лоадере)

                    preds = model(imgs) # forward pass - прогоняем тензор с картинками через модель
                    loss = F.cross_entropy(preds, labels) # считаем функцию потерь
                    acc = accuracy(preds, labels) # считаем метрику

                    # храним loss и accuracy для батча
                    loss_meter[mode].add(loss.item(), bs)
                    accuracy_meter[mode].add(acc, bs)

                    # если мы в фазе обучения
                    if mode == 'training':
                        optimizer.zero_grad() # обнуляем прошлый градиент
                        loss.backward() # делаем backward pass (считаем градиент)
                        optimizer.step() # обновляем веса
            # в конце фазы выводим значения loss и accuracy
            log(mode, epoch, loss_meter[mode], accuracy_meter[mode])

            # сохраняем результаты по всем эпохам
            loss_track[mode].append(loss_meter[mode].value())
            accuracy_track[mode].append(accuracy_meter[mode].value())
    return loss_track, accuracy_track
```
Обучаем базовую модель. Проверим загрузку видеокарты, прежде чем запустить обучение:
```
!nvidia-smi
```
Запускаем обучение на 10 эпох
```py
loss_track, accuracy_track = trainval(model, loaders, optimizer, epochs=10)
```
Визуализируем метрики в ходе обучения на графике:
```py
from matplotlib import pyplot as plt
%matplotlib inline
plt.plot(accuracy_track['training'], label='training')
plt.plot(accuracy_track['validation'], label='validation')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.grid()
plt.legend()
```
<img width="576" height="432" alt="image" src="https://github.com/user-attachments/assets/f69b8d99-cf98-4c4a-a488-9459e8790801" />

Fine-tuning предобученной модели. Теперь попробуем поработать с предобученной сетью ResNet-18

<img width="850" height="229" alt="image" src="https://github.com/user-attachments/assets/58bc0fe6-93b9-4fe2-adb3-60b8461ae2e2" />

```py
resnet = torchvision.models.resnet18(pretrained=True) # инициализируем модель
resnet
```
Напишем функцию для заморозки весов модели:
```py
def set_parameter_requires_grad(model):
  """
  Функция для заморозки весов модели
  """
  for param in model.parameters():
    param.requires_grad = False

set_parameter_requires_grad(resnet)
```
Меняем последний слой модели, чтобы он предсказывал 5 классов, а не 1000 Когда мы заново определяем слой, у него по умолчанию стоит аттрибут requires_grad = True. То есть этот полносвязный слой будет обучаться:
```py
resnet.fc = nn.Linear(512, 5)
```
Проверим все ли сработало правильно, выведем веса, которые будут обучаться
```py
for name, param in resnet.named_parameters():
    if param.requires_grad:
        print(name)
```
Запустим функцию обучения модели. Внимание - необходимо заново задать оптимизатор, чтобы он теперь работал с весами resnet
```py
resnet.to(device)
optimizer = torch.optim.Adam(params = resnet.parameters()) # алгоритм оптимизации
loss_track, accuracy_track = trainval(resnet, loaders, optimizer, epochs=5)
```
Выведем метрики качества обучения на графике:
```py
plt.plot(accuracy_track['training'], label='training')
plt.plot(accuracy_track['validation'], label='validation')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.grid()
plt.legend()
```
<img width="584" height="432" alt="image" src="https://github.com/user-attachments/assets/67eae2dc-c044-40a9-bc3c-7601fdc9f9ab" />

Уже после 5 эпох получили точность 86 процентов. Это впечатляет! Сохраним веса модели:
```py
weights_fname = 'drive/MyDrive/flower-resnet.pth'
torch.save(resnet.state_dict(), weights_fname)
```
Теперь посмотрим как модель предсказывает:
```py
import matplotlib.pyplot as plt
%matplotlib inline
import warnings
warnings.filterwarnings("ignore")

def predict_image(img, model):
    # Convert to a batch of 1
    xb = img.unsqueeze(0).to(device)
    # Get predictions from model
    yb = model(xb)
    # Pick index with highest probability
    _, preds  = torch.max(yb, dim=1)
    # Retrieve the class label
    return dataset.classes[preds[0].item()]

for i in range(1,10):
  img, label = val_set[i]
  plt.imshow(img.clip(0,1).permute(1, 2, 0))
  plt.axis('off')
  plt.title('Label: {}, Predicted: {}'.format(dataset.classes[label],predict_image(img, resnet)))
  plt.show()
  # print('Label:', dataset.classes[label], ',Predicted:', predict_image(img, resnet))
```
