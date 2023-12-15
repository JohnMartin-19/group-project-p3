--this table join establish the relationship between tables
CREATE TABLE recipe_ingredients (
  recipe_id INT REFERENCES recipes(id),
  ingredient_id INT REFERENCES ingredients(id),
  PRIMARY KEY (recipe_id, ingredient_id)
);