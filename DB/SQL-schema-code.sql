CREATE TABLE Cocktail (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    glass VARCHAR(100),
    image VARCHAR(255),
    recipe TEXT
);

CREATE TABLE Ingredient (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE Cocktail_Ingredient (
    cocktail_id INT,
    ingredient_id INT,
    amount VARCHAR(50),
    PRIMARY KEY (cocktail_id, ingredient_id),
    FOREIGN KEY (cocktail_id) REFERENCES Cocktail(id),
    FOREIGN KEY (ingredient_id) REFERENCES Ingredient(id)
);

CREATE TABLE Cocktail_Category (
    cocktail_id INT,
    category VARCHAR(100) NOT NULL,
    PRIMARY KEY (cocktail_id, category),
    FOREIGN KEY (cocktail_id) REFERENCES Cocktail(id)
);