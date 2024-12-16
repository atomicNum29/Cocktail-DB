CREATE TABLE Cocktail (
    cocktail_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    glass VARCHAR(100),
    image_url VARCHAR(255),
    recipe TEXT
);

CREATE TABLE Ingredient (
    ingredient_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE Cocktail_Ingredient (
    cocktail_id INT,
    ingredient_id INT,
    amount VARCHAR(50),
    PRIMARY KEY (cocktail_id, ingredient_id),
    FOREIGN KEY (cocktail_id) REFERENCES Cocktail(cocktail_id),
    FOREIGN KEY (ingredient_id) REFERENCES Ingredient(ingredient_id)
);

CREATE TABLE Cocktail_Category (
    cocktail_id INT,
    category_name VARCHAR(100) NOT NULL,
    PRIMARY KEY (cocktail_id, category_name),
    FOREIGN KEY (cocktail_id) REFERENCES Cocktail(cocktail_id)
);