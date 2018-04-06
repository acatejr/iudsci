-- Assignment 3

-- Problem 1
-- Consider the scenario from Problem 2 of Assignment 1, where you designed an
-- ER diagram for a company database. Write SQL statements to create the corresponding
-- relations and capture as many of the constraints as possible.

CREATE TABLE Professor(
    ssn INTEGER NOT NULL,
    PRIMARY KEY(ssn)
);

CREATE TABLE Course(
    courseid INTEGER NOT NULL,    
    PRIMARY KEY(courseid)
);

CREATE TABLE Teaches (
    id INTEGER NOT NULL,
    ssn INTEGER NOT NULL,
    courseid INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (ssn) REFERENCES Professor(ssn),
    FOREIGN KEY (courseid) REFERENCES Course(courseid)
);

-- Problem 2
-- Consider the scenario from slide 15 of Day 2, where you designed an ER diagram
-- for a university library. Write SQL statements to create the corresponding relations and
-- capture as many of the constraints as possible.
drop table if exists borrows;
drop table if exists has;
drop table if exists library;
drop table if exists book;
drop table if exists student;

CREATE TABLE Library (
    id INTEGER NOT NULL,
    l_loc VARCHAR(100),
    l_name VARCHAR(100),
    PRIMARY KEY (id)
);

CREATE TABLE Book (
    id INTEGER NOT NULL,
    b_title VARCHAR(100) NOT NULL, -- We at least need to know the title of the book
    b_author VARCHAR(100),
    b_edition VARCHAR(10), -- Could be a combination of ints and chars
    PRIMARY KEY (id)
);

CREATE TABLE Student (
    id INTEGER NOT NULL,
    s_name VARCHAR(100) NOT NULL,
    s_phone VARCHAR(100) NOT NULL,
    s_dob DATETIME, -- Ok to be null or empty
    PRIMARY KEY (id)
);

CREATE TABLE Has (
   id INTEGER NOT NULL,
   library_id INTEGER NOT NULL,
   book_id INTEGER NOT NULL,
   FOREIGN KEY (book_id) REFERENCES Book(id),
   FOREIGN KEY (library_id) REFERENCES Library(id),
   PRIMARY KEY (id, library_id, book_id)
);

CREATE TABLE borrows (
  id INTEGER NOT NULL,
  student_id INTEGER NOT NULL,
  book_id INTEGER NOT NULL,
  FOREIGN KEY (book_id) REFERENCES Book(id),
  FOREIGN KEY (student_id) REFERENCES Student(id),
  PRIMARY KEY (id, student_id, book_id)
);

-- Problem 3
-- Although you always wanted to be an artist, you ended up being an expert on
-- databases because you love to cook data and you somehow confused database with data
-- baste. Your old love is still there, however, so you set up a database company, ArtBase
-- that builds a product for art galleries. The core of this product is a database with a schema
-- that captures all the information that galleries need to maintain.

-- Galleries keep information about artists, their names (which are unique), birthplaces, age,
-- and style of art. 

-- For each piece of artwork, the artist, the year it was made, its unique title,
-- its type of art (e.g., painting, lithograph, sculpture, photograph), and its price must be
-- stored. 

-- Pieces of artwork are also classified into groups of various kinds, 
-- For example, portraits, still lives, works by Picasso, or works of the 19th century; 
-- A given piece may belong to more than one group. 
-- Each group is identified by a name (like those just given) that describes the group. 

-- Finally, galleries keep information about customers. For each customer, galleries 
-- keep that person’s unique name, address, total amount of dollars spent in the 
-- gallery (very important!), and the artists and groups of art that the customer
-- tends to like.

-- Draw an ER diagram for the database. Write SQL statements to create the corresponding
-- relations and capture as many of the constraints as possible.

-- To complete this problem I used MySQL Workbench ERD Designer and exported the ERD diagram 
-- to a pdf file for your review.  I also exported the diagram to sql which is included below.

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

