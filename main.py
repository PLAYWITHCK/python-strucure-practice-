from ui import show_menu, get_user_choice
from logic import add_expense, calculate_total, show_expenses

def main():
    expenses = []

    while True:
        show_menu()
        choice = get_user_choice()

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            show_expenses(expenses)

        elif choice == "3":
            total = calculate_total(expenses)
            print(f"Total expenses: {total}")

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
