import random

FILE_NAME = "games.txt"


def load_games():
    try:
        with open(FILE_NAME, "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []


def add_game():
    print("\nChoose category:")
    print("1. Action")
    print("2. open world")
    print("3. Sports")
    print("4. Shooting")

    choice = input("Choose category: ")

    if choice == "1":
        category = "Action"
    elif choice == "2":
        category = "open world"
    elif choice == "3":
        category = "Sports"
    elif choice == "4":
        category = "Shooting"
    else:
        print("Invalid choice.")
        return

    game = input("Enter game name: ")

    if game.upper() == "Q":
        return

    with open(FILE_NAME, "a") as f:
        f.write(f"{game},{category}\n")

    print("Game added successfully!")


def recommend():
    games = load_games()

    if not games:
        print("No games found. Please add some games first.")
        return

    print("\nChoose category:")
    print("1. Action")
    print("2. open world")
    print("3. Sports")
    print("4. Shooting")

    choice = input("Choose a category: ")

    if choice == "1":
        category = "Action"
    elif choice == "2":
        category = "open world"
    elif choice == "3":
        category = "Sports"
    elif choice == "4":
        category = "Shooting"
    else:
        print("Invalid choice.")
        return

    filtered = []

    for game in games:
        name, cat = game.split(",")
        name = name.strip()
        cat = cat.strip()

        if cat.lower() == category.lower():
            filtered.append(name)

    if not filtered:
        print(f"No games found in category '{category}'.")
        return

    game = random.choice(filtered)
    print(f"Recommended game: {game}")


def main():
    while True:
        print("\n===== Game System =====")
        print("1. Add game")
        print("2. Recommend game")
        print("Q. Quit")

        choice = input("Choose: ")

        if choice == "1":
            add_game()

        elif choice == "2":
            recommend()

        elif choice.upper() == "Q":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


main()