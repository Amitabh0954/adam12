ALTER TABLE products ADD COLUMN is_deleted BOOLEAN DEFAULT FALSE NOT NULL;

#### 6. Ensure this feature works by initializing it in the application