class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.recipe_manager = RecipeManager()

class Recipe:
    def __init__(self, name, instructions):
        self.name = name
        self.instructions = instructions
        self.ingredients = []
        self.categories = []
        self.tags = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
    def remove_ingredient(self, ingredient):
        self.ingredients.remove(ingredient)
    def add_tag(self, tag):
        self.tags.append(tag)
    def add_category(self, category):
            self.categories.append(category)


class RecipeManager:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def get_recipe_by_ingredient(self, ingredient):
        return [recipe for recipe in self.recipes if ingredient in recipe.ingredients]

    def get_recipes_by_category(self, category):
        return [recipe for recipe in self.recipes if category in recipe.categories]
    
    def get_recipes_by_tag(self, tag):
        return [recipe for recipe in self.recipes if tag in recipe.tags]

class RecipeApp:
    def __init__(self):
        self.users = []

    def create_user(self, username, password):
        new_user = User(username, password)
        self.users.append(new_user)
        return new_user

    def authenticate_user(self, username, password):
        return next((user for user in self.users if user.username == username and user.password == password), None)    

''
recipe_app = RecipeApp()
user = recipe_app.create_user("Edda Nziza Makuyu", "siri_salama")

recipe = Recipe("Ugali", "Changanya unga na maji, chemsha hadi iwe na muundo mzito.")
recipe.add_ingredient("unga")
recipe.add_ingredient("maji")
recipe.add_category("mchana")
recipe.add_tag("kitamu")

print(f"User Created: {user.username}")

# Print information about the recipe
print(f"Recipe Created: {recipe.name}")
print(f"Instructions: {recipe.instructions}")
print(f"Ingredients: {', '.join(recipe.ingredients)}")
print(f"Categories: {', '.join(recipe.categories)}")
print(f"Tags: {', '.join(recipe.tags)}")
