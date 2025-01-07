shopping_list = []

print("Welcome to our shopping list manager")
print("Please choose in the options below:")
print("A. add item")
print("B. remove item")
print("C. display items")
print("D. EXIT")

def add_item():
    user_input = input("Enter the name of the item you want to add: ").capitalize()
    shopping_list.append(user_input)
    

def remove_item():
    user_input = input("Enter the name of the item you want to remove: ").capitalize()
    if user_input in shopping_list:
        shopping_list.remove(user_input)
        print("The item has been removed successfully")
    else:
        print("The item you are trying to remove is not in our shopping list")
    

def display_menu():
    print(shopping_list)

def exit_app():
    print("Thank you for shopping with us. we will be happy seeing you coming back")
    quit()

while True:
    user_choice = input("Choose in the options above: ").upper()

    if user_choice == "A":
        add_item()
    if user_choice == "B":
        remove_item()
    if user_choice == "C":
        display_menu()
    if user_choice == "D":
        exit_app()
    print("done, thank you!")

