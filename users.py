class User:
    def __init__(self, user_id, name, age, email):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.email = email

    def __repr__(self):
        return f"User({self.user_id}, {self.name}, {self.age}, {self.email})"

    def __str__(self):
        return f"User ID: {self.user_id}\nName: {self.name}\nAge: {self.age}\nEmail: {self.email}"

# Sample data for 25 users
users_data = [
    {"id": 1, "name": "Abdullahi Sabtow", "age": 33, "email": "yantiranchez@gmail.com"},
    {"id": 2, "name": "Salim Bokhsan", "age": 29, "email": "salim@gmail.com.com"},
    {"id": 3, "name": "Charlie", "age": 28, "email": "charlie@example.com"},
    {"id": 4, "name": "David", "age": 22, "email": "david@example.com"},
    {"id": 5, "name": "Eva", "age": 27, "email": "eva@example.com"},
    {"id": 6, "name": "Frank", "age": 31, "email": "frank@example.com"},
    {"id": 7, "name": "Grace", "age": 29, "email": "grace@example.com"},
    {"id": 8, "name": "Hannah", "age": 26, "email": "hannah@example.com"},
    {"id": 9, "name": "Ian", "age": 24, "email": "ian@example.com"},
    {"id": 10, "name": "Jack", "age": 32, "email": "jack@example.com"},
    {"id": 11, "name": "Katie", "age": 23, "email": "katie@example.com"},
    {"id": 12, "name": "Liam", "age": 28, "email": "liam@example.com"},
    {"id": 13, "name": "Mia", "age": 30, "email": "mia@example.com"},
    {"id": 14, "name": "Nora", "age": 29, "email": "nora@example.com"},
    {"id": 15, "name": "Oliver", "age": 27, "email": "oliver@example.com"},
    {"id": 16, "name": "Penny", "age": 25, "email": "penny@example.com"},
    {"id": 17, "name": "Quinn", "age": 26, "email": "quinn@example.com"},
    {"id": 18, "name": "Ryan", "age": 31, "email": "ryan@example.com"},
    {"id": 19, "name": "Samantha", "age": 24, "email": "samantha@example.com"},
    {"id": 20, "name": "Tyler", "age": 28, "email": "tyler@example.com"},
    {"id": 21, "name": "Uma", "age": 29, "email": "uma@example.com"},
    {"id": 22, "name": "Vincent", "age": 30, "email": "vincent@example.com"},
    {"id": 23, "name": "Wendy", "age": 31, "email": "wendy@example.com"},
    {"id": 24, "name": "Xander", "age": 26, "email": "xander@example.com"},
    {"id": 25, "name": "Yara", "age": 27, "email": "yara@example.com"},
]

# Create a list of User objects using the sample data
users = [User(data["id"], data["name"], data["age"], data["email"]) for data in users_data]

def display_all_users(user_list):
    for user in user_list:
        print(user)
        
if __name__ == "__main__":
    # Display all users
    display_all_users(users)

class user_Manager:
    def __init__(self):
        self.user = []

    # def add_user(self, user):
    #     self.users.append(user)

    # def get_user_by_ingredient(self, ingredient):
    #     return [user for user in self.user if ingredient in user.ingredients]

    # def get_user_by_category(self, category):
    #     return [user for user in self.users if category in user.categories]
    
    # def get_users_by_tag(self, tag):
    #     return [user for user in self.users if tag in user.tags]

class user_App:
    def __init__(self):
        self.users = []

    def create_user(self, username, password):
        new_user = User(username, password)
        self.users.append(new_user)
        return new_user

    def authenticate_user(self, username, password):
        return next((user for user in self.users if user.username == username and user.password == password), None)    

