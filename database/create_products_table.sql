CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL UNIQUE,
    price FLOAT NOT NULL,
    description TEXT NOT NULL
);

#### 8. Update requirements.txt for necessary packages