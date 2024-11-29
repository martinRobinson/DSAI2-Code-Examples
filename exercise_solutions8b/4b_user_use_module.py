from user import Admin

albert = Admin("albert", "einstein", "ramelton")
albert.describe_user()

albert_privileges = [
    "can reset passwords",
    "can moderate discussions",
    "can suspend accounts",
]
albert.privileges = albert_privileges

print(f"\nThe admin {albert.username} has these privileges: ")
albert.show_privileges()
