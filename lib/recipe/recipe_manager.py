class RecipeManager:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def get_recipe_by_ingredient(self, ingredient):
        return [recipe for recipe in self.recipes if ingredient in recipe.ingredients]
