UPDATE cart_item
SET quantity = ?, added_at = CURRENT_TIMESTAMP
WHERE cart_id = (SELECT id FROM cart WHERE user_id = ?) AND product_id = ?;