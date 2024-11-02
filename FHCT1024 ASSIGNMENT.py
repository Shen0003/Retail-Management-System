#Main Menu
def MainMenu():
    print(r"		  ___    ____    ___   _____     __         ______   ______    ____    ____    _______    ")
    print(r"		  \  \  /    \  /  /  |  ___|   | |        |  ____|  |  _  |  |  _ \  / _  |  |   ____|   ")
    print(r"		   \  \/  /\  \/  /   | |___    | |        | |       | | | |  | | \ \/ / | |  |  |____    ")
    print(r"		    \    /  \    /    |  ___|   | |        | |       | | | |  | |  \__/  | |  |   ____|   ")
    print(r"		     \  /    \  /     | |___    | |____    | |____   | |_| |  | |        | |  |  |____    ")
    print(r"		      \/      \/      |_____|   |______|   |______|  |_____|  |_|        |_|  |_______|   ")
    print("="*120)
    print("\t\t\t\t\t\tGodShen Sport Retail Sdn Bhd\n")
    print("="*120)
    print("\t\t\t\t\t\t<1>Item Maintenance\n"+"\t\t\t\t\t\t<2>Stock Management\n"+"\t\t\t\t\t\t<3>Stock Replacement\n"+"\t\t\t\t\t\t<4>Sales\n"+"\t\t\t\t\t\t<Q>uit\n")
    print("="*120)

#Item Maintainence(Option 1)
def ItemMaintain():
    print("="*120)
    print("\t\t\t\t\t\tItem Maintenance")
    print("="*120)
    print("\t\t\t\t\t\tNo Code\t Name\t\t    Price(RM)")
    print("="*120)
    for i in range(len(Code)):
        print("\t\t\t\t\t\t%d. %-5s %-18s %.2f" %((i+1),Code[i],Item[i],Price[i]))
        
    print("="*120)
    print("\t\t\t\t\t\t<A>dd\t","<M>odify\t","<D>elete\t\t","<Q>uit")
    print("="*120)
    #Item Maintanence(Internal Option - Add, Modify, Delete, Quit)
    print()
    option = input("Enter Option: ")
    while option.upper() != "Q":
        #Add
        if option.upper() == "A":
            ItemCode = input("Enter New Item Code: ").upper() #Ask for the item code for the new item that want to add Code List(Main function)
            while ItemCode in Code: #Check for the new ItemCode key in by the user is repeated or not from the Code list(Main function)
                print("The item code is already used! Please choose a new item code!")
                ItemCode = input("Enter New Item Code: ").upper()
            ItemName = input("Enter New Item Name: ").upper() #Ask for the item name for the new item that want to add into the Item List(Main function)
            while ItemName in Item: #Check for the new item name key in by the user is repeated or not from the Item list(Main function)
                print("The item name is already used! Please choose a new item name!") 
                ItemName = input("Enter New Item Name: ").upper()
            ItemPrice = input("Enter New Item Price (RM): ") #Ask for the new item price that want to add into the Price List(Main function)
            while ItemPrice.isdigit() == False: #Check for the item price is digit/integer or not (Validation for the item price)
                print("Invalid item price. Please use number!")
                ItemPrice = input("Enter New Item Price (RM): ")
            ItemPrice = float(ItemPrice)

            ItemStock = input("Enter New Item Quantity: ") #Ask for the new item quantity that want to add into the Stock List(Main function)
            while ItemStock.isdigit() == False: #Check for the item stock is digit/integer or not (Validation for the item stock)  
                print("Invalid item quantity. Please use number!")
                ItemStock = input("Enter New Item Quantity: ")
            ItemStock = int(ItemStock)

            Code.append(ItemCode) #adding the new item code into the Code List(Main function)
            Item.append(ItemName) #adding the new item name into the Item List(Main function)
            Price.append(ItemPrice) #adding the new item price into the Price List(Main function)
            Stock.append(ItemStock) #adding the new item quantity into the Stock List(Main function)
            ItemNo.append(1)
            sort_number()
            
            screen_clear()
            print("="*120)
            print("\t\t\t\t\t\tItem Maintenance")
            print("="*120)
            print("\t\t\t\t\t\tNo Code\t Name\t\t    Price(RM)")
            print("="*120)
            for i in range(len(Code)):
                print("\t\t\t\t\t\t%d. %-5s %-18s %.2f" %(((i+1),Code[i],Item[i],Price[i])))
            print("="*120)
            print("\t\t\t\t\t\t<A>dd\t","<M>odify\t","<D>elete\t\t","<Q>uit")
            print("="*120)
            print()
            option = input("Enter Option: ")       
        #Modify
        elif option.upper() == "M":
            modify = int(input("Item do you wish to change(ItemNumber): ")) #Ask for ItemNo for the item that want to change
            while modify not in ItemNo: #Validation for the ItemNo
                print("Invalid Item Number!")
                modify = int(input("Item do you wish to change(ItemNumber): "))###################################################

            selection = input("Which do you want to change(Code/Name/Price): ")
            while selection.upper() != "CODE" and selection.upper() != "NAME" and selection.upper() != "PRICE":  #Validation for selection
                print("Invalid selection!")################################
                selection = input("Which do you want to change(Code/Name/Price): ") #Ask for the selection that need to modify
            if selection.upper() == "CODE":
                ItemCode = input("New Code: ").upper()  #New item code                                                           
                while ItemCode in Code: #Check for the new item code key in by the user is repeated or not from the Code list(Main function)
                    print("The item code is already used! Please choose a new item code!")
                    ItemCode = input("New Code: ").upper()
                Code[modify - 1] = ItemCode     #Change the previous item code with the new item code
            elif selection.upper() == "NAME":
                ItemName = input("New Name: ").upper()  #New item name                                                           
                while ItemName in Item: #Check for the new item name key in by the user is repeated or not from the Item list(Main function)
                    print("The item name is already used! Please choose a new item name!") 
                    ItemName = input("New Name: ").upper()
                Item[modify - 1] = ItemName     #Change the previous item name with the new item name
            elif selection.upper() == "PRICE":
                ItemPrice = float(input("New Price: "))  #New item price
                Price[modify - 1] = ItemPrice            #Change the previous item price with the new item price
            else:
                print("Invalid selection") #Validation for selection
                selection = input("Which do you want to change(Code/Name/Price): ")
                
            screen_clear()
            print("="*120)
            print("\t\t\t\t\t\tItem Maintenance")
            print("="*120)
            print("\t\t\t\t\t\tNo Code\t Name\t\t    Price(RM)")
            print("="*120)
            for i in range(len(Code)):
                print("\t\t\t\t\t\t%d. %-5s %-18s %.2f" %(((i+1),Code[i],Item[i],Price[i])))
            print("="*120)
            print("\t\t\t\t\t\t<A>dd\t","<M>odify\t","<D>elete\t\t","<Q>uit")
            print("="*120)
            print()
            option = input("Enter Option: ")
        #Delete
        elif option.upper() == "D":
            delete = int(input("Which item do you want do delete(ItemNumber): ")) #ask for the ItemNo for the item want to delete
            while delete not in ItemNo: #Validation for delete
                print("Invalid item number!")
                delete = int(input("Which item do you want do delete(ItemNumber): "))

            ItemNo.pop(delete - 1)
            Code.pop(delete - 1) #Delete the selected item code of the selected item in the Code list(Main function)
            Item.pop(delete - 1) #Delete the selected item name of the selected item in the Item list(Main function)
            Price.pop(delete - 1) #Delete the selected item price of the selected item in the Price list(Main function)
            Stock.pop(delete -1) #Delete the selected item quantity of the selected item Stock list(Main function)

            sort_number()
            screen_clear()
            print("="*120)
            print("\t\t\t\t\t\tItem Maintenance")
            print("="*120)
            print("\t\t\t\t\t\tNo Code\t Name\t\t    Price(RM)")
            print("="*120)
            for i in range(len(Code)):
                print("\t\t\t\t\t\t%d. %-5s %-18s %.2f" %(((i+1),Code[i],Item[i],Price[i])))
            print("="*120)
            print("\t\t\t\t\t\t<A>dd\t","<M>odify\t","<D>elete\t\t","<Q>uit")
            print("="*120)
            print()
            option = input("Enter Option: ")
        else:
            print("Invalid Option!") #Validation for option so user only can choose A/M/D/Q, otherwise print invalid option
            option = input("Enter Option: ")

    screen_clear()
    MainMenu()
    

#Stock Management(Option 2)
def StockManage():
    print("="*120)
    print("\t\t\t\t\t\tStock Management Menu")
    print("="*120)
    print("\t\t\t\t\t\tCode  Name\t\t Price(RM)")
    print("="*120)
    for i in range(len(Code)):
        print("\t\t\t\t\t\t%-5s %-18s %.2f" %((Code[i],Item[i],Price[i])))
    print("="*120)
    print()
    
    ItemCode = input("Enter Item Code <Q>uit: ")#Ask for the ItemCode for the item that need to check

    while ItemCode.upper() != "Q":

        if ItemCode.upper() in Code: #Check if the ItemCode key in by the user is available in the Code list(Main function) or not
            index = Code.index(ItemCode.upper()) #Get the index number of the ItemCode key in from the Code list(Main function)
            quantity = input("Enter Item Quantity(For Checking): ") #Ask for the quantity that need to be checked

            while quantity.isdigit() == False: #Check for the item stock is digit/integer or not (Validation for the item stock)  
                print("Invalid item quantity. Please use number!")
                quantity = input("Enter Item Quantity: ")
            quantity = int(quantity)
            if quantity <= Stock[index]: #Check if the amount of the stock in the Stock list(Main function) by using the index number is sufficient or not for the quantitiy key in by the user
                print("Stock is sufficient!")
            else:
                print("Stock is insufficient!")
        else:
           print("Invalid item code!") #Validation for item code
           
        ItemCode  = input("Enter Item Code <Q>uit: ")

    screen_clear()
    MainMenu()
                
#Stock Replacement(Option 3)
def StockReplace():
    print("="*120)
    print("\t\t\t\t\t\tStock Replacement Menu")
    print("="*120)
    print("\t\t\t\t\t\tCode  Name\t\t Price(RM)\t Stock")
    print("="*120)
    for i in range(len(Code)):
        print("\t\t\t\t\t\t%-5s %-18s %.2f %12d" %((Code[i],Item[i],Price[i],Stock[i])))
    print("="*120)
    print()

    ItemCode = input("Enter Item Code <Q>uit: ") #Ask for the ItemCode for the item that need to be added

    while ItemCode.upper() != "Q":

        if ItemCode.upper() in Code: #Check if the ItemCode key in by the user is available in the Code list(Main function) or not
            index = Code.index(ItemCode.upper()) #Get the index number of the ItemCode key in from the Code list(Main function)
            quantity = input("Enter Quantity(ADD): ") #Ask for the quantity that need to be added
            while quantity.isdigit() == False: #Check for the item stock is digit/integer or not (Validation for the item stock)  
                print("Invalid item quantity. Please use number!")
                quantity = input("Enter Item Quantity: ")
            quantity = int(quantity)
            Stock[index] = Stock[index] + quantity #Use the index number get to refer to the correct item's quantitiy in the Stock list(Main function) to add the quantity key in by the user with the orginal quantitiy in the Stock list(Main function)
            screen_clear()
            print("="*120)
            print("\t\t\t\t\t\tStock Replacement Menu")
            print("="*120)
            print("\t\t\t\t\t\tCode  Name\t\t Price(RM)\t Stock")
            print("="*120)
            for i in range(len(Code)):
                print("\t\t\t\t\t\t%-5s %-18s %.2f %12d" %((Code[i],Item[i],Price[i],Stock[i])))
            print("="*120)
            print()   
        else:
            print("Invalid item code!") #Validation for the ItemCode
            
        ItemCode  = input("Enter Item Code <Q>uit: ")

    screen_clear()
    MainMenu()

#Sales(Option 4)

def Sales():
    
    print("="*120)
    print("\t\t\t\t\t\t  Sales Transaction Menu")
    print("="*120)
    print("\t\t\t\t\t   Code  Name\t\t Price(RM)\t Stock")
    print("="*120)
    for i in range(len(Code)):
        print("\t\t\t\t\t   %-5s %-15s %.2f %12d" %((Code[i],Item[i],Price[i],Stock[i])))
    print("="*120)
    print()
    
    #Creating order
    receipt = False
    #List to store the item bought
    cart_code = [] 
    cart_item = []
    amount = []
    item_price =[]
    
    total_payment = 0
    buy = input("Enter item code <C>onfirm <Q>uit: ").upper() #Ask for the item code of the item that the user bought

    while buy.upper() != "Q": 
        
        if buy.upper() in Code: #Validation for the item code key in by the user, check the item code is in the Code list(Main function) or not
            index = Code.index(buy.upper())
            cart_code.append(buy)
            
            quantity = input("Enter the number of unit(s):")
            while quantity.isdigit() == False: #Check for the item stock is digit/integer or not (Validation for the item stock)  
                print("Invalid item quantity. Please use number!")
                quantity = input("Enter the number of unit(s): ")
            quantity = int(quantity)
            
            cart_item.append(Item[index])
            item_price.append(Price[index])
            
            
            
            while quantity > Stock[index] or quantity == 0: #Check for the quantity of the item from the Stock list(Main function) key in by the user is sufficient or not 
                print("Not enough stock")
                quantity = input("Enter the number of unit(s): ")
                while quantity.isdigit() == False: #Check for the item stock is digit/integer or not (Validation for the item stock)  
                    print("Invalid item quantity. Please use number!")
                    quantity = input("Enter the number of unit(s): ")
                quantity = int(quantity)    

            total_payment += Price[index] * quantity #Total payment calculation(before membership discount)
            Stock[index] -= quantity
            amount.append(quantity)
            buy = input("Enter item code <C>onfirm <Q>uit: ").upper()
         
        else:
            if buy.upper() != "C" and buy.upper() != "Q":
                print("Invalid item code!")
            
                buy = input("Enter item code <C>onfirm <Q>uit: ").upper()
 
        if buy.upper() == "C":
            #Membership discount
            membership = input("Do you have membership?(y/n): ") #Ask for the membership 
            while membership.upper() != "Y" and membership.upper() != "N": #Validation for the membership key in by the user
                print("Invalid option!")
                membership = input("Do you have membership?(y/n): ").upper()

            if membership.upper() == "Y": #Have membership
                membershiptier = input("Enter membership tier(Premium/Gold/Normal): ") #Ask for the membership tier

                while membershiptier.upper() != "Q": 
                    if membershiptier.upper() != "PREMIUM" and membershiptier.upper() != "GOLD" and membershiptier.upper() != "NORMAL": #Validation for the membership tier key in by the user
                        print("Invalid membership tier!")
                        membershiptier = input("Enter membership tier(Premium/Gold/Normal):")  

                    else: 
                        if membershiptier.upper() == "PREMIUM":
                            total_payment = total_payment * 0.80 #Total payment calculation for Premium membership
                            
                        elif membershiptier.upper() == "GOLD":
                            total_payment = total_payment * 0.90 #Total payment calculation for Gold membership
                            
                        elif membershiptier.upper() == "NORMAL":
                            total_payment = total_payment * 0.95 #Total payment calculation for Normal membership

                        receipt = True
                        membershiptier = "Q"

                
                if receipt == True: 
                    screen_clear()
                    print("-"*120)
                    #Print Receipt
                    now = datetime.datetime.now()
                    time = now.strftime("%d/%m/%Y %H:%M:%S")
                    print("\t\t\t\t\t      GodShen Sport Retail Sdn. Bhd.")
                    print("\t\t\t\t\t    "f'{"Date and time: %s" %time:}')

                    print("-"*120)
                    print("\t\t\t\t     Code  Name\t\t Quantity\t Price(RM)")
                    print("-"*120)
                    for i in range(len(cart_code)):
                        print("\t\t\t\t     %-5s %-13s %-15d %.2f" %((cart_code[i],cart_item[i],amount[i],item_price[i])))
                    print("-"*120)
                    #Rounding to the nearest 5 cents
                    total_payment = ('%.2f' % total_payment)
                    total_payment = str(total_payment)
                    last_digit = ("0.0"+ total_payment[-1])
                    last_digit = float(last_digit)

                    total_payment = float(total_payment)

                    if last_digit > 0.05:
                        total_payment += (0.1 - last_digit)

                elif last_digit < 0.05 and last_digit >= 0:
                    total_payment -= last_digit

                print("\t\t\t\t     Total Payment:RM %.2f" % total_payment) #Final total payment (after membership discount)
                receipt = False
                print("-"*120)
                #Save the receipt into the Receipt.txt file
                f = open("Receipt.txt","a+")
                    
                f.write("-"*50)
                f.write("\n\t  GodShen Sport Retail Sdn. Bhd.\n")
                f.write("\t"f'{"Date and time: %s" %time:}')
                f.write("\n")
                f.write("-"*50)
                f.write("\n Code  Name\t     Quantity\t     Price(RM)\n")
                f.write("-"*50)
                for i in range(len(cart_code)):
                    f.write("\n %-5s %-13s %-15d %.2f \n" %((cart_code[i],cart_item[i],amount[i],item_price[i])))
                f.write("-"*50)
                f.write("\n Total Payment:RM %.2f\n" % total_payment)
                f.write("-"*50)
                f.write("\n")
                f.close
                
                Quit = input("Enter Q to quit: ")
                while Quit.upper() != "Q":
                    print("Invalid Input!")
                    Quit = input("Enter Q to quit: ")

                buy = "Q"
            
                           
            elif membership.upper() == "N": #No membership
                screen_clear()
                print("-"*120)
                #Print Receipt
                now = datetime.datetime.now()
                time = now.strftime("%d/%m/%Y %H:%M:%S")
                print("\t\t\t\t\t      GodShen Sport Retail Sdn. Bhd.")
                print("\t\t\t\t\t    "f'{"Date and time: %s" %time:}')

                print("-"*120)
                print("\t\t\t\t     Code  Name\t\t Quantity\t Price(RM)")
                print("-"*120)
                for i in range(len(cart_code)):
                    print("\t\t\t\t     %-5s %-13s %-15d %.2f" %((cart_code[i],cart_item[i],amount[i],item_price[i])))
                print("-"*120)
                #Rounding to the nearest 5 cents
                total_payment = ('%.2f' % total_payment) 
                total_payment = str(total_payment)
                last_digit = ("0.0"+ total_payment[-1])
                last_digit = float(last_digit)

                total_payment = float(total_payment)

                if last_digit > 0.05:
                    total_payment += (0.1 - last_digit)

                elif last_digit < 0.05 and last_digit >= 0:
                    total_payment -= last_digit

                print("\t\t\t\t     Total Payment:RM %.2f" % total_payment) #Final total payment (after membership discount)
                print("-"*120)
                #Save the receipt into the Receipt.txt file
                f = open("Receipt.txt","a+")
                
                f.write("-"*50)
                f.write("\n\t  GodShen Sport Retail Sdn. Bhd.\n")
                f.write("\t"f'{"Date and time: %s" %time:}')
                f.write("\n")
                f.write("-"*50)
                f.write("\n Code  Name\t     Quantity\t     Price(RM)\n")
                f.write("-"*50)
                for i in range(len(cart_code)):
                    f.write("\n %-5s %-13s %-15d %.2f \n" %((cart_code[i],cart_item[i],amount[i],item_price[i])))
                f.write("-"*50)
                f.write("\n Total Payment:RM %.2f\n" % total_payment)
                f.write("-"*50)
                f.write("\n") 
                f.close

                Quit = input("Enter Q to quit: ")
                while Quit.upper() != "Q":
                    print("Invalid Key!")
                    Quit = input("Enter Q to quit: ")

                buy = "Q"

    screen_clear()
    MainMenu()

#Clear screen when turn to next option
def screen_clear():

    if os.name == 'posix':
        #For mac and linux
        os.system('clear')

    else:
        #For windows
        os.system('cls')           

def sort_number():
    for i in range(len(Code)):
        ItemNo[i] = i+1

    
    
#Main Function
import os
import datetime
from time import sleep


#List to store the data that have been read from the Menu.txt file
ItemNo = []
Code = []
Item = []
Price = []
Stock = []

#Read the date from the Menu.txt file and store into the 5 different list
f = open("Menu.txt" ,"r")
for line in f:
    splitline = line.split("|")
    ItemNo.append(int(splitline[0]))
    Code.append(splitline[1])
    Item.append(splitline[2])
    Price.append(float(splitline[3]))
    Stock.append(int(splitline[4]))
f.close

MainMenu()
option = input("Option: ") #Ask for the option

while option.upper() != "Q":
    if option == "1":
        screen_clear()
        ItemMaintain()
    elif option == "2":
        screen_clear()
        StockManage()
    elif option == "3":
        screen_clear()
        StockReplace()
    elif option == "4":
        screen_clear()
        Sales()
    else:
        print("Invalid Option!") #Validation for the option
    
    option = input("Option: ")

#Overwrite and save the latest data into the Menu.txt file
f = open("Menu.txt","w")
f.truncate()
for i in range(len(Code)):
        f.write(str(ItemNo[i])+'|'+Code[i]+'|'+Item[i]+'|'+str(Price[i])+'|'+str(Stock[i])+'\n')
f.close

screen_clear()
print("\n"*8)
print(r"			  _____   _   _      _      _   _   _  __ ")
print(r"			 |_   _| | | | |    / \    | \ | | | |/ / ")
print(r"			   | |   | |_| |   / _ \   |  \| | | ' /  ")
print(r"			   | |   |  _  |  / ___ \  | |\  | | . \  ")
print(r"			   |_|   |_| |_| /_/   \_\ |_| \_| |_|\_\ ")
print("")
print(r"			          __   __   ___    _   _          ")
print(r"			          \ \ / /  / _ \  | | | |         ")
print(r"			           \ V /  | | | | | | | |         ")
print(r"			            | |   | |_| | | |_| |         ")
print(r"			            |_|    \___/   \___/          ")

sleep(3) #Automatically close the program after 3 seconds
 
    
    
    
    
    



    

