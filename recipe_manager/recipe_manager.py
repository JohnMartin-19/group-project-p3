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
        self.ingredients.remove(ingredredient)
class RecipeManager:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def get_recipe_by_ingredient(self, ingredient):
        return [recipe for recipe in self.recipes if ingredient in recipe.ingredients]