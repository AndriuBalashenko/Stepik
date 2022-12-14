/*
СОЗДАНИЕ ТАБЛИЦЫ 
Поле	Тип, описание
book_id	INT PRIMARY KEY AUTO_INCREMENT
title	VARCHAR(50)
author	VARCHAR(30)
price	DECIMAL(8, 2)
amount	INT
*/

CREATE TABLE book(
	book_id INT PRIMARY KEY AUTO_INCREMENT,
	title VARCHAR(50),
	author VARCHAR(30),
	price DECIMAL(8, 2),
	amount INT
	);

/*
Занесите новую строку в таблицу book (текстовые значения (тип VARCHAR) заключать либо в двойные, 
либо в одинарные кавычки):
*/

INSERT INTO book (title, author, price, amount) 
            VALUES ('Мастер и Маргарита','Булгаков М.А.', 670.99, 3);

/*Просмотр таблицы всей*/
SELECT * FROM book;

/*Добавление сразу много строк*/
INSERT INTO book (title, author, price, amount) 
			VALUES  ('Белая гвардия', 'Булгаков М.А.', 540.50, 5),
					('Идиот', 'Достоевский Ф.М.', 460.00, 10),
					('Братья Карамазовы', 'Достоевский Ф.М.', 799.01, 2);

/*Вариант с добавлением в таблицу без описания полей*/
INSERT INTO book
     VALUES (DEFAULT, 'Белая гвардия',     'Булгаков М.А.',    540.50, 5),
            (DEFAULT, 'Идиот',             'Достоевский Ф.М.', 460.00, 10),
            (DEFAULT, 'Братья Карамазовы', 'Достоевский Ф.М.', 799.01, 2);

/*Просмотр таблицы всей*/
SELECT * FROM book;

/*
Выбрать авторов, название книг и их цену из таблицы book.
+------------------+-----------------------+--------+
| author           | title                 | price  |
+------------------+-----------------------+--------+
| Булгаков М.А.    | Мастер и Маргарита    | 670.99 |
| Булгаков М.А.    | Белая гвардия         | 540.50 |
| Достоевский Ф.М. | Идиот                 | 460.00 |
| Достоевский Ф.М. | Братья Карамазовы     | 799.01 |
| Есенин С.А.      | Стихотворения и поэмы | 650.00 |
+------------------+-----------------------+--------+
*/
SELECT author, title, price FROM book;

/*
Выбрать названия книг и авторов из таблицы book, для поля title задать имя(псевдоним) Название, для поля author –  Автор. 

Результат:

+-----------------------+------------------+
| Название              | Автор            |
+-----------------------+------------------+
| Мастер и Маргарита    | Булгаков М.А.    |
| Белая гвардия         | Булгаков М.А.    |
| Идиот                 | Достоевский Ф.М. |
| Братья Карамазовы     | Достоевский Ф.М. |
| Стихотворения и поэмы | Есенин С.А.      |
+-----------------------+------------------+
*/
SELECT title as Название, author as  Автор FROM book;

/*
Для упаковки каждой книги требуется один лист бумаги, цена которого 1 рубль 65 копеек. 
Посчитать стоимость упаковки для каждой книги (сколько денег потребуется, чтобы упаковать 
все экземпляры книги). В запросе вывести название книги, ее количество и стоимость упаковки, 
последний столбец назвать pack. 

Результат:

+-----------------------+--------+-------+
| title                 | amount | pack  |
+-----------------------+--------+-------+
| Мастер и Маргарита    | 3      | 4.95  |
| Белая гвардия         | 5      | 8.25  |
| Идиот                 | 10     | 16.50 |
| Братья Карамазовы     | 2      | 3.30  |
| Стихотворения и поэмы | 15     | 24.75 |
+-----------------------+--------+-------+
*/
SELECT title, amount, amount * 1.65 AS pack 
FROM book;

/*
Функция
CEILING(x)	возвращает наименьшее целое число, большее или равное x
(округляет до целого числа в большую сторону)	
CEILING(4.2)=5
CEILING(-5.8)=-5

ROUND(x, k)	округляет значение x до k знаков после запятой,
если k не указано – x округляется до целого	
ROUND(4.361)=4
ROUND(5.86592,1)=5.9

FLOOR(x)	возвращает наибольшее целое число, меньшее или равное x
(округляет до  целого числа в меньшую сторону)	
FLOOR(4.2)=4
FLOOR(-5.8)=-6

POWER(x, y)	возведение x в степень y	
POWER(3,4)=81.0

SQRT(x)	квадратный корень из x	
SQRT(4)=2.0
SQRT(2)=1.41...

DEGREES(x)	конвертирует значение x из радиан в градусы	DEGREES(3) = 171.8...

RADIANS(x)	конвертирует значение x из градусов в радианы	RADIANS(180)=3.14...

ABS(x)	модуль числа x	ABS(-1) = 1

ABS(1) = 1

PI()	pi = 3.1415926...	 


В конце года цену всех книг на складе пересчитывают – снижают ее на 30%. Написать SQL запрос, 
который из таблицы book выбирает названия, авторов, количества и вычисляет новые цены книг. 
Столбец с новой ценой назвать new_price, цену округлить до 2-х знаков после запятой.

Результат:

+-----------------------+------------------+--------+-----------+
| title                 | author           | amount | new_price |
+-----------------------+------------------+--------+-----------+
| Мастер и Маргарита    | Булгаков М.А.    | 3      | 469.69    |
| Белая гвардия         | Булгаков М.А.    | 5      | 378.35    |
| Идиот                 | Достоевский Ф.М. | 10     | 322.00    |
| Братья Карамазовы     | Достоевский Ф.М. | 2      | 559.31    |
| Стихотворения и поэмы | Есенин С.А.      | 15     | 455.00    |
+-----------------------+------------------+--------+-----------+
*/
SELECT title, author, amount,
ROUND(price * 0.7, 2) AS new_price
FROM book;

/*
IF(логическое_выражение, выражение_1, выражение_2)

При анализе продаж книг выяснилось, что наибольшей популярностью пользуются книги Михаила Булгакова, 
 втором месте книги Сергея Есенина. Исходя из этого решили поднять цену книг Булгакова на 10%, 
 а цену книг Есенина - на 5%. Написать запрос, куда включить автора, название книги и новую цену, 
 последний столбец назвать new_price. Значение округлить до двух знаков после запятой.

 +------------------+-----------------------+-----------+
| author           | title                 | new_price |
+------------------+-----------------------+-----------+
| Булгаков М.А.    | Мастер и Маргарита    | 738.09    |
| Булгаков М.А.    | Белая гвардия         | 594.55    |
| Достоевский Ф.М. | Идиот                 | 460.00    |
| Достоевский Ф.М. | Братья Карамазовы     | 799.01    |
| Есенин С.А.      | Стихотворения и поэмы | 682.50    |
+------------------+-----------------------+-----------+
*/
SELECT author, title,
ROUND (IF(author = 'Булгаков М.А.', price * 1.1, IF(author = 'Есенин С.А.', price * 1.05, price)), 2) AS new_price
FROM book;

/*
Вывести автора, название  и цены тех книг, количество которых меньше 10.

Результат:

+------------------+--------------------+--------+
| author           | title              | price  |
+------------------+--------------------+--------+
| Булгаков М.А.    | Мастер и Маргарита | 670.99 |
| Булгаков М.А.    | Белая гвардия      | 540.50 |
| Достоевский Ф.М. | Братья Карамазовы  | 799.01 |
+------------------+--------------------+--------+
*/
SELECT author, title, price 
FROM book
WHERE amount < 10;

/*
Приоритеты операций:

круглые скобки
умножение  (*),  деление (/)
сложение  (+), вычитание (-)
операторы сравнения (=, >, <, >=, <=, <>)
NOT
AND
OR
*/

/*
Вывести название, автора и цену тех книг, которые написал Булгаков, ценой больше 600 рублей
*/
SELECT title, author, price 
FROM book
WHERE price > 600 AND author = 'Булгаков М.А.';

/*
Вывести название, цену  тех книг, которые написал Булгаков или Есенин, ценой больше 600 рублей
*/
SELECT title, author, price 
FROM book
WHERE (author = 'Булгаков М.А.' OR author = 'Есенин С.А.') AND price > 600;
/*
Вывести название, автора,  цену  и количество всех книг, цена которых меньше 500 или больше 600, 
а стоимость всех экземпляров этих книг больше или равна 5000.
+-----------------------+-------------+--------+--------+
| title                 | author      | price  | amount |
+-----------------------+-------------+--------+--------+
| Стихотворения и поэмы | Есенин С.А. | 650.00 | 15     |
+-----------------------+-------------+--------+--------+
*/
SELECT title, author, price, amount
FROM book 
WHERE (price < 500 OR price > 600) AND price * amount >= 5000;

/*
Выбрать названия и количества тех книг, количество которых от 5 до 14 включительно.
*/
SELECT title, amount 
FROM book
WHERE amount BETWEEN 5 AND 14;

/*
Выбрать названия и цены книг, написанных Булгаковым или Достоевским.
*/
SELECT title, price 
FROM book
WHERE author IN ('Булгаков М.А.', 'Достоевский Ф.М.');

/*
Вывести название и авторов тех книг, цены которых принадлежат интервалу от 540.50 до 800 (включая границы),  а количество или 2, или 3, или 5, или 7 .

Результат:

+--------------------+------------------+
| title              | author           |
+--------------------+------------------+
| Мастер и Маргарита | Булгаков М.А.    |
| Белая гвардия      | Булгаков М.А.    |
| Братья Карамазовы  | Достоевский Ф.М. |
+--------------------+------------------+
*/
SELECT title, author
FROM book 
WHERE price BETWEEN 540.50 AND 800 
	AND (amount = 2 or amount = 3 or amount = 5 or amount = 7);

/*
Столбцы после ключевого слова ORDER BY можно задавать:

названием столбца;
номером столбца;
именем столбца (указанным после AS).
*/

/*
Вывести название, автора и цены книг. 
Информацию  отсортировать по названиям книг в алфавитном порядке.
*/

SELECT title, author, price
FROM book
ORDER BY title;
/*Аналог*/
SELECT title, author, price
FROM book
ORDER BY 1;

/*
Вывести автора, название и количество книг, в отсортированном в алфавитном порядке по автору и 
по убыванию количества, для тех книг, цены которых меньше 750 рублей.
*/
SELECT author, title, amount AS Количество
FROM book
WHERE price < 750
ORDER BY author, amount DESC;

SELECT author, title, amount AS Количество
FROM book
WHERE price < 750
ORDER BY 1, 3 DESC;

/*
Важно! Если названия столбцов заключены в кавычки, 
то при использовании их в сортировке, необходимо записывать их БЕЗ КАВЫЧЕК.
*/

/*
Вывести  автора и название  книг, количество которых принадлежит интервалу от 2 до 14 (включая границы). Информацию  отсортировать сначала по авторам (в обратном алфавитном порядке), а затем по названиям книг (по алфавиту).

Результат:

+------------------+--------------------+
| author           | title              |
+------------------+--------------------+
| Достоевский Ф.М. | Братья Карамазовы  |
| Достоевский Ф.М. | Идиот              |
| Булгаков М.А.    | Белая гвардия      |
| Булгаков М.А.    | Мастер и Маргарита |
+------------------+--------------------+
*/
SELECT author, title 
FROM book 
WHERE amount BETWEEN 2 AND 14
ORDER BY author DESC, title;

/*%	Любая строка, содержащая ноль или более символов	SELECT * FROM book WHERE author LIKE '%М.%'
выполняет поиск и выдает все книги, инициалы авторов которых содержат «М.»

_ (подчеркивание)	Любой одиночный символ	SELECT * FROM book WHERE title LIKE 'Поэм_'
выполняет поиск и выдает все книги, названия которых либо «Поэма», либо «Поэмы» и пр.

*/

/*
Вывести название и автора тех книг, название которых состоит из двух и более слов, а инициалы автора содержат букву «С». Считать, что в названии слова отделяются друг от друга пробелами и не содержат знаков препинания, между фамилией автора и инициалами обязателен пробел, инициалы записываются без пробела в формате: буква, точка, буква, точка. Информацию отсортировать по названию книги в алфавитном порядке.

Результат:

+-----------------------+-------------+
| title                 | author      |
+-----------------------+-------------+
| Капитанская дочка     | Пушкин А.С. |
| Стихотворения и поэмы | Есенин С.А. |
+-----------------------+-------------+
*/

SELECT title,author
FROM book
WHERE title LIKE '_% %' AND title NOT LIKE '% %' AND title NOT LIKE '_% ' AND (
    author LIKE '% _.С.%' OR author LIKE '% С._.%')
ORDER BY 1;

/*Магазин счёл, что классика уже не пользуется популярностью, поэтому необходимо в выборке:

1. Сменить всех авторов на "Евгений Клейменов".

2. К названию каждой книги в начале дописать "Евгений Клейменов и".

3. Цену поднять на 42%.

4. Отсортировать по убыванию цены и убыванию названия.*/

SELECT 
    "Евгений Клейменов" AS author, 
    CONCAT("Евгений и ", title) AS title, 
    round((price * 1.42),2) AS price
FROM book
ORDER BY 3 DESC, 2 DESC

