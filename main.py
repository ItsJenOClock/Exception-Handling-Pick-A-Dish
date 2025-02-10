def select_dish(foods, selected_food):
    # try:
    #     selected_food < 1
    # except:

    print(f"Ah, {foods[selected_food]}! An excellent choice!")




def your_menu(foods):
    try:
        index = 1
        for dish in foods:
            print(f"{index}. {dish}")
            index += 1
    
        selected_choice = int(input("Your order number? "))        

        if selected_choice < 1:
            assert selected_choice >= 1, f"{selected_choice}"

        select_dish(foods, selected_choice - 1)
    except IndexError as error:
        print(f"IndexErorr: {error} was entered.")
        print("Next time try entering an integer on the menu!")
    except ValueError as error:
        print(f"ValueError: {error} was entered.")
        print("Next time try entering an integer on the menu!")
    except AssertionError as error:
        print(f"AssertionError: {error} was entered.")
        print("You cannot enter that number. Next time try entering an integer on the menu!")

menu_items = [
    "Yakisoba",
    "Pho Tai Nam Gan",
    "Chile Verde",
    "Swiss & Mushroom Burger",
    "Saag Paneer",
]

your_menu(menu_items)
print("Yum!")