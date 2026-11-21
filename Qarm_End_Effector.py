##FINAL PROGRAM
import csv
import random
import bcrypt

##Main
def main():
    """The main method is responsible for taking the user through the whole ordering process. It welcomes the user and calls authenticate before moving on to the main loop of filling orders. The order filling involves calling the scan barcode function and passing its return value to the lookup products function which creates the list of products and prices used in pack products and complete order. At the end of the while loop the user is asked whether they would like to place more orders and then based on the response the program either repeats or continues to customer summary."""
    print("Welcome")#Prints a welcome message and calls authenticate before continuing
    userid = authenticate()
    done = False
    while done == False:#The for loop does the majority of the process and repeats until the user decides they are done
        products = scan_barcode()#calls the scan barcode function to get the string of products
        # products = "Sponge Labubu Bowl" - This line was sed for testing

        prods_and_prices = lookup_products(products)#passes the string of products to lookup products and gets a list of the products with corresponding prices

        pack_products(prods_and_prices)#Places the objects ordered into the destination using q arm instructions

        complete_order(userid, prods_and_prices)#completes the order using the userid and list of products with prices

        checkup = input(f"Type done to exit, type anything else to fill another order ")#checks if the user wants to fill more orders or move on to customer summary

        if checkup == "done":
            done = True

    customer_summary(userid)

##Pack Products
def pack_products(product_list):
    """The pack products function is responsible for accepting a list of items and their corresponding prices and giving the q arm instructions to pack the items while returning a message the the user that the item was successfully placed in the destination."""
    for item in product_list:#This for loop traverses the list of items that need to be packed and excecutes the q arm code needed to pack them while printing a message that says the item was packed
        if item[0]=="Sponge":
            #Sponge Q arm Code
            arm.home()
            arm.rotate_gripper(-35)
            sleep(1)
            arm.rotate_gripper(40)
            arm.set_arm_position([0.5883036640807882, 0.1721177710446971, 0.06156889264959298])
            sleep(3)
            arm.rotate_gripper(-50)
            print(f"{item[0]} packed")

        elif item[0]=="Bottle":
            #Bottle Q arm code
            arm.home()
            arm.rotate_gripper(-35)
            sleep(1)
            arm.rotate_gripper(40)
            arm.set_arm_position([0.601272611451039, 0.11915105958036404, 0.06156889264959298])
            arm.rotate_gripper(-60)
            sleep(3)
            print(f"{item[0]} packed")

        elif item[0]=="Rook":
            #Rook Q arm code
            arm.home()
            arm.rotate_gripper(-35)
            sleep(1)
            arm.rotate_gripper(30)
            arm.set_arm_position([0.5980516251425072, 0.03721167177378604, 0.038510742116851775])
            sleep(3)
            arm.rotate_gripper(-60)
            sleep(1)
            print(f"{item[0]} packed")

        elif item[0]=="D12":
            #Q arm code for the  D12
            arm.home()
            sleep(1)
            arm.rotate_gripper(35)
            arm.set_arm_position([0.5875209534147573, -0.03474686541870006, 0.0113255320119270886])
            sleep(3)
            arm.rotate_gripper(-60)
            sleep(1)
            print(f"{item[0]} packed")

        elif item[0]=="Bowl":
            #Q arm code for the bowl
            arm.home()
            sleep(1)
            arm.rotate_gripper(30)
            sleep(3)
            arm.rotate_base(-17)
            arm.rotate_elbow(-17)
            sleep(2)
            arm.rotate_shoulder(57)
            sleep(1)
            arm.rotate_gripper(-75)
            sleep(1)
            sleep(1)
            arm.rotate_shoulder(-22)
            print(f"{item[0]} packed")

        elif item[0]=="WitchHat":
            #Q arm code for the witch hat
            arm.home()
            sleep(1)
            arm.rotate_gripper(30)
            arm.set_arm_position([0.5793840561555342, -0.09735550520201432, 0.01037217084375673615])
            sleep(3)
            arm.rotate_gripper(-60)
            sleep(1)
            arm.rotate_shoulder(-22)
            print(f"{item[0]} packed")
        #Q arm code for dropping the item in the basket
        arm.set_arm_position([0.24600864530246057, -0.2780561023175753, 0.2638301473950316])
        sleep(2)
        arm.rotate_gripper(90)
        arm.home()
        arm.rotate_gripper(-90)

##Sign up
def sign_up():
    """Handles the sign up process (ie. creation of new user id and password)

    Opens a csv file of user ids and encryted passwords, and takes
    all usernames and puts them into a list. We can then use this to compare
    new userids to the list to see if userid is the same as existing users.
    if user id is eligible, user creates a password that must have an upper
    case letter, a lower case letter, a digit, and a symbol. The password
    must be at least 6 characters long. Once password is eligible, encypt the
    password. Save both the new username and password to the csv file.

    """

    file_name = "users.csv"

    # Try to open file. If not found, create with header.
    try:
        with open(file_name, "r") as f:
            pass
    except FileNotFoundError:
         open(file_name, "w").close()

    # Read existing userids
    try:
        file = open("users.csv", "r")
        userids = []
        for line in file:
            line = line.strip()
            col = line.split(",")
            userids.append(col[0].strip())
        file.close()
    except FileNotFoundError:
        print("Invalid file")

    while True:
        # Input userid
        userid = input("Enter desired userid: ").strip()

        if userid not in userids:
            break
        else:
            print("Error: That userid already exists.")

    while True:
        # Input password
        password = input("Enter password: ")

        # Validate password manually
        special_symbols = "!.@#$%^&*()_[]"

        has_upper = False
        has_lower = False
        has_digit = False
        has_symbol = False

        for ch in password:
            if ch.isupper():
                has_upper = True
            elif ch.islower():
                has_lower = True
            elif ch.isdigit():
                has_digit = True
            elif ch in special_symbols:
                has_symbol = True

        if len(password) < 6 or not (has_upper and has_lower and has_digit and has_symbol):
            print("Error: Password must be:")
            print("- at least 6 characters")
            print("- contain uppercase, lowercase, digit, and a symbol (!.@#$%^&*()_[])")
        else:
            break

    # Encrypt password with bcrypt
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt() ).decode('utf-8')

    # Save to csv
    with open(file_name, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([userid, hashed_pw])

    print("✅ Account created successfully!")

##Authenticate
def authenticate():
    '''this function opens up a csv file of user id's and passwords and reads it. It compares it to the entered passwords of the user logging in to make sure they are entering a valid id. It then returns the user id once logged in.
    '''
    user_list = []

    while True:
        print("Do you have an account?")
        choice = input("Enter yes or no: ")
        if choice == "yes" or choice == "no":
            break
        else:
            print("Invalid input")

    if choice == "no":
        sign_up()

    with open("users.csv", "r", newline="") as file: #open users.csv file and convert it to a nested list.
        users = csv.reader(file)
        for user in users:
            user_list.append(user)

    username_valid = False
    password_valid = False

    while username_valid == False or password_valid == False: #runs until the user enters a valid username and password.
        username_valid = False
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        for user in user_list:
            if user[0] == username:
                username_valid = True
                user_name = user[0]
                if bcrypt.checkpw( password.encode('utf-8'),user[1].encode('utf-8')): #compare encrypted password with users entered password.
                    password_valid = True

        if username_valid == True and password_valid == True:
            print("Success!")
        else:
            print("Incorrect Username or Passord")

    return user_name



##Lookup Products
def lookup_products(products):
    """The lookup products function is passed a string of product names and then used the products.csv file to make a 2D list of items with both the item name and price. It does this by checking for each element in the products.csv file and then adding the corresponding line(as a list) to the list it is returning.
    """
    ordered_products = products.split()#Splits the passed string of products into a list that the main for loop can traverse

    filename = input("Enter the name of your products file:")#Recieves the file the user would like to take the products from and then adds .csv to the end
    filename = filename
    file = open(filename)

    products_csv=[]
    for line in file:#This loop is responsible for turning the products.csv file into a list so it can be traversed multiple times
        product_line = line.split(",")
        products_csv.append(product_line)

        split_price = product_line[1].split("\n")#These lines get rid of the linebreak at the end of the numbers
        product_line[1] = split_price[0]

    file.close()#closes the products file

    product_list = []#Creates the empty list where the products and prices will be stored

    for i in range(len(ordered_products)):#Traverses the list of ordered products  and checks each product in the list for the price which it then adds the combination of to the list it is returning
        found = False#Establishes the variable found so that the user can be warned if the given product was not found in the products.csv file
        for product in products_csv:#Traverses the lines in the products.csv file and checks the product in the main list against each product to see which it is

            if product[0] == ordered_products[i]:#If the product name matches the current item in the products list then it adds the product name and price to the list it is returning and sets the found variable to true so that it wont unnecessarily warn the user
                product_list.append(product)
                found = True
        if found == False:#Warns the user if the product was not found
                print("Warning: Product Not Found")
    return product_list

##Complete Order
def complete_order(id, products):
    '''
    Provides the user with a reciept of their order, along with a count of how many orders they have placed.
    Accepts: User id, 2d list of products ordered and their prices
    Outputs: Each item and their prices, order subtotal, order discount (randomly selected between 5% and 50%), tax, final total, total orders placed
    Returns: Nothing
    '''
    orders = open(f"{__file__}\\..\\orders.csv", "a")
    prices = []
    items = []
    total_cost = 0
    total_orders = 0

    # Split each product into the name and the price and append each part to a different array
    for product in products:
        prices.append(float(product[1]))
        items.append(product[0])

    # Iterate through the prices array, compute total cost, discount, and tax
    for price in prices:
        total_cost += price

    # Discount is computed before tax
    discount = round(total_cost * random.uniform(0.05, 0.5), 2)
    total_cost -= discount
    tax = round(total_cost * 0.13, 2)
    total_cost *= 1.13
    total_cost = round(total_cost, 2)

    # Write the user id, total cost of order, and the names of all ordered items to orders.csv
    orders.write(f"{id}, {total_cost}, {", ".join(items).strip(", ")}\n")

    orders.close()
    orders = open(f"{__file__}\\..\\orders.csv", "r")

    # Iterate through orders.csv and count how many lines start with the user's id
    for row in orders.readlines():
        curr = row.strip("\n").split(", ")
        if (curr[0] == id):
            total_orders += 1

    # Print each item and their price, with padding to keep it all right-justified
    for i in range(len(items)):
        print(f"Item: {items[i]}{" " * (10 - len(items[i]))}Price:{" " * (max(len(f"{price:.2f}") for price in prices) - len(f"{prices[i]:.2f}"))} ${prices[i]:.2f}")

    # Print subtotal, discount, tax, and final total, with padding to keep it all right-justified
    subtotal = round(sum(price for price in prices), 2)

    # Anonymous function to compute padding for given value and title
    padding = lambda num, title : 15 + len(f"{subtotal:.2f}") - len(f"{num:.2f}") - len(title)

    print(f"\nSubtotal:{" " * padding(subtotal, 'Subtotal')} ${subtotal:.2f}\nTotal discount:{" " * padding(discount, 'Total Discount')} ${discount:.2f}\nTax:{" " * padding(tax, 'Tax')} ${tax:.2f}\nFinal total:{" " * padding(total_cost, 'Final total')} ${total_cost:.2f}")
    print(f"\nTotal orders placed by user {id}: {total_orders}")

    orders.close()



##Customer Summary
def customer_summary(userid):
    """
    Takes .csv file from userid. Uses contents of username.orders.csv and outputs order history summary
    and total spent by the customer in a professional format.
"""
    f = open("orders.csv", 'r')
    reader = csv.reader(f)
    order = list(reader)
    products = {}

    total = 0

    print("\n=============={ Customer Summary }==============\n")
    print(f"Username: {userid}")
    print("-------- Order Summary --------")
    for i in range(len(order)):
        # Check if the first entry in the line (ie. the userid) matches the current user
        if order[i][0] == userid:
            print(f"> {order[i][0]}: ${order[i][1]}")
            total += float(order[i][1])
            # Iterate through the part of the line that holds the products for the current order
            for j in range(2, len(order[i])):
                # If the current product is not already in products, add it
                if (not order[i][j] in products):
                    products.update({order[i][j] : 1})
                else:
                    products[order[i][j]] += 1

    print(f"\n>> TOTAL: ${total:.2f}")
    print("-------------------------------")
    print(f"Products ordered:")

    # Iterate through products, print the key (ie. the product name) and the value (ie. number ordered) for each entry
    for i in range(len(list(products.keys()))):
        print(f"{list(products.keys())[i]}: {products[list(products.keys())[i]]}")
    f.close()

main()