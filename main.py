from functions import *
from order import *
from sell import *


def main():
    """This function assembles all the functions to run the program in the flow"""
    welcome_message()
    while True:
        action()
        invalidAction = True
        while invalidAction:
            try:
                user_action = int(input("Enter value of option: "))
                invalidAction = False
            except:
                print("Please input valid Input(Only Numbers)")
        if user_action == 1:
            soldBikes = [] # initializing list to store sold bikes

            anotherSale = 'y'
            while anotherSale == 'y':
                get_bikes() #getting bikes
                bike_id = valid_bike_id() # getting valid bike id and storing in bike_id
                quantity = valid_bike_quantity_sell(bike_id) # getting valid bike quantity and storing in quantity

                soldBikes.append([bike_id, quantity]) # adding list of bike_id and quantity in soldBikes list

                update_stocks_sell(bike_id, quantity) # updating stocks

                print("If yes |Y| else |N| or any other input will be considered No ")
                anotherSale = input("Do you want to sell more bikes(y/n): ").lower() # asking for another sale
                
            name_ = input("Enter name of the Customer: ")
            address = input("Enter address of the Customer: ")
            contactNumber = input("Enter contact number of the Customer: ")
            sell_bill(soldBikes, name_, address, contactNumber) # printing sell bill
                    
        elif user_action == 2:
            orderedBikes = []

            anotherSale = 'y'
            while anotherSale == 'y':
                get_bikes() # getting bikes/displaying bikes
                bike_id = valid_bike_id() #  getting valid bike id and storing in bike_id
                quantity = valid_bike_quantity_order() # getting valid bike quantity and storing in quantity

                orderedBikes.append([bike_id, quantity]) # adding list of bike_id and quantity in orderedBikes list

                update_stocks_order(bike_id, quantity) # updating stocks

                print("If yes |Y| else |N| or any other input will be considered No ")
                anotherSale = input("Do you want to order more bikes(y/n): ").lower() # asking for anothert order
                
            name_ = input("Enter name of the Shipping Company: ")
            address = input("Enter address of the Shipping Company: ")
            contactNumber = input("Enter contact number of the company : ")
            order_bill(orderedBikes, name_, address, contactNumber) # printing order bill
                    
        elif user_action == 3:
            get_bikes() # displaying bikes

        elif user_action == 4:
            exit_message() # exit message
            exit()
        else:
            print("\n")
            print("Enter valid option")
            print("\n")


main()
