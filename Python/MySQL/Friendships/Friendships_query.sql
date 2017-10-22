SELECT users.first_name, users.last_name, friendships.user_id, friendships.friend_id, users2.first_name AS friend_first_name, users2.last_name AS friend_last_name FROM users
LEFT JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users AS users2 ON users2.id = friendships.friend_id
WHERE friendships.user_id = 1 OR friendships.friend_id = 1