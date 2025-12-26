UPDATE product
SET name = ?, price = ?, description = ?, updated_at = CURRENT_TIMESTAMP
WHERE id = ?;