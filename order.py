from functions import * #importing functions from functions.py


def valid_bike_quantity_order():
    """this function checks whether the quamtity is valid or not and returns the valid quantity"""
    invalidQuantity = True
    while invalidQuantity:
        try:
            validBikeQuantity = int(input("Enter Quantity of bike to order: ")) # taking quantity from user
            invalidQuantity = False
            while validBikeQuantity < 1: # validating quantity
                print("Please enter valid quantity of bikes")
                get_bikes()
                validBikeQuantity = int(input("enter valid quantity to order: "))
                invalidQuantity = False
        except:
            print("Please Enter Valid Quantity (Only Numbers)")
            invalidQuantity = True
    return validBikeQuantity


# valid_bike_quantity_order()

def update_stocks_order(bike_id, quantity):
    """this function updates the text file after ordering the bikes"""

    bikes = return_2d_list()
    bikes[bike_id-1][3] = int(bikes[bike_id-1][3]) + quantity #updating and adding the quantity after ordering
    file = open("bikes.txt", "w") # opening bikes.txt in write mode to update stocks
    for bike in bikes:
        file.write(str(bike[0]) + "," + str(bike[1]) + "," + str(bike[2]) + "," + str(bike[3]) + "," + str(bike[4]) + "\n")
    file.close()
    get_bikes()
# update_stocks_order()



def order_bill(orderedBikes, name_, address, contactNumber):
    """this function prints the bill for ordered bikes and also writes the bill in text file generating unique name for each file"""

    bikes = return_2d_list()

    #printing bill
    print("")
    print("-----------------------------------------------------------------------------------------")
    print("\t\t\t**************Bike Management System****************")
    print("\t\t\t############### ORDER BillS #################\n")
    print("Name: " + name_)
    print("Address: " + address)
    print("Contact Number: " + contactNumber)
    print("Date and Time:" + date() + "\t"+time()+"\n")

    print("-----------------------------------------------------------------------------------------")
    print("Bike-name          Color       Price(Unit)      Quantity       Total Price($)")
    print("-----------------------------------------------------------------------------------------")
    totalPrice = 0
    for orderBike in orderedBikes:
        for bike_index in range(len(bikes)):
            if orderBike[0] == bike_index + 1:
                print(str(bikes[bike_index][0]) + "\t\t"+str(bikes[bike_index][2]) + "\t\t" + str(
                    bikes[bike_index][4]) + "\t\t" + str(orderBike[1]) + "\t\t" + str(orderBike[1] * int(bikes[bike_index][4])))
                totalPrice = totalPrice + (orderBike[1] * int(bikes[bike_index][4]))
    print("-----------------------------------------------------------------------------------------")
    print("Total Bill Amount = $" + str(totalPrice))
    print("-----------------------------------------------------------------------------------------")

    #openeing file in write mode to write the bill
    file = open("order_bills/"+name_+contactNumber+" "+date_time()+".txt", "w") # generating bill of unique name to write the bill
    file.write("\t\t\t**************Bike Management System****************")
    file.write("\n")
    file.write("\t\t\t############### ORDER BillS #################\n")
    file.write("Name: "+name_+"\n")
    file.write("Address: "+address)
    file.write("\n")
    file.write("Contact: "+contactNumber+"\n")
    file.write("Date and Time of Order: "+date()+"\t"+time() + "\n")

    file.write("-----------------------------------------------------------------------------------------\n")
    file.write("Bike-name          Color       Price(Unit)      Quantity       Total Price($)"+"\n")
    file.write("-----------------------------------------------------------------------------------------\n")

    for orderBike in orderedBikes:
        for bike_index in range(len(bikes)):
            if orderBike[0] == bike_index + 1:
                file.write(str(bikes[bike_index][0])+"\t\t"+str(bikes[bike_index][2]) + "\t\t" + str(
                    bikes[bike_index][4]) + "\t\t" + str(orderBike[1]) + "\t\t" + str(orderBike[1] * int(bikes[bike_index][4])) + "\n")
    file.write("-----------------------------------------------------------------------------------------\n")
    file.write("Total Bill Amount = $" + str(totalPrice) + "\n")
    file.write("-----------------------------------------------------------------------------------------\n")

    file.close()




