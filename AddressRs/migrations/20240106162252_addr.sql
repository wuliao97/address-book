-- Add migration script here
CREATE TABLE IF NOT EXISTS address(
    name TEXT PRIMARY KEY NOT NULL,
    phone_number TEXT NOT NULL,
    address_line TEXT NOT NULL,
    city TEXT NOT NULL,
    region TEXT NOT NULL,
    country TEXT NOT NULL,
    post_code TEXT NOT NULL
);