# Создание файла exe из PyCharm
Открываем терминал в среде разработки посредством комбинации ``Alt+F12``, затем в нём запускаем установку pyinstaller  
`` pip install pyinstaller ``
Преобразуем скрипт в исполняемый файл - `` pyinstaller your_script.py``  
Опционально: создаём один файл - ``pyinstaller --onefile your_script.py``  
Опционально: скрываем дополнительно консоль - ``pyinstaller --onefile --noconsole your_script.py`` 

