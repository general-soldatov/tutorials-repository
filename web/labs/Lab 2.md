# LAB 2 "Основы языка разметки HTML"

## Цель работы
Ознакомиться с основными понятиями: тег, атрибут тега,  со структурой HTML документа. Создать простейшую страницу HTML. Познакомиться с применением заголовков на веб странице.

## Теоретическое введение
Документ HTML представляет собой файл, содержащий обыкновенный текст со специальными командами. Такой файл может быть подготовлен в произвольном текстовом редакторе. Хотя существуют специальные программы-конверторы и HTML-редакторы.
Документ HTML состоит из содержимого, то есть собственно полезной информации, и команд, задающих структуру. Каждая команда (управляющая конструкция) HTML документа, называемая «тег», должна заключаться в угловые скобки следующим образом: <тег>. Чаще всего в документе встречаются парные теги (открывающий и соответствующий ему закрывающий), так как браузеру необходимо знать область действия тега. Существуют и одиночные теги, однако, используются они только там, где область действия очевидна и дополнительной информации не требуется (ясно, например, что если мы встретили тег "начало абзаца" (<Р>), то предыдущий абзац уже закончился). В сомнительном же случае
лучше перестраховаться и поставить закрывающий парный тег, иначе документ может оказаться нечитаемым. Открывающий и закрывающий теги называются одинаково и отличаются друг от друга только символом "наклонная черта" или "слэш" - "/", который ставится сразу после открывающей угловой скобки закрывающего тега. Закрытие парных тегов выполняется так, чтобы соблюдались правила вложения.
```html
 <В><I>На этот текст воздействуют два тега</I></B>
 ```
Язык HTML в большинстве случаев совершено равнодушен к регистру, в котором набираются теги. Скажем, браузеру совершенно все равно, наберете вы тег, служащий для рисования горизонтальной линии, как `<HR>` или `<hr>` - эффект
будет один и тот же. HTML не признает никакого дополнительного форматирования текста, кроме как с помощью тегов. В результате текст, превосходно смотрящийся в текстовом редакторе, в окне браузера сольется в единую нечитаемую массу. Так, на месте нескольких пробелов будет лишь один пробел. Исчезнут все заголовки, пустые строки, деление текста на абзацы. Без тегов HTML браузер просто игнорирует все элементы форматирования.
Определение HTML как языка разметки основывается на том, что при удалении из документа всех тегов получается текстовый документ, совершенно эквивалентный по содержанию исходному гипертекстовому документу. Таким образом, при отображении документа HTML сами теги не отображаются, но влияют на способ отображения остальной части документа.

## Порядок выполнение
1. Создайте на локальном диске папку Lab_1
2. Откройте текстовый редактор Notepad
3. В текстовом редакторе напишите следующий код:
```html
<!DOCTYPE html>
<html>

<head></head>
<body></body>

</html>
```
4. Сохраните данный документ в папке Lab_1 и назовите его Index1.html
5. При сохранении в поле кодировка выберите кодировку UTF-8 (она необходима для корректного отображения браузером символов
6. Откройте сохраненный файл с помощью браузера (у вас должна открыться пустая страница)
7. Откройте файл Index1.html в блокноте
8. Внутри тега <HEAD> добавьте тег
```html
<TITLE> Моя первая страница </TITLE>
```
9. Сохраните файл и снова откройте его с помощью браузера. Теперь ваша вкладка должна называться МОЯ ПЕРВАЯ СТРАНИЦА.
10. Добавьте внутрь тега <BODY></BODY> Текст ПРИВЕТ МИР!!!
11. Сохраните файл и посмотрите результат в браузере
12. Для тега <BODY> добавьте атрибут bgcolor=#ff00ff (<body bgcolor=#ff00ff> )
13. Сохраните и посмотрите результат в браузере (цвет фона должен
поменяться)
14. Для тега <BODY> добавьте атрибут text=#ff0000
15. Сохраните и посмотрите результат в браузере (должен поменяться цвет)
16. В тег <BODY> напишите следующий код:
```html
<h1>Header level 1</h1>
<h2>Header level 2</h2>
<h3>Header level 3</h3>
<h4>Header level 4</h4>
<h5>Header level 5</h5>
<h6>Header level 6</h6>
```
17. Сохраните файл и запустите в браузере

## Содержание отчёта
