# Epic Title: User Account Management

CREATE TABLE password_reset_requests (
    request_id VARCHAR(255) PRIMARY KEY,
    user_id INT NOT NULL,
    created_at DATETIME NOT NULL,
    expires_at DATETIME NOT NULL,
    is_used BOOLEAN NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (user_id)
);