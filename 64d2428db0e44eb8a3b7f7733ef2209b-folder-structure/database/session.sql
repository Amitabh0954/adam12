# Epic Title: User Account Management

CREATE TABLE sessions (
    session_id VARCHAR(255) PRIMARY KEY,
    user_id INT NOT NULL,
    created_at DATETIME NOT NULL,
    last_accessed_at DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (user_id)
);