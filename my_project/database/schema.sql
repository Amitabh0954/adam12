CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    login_attempts INTEGER DEFAULT 0 NOT NULL,
    first_name TEXT,
    last_name TEXT,
    preferences TEXT
);

CREATE TABLE session (
    session_id TEXT PRIMARY KEY,
    data TEXT,
    expiry INTEGER
);

CREATE TABLE password_reset (
    id TEXT PRIMARY KEY,
    user_id INTEGER,
    token TEXT,
    expires_at DATETIME,
    FOREIGN KEY(user_id) REFERENCES user(id)
);

CREATE TABLE category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    parent_id INTEGER,
    FOREIGN KEY(parent_id) REFERENCES category(id)
);

CREATE TABLE product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    price REAL NOT NULL,
    description TEXT NOT NULL,
    category_id INTEGER NOT NULL,
    deleted BOOLEAN NOT NULL DEFAULT 0,
    FOREIGN KEY(category_id) REFERENCES category(id)
);

CREATE TABLE shopping_cart (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    session_id TEXT,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    FOREIGN KEY(user_id) REFERENCES user(id),
    FOREIGN KEY(product_id) REFERENCES product(id)
);

### Step 4: Ensure all necessary dependencies are included (no change needed here):