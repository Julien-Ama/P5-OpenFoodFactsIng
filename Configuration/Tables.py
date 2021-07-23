

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Table product

CREATE TABLE IF NOT EXISTS `product`
(
`id` INT(11) NOT NULL AUTO_INCREMENT,
`brands` VARCHAR(80) NOT NULL,
`code` varchar(80) NOT NULL,
`nutriscore_grade` VARCHAR(5) NOT NULL,
`product_name_fr` VARCHAR(950) NOT NULL,
`stores` varchar(255) NOT NULL,
`url` VARCHAR(255) NOT NULL,
`categories` varchar(950) NOT NULL ,

PRIMARY KEY(`id`)
)
ENGINE = MyISAM
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

# Table favorite

CREATE TABLE IF NOT EXISTS `favorite`
(
`id` INT(11) NOT NULL AUTO_INCREMENT,
`brands` VARCHAR(80) NOT NULL,
`nutriscore_grade` VARCHAR(5) NOT NULL,
`stores` varchar(255) NOT NULL,
`code` varchar(80) NOT NULL,
`url` VARCHAR(255) NOT NULL,

PRIMARY KEY(`id`)
);

# Table category

CREATE TABLE IF NOT EXISTS `category`
(
`id` INT(11) NOT NULL AUTO_INCREMENT,
`categories` VARCHAR(950) NOT NULL,

PRIMARY KEY(`id`)
);

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
