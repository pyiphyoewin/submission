CREATE TABLE User (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);


CREATE TABLE Product (
    id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    available_date DATE NOT NULL,
    stock_quantity INT NOT NULL,
    image_url VARCHAR(255),
    category ENUM('Apparel', 'Accessories', 'Home', 'Tech', 'Beauty', 'Food', 'Others') NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE CustomizedProduct (
    id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    available_date DATE NOT NULL,
    stock_quantity INT NOT NULL,
    image_url VARCHAR(255),
    category ENUM('Apparel', 'Accessories', 'Home', 'Tech', 'Beauty', 'Food', 'Others') NOT NULL,
    brand VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE PromotionalProduct (
    id INT NOT NULL AUTO_INCREMENT,
    base_product_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (base_product_id) REFERENCES CustomizedProduct(id)
);

CREATE TABLE MicroStore (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    user_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES User(id)
);

CREATE TABLE MicroStore_Product (
    id INT NOT NULL AUTO_INCREMENT,
    micro_store_id INT NOT NULL,
    product_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (micro_store_id) REFERENCES MicroStore(id),
    FOREIGN KEY (product_id) REFERENCES PromotionalProduct(id)
);

CREATE TABLE Storefront (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    user_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES User(id)
);

CREATE TABLE Storefront_Product (
    id INT NOT NULL AUTO_INCREMENT,
    storefront_id INT NOT NULL,
    product_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (storefront_id) REFERENCES Storefront(id),
    FOREIGN KEY (product_id) REFERENCES CustomizedProduct(id)
);
