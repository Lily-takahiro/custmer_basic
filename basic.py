# CRM Application


def show_menu():
    print("===== Welcome to CRM Application =====")
    print("[S]how: Show all users info")
    print("[A]dd: Add new user")
    print("[Q]uit: Quit The Application")
    print("======================================")


def show_users(users):
    if not users:
        print("No users found.")
    else:
        for user in users:
            print(f"Name: {user['name']} Age: {user['age']}")


def add_user(users):
    name = input("New user name > ").strip()
    age_input = input("New user age > ").strip()
    if not age_input.isdigit():
        print("Invalid age. Please enter a number.")
        return
    age = int(age_input)
    users.append({"name": name, "age": age})
    print(f"Add new user: {name}")


def main():
    users = [{"name": "Bob", "age": 15}, {"name": "Tom", "age": 57}, {"name": "Ken", "age": 73}]

    while True:
        show_menu()
        command = input("Your command > ").strip().upper()

        if command == "S":
            show_users(users)
        elif command == "A":
            add_user(users)
        elif command == "Q":
            print("Bye!")
            break
        else:
            print(f"{command.lower()}: command not found")


if __name__ == "__main__":
    main()
