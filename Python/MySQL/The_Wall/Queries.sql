SELECT * FROM users
LEFT JOIN messages ON messages.user_id = users.id
LEFT JOIN comments ON comments.user_id = users.id;

INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (1, "This is my message.", NOW(), NOW());

INSERT INTO comments (message_id, user_id, comment, created_at, updated_at) VALUES (1, 1, "This is a comment.", NOW(), NOW())