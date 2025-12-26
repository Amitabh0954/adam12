DELETE FROM cart_item
WHERE cart_id = (SELECT id FROM cart WHERE user_id = ?) AND product_id = ?;