-- INSERT INTO users (user_id, username, password_hash, avatar_path)
-- VALUES (
--         512,
--         'heisenberg',
--         'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3',
--         'avatars\512'
--        )

-- UPDATE users SET chats = chats || 8812 WHERE username = 'heisenberg';

-- UPDATE chats SET users_id = users_id || '{512, 4713}'
-- INSERT INTO chat8812 (chat_id, sender_id, content)
-- VALUES (8812, 512, 'Да');
-- ALTER TABLE chat8812 ADD COLUMN readed int8[] DEFAULT '{}'::int8[];
-- ALTER TABLE chats ADD  COLUMN users_send boolean DEFAULT true;
-- ALTER TABLE chats RENAME COLUMN username TO name;
INSERT INTO chats (name, users_id, admins_id, open, users_invite, avatar_path, created_by, users_send)
VALUES ('sdf', '{512}'::int8[], '{512}'::int8[], True, True,
        'sdf', 512, True);