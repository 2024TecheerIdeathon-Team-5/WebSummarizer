CREATE TABLE `Bookmark` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `title` varchar(255),
  `url` varchar(255) NOT NULL,
  `summary` text,
  `category_id` int
);

CREATE TABLE `Category` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255),
  `parent_id` int
);

ALTER TABLE `Bookmark` ADD FOREIGN KEY (`category_id`) REFERENCES `Category` (`id`);

ALTER TABLE `Category` ADD FOREIGN KEY (`parent_id`) REFERENCES `Category` (`id`);
