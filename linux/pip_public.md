# Упаковка проектов для pip

Вначале обновляем утилиту:  
```bash
python3 -m pip install --upgrade pip
```  
## Настройка метаданных 
Откройте pyproject.toml и введите следующее содержимое. Измените, name включив свое имя пользователя; это гарантирует, что у вас будет уникальное имя пакета, которое не будет конфликтовать с пакетами, загруженными другими людьми, следуя этому руководству.
```toml
[project]
name = "example_package_YOUR_USERNAME_HERE"
version = "0.0.1"
authors = [
  { name="Example Author", email="author@example.com" },
]
description = "A small example package"
readme = "README.md"
requires-python = ">=3.8"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

[project.urls]
Homepage = "https://github.com/pypa/sampleproject"
Issues = "https://github.com/pypa/sampleproject/issues"
```
Описание и лицензия добавляются из файлов `README.md` и 'LICENSE`.  
## Сборка проекта
Обновляем утилиту упаковщика pip.  
```bash
python3 -m pip install --upgrade build
```
Теперь выполните эту команду из того же каталога, где находится `pyproject.toml`:
```bash
python3 -m build
```
Теперь можем использовать twine для загрузки дистрибутивных пакетов. Устанавливаем Twine:
```bash
python3 -m pip install --upgrade twine
```
После установки запустим Twine, чтобы загрузить все архивы в репозиторий:
```bash
python3 -m twine upload dist/*
```
Вам будет предложено ввести имя пользователя и пароль. Для имени пользователя используйте `__token__`. Для пароля используйте значение токена, включая pypi-префикс.
Более подробно описано в [документации](https://packaging.python.org/en/latest/tutorials/packaging-projects/), описание конфигурационного [файла](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#writing-pyproject-toml)
