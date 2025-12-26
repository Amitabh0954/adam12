CREATE TABLE product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL,
    price REAL NOT NULL CHECK (price > 0),
    category_id INTEGER NOT NULL,
    FOREIGN KEY (category_id) REFERENCES category (id) ON DELETE CASCADE
);