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

### Step 4: Update `app.py` to register the profile controller blueprint: