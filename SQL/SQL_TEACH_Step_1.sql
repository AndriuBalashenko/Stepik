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