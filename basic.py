from config import User


def main():
    print(
        """===== Welcome to CRM Application =====
[S]how: Show all users info
[A]dd: Add new user
[Q]uit: Quit application
======================================"""
    )

    while True:
        choice = input("Your command > ")
        cmd = choice.upper()
        if cmd == "S":
            show()
        elif cmd == "A":
            add()
        elif cmd == "Q":
            print("Bye!")
            exit()
        else:
            print(f"{choice}: command not found")
        print("")


def show():
    for user in User.select():
        print(f"Name: {user.name} Age: {user.age}")


def add():
    name = input("New user name > ")
    age = input("New user age > ")

    user = User.create(name=name, age=age)
    print(f"Add new user: {user.name}")


if __name__ == "__main__":
    main()
