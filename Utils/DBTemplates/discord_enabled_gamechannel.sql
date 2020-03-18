/*
DESCRIBE `discord_enabled_gamechannel`;

+------------+--------------+------+-----+---------+----------------+
| Field      | Type         | Null | Key | Default | Extra          |
+------------+--------------+------+-----+---------+----------------+
| id         | int(11)      | NO   | PRI | NULL    | auto_increment |
| guild_id   | varchar(128) | NO   | MUL | NULL    |                |
| channel_id | varchar(128) | NO   |     | NULL    |                |
+------------+--------------+------+-----+---------+----------------+
*/

-- SHOW CREATE TABLE `discord_enabled_gamechannel`;

CREATE TABLE `discord_enabled_gamechannel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `guild_id` varchar(128) NOT NULL,
  `channel_id` varchar(128) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `entry_key` (`guild_id`,`channel_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
