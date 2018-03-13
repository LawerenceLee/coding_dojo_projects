SELECT users.first_name, users.last_name, friend.first_name as friend_first_name, friend.last_name as friend_last_name  FROM users
LEFT JOIN friendships ON friendships.user_id = users.id
LEFT JOIN users as friend ON friendships.friend_id = friend.id
ORDER BY friend_last_name DESC;

