# ------------------------------------------------------------------------------
# A DIALOG SYSTEM FOR ORDERING PIZZA
#
# by | Oskar Garcia OG2236 |
# Columbia University | ENGIE1006 | Spring 2019
# Project2 – V.1.0
# ______________________________________________________________________________


#
# -- Toppings function


def toppings():

    topping = ""  # -- Stores current topping choice
    toppings_list = []  # -- Collects current pizza's toppings
    spacer = " and "  # -- Serves as a spacer for the return value
    available_toppings = ["pepperoni", "mushrooms", "spinach"]

    while topping != "done":

        topping = input("\nAdd a topping: pepperoni, mushrooms,"
                        " spinach,\nor say 'done':\n")

        if topping in available_toppings:
            toppings_list.append(topping)

        elif topping != "done":  # -- Handles input errors
            print("\nPlease enter one of the available toppings!")

    return spacer.join(toppings_list)  # -- Returns string with toppings


#
# -- Pizza function


def pizza():

    pizza_size = ""  # -- Stores pizza size
    available_sizes = ["small", "medium", "large"]

    while pizza_size not in available_sizes:

        pizza_size = input("\nChoose small, medium, or large?:\n")

        if pizza_size not in available_sizes:  # -- Handles input error
            print("\nPlease select one of the available sizes!")

    pizza_toppings = toppings()

    return "{0} pizza with {1}".format(pizza_size, pizza_toppings)


#
# -- Dressing function


def dressing():

    dressing_flavor = ""  # -- Stores dressing choice
    available_dressings = ["vinaigrette", "ranch", "blue cheese", "lemon"]

    while dressing_flavor not in available_dressings:

        dressing_flavor = input("\nplease choose a dressing: vinaigrette,"
                                " ranch,\nblue cheese, or lemon:\n")

        if dressing_flavor not in available_dressings:  # -- Handles input error
            print("\nPlease select one of the available dressings!")

    return dressing_flavor


#
# -- Salad function


def salad():

    salad_type = ""  # -- Stores salad choice
    available_salads = ["garden", "greek"]

    while salad_type not in available_salads:

        salad_type = input("\nWould you like a garden salad or greek salad?\n")

        if salad_type not in available_salads:  # -- Handles input error
            print("\nPlease select one of the available salads!")

    dressing_choice = dressing()

    return "{0} salad with {1} dressing".format(salad_type, dressing_choice)


#
# -- Select meal function


def select_meal():

    dish_type = ""  # -- Stores current dish selection
    pizza_list = []  # -- Collects pizza orders
    salad_list = []  # -- Collects salad orders
    dish_choices = ["pizza", "salad"]

    print("\n|| Welcome to Ristoranti del Diavolo ||\n")

    while dish_type != "done":

        dish_type = input("Would you like pizza or salad?\n")

        if dish_type in dish_choices:

            if dish_type == "pizza":  # -- Handles pizza processing
                pizza_list.append(pizza())

            elif dish_type == "salad":
                salad_list.append(salad())  # -- Handles salad processing

            print("\nYou have ordered:\n")  # -- Outputs order status

            for i in pizza_list:
                print("– A {0}".format(i))

            for i in salad_list:
                print("– A {0}".format(i))

            print("\nPlease place another order or say 'done':")

        elif dish_type != "done":  # -- Handles input errors
            print("\nPlease select one of the available dishes!\n")

    print("\nYour order has been placed. Goodbye.--")


#
# -- Testing framework

select_meal()
