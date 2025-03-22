CREATE TABLE IF NOT EXISTS users(
    user_id SERIAL8 PRIMARY KEY,
    username text UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    avatar_path VARCHAR(255) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    last_login TIMESTAMPTZ NOT NULL
);

CREATE TABLE IF NOT EXISTS chats(
    chat_id SERIAL8 PRIMARY KEY,
    users_id int8[],
    admins_id int8[],
    open bool DEFAULT FALSE,
    users_Invite bool DEFAULT FALSE,
    avatar_path VARCHAR(255),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by SERIAL8
)