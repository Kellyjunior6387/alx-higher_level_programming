-- Converts database to UTF8
USE `hbtn_0C_0`
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utfmb4_unicode_ci;
