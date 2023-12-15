--creating a table for recipes and ingredients
CREATE TABLE recipes (
  id SERIAL PRIMARY KEY,
  name VARCHAR NOT NULL,
  instructions TEXT,
);

CREATE TABLE ingredients (
  id SERIAL PRIMARY KEY,
  name VARCHAR NOT NULL,

);

--Inserting data inot the table
INSERT INTO recipes (name, instructions) VALUES ('Pasta', 'Boil pasta, add sauce.');
INSERT INTO ingredients (name) VALUES ('Pasta'), ('Sauce');
INSERT INTO recipe_ingredients (recipe_id, ingredient_id) VALUES (1, 1), (1, 2);


--to retireve data using queries e.g get recipes with their ingredients
SELECT recipes.name AS recipe_name, ingredients.name AS ingredient_name
FROM recipes
JOIN recipe_ingredients ON recipes.id = recipe_ingredients.recipe_id
JOIN ingredients ON recipe_ingredients.ingredient_id = ingredients.id;
