-- Check if the user user_0d_1 already exists
SELECT COUNT(*) INTO @user_exists FROM mysql.user WHERE User = 'user_0d_1';

-- Create user_0d_1 if it doesn't exist
IF @user_exists = 0 THEN
    CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
END IF;

-- Grant all privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Flush privileges to apply changes
FLUSH PRIVILEGES;

