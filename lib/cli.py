from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Recipe, MealPlan
from datetime import datetime, timedelta

# Replace 'sqlite:///meal_planner.db' with the appropriate database connection string
engine = create_engine('sqlite:///meal_planner.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def create_user(username, email):
    user = User(username=username, email=email)
    session.add(user)
    session.commit()
    return user

def create_recipe(name, ingredients, instructions):
    recipe = Recipe(name=name, ingredients=ingredients, instructions=instructions)
    session.add(recipe)
    session.commit()
    return recipe

def generate_meal_plan(user, date, recipes):
    for recipe in recipes:
        meal_plan_entry = MealPlan(user=user, recipe=recipe, date=date)
        session.add(meal_plan_entry)
    session.commit()

def main():
    print("Welcome to the Meal Plan Generator CLI!")

    # Get user input
    username = input("Enter your username: ")
    email = input("Enter your email: ")
    user = create_user(username, email)

    print("\nAvailable Recipes:")
    # You should have a list of predefined recipes or fetch them from a database
    recipe_data = [
        {"name": "Spaghetti Bolognese", "ingredients": "Pasta, Meat, Tomato Sauce", "instructions": "Cook pasta, brown meat, add sauce."},
        {"name": "Chicken Stir-Fry", "ingredients": "Chicken, Vegetables, Soy Sauce", "instructions": "Stir-fry chicken and vegetables, add soy sauce."},
        # Add more recipes as needed
    ]

    recipes = []
    for data in recipe_data:
        recipe = create_recipe(data["name"], data["ingredients"], data["instructions"])
        recipes.append(recipe)
        print(f"- {data['name']}")

    # Generate a meal plan for the next 7 days
    today = datetime.now().date()
    for i in range(7):
        date = today + timedelta(days=i)
        print(f"\nGenerating Meal Plan for {date}...")
        generate_meal_plan(user, date, recipes)
        print("Meal Plan generated successfully!")

if __name__ == "__main__":
    main()
