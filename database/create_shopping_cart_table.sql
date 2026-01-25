CREATE TABLE shopping_cart (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE shopping_cart_item (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cart_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (cart_id) REFERENCES shopping_cart (id),
    FOREIGN KEY (product_id) REFERENCES products (id)
);

#### 8. Update requirements.txt