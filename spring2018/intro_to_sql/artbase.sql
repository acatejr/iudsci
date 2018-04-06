-- MySQL Script generated by MySQL Workbench
-- Fri Apr  6 10:56:27 2018
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema testdb
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `testdb` ;

-- -----------------------------------------------------
-- Schema testdb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `testdb` DEFAULT CHARACTER SET utf8 ;
USE `testdb` ;

-- -----------------------------------------------------
-- Table `testdb`.`Artists`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `testdb`.`Artists` ;

CREATE TABLE IF NOT EXISTS `testdb`.`Artists` (
  `id` INT NOT NULL,
  `name` VARCHAR(200) NULL,
  `birthplace` VARCHAR(200) NULL,
  `age` INT NULL,
  `art_tile` VARCHAR(75) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `testdb`.`ArtWork`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `testdb`.`ArtWork` ;

CREATE TABLE IF NOT EXISTS `testdb`.`ArtWork` (
  `id` INT NOT NULL,
  `artist_id` INT NULL,
  `year_made` INT NULL,
  `title` VARCHAR(200) NULL,
  `type` VARCHAR(45) NULL,
  `price` REAL NULL,
  PRIMARY KEY (`id`),
  INDEX `artist_id_idx` (`artist_id` ASC),
  UNIQUE INDEX `title_UNIQUE` (`title` ASC),
  CONSTRAINT `artist_id`
    FOREIGN KEY (`artist_id`)
    REFERENCES `testdb`.`Artists` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `testdb`.`ArtWorkGroups`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `testdb`.`ArtWorkGroups` ;

CREATE TABLE IF NOT EXISTS `testdb`.`ArtWorkGroups` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `testdb`.`BelongsTo`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `testdb`.`BelongsTo` ;

CREATE TABLE IF NOT EXISTS `testdb`.`BelongsTo` (
  `id` INT NOT NULL,
  `artwork_id` INT NOT NULL,
  `group_id` INT NOT NULL,
  PRIMARY KEY (`id`, `artwork_id`, `group_id`),
  INDEX `artwork_id_idx` (`artwork_id` ASC),
  INDEX `group_id_idx` (`group_id` ASC),
  CONSTRAINT `artwork_id`
    FOREIGN KEY (`artwork_id`)
    REFERENCES `testdb`.`ArtWork` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `group_id`
    FOREIGN KEY (`group_id`)
    REFERENCES `testdb`.`ArtWorkGroups` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'i';


-- -----------------------------------------------------
-- Table `testdb`.`Customers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `testdb`.`Customers` ;

CREATE TABLE IF NOT EXISTS `testdb`.`Customers` (
  `id` INT NOT NULL,
  `name` VARCHAR(200) NULL,
  `address` VARCHAR(200) NULL,
  `total_money_spent` REAL NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `testdb`.`LikesGroups`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `testdb`.`LikesGroups` ;

CREATE TABLE IF NOT EXISTS `testdb`.`LikesGroups` (
  `id` INT NOT NULL,
  `customer_id` INT NOT NULL,
  `group_id` INT NOT NULL,
  PRIMARY KEY (`id`, `customer_id`, `group_id`),
  INDEX `group_id_idx` (`group_id` ASC),
  INDEX `customer_id_idx` (`customer_id` ASC),
  CONSTRAINT `group_id`
    FOREIGN KEY (`group_id`)
    REFERENCES `testdb`.`ArtWorkGroups` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `customer_id`
    FOREIGN KEY (`customer_id`)
    REFERENCES `testdb`.`Customers` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `testdb`.`LikesArtists`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `testdb`.`LikesArtists` ;

CREATE TABLE IF NOT EXISTS `testdb`.`LikesArtists` (
  `id` INT NOT NULL,
  `customer_id` INT NOT NULL,
  `artist_id` INT NOT NULL,
  PRIMARY KEY (`id`, `customer_id`, `artist_id`),
  INDEX `customer_id_idx` (`customer_id` ASC),
  INDEX `artist_id_idx` (`artist_id` ASC),
  CONSTRAINT `customer_id`
    FOREIGN KEY (`customer_id`)
    REFERENCES `testdb`.`Customers` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `artist_id`
    FOREIGN KEY (`artist_id`)
    REFERENCES `testdb`.`Artists` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
