def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            user_input = input("Enter the name of the item you want to add: ").capitalize()
            shopping_list.append(user_input)

        elif choice == '2':
            # Prompt for and remove an item
            user_input = input("Enter the name of the item you want to remove: ").capitalize()
            if user_input in shopping_list:
                shopping_list.remove(user_input)
                print("The item has been removed successfully")
            else:
                print("The item you are trying to remove is not in our shopping list")

        elif choice == '3':
            # Display the shopping list
            print(shopping_list)

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
