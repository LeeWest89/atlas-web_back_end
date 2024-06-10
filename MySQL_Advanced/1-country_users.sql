-- creates a table users now with country data
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country VARCHAR(2) NOT NULL DEFAULT 'US',
    CONSTRAINT country_check CHECK (country IN ('US', 'CO', 'TN'))
);

ALTER TABLE users
ADD COLUMN country VARCHAR(2) NOT NULL DEFAULT 'US',
ADD CONSTRAINT country_check CHECK (country IN ('US', 'CO', 'TN'));