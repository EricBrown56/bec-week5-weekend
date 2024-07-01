CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    availability BOOLEAN DEFAULT 1
);

CREATE DATABASE library_system;
USE library_system;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL,
    email VARCHAR(250) NOT NULL UNIQUE
);

CREATE TABLE borrowed_books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    borrow_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);

ALTER TABLE borrowed_books
DROP COLUMN borrow_date;

ALTER TABLE borrowed_books
ADD COLUMN borrow_date TIMESTAMP;

ALTER TABLE borrowed_books
DROP COLUMN return_date;

ALTER TABLE borrowed_books
ADD COLUMN return_date TIMESTAMP;

INSERT INTO books (title)
VALUES ('Animal Farm'), ('Don Quixote'), ('Pride and prejudice'),
('To Kill a Mockingbird'), ('The Odyssey');

SELECT * FROM books;

INSERT INTO users (user_name, email)
VALUES ('Eric', 'eric@eric.com'),
('Brian', 'brian@brain.com'),
('Marco', 'marco@marco.com');

SELECT * FROM users;

SELECT * FROM borrowed_books;