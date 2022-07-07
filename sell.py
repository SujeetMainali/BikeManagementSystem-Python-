from functions import * # importing functions from functions.py


def valid_bike_quantity_sell(bike_id):
    """this function checks whether the quantity provided is valid or not and returns  the valid bike quantity"""
    bikes = return_2d_list()
    quantity = int(bikes[bike_id-1][3])
    invalidQuantity = True
    while invalidQuantity:
        try:
            validBikeQuantity = int(input("Enter Quantity of bike to sell: ")) # getting quantity from user
            invalidQuantity = False
            while validBikeQuantity < 1 or validBikeQuantity > quantity: # validating quantity
                print("Please enter valid quantity of bikes")
                get_bikes()
                validBikeQuantity = int(
                    input("enter valid quantity to sell: "))
                invalidQuantity = False
        except:
            print("Please Enter Valid Quantity (Only Numbers)")
            invalidQuantity = True
    return validBikeQuantity


# valid_bike_quantity_sell(bike_id = valid_bike_id())


def update_stocks_sell(bike_id, quantity):
    """this function updates the text file after selling the bikes"""

    bikes = return_2d_list()
    bikes[bike_id-1][3] = int(bikes[bike_id-1][3])-quantity # subtracting and updating quantity
    # opening bikes..txt in write mode to update 
    file = open("bikes.txt", "w")
    for bike in bikes:
        file.write(str(bike[0]) + "," + str(bike[1]) + "," +
                   str(bike[2]) + "," + str(bike[3]) + "," + str(bike[4]) + "\n")
    file.close()
    get_bikes()
# update_stocks_sell()


def sell_bill(soldBikes, name_, address, contactNumber):
    """this function prints the bill for sold bikes and also writes the bill in text file generating unique name for each file"""

    bikes = return_2d_list()

    # printing sell bills
    print("")
    print("-----------------------------------------------------------------------------------------")
    print("\t\t\t**************Bike Management System****************")
    print("\t\t\t############### SELL BillS #################\n")
    print("Name: " + name_)
    print("Address: " + address)
    print("Contact Number: " + contactNumber)
    print("Date and Time:" + date() + "\t"+time()+"\n")

    print("-----------------------------------------------------------------------------------------")
    print("Bike-name          Color       Price(Unit)      Quantity       Total Price($)")
    print("-----------------------------------------------------------------------------------------")
    totalPrice = 0
    for soldBike in soldBikes:
        for bike_index in range(len(bikes)):
            if soldBike[0] == bike_index + 1:
                print(str(bikes[bike_index][0]) + "\t\t" + str(bikes[bike_index][2]) + "\t\t" + str(
                    bikes[bike_index][4]) + "\t\t" + str(soldBike[1]) + "\t\t" + str(soldBike[1] * int(bikes[bike_index][4])))
                totalPrice = totalPrice + (soldBike[1] * int(bikes[bike_index][4]))

    print("-----------------------------------------------------------------------------------------")
    print("Total Bill Amount = $" + str(totalPrice))
    print("-----------------------------------------------------------------------------------------")

    # creting a new txt file of unique name to write bill
    file = open("sell_bills/"+name_+contactNumber+" "+str(date_time())+".txt", "w")
    file.write("\t\t\t**************Bike Management System****************")
    file.write("\n")
    file.write("\t\t\t############### SELL BillS #################\n")
    file.write("Name: "+name_+"\n")
    # file.write("\n")
    file.write("Address: "+address)
    file.write("\n")
    file.write("Contact: "+contactNumber+"\n")
    file.write("Date and Time of buy: "+date()+"\t"+time() + "\n")

    file.write(
        "-----------------------------------------------------------------------------------------\n")
    file.write(
        "Bike-name          Color       Price(Unit)      Quantity       Total Price($)"+"\n")
    file.write(
        "-----------------------------------------------------------------------------------------\n")

    for soldBike in soldBikes:
        for bike_index in range(len(bikes)):
            if soldBike[0] == bike_index + 1:
                file.write(str(bikes[bike_index][0])+"\t\t"+str(bikes[bike_index][2]) + "\t\t" + str(bikes[bike_index]
                           [4]) + "\t\t" + str(soldBike[1]) + "\t\t" + str(soldBike[1]*int(bikes[bike_index][4])) + "\n")
    file.write(
        "-----------------------------------------------------------------------------------------\n")
    file.write("Total Bill Amount = $" + str(totalPrice) + "\n")
    file.write(
        "-----------------------------------------------------------------------------------------\n")
    file.close()
