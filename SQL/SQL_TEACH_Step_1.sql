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

*/