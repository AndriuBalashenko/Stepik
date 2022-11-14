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