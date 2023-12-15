class Recipe:
    def __init__(self, name, instructions):
        self.name = name
        self.instructions = instructions
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

