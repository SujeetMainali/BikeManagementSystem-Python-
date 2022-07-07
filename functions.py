import datetime

def welcome_message():
    """This function displays the welcome message of the program"""
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("++\t\t\t\t\t\t\t\t\t\t\t++")
    print("++\t\t\t\t\t\t\t\t\t\t\t++")
    print("++\t\t\tWelcome to Bike Management System\t\t\t\t++")
    print("++\t\t\t\t\t\t\t\t\t\t\t++")
    print("++\t\t\t\t\t\t\t\t\t\t\t++")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


def exit_message():
    """This function displays the exit message of the program"""
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("++\t\t\t\t\t\t\t\t\t\t\t++")
    print("++\t\t\t\t\t\t\t\t\t\t\t++")
    print("++\t\t\tThank You For Using Bike Management System\t\t\t++")
    print("++\t\t\t\t\t\t\t\t\t\t\t++")
    print("++\t\t\t\t\t\t\t\t\t\t\t++")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


def action():
    """This function displays the actions that ccan be performed in the program"""
    print("1. Sell Bikes")
    print("2. Order Bikes")
    print("3. Display Bikes")
    print("4. Exit")

# action()


def get_bikes():
    """This function reads the main text file(bikes.txt) and displays it in tabular form"""
    print("-----------------------------------------------------------------------------------------")
    print("Bike_ID      Bike-name          Company          Color       Stock             Price($)")
    print("-----------------------------------------------------------------------------------------")
    file = open("bikes.txt", "r") #opening bikes.txt in reading mode and storing in file
    bike_id = 1

    for line in file:
        print("", bike_id, "\t\t"+line.replace(",", "\t\t")) # providing bike id to bikes and storing in tabular form
        bike_id += 1
    print("-----------------------------------------------------------------------------------------")
    file.close() #closing file

# get_bikes()


def return_2d_list():
    """this function returns the 2D list of the bikes"""
    file = open("bikes.txt")
    list_2d = [] #initializing list
    for line in file:
        line = line.replace("\n", "")
        line = line.split(",") # separating items in list with comma
        list_2d.append(line) # appending/adding items to list
    return list_2d
# print(return_2d_list())
# return_2d_list()


def valid_bike_id():
    """this function checks the id of the bike whether it exists or not"""
    
    invalidId = True
    while invalidId:
        try:
            bike_id = int(input("enter id : "))
            invalidId = False
        
            while bike_id <= 0 or bike_id > len(return_2d_list()): #comparing bike id whether it is less than 0 or greater than list
                print("please provide valid bike ID")
        # get_bikes()
                bike_id = int(input("Please Enter Valid Bike ID : "))
                invalidId = False
        except:
            print("Please Enter Valid ID (Only Numbers)")
            invalidId = True
    return bike_id

# valid_bike_id()


def date_time():
    """this function uses date time to generate a unique numbers"""
    date_time = str(datetime.datetime.now().strftime("%Y%m%d%w%I%M%S%f")) #%Y =full year, %m = month(01..) %d = twoDigit day I=hour(12/2)
    return date_time
     
# date_time()
# print(date_time())


def date():
    """This functio returns date"""
    date = str(datetime.datetime.now().strftime("%Y %b %d %A"))# full year month(abb alphabet) day(01..) week(alphabetFull)
    return date
# date()
# print(date())


def time():
    """This function returns time"""
    time = str(datetime.datetime.now().strftime("%I:%M:%S:%f %p")) 
    return time
# time()
# print(time())
