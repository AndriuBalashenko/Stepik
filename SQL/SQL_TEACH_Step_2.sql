/*
Отобрать различные (уникальные) элементы столбца amount таблицы book.
+--------+
| amount |
+--------+
| 3      |
| 5      |
| 10     |
| 15     |
+--------+
*/
SELECT DISTINCT amount
FROM book;

/*
Посчитать, количество различных книг и количество экземпляров книг каждого автора ,
хранящихся на складе.
Столбцы назвать Автор, Различных_книг и Количество_экземпляров соответственно.
+------------------+----------------+------------------------+
| Автор            | Различных_книг | Количество_экземпляров |
+------------------+----------------+------------------------+
| Булгаков М.А.    | 2              | 8                      |
| Достоевский Ф.М. | 3              | 23                     |
| Есенин С.А.      | 1              | 15                     |
+------------------+----------------+------------------------+
*/

SELECT author AS 'Автор', COUNT(title) AS 'Различных_книг',
	SUM(amount) AS 'Количество_экземпляров'
FROM book
GROUP BY author;

/*
Вывести фамилию и инициалы автора, минимальную, максимальную и среднюю цену книг каждого автора .
Вычисляемые столбцы назвать Минимальная_цена, Максимальная_цена и Средняя_цена соответственно.
+------------------+------------------+-------------------+--------------+
| author           | Минимальная_цена | Максимальная_цена | Средняя_цена |
+------------------+------------------+-------------------+--------------+
| Булгаков М.А.    | 540.50           | 670.99            | 605.745000   |
| Достоевский Ф.М. | 460.00           | 799.01            | 579.836667   |
| Есенин С.А.      | 650.00           | 650.00            | 650.000000   |
+------------------+------------------+-------------------+--------------+
*/

SELECT author, MIN(price) AS 'Минимальная_цена',
	MAX(price) AS 'Максимальная_цена',
	AVG(price) AS 'Средняя_цена'
FROM book
GROUP BY author;

/*
Для каждого автора вычислить суммарную стоимость книг S (имя столбца Стоимость), а также вычислить налог на
добавленную стоимость  для полученных сумм (имя столбца НДС ) , который включен в стоимость и составляет k = 18%,
а также стоимость книг  (Стоимость_без_НДС) без него. Значения округлить до двух знаков после запятой.
В запросе для расчета НДС(tax)  и Стоимости без НДС(S_without_tax) использовать следующие формулы:

+------------------+-----------+---------+-------------------+
| author           | Стоимость | НДС     | Стоимость_без_НДС |
+------------------+-----------+---------+-------------------+
| Булгаков М.А.    | 4715.47   | 719.31  | 3996.16           |
| Достоевский Ф.М. | 11802.03  | 1800.31 | 10001.72          |
| Есенин С.А.      | 9750.00   | 1487.29 | 8262.71           |
+------------------+-----------+---------+-------------------+
 */

 SELECT author, SUM(price * amount) AS Стоимость,
	ROUND(SUM((price * amount)* 18/100)/(1+18/100),2) AS НДС,
	ROUND(SUM((price * amount)) / (1 + 18/100),2) AS Стоимость_без_НДС
FROM book
GROUP BY author;

/*
Вывести  цену самой дешевой книги, цену самой дорогой и среднюю цену уникальных книг на складе.
Названия столбцов Минимальная_цена, Максимальная_цена, Средняя_цена соответственно.
Среднюю цену округлить до двух знаков после запятой.

+------------------+-------------------+--------------+
| Минимальная_цена | Максимальная_цена | Средняя_цена |
+------------------+-------------------+--------------+
| 460.00           | 799.01            | 600.17       |
+------------------+-------------------+--------------+
*/
SELECT ROUND(MIN(price), 2) AS Минимальная_цена,
	ROUND(MAX(price), 2) AS Максимальная_цена,
	ROUND(AVG(price), 2) AS Средняя_цена
FROM book;

/*
Вычислить среднюю цену и суммарную стоимость тех книг, количество экземпляров которых принадлежит интервалу от 5 до 14,
включительно. Столбцы назвать Средняя_цена и Стоимость, значения округлить до 2-х знаков после запятой.
+--------------+-----------+
| Средняя_цена | Стоимость |
+--------------+-----------+
| 493.67       | 12107.50  |
+--------------+-----------+
*/
SELECT ROUND(AVG(price),2) AS Средняя_цена,
    SUM(price*amount) AS Стоимость
FROM book
WHERE amount BETWEEN 5 and 14;

/*
Посчитать стоимость всех экземпляров каждого автора без учета книг «Идиот» и «Белая гвардия». В результат включить только тех авторов, у которых суммарная стоимость книг (без учета книг «Идиот» и «Белая гвардия») более 5000 руб.
Вычисляемый столбец назвать Стоимость. Результат отсортировать по убыванию стоимости.
+------------------+-----------+
| author           | Стоимость |
+------------------+-----------+
| Есенин С.А.      | 9750.00   |
| Достоевский Ф.М. | 7202.03   |
+------------------+-----------+
*/

SELECT author, SUM(price * amount) AS Стоимость
FROM book
WHERE title <> 'Идиот' AND title <> 'Белая гвардия'
GROUP BY author
HAVING SUM(price * amount) > 5000
ORDER BY SUM(price * amount) DESC;


/*
Сколько стоит одна буква из суммарного кол-ва букв полученных из названия книги авторов,
отфильтровать по убыванию и вывести то все что > 30

+------------------+------------------------+-------------+------------------+
| author           | count_all_title_letter | total_price | price_one_letter |
+------------------+------------------------+-------------+------------------+
| Есенин С.А.      | 40                     | 9750.00     | 243.75           |
| Достоевский Ф.М. | 53                     | 11802.03    | 222.68           |
| Булгаков М.А.    | 59                     | 4715.47     | 79.92            |
+------------------+------------------------+-------------+------------------+
*/

SELECT
    author,
    SUM(LENGTH(title)) AS count_all_title_letter,
    SUM(price * amount) AS total_price,
    round(SUM(price * amount) / SUM(LENGTH(title)), 2) AS price_one_letter
FROM book
GROUP BY author
HAVING price_one_letter > 30
ORDER BY price_one_letter DESC;

/*
Вывести информацию (автора, название и цену) о тех книгах, цены которых превышают минимальную цену книги на складе
не более чем на 150 рублей в отсортированном по возрастанию цены виде.
+------------------+----------------+--------+
| author           | title          | price  |
+------------------+----------------+--------+
| Достоевский Ф.М. | Идиот          | 460.00 |
| Достоевский Ф.М. | Игрок          | 480.50 |
| Булгаков М.А.    | Белая гвардия  | 540.50 |
| Пушкин А.С.      | Евгений Онегин | 610.00 |
+------------------+----------------+--------+
*/

SELECT author, title, price
FROM book
WHERE price - (SELECT MIN(price)
	FROM book) <= 150
ORDER BY price;

/*
Вывести информацию (автора, книгу и количество) о тех книгах,
количество экземпляров которых в таблице book не дублируется.
+---------------+-----------------------+--------+
| author        | title                 | amount |
+---------------+-----------------------+--------+
| Булгаков М.А. | Белая гвардия         | 5      |
| Есенин С.А.   | Стихотворения и поэмы | 15     |
+---------------+-----------------------+--------+
*/

SELECT author, title, amount
FROM book
WHERE amount IN(
		SELECT amount
		FROM book
		GROUP BY amount
		HAVING COUNT(amount)=1
		);
/*
Вывести информацию о книгах(автор, название, цена), цена которых меньше самой большой из минимальных цен,
вычисленных для каждого автора.

+------------------+---------------+--------+
| author           | title         | price  |
+------------------+---------------+--------+
| Булгаков М.А.    | Белая гвардия | 540.50 |
| Достоевский Ф.М. | Идиот         | 460.00 |
| Достоевский Ф.М. | Игрок         | 480.50 |
+------------------+---------------+--------+
*/

SELECT author, title, price
FROM book
WHERE price < ANY (
			SELECT MIN(price)
			FROM book
			GROUP BY author
			);

/*
Посчитать сколько и каких экземпляров книг нужно заказать поставщикам, чтобы на складе стало одинаковое количество
экземпляров каждой книги, равное значению самого большего количества экземпляров одной книги на складе.
Вывести название книги, ее автора, текущее количество экземпляров на складе и количество заказываемых экземпляров книг.
Последнему столбцу присвоить имя Заказ. В результат не включать книги, которые заказывать не нужно.

+--------------------+------------------+--------+-------+
| title              | author           | amount | Заказ |
+--------------------+------------------+--------+-------+
| Мастер и Маргарита | Булгаков М.А.    | 3      | 12    |
| Белая гвардия      | Булгаков М.А.    | 5      | 10    |
| Идиот              | Достоевский Ф.М. | 10     | 5     |
| Братья Карамазовы  | Достоевский Ф.М. | 3      | 12    |
| Игрок              | Достоевский Ф.М. | 10     | 5     |
+--------------------+------------------+--------+-------+
*/

SELECT title, author, amount,
	(SELECT MAX(amount) FROM book) - amount AS Заказ
FROM book
WHERE amount <> (SELECT MAX(amount) FROM book)

/*
Хозяин магазина любитель числа 10. Ему не нравится, когда количество книг не равно его любимому числу.
Необходимо составить список с указанием названия книги, автора, количества книг на данный момент, необходимое
для заказа количество книг, необходимое для продажи количество книг.
Записи, которые не требуют внимания выводить не нужно.
+------------------+-----------------------+--------+----------------+------------+
| author           | title                 | amount | Заказ          | Продать    |
+------------------+-----------------------+--------+----------------+------------+
| Булгаков М.А.    | Мастер и Маргарита    | 3      | 7              | Достаточно |
| Булгаков М.А.    | Белая гвардия         | 5      | 5              | Достаточно |
| Достоевский Ф.М. | Братья Карамазовы     | 3      | 7              | Достаточно |
| Есенин С.А.      | Стихотворения и поэмы | 15     | Продать лишнее | 5          |
+------------------+-----------------------+--------+----------------+------------+
*/
SELECT author, title, amount,
	IF (amount < 10, (10 - amount), 'Продать лишнее') AS Заказ,
	IF (amount > 10, ABS(10 - amount), "Достаточно") AS Продать
FROM book
WHERE amount <> (10);

/*
Создать таблицу поставка (supply), которая имеет ту же структуру, что и таблиц book.

Поле	Тип, описание
supply_id	INT PRIMARY KEY AUTO_INCREMENT
title	VARCHAR(50)
author	VARCHAR(30)
price	DECIMAL(8, 2)
amount	INT
*/

CREATE TABLE supply(
	supply_id INT PRIMARY KEY AUTO_INCREMENT,
	title VARCHAR(50),
	author VARCHAR(30),
	price DECIMAL(8, 2),
	amount INT
	);

/*
Добавление одной записи в таблицу осуществляется с помощью запроса INSERT, подробно рассмотренного в первом уроке. Запросы обязательно разделять точкой с запятой.

Допускается вставка нескольких записей одновременно, для этого используется SQL запрос следующего вида:

INSERT INTO имя_таблицы(столбец_1, столбец_2, ..., столбец_N)
VALUES
    (значение_1_1, значение_1_2, ..., значение_1_N),
    (значение_2_1, значение_2_2, ..., значение_2_N),
    ...
    (значение_M_1, значение_M_2, ..., значение_M_N);
*/

/*
Занесите в таблицу supply четыре записи, чтобы получилась следующая таблица:

supply_id	title	author	price	amount
1	Лирика	Пастернак Б.Л.	518.99	2
2	Черный человек 	Есенин С.А.	570.20	6
3	Белая гвардия	Булгаков М.А.	540.50	7
4	Идиот	Достоевский Ф.М.	360.80	3
*/

INSERT INTO supply (title, author, price, amount)
VALUES
    ('Лирика','Пастернак Б.Л.', 518.99, 2),
    ('Черный человек', 'Есенин С.А.', 570.20, 6),
    ('Белая гвардия','Булгаков М.А.', 540.50, 7),
    ('Идиот', 'Достоевский Ф.М.', 360.80, 3);

/*
Добавить из таблицы supply в таблицу book, все книги, кроме книг,
написанных Булгаковым М.А. и Достоевским Ф.М.

+---------+-----------------------+------------------+--------+--------+
| book_id | title                 | author           | price  | amount |
+---------+-----------------------+------------------+--------+--------+
| 1       | Мастер и Маргарита    | Булгаков М.А.    | 670.99 | 3      |
| 2       | Белая гвардия         | Булгаков М.А.    | 540.50 | 5      |
| 3       | Идиот                 | Достоевский Ф.М. | 460.00 | 10     |
| 4       | Братья Карамазовы     | Достоевский Ф.М. | 799.01 | 2      |
| 5       | Стихотворения и поэмы | Есенин С.А.      | 650.00 | 15     |
| 6       | Лирика                | Пастернак Б.Л.   | 518.99 | 2      |
| 7       | Черный человек        | Есенин С.А.      | 570.20 | 6      |
+---------+-----------------------+------------------+--------+--------+
*/

INSERT INTO book (title, author, price, amount)
SELECT title, author, price, amount
FROM supply
WHERE author NOT IN( 'Булгаков М.А.' ,  'Достоевский Ф.М.');

/*
Занести из таблицы supply в таблицу book только те книги, авторов которых нет в  book.
+---------+-----------------------+------------------+--------+--------+
| book_id | title                 | author           | price  | amount |
+---------+-----------------------+------------------+--------+--------+
| 1       | Мастер и Маргарита    | Булгаков М.А.    | 670.99 | 3      |
| 2       | Белая гвардия         | Булгаков М.А.    | 540.50 | 5      |
| 3       | Идиот                 | Достоевский Ф.М. | 460.00 | 10     |
| 4       | Братья Карамазовы     | Достоевский Ф.М. | 799.01 | 2      |
| 5       | Стихотворения и поэмы | Есенин С.А.      | 650.00 | 15     |
| 6       | Лирика                | Пастернак Б.Л.   | 518.99 | 2      |
+---------+-----------------------+------------------+--------+--------+
*/

INSERT INTO book (title, author, price, amount)
SELECT title, author, price, amount
FROM supply
WHERE author NOT IN (
        SELECT author
        FROM book
      );

/*
Уменьшить на 10% цену тех книг в таблице book, количество которых принадлежит интервалу от 5 до 10, включая границы.

+---------+-----------------------+------------------+--------+--------+
| book_id | title                 | author           | price  | amount |
+---------+-----------------------+------------------+--------+--------+
| 1       | Мастер и Маргарита    | Булгаков М.А.    | 670.99 | 3      |
| 2       | Белая гвардия         | Булгаков М.А.    | 486.45 | 5      |
| 3       | Идиот                 | Достоевский Ф.М. | 414.00 | 10     |
| 4       | Братья Карамазовы     | Достоевский Ф.М. | 799.01 | 2      |
| 5       | Стихотворения и поэмы | Есенин С.А.      | 650.00 | 15     |
+---------+-----------------------+------------------+--------+--------+
*/

UPDATE book
SET price = 0.9 * price
WHERE amount BETWEEN 5 AND 10 ;

SELECT * FROM book;

/*
В таблице book необходимо скорректировать значение для покупателя в столбце buy таким образом, чтобы оно не превышало
количество экземпляров книг, указанных в столбце amount. А цену тех книг, которые покупатель не заказывал, снизить
на 10%.

+---------+-----------------------+------------------+--------+--------+-----+
| book_id | title                 | author           | price  | amount | buy |
+---------+-----------------------+------------------+--------+--------+-----+
| 1       | Мастер и Маргарита    | Булгаков М.А.    | 603.89 | 3      | 0   |
| 2       | Белая гвардия         | Булгаков М.А.    | 540.50 | 5      | 3   |
| 3       | Идиот                 | Достоевский Ф.М. | 460.00 | 10     | 8   |
| 4       | Братья Карамазовы     | Достоевский Ф.М. | 719.11 | 2      | 0   |
| 5       | Стихотворения и поэмы | Есенин С.А.      | 650.00 | 15     | 15  |
+---------+-----------------------+------------------+--------+--------+-----+
*/

UPDATE book
SET buy = IF(buy > amount, amount, buy),
    price = IF(buy=0, 0.9*price, price);

SELECT * FROM book;