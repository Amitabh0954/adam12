CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    login_attempts INTEGER DEFAULT 0 NOT NULL
);

CREATE TABLE session (
    session_id TEXT PRIMARY KEY,
    data TEXT,
    expiry INTEGER
);