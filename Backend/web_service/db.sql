CREATE TABLE `Article` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `title` varchar(255),
  `url` varchar(255) NOT NULL,
  `image_url` varchar(255),
  `summary` varchar(255),
  `category` varchar(255)
);