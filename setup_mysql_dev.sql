-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS ME_db;
CREATE USER IF NOT EXISTS 'melani_dev'@'localhost' IDENTIFIED BY 'Mel0ni_dev_123';
GRANT ALL PRIVILEGES ON `ME_db`.* TO 'melani_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'melani_dev'@'localhost';
FLUSH PRIVILEGES;