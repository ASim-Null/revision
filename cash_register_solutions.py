 SOLUTIONS TO TASK 1     

Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items
Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

'''


#############################################
# Bora 
#############################################


class CashRegister:
    def __init__(self):
        self.total_items = None # {'item': 'price'}
        self.total_price = 0
        self.discount = 0

    def add_item(self, item, price):
        self.item = item
        self.price = price
        if self.total_items == None:
            self.total_items = {}
            self.total_items[self.item] = self.price
        else:
            self.total_items[self.item] = self.price

    def remove_item(self, removeItem):
        self.removeItem = removeItem
        self.total_items.pop(self.removeItem)

    def apply_discount(self, discount):
        self.discount = discount
        self.total_price = self.total_price - discount
        print('-----Total after discount is', self.total_price, '£')

    def get_total(self):
        self.total_price = sum(self.total_items.values())
        print('-----------Total amount due', self.total_price, '£')

    def show_items(self):
        #self.showItems = self.total_items.keys()
        print('-------💁 ‍️Welcome to Tesco 💁-------')
        # print(self.total_items.keys())
        for item in (self.total_items):
            print(item, '-💵-💵-💵-', self.total_items[item], '£')
        #print(self.total_items)
    def reset_register(self):
        self.total_items = None
        self.total_price = 0
        self.total_items = 0
        self.discount = 0

# # EXAMPLE code run:
# tesco = CashRegister()
# # ADD ITEM
# tesco.add_item('apple', 2)
# tesco.add_item('banana', 3)
# tesco.add_item('kiwi', 1)
# tesco.add_item('chicken', 5)
# tesco.add_item('Milk', 1.5)
#
# # REMOVE ITEM
# tesco.remove_item('banana')
#
# # SHOW ITEM
# tesco.show_items()
#
# # GET TOTAL
# tesco.get_total()
#
# # APPLY DISCOUNT
# tesco.apply_discount(3)
#
# # RESET
# #tesco.reset_register()


#############################################
# Heather 
#############################################


class CashRegister:

    # Each item should be passed in with: price, quantity, total price
    def __init__(self):
        self.__total_items = list()
        self.__subtotal = 0
        self.__total_price = 0
        self.__discount = 0

    def __update_subtotal(self, price):
        self.__subtotal += price  
        self.__update_total()     

    # This will need to update the total every time an item is changed
    # This is a private method!!!
    def __update_total(self):
        self.__total_price = round(self.__subtotal * ((100 - self.__discount) / 100), 2)

    def __find_item(self, query):
        try: 
            return self.__total_items.index([item for item in self.__total_items if item.get_item_name() == query.get_item_name()][0])
        except:
            return False

    # This also needs to update the quantity of the item if the item already exists
    def add_item(self, newitem):
        if self.__find_item(newitem):
            index = self.__find_item(newitem)
            self.__total_items[index].quantity += newitem.quantity
        else:
            self.__total_items.append(newitem)
        self.__update_subtotal(newitem.price)

    # This needs to take the quantity of the item down by one (if quantity = 0, remove the item)
    def remove_item(self, removed_item):
        try:
            index = self.__find_item(removed_item)
            self.__total_items[index].quantity -= 1
            if self.__total_items[index].quantity == 0:
                bye_bye = self.__total_items.pop(index)
                self.__update_subtotal(-bye_bye.price)
            else:
                self.__update_subtotal(-self.__total_items[index].price)      
        except:
            print("Could not remove item; item not found.")

    # Discount on all items - update discount property
    def apply_discount(self, discount):
        if (self.__discount + discount) > 100:
            print("Discount invalid. Cannot discount more than 100%.")
        elif (self.__discount + discount) < 0:
            print("Discount invalid. Cannot discount less than 0%")
        else:
            self.__discount += discount
        
        self.__update_total()

    # Display the total for the user
    def display_total(self):
        print("Subtotal: £" + str(self.__subtotal))
        if self.__discount > 0:
            print(f"Discount: {self.__discount}%.\nTotal: £{self.__total_price}")
        else:
            print(f"Total: £{self.__total_price}")

    # Return the total to the main body so user payment can be checked
    def return_total(self):
        return self.__total_price
    
    # Print each item formatted nicely
    def show_items(self):
        print("ITEM     QUANTITY     PRICE")
        for item in self.__total_items:
            print(f"{item.name}     x{item.quantity}     £{float(item.price*item.quantity):.2f}")
        self.display_total()

    # Return all variables to their original state - use del??
    # This should be called when a sale is cancelled or completed
    def reset_register(self):
        self.__del__()


class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
    
    def get_item_name(self):
        return self.name


# EXAMPLE code run:
barcodes = {
    1: Item(name="Nintendo 3DS", price=90.00, quantity=1),
    2: Item(name="Nintendo Game Boy", price=50.00, quantity=1),
    3: Item(name="Nintendo Switch", price=299.99, quantity=1)
}

sale = CashRegister()
n = None
while True:
    n = input("Scan a barcode (1, 2, 3) or finish scanning (f): ")
    if n == 'f':
        break
    try:
        sale.add_item(barcodes[int(n)])
    except:
        print("Item does not exist.")

answer = input("Did you want to remove any items? (y/n): ")
if answer == 'y':
    remove = input("Please scan the barcode of the item you would like to remove (1, 2, 3): ")
    try:
        sale.remove_item(barcodes[int(remove)])
    except:
        print("Item does not exist.")

answer2 = input("Would you like to apply a discount? (y/n): ")
if answer2 == 'y':
    discount = input("Please input a percentage to be discounted: ")
    sale.apply_discount(int(discount))

sale.show_items()

to_pay = sale.return_total()
payment = None
while payment != 0:
    payment = int(input("Please enter your payment amount: "))
    to_pay = round(to_pay - payment, 2)
    if to_pay < 0:
        print(f"You have overpaid. Please take your change of £{abs(to_pay)}.")
        break
    elif to_pay > 0:
        print(f"You have underpaid. Please pay additional £{to_pay}.")
        

print("Thank you. Goodbye!")


#############################################
# Heidi 
#############################################

class CashRegister:

    def __init__(self):

        self.total_items = {} # I initiated this as an empty dict, did not see another way to do it! {'item': 'price'}
        self.total_price = 0.0 # I changed these to floats to match pricing!
        self.discount = 0.0
        self.items = [] # list of just the item names

    def add_item(self, item, price):
        self.total_items[item] = price
        return self.total_items

    def remove_item(self, item):
        del self.total_items[item]
        return self.total_items

    def apply_discount(self, disc_amt):
        self.discount = self.discount + disc_amt
        self.total_price = self.total_price - self.discount
        return self.total_price

    def get_total(self):
        self.total_price = 0 #
        for price in self.total_items.values():
            self.total_price = self.total_price + price
        return self.total_price

    def show_items(self):
        self.items = list(self.total_items.keys())
        self.items = ', '.join(self.items) # formatting to remove brackets and return as a text list
        return self.items

    def reset_register(self):
        self.total_items = {}  # {'item': 'price'}
        self.total_price = 0.0
        self.discount = 0.0

# Shop 1 adds items, calculates a total before discount, applies the discount and then gives total.
# Finally, it resets the register back to its initial state.
shop1 = CashRegister()
shop1.add_item("cucumber", .50)
shop1.add_item("red pepper", 1.50)
print('The items in your trolley are: {}'.format(shop1.show_items()))
shop1.get_total()
print('Your subtotal is: £{:.2f}'.format(shop1.total_price))
shop1.apply_discount(.25)
print('Total after discount applied: £{:.2f}'.format(shop1.total_price))
shop1.reset_register()
print('Thank you for shopping with us. Basket now empty: {}'.format(shop1.total_items))
#printed the empty basket total_items just to demonstrate!

## Shop 2 adds and deletes items, and shows subtotals and trolley status along the way
# shop2 = CashRegister()

# shop2.add_item("orange juice", 3.00)
# shop2.add_item("milk", 1.50)
# shop2.add_item("apricots", .50)
# shop2.add_item("blackberries", 2.00)
# print('The items in your trolley are: {}'.format(shop2.show_items()))
# shop2.get_total()
# print('Your subtotal is: £{:.2f}'.format(shop2.total_price))
# shop2.remove_item("orange juice")
# print('The items in your trolley are: {}'.format(shop2.show_items()))
# shop2.get_total()
# print('Your total is now: £{:.2f}'.format(shop2.total_price))
# shop2.reset_register()
# print('Thank you for shopping with us. Basket now empty: {}'.format(shop2.total_items))


#############################################
# Lakshika 
#############################################

class CashRegister:

    def __init__(self,total_items,total_price,discount):

        self.total_items = {} # {'item': 'price'}
        self.total_price = 0
        self.discount = 0
        

    def add_item(self, item, price):
        self.total_items[item] = price
        pass

    def remove_item(self,item):
        if item in self.total_items.keys():
            self.total_items.pop(item)
        else:
            print("This item does not exist in your basket. Please enter a valid item.")
        pass

    def apply_discount(self,discount):
        if self.discount <= 75:  #discount should not be greater than 75, can't give stuff for free :)
            deduct = self.total_price * (discount/100) 
            self.total_price = self.total_price - deduct
            return self.total_price
        else:
            print("Invalid discount")
        pass

    def get_total(self):
        for price in self.total_items.values():
            self.total_price  = self.total_price + int(price)
        return self.total_price
        pass

    def show_items(self):
        print("Below is the list of all the items in your basket. Please proceed to pay:")
        for item, price in self.total_items.items():
            print(item, ' : ', price)
        pass

    def reset_register(self):
        print("Starting afresh:")
        self.total_items.clear()
        return(self.total_items)
        pass


#EXAMPLE code run:

print("Welcome to XYZ Store, please select a task from the menu:")
print("1. Add items in my basket")
print("2. Remove an item from my basket")
print("3. Show all items in my basket")
print("4. Total to pay")
print("5. Apply Discount")
print("6. Restart")
print("7. Exit")

selection = int(input("Enter your selection:"))
#Creating an object
cr = CashRegister(0,0,0)

while selection!= 7:
    if selection == 1:
        item, price = input("Please input the item name and price:").split()
        cr.add_item(item,price)
        selection = int(input("To continue press 1 or enter something else"))

    elif selection == 2:
        item = input("Please input the item you wish to remove:")
        cr.remove_item(item)
        selection = int(input("To continue press 2 or enter something else."))

    elif selection == 3:
        cr.show_items()
        selection = int(input("Please enter what you wish to do next:"))

    elif selection == 4:
        payment = cr.get_total()
        print ("Please pay:", payment)
        selection = int(input("Please enter 5 to apply discount alternatively select what you wish to do next:"))

    elif selection == 5:
        disc = int(input("Please enter your discount"))
        payment = cr.apply_discount(disc)
        print ("Discount applied.Please pay:", payment)
        selection = int(input("Please enter 6  to restart again or 7 to check out:"))

    elif selection == 6:
        basket = cr.reset_register()
        print ("Basket has no items", basket)
        selection = int(input("Please enter what you wish to do next:"))


#############################################
# Robyn 
#############################################

class CashRegister:

    def __init__(self):
        self.total_items = {}  # {'item': 'price'}
        self.total_price = 0
        self.discount = 0

    # This is instead of the reset_register method. I did it this way so that
    # this is always run at the start of a new transaction to be sure
    # everything is reset and that it prints the business name at the top of
    # the print out like you would have on a receipt.
    def new_transaction(self):
        self.total_items.clear()
        self.total_price = 0
        self.discount = 0
        welcome = "ROBYN'S CORNER SHOP"
        print(f"\n"
              f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
              f"{welcome:^40}\n"
              f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def add_item(self, item, price):
        self.total_items[item.capitalize()] = price
        self.total_price += price
        print(f"{item.capitalize():>30s}{price:>10.2f}")

    def remove_item(self, item):
        try:
            removed = self.total_items.pop(item.capitalize())
        except KeyError:
            print("Item not found.")
        else:
            self.total_price -= removed
            item_str = f"*CANCELLED* {item.capitalize()}"  # Assign output messages to variables
            price_str = f"–{removed:.2f}"                  # so I can align within print function.
            print(f"{item_str:>30s}{price_str:>10}")

    def apply_discount(self, percentage_discount):
        self.discount = (percentage_discount/100) * self.total_price
        self.total_price = self.total_price - self.discount

    def get_total(self):
        print(f"————————————————————————————————————————")
        # Add discount details if discount was applied
        if self.discount:
            discount_str = "DISCOUNT APPLIED"
            discount_amount_str = f"-£{self.discount:.2f}"
            print(f"{discount_str:>30s}{discount_amount_str:>10}")
        total_str = "TOTAL"
        total_price_str = f"£{self.total_price:.2f}"
        print(f"{total_str:>30s}{total_price_str:>10}\n"
              f"————————————————————————————————————————")

    # This isn't really needed as I wanted the items to print out as they are
    # entered into the till because this is what would happen with a real till.
    # But have included it just in case it is required as it was part of the
    # starter code.
    def show_items(self):
        if not self.total_items:
            output = "No items added yet"
            print(f"{output:^40}")
        else:
            for item in self.total_items:
                price = f"£{self.total_items.get(item):.2f}"
                print(f"{item:>30s}{price:>10}")


# —————————————————————————————————————————————————————————————————————————————
# EXAMPLES OF CODE IN ACTION
# —————————————————————————————————————————————————————————————————————————————

# Create object of the CashRegister class.
till = CashRegister()

# Example customer with discount and changed mind about an item.
till.new_transaction()
till.add_item('bread', 1.10)
till.add_item('milk', 0.80)
till.add_item('picnic blanket', 12.50)
till.add_item('cornflakes', 2.80)
till.add_item('apples', 2.45)
till.add_item('wine', 11.00)
till.add_item('birthday cake', 7.50)
till.remove_item('picnic blanket')
till.apply_discount(15)
till.get_total()

# Example customer without discount
# Same till object used to demonstrate that new_transaction (i.e. register_rest) works.
till.new_transaction()
till.add_item('shampoo', 3.50)
till.add_item('pens', 2.40)
till.add_item('pencil case', 4.60)
till.add_item('chocolate bar', 0.75)
till.get_total()

# Example to prove that show_items works and that items are stored in
# total_items dict. (Although as I said early, not really needed as this code
# prints items as it goes like a normal till would.)
print("\n>>> till.show_items()")
till.show_items()


#############################################
# Stacy 
#############################################

class CashRegister:

    def __init__(self):

        self.total_items = None  # {'item': 'price'}
        self.total_price = 0
        self.discount = 0

    def add_item(self, item, price):

        if not isinstance(price, float):
            raise TypeError("price must be set to float")
        if self.total_items is None:
            self.total_items = dict({item: price})
        else:
            self.total_items[item] = self.total_items.get(item, 0) + price
            self.total_price += price

    def remove_item(self, item):
        if self.total_items is None:
            return 1
        # rm from the total price
        self.total_price -= self.total_items[item]
        # rm from total items
        self.total_items.pop(item)
        print("REMOVED -", item)

    def apply_discount(self, discount):
        if not isinstance(discount, int):
            raise TypeError("discount must be an integer")
        self.discount += float(discount)
        print("Discount of {}% Applied Successfully".format(discount))

    def get_total(self):
        disc = (self.discount / 100) * self.total_price
        if self.discount > 0:
            print('Total', ':', self.total_price - disc)
        else:
            print('Total', ':', self.total_price)

    def show_items(self):
        print('----------------------------')
        for key in self.total_items:
            print(key, ' : ', self.total_items[key])

    def reset_register(self):
        self.total_items = None  # {'item': 'price'}
        self.total_price = 0
        self.discount = 0


# EXAMPLE code run:
new_register = CashRegister()
new_register.add_item("coca-cola", 0.99)
new_register.add_item("coca-cola", 0.99)
new_register.add_item("shower gel", 15.67)
new_register.add_item("shower towel", 10.99)
new_register.show_items()
# remove the item by it's name
new_register.remove_item("coca-cola")
new_register.show_items()
new_register.get_total()
# discount gets applied in %
new_register.apply_discount(50)
new_register.get_total()

# I'd improve it and add items quantity, so I could remove multiple items


''' 

                    SOLUTIONS TO TASK 2   

Write a base class to represent a student. Below is a starter code. 
Feel free to add any more new features to your class. 
As a minimum a student has a name and age and a unique ID.
Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student. 
"""

# class CFGStudent(<should inherit from Student>)
#     create new methods that manage student's subects (add/remove new subject and its graade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)

'''


#############################################
# Bora 
#############################################


class Student:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()

class CFGStudent(Student):
    def getStdInfo(self):
        print('Student name : ', self.name, '\nAge: ', self.age, '\nID:', self.id)

    def addSpecialization(self, specialization):
        self.specialization = specialization
        print('Specialization :',self.specialization)

    def addSubject(self, subject, grade):
        self.subject = subject
        self.grade = grade
        self.subjects[self.subject] = grade

    def removeSubject(self, subject):
        self.subject = subject
        self.subjects.pop(subject)

    def getAvarage(self):
        aveGrade = 0
        count = 0
        for grade in self.subjects:
            aveGrade += self.subjects[grade]
            count += 1
        print('Overall grade for', self.name, 'is',aveGrade / count)

    def getSubjects(self):
        print(self.name, 'has taken below subjects for this semester')
        for sbj in self.subjects:
            print(sbj)
# EXAMPLE
# bora = CFGStudent('Bora Kim', 30, 1)

# ADD SUBJECTS
# bora.addSubject('Python Theory', 90)
# bora.addSubject('Python final assessment', 100)
# bora.addSubject('SQL Theory', 80)
# bora.addSubject('SQL final assessment', 99)
# bora.addSubject('AWS Theory', 80)
# bora.addSubject('AWS final assessment', 99)

# REMOVE SUBJECT
# bora.removeSubject('SQL Theory')
# bora.removeSubject('SQL final assessment')

# GET SUBJECTS
# bora.getSubjects()

# GET AVERAGE
# bora.getAvarage()

# ADD SPECIALIZATION AND PRINT
# bora.addSpecialization('Software')

# GET STUDENT INFO
# bora.getStdInfo()

# ANOTHER EXAMPLE
# pam = CFGStudent('Pam', 20, 2)
# pam.addSubject('AWS master class', 20)
# pam.getStdInfo()



#############################################
# Heidi 
#############################################


 class Student:

     def __init__(self, name, age, id):
         self.name = name
         self.age = age
         self.id = id
         self.subjects = dict()
         self.subj_names = []


 class CFGStudent(Student):


     def add_subj(self, subject, grade):
         self.subjects[subject] = grade


     def del_subj(self, subject):
         del self.subjects[subject]


     def view_subjs(self):
         self.subj_names = list(self.subjects.keys())
         self.subj_names = ', '.join(self.subj_names)
         return self.subj_names

     def calc_sum_of_grades(self):
         total_grade = 0
         for grade in self.subjects.values():
             total_grade += grade
         return total_grade

     def calc_avg_grade(self):
         try:
             avg_grade = self.calc_sum_of_grades() / (len(self.subjects.values()))
             return avg_grade

         except ZeroDivisionError:
             print('You have not entered any grades for this student yet.')
             return



## Mary Ellen demonstrates adding subjects and calculating an average
mary_ellen = CFGStudent('Mary Ellen', 28, 111)
mary_ellen.add_subj('Python 1', 88)
mary_ellen.add_subj('Python 2', 99)
print(mary_ellen.subjects)
print('{} is taking: {}'.format(mary_ellen.name, mary_ellen.view_subjs()))
print("{}'s final grade is: {}".format(mary_ellen.name, mary_ellen.calc_avg_grade()))

## Josie demonstrates adding and deleting subjects and calculating an average
josie = CFGStudent('Josie', 47, 112)
josie.add_subj('Intro to SQL', 59)
josie.add_subj('Advanced SQL', 65)
josie.add_subj('pandas', 83)
josie.add_subj('Python 1', 88)
print('{} is taking: {}'.format(josie.name, josie.view_subjs()))
josie.del_subj('Python 1')
print('After drop, {} is taking: {}'.format(josie.name, josie.view_subjs()))
print("{}'s final grade is: {}".format(josie.name, josie.calc_avg_grade()))


## Xena demonstrates what happens if you do not enter any grades
xena = CFGStudent('Xena', 32, 113)
print(xena.calc_avg_grade())


#############################################
# Lakshika 
#############################################

import statistics

class Student:

    def __init__(self, name, age, id, subjects):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()

class CFGStudent(Student):
    def __init__(self, name, age,id, subjects,specialisation):
        super().__init__(name, age, id, subjects)
        self.subjects = subjects
        self.average_mark = 0
        self.specialisation = specialisation

    def add_subject(self,new_subject,new_grade):
        self.subjects[new_subject] = new_grade
        pass

    def remove_subject(self,pop_subject):
        if pop_subject in self.subjects.keys():
            self.subjects.pop(pop_subject)
        else:
            print("This subject does not exist. Please enter a valid subject.")
        pass

    def view_allsubjects(self):
        print("Below is the list of all the subjects for the student:")
        print(self.subjects.keys())
        pass

    def avg_mark(self):
        values = self.subjects.values()
        marks_list = list(values)
        average_mark = statistics.mean(marks_list)
        return average_mark
        pass


subjects = {'Maths':50, 'English': 70}
Lakshika = CFGStudent('Lakshika', 25, 'E45',subjects,'Software')
Lakshika.add_subject('French', 90)
Lakshika.view_allsubjects()
Lakshika.remove_subject('French')
Lakshika.view_allsubjects() #view after removing a subject
avg_score = Lakshika.avg_mark()
print("Average score:",avg_score)


#############################################
# Robyn 
#############################################


# NOTE: I decided to remove subjects from the Student base class as it doesn't
#       work for all student types. For example, an A-level student would take
#       several subjects but a university student usually takes one subject.
#       Also a Nanodegree student doesn't really take subjects that have a
#       grade - we have assessments and grades. So having a dictionary of
#       subjects and grades doesn't make sense in the base class. These details
#       are specific to the type of student.


class Student:
    """A base class to represent a student"""

    def __init__(self, fname, lname, age, institution, s_id):
        """Initialise the class Student
        :param fname: student's first name
        :type fname: str
        :param lname: student's last name
        :type lname: str
        :param age: student's age
        :type age: int
        :param institution: student's institution
        :type institution: str
        :param id: student's student ID reference
        :type id: str
        """
        self.fname = fname.capitalize()
        self.lname = lname.capitalize()
        self.age = age  # it would make more sense if this was DOB but the task specifies a student has to have an age
        self.institution = institution.title()
        self.s_id = s_id

    def view_student_details(self):
        """Print out data held on a student
        :return: print out of student details
        """
        print(f"–––––––––––––––\n"
              f"STUDENT DETAILS\n"
              f"–––––––––––––––\n"
              f"First Name: {self.fname}\n"
              f"Last Name: {self.lname}\n"
              f"Age: {self.age}\n"
              f"Institution: {self.institution}\n"
              f"Student ID: {self.s_id}\n")


# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# WRITE A SUBCLASS TO REPRESENT A NANODEGREE STUDENT
# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––


class CFGNanoStudent(Student):
    """A subclass of Student to represent a Code First Girls Nanodegree student"""

    def __init__(self, fname, lname, age, institution, s_id, specialisation):
        """Initialise the CFGNanoStudent subclass
        :param fname: student's first name
        :type fname: str
        :param lname: student's last name
        :type lname: str
        :param age: student's age
        :type age: int
        :param institution: student's institution
        :type institution: str
        :param s_id: students student ID
        :type s_id: str
        :param specialisation: Nanodegree specialisation – software or data
        :type specialisation: str
        """
        super().__init__(fname, lname, age, institution, s_id)
        self.course = "Nanodegree"
        self.specialisation = specialisation.capitalize()
        self.modules = set()
        self.grades = {"Foundation Theory": None,
                       "Specialisation Theory": None,
                       "Foundation Exam": None,
                       "Specialisation Exam": None,
                       "Homework": None,
                       "Project": None}
        self.final_result = None

    def view_student_details(self):
        """Print out data held on a CFG Nanodegree student.
        Overrides Student.view_student_details(self).
        :return: print out of student details
        """
        print(f"\n–––––––––––––––\n"
              f"STUDENT DETAILS\n"
              f"–––––––––––––––\n"
              f"First Name: {self.fname}\n"
              f"Last Name: {self.lname}\n"
              f"Age: {self.age}\n"
              f"Institution: {self.institution}\n"
              f"Student ID: {self.s_id}\n"
              f"Course: {self.course}\n"
              f"Specialisation: {self.specialisation}\n"
              f"Modules: {', '.join(self.modules)}\n"
              f"Final Result: {self.final_result}\n")

    def module_reg(self, module_name):
        """Register student on a module
        :param module_name: name of module
        :type module_name: str
        :return: adds named module to student's modules set
        """
        self.modules.add(module_name)
        print(f"{self.fname} {self.lname} has been successfully registered on "
              f"{module_name}.")

    def module_dereg(self, module_name):
        """De-register student for a module
        :param module_name: name of module
        :type module_name: str
        :return: removes named module from student's modules set
        """
        self.modules.discard(module_name)
        print(f"{self.fname} {self.lname} is no longer registered on "
              f"{module_name}.")

    def add_grade(self, assessment, grade):
        """Add a grade for the specified assessment
        :param assessment: name of assessment, must be one of:
                           "Foundation Theory"
                           "Specialisation Theory"
                           "Foundation Exam"
                           "Specialisation Exam"
                           "Homework"
                           "Project"
        :type assessment: str
        :param grade: grade achieved in assessment (%)
        :type grade: int
        :return: grade is added as a value to the specified assessment key in
                 the student's grades dict
        """
        assessment = assessment.title()
        try:
            self.grades[assessment] = grade
        except KeyError:
            print("Assessment type not found.")
        else:
            print(f"Mark successfully entered on the student's record.")

    def weighted_grade(self):
        """Calculates the Nanodegree student's final weighted grade
        :return: grade (%) assigned to self.final_result
        """
        # Assessment weightings
        w_foundation_theory = 5
        w_specialisation_theory = 5
        w_foundation_exam = 20
        w_specialisation_exam = 20
        w_homework = 10
        w_project = 40

        # Student's results
        r_foundation_theory = self.grades["Foundation Theory"]
        r_specialisation_theory = self.grades["Specialisation Theory"]
        r_foundation_exam = self.grades["Foundation Exam"]
        r_specialisation_exam = self.grades["Specialisation Exam"]
        r_homework = self.grades["Homework"]
        r_project = self.grades["Project"]

        # Calculate weighted grade
        weighted_grade = (
                                 (w_foundation_theory * r_foundation_theory) +
                                 (w_specialisation_theory * r_specialisation_theory) +
                                 (w_foundation_exam * r_foundation_exam) +
                                 (w_specialisation_exam * r_specialisation_exam) +
                                 (w_homework * r_homework) +
                                 (w_project * r_project)
                         ) / 100

        self.final_result = weighted_grade
        print(f"Nanodegree Final Grade: {int(weighted_grade)} %")


# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# EXAMPLES OF CODE IN ACTION
# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

# Examples of base class Student
e_evans = Student('elen',
                  'evans',
                  26,
                  "code first girls",
                  394827)

s_williams = Student('sioned',
                     'williams',
                     23,
                     "lancaster university",
                     394144)

e_evans.view_student_details()
s_williams.view_student_details()


# Example Nanodegree student
e_jones = CFGNanoStudent('eleri',
                         'jones',
                         27,
                         "Code First Girls",
                         294839,
                         "software")

# Register Eleri on modules
e_jones.module_reg("Python Foundation")
e_jones.module_reg("Software Specialisation")
e_jones.view_student_details()

# Eleri was mistakenly registered on Python Foundation. She should have been
# registered on Python Refresher and SQL Foundation.
e_jones.module_dereg("Python Foundation")
e_jones.module_reg("Python Refresher")
e_jones.module_reg("SQL Foundation")
e_jones.view_student_details()

# Add grades and calculate final grade
e_jones.add_grade("Foundation Theory", 78)
e_jones.add_grade("Specialisation Theory", 82)
e_jones.add_grade("Foundation Exam", 67)
e_jones.add_grade("Specialisation Exam", 71)
e_jones.add_grade("Homework", 94)
e_jones.add_grade("Project", 76)
e_jones.weighted_grade()
e_jones.view_student_details()


# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# DOCUMENTING CLASSES AND METHODS
# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Not part of the assessment but wanted to play with documenting my methods.
# This is helpful when reading through the code and you can also print the
# __doc__ method. The docstring also opens as a pop up when you hover over the
# method name in PyCharm. There are different docstring formats. These use the
# reStructured Text format, which is the official Python documentation
# standard. Others include Google docstrings, NumPy/SciPy docstrings and
# Epytext.

print(Student.__doc__)
print(CFGNanoStudent.__doc__)
print(CFGNanoStudent.view_student_details.__doc__)


#############################################
# Vanessa 
#############################################

class Student():

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id


# EXAMPLE RUN
originalstudent = Student('Bonnie', 20, 1)


class SofwareStudent(Student):
     def __init__(self, name, age, id, year):
        super().__init__(name, age, id)
        self.year = year

    def intro(self):
        print(f"Hello, my name is {self.name} and I am studying Software engineering. I am in my {self.year} year.")


# EXAMPLE RUN
student1 = SofwareStudent('May', 19, 2, '2nd')
student1.intro()


 # class CFGStudent(<should inherit from Student>)
 #     create new methods that manage student's subects (add/remove new subject and its graade to the dict)
 #     create a method to view all subjects taken by a student
 #     create a method  (and a new variable) to get student's overall mark (use average)


 # creating child class of student called CFGStudent
class CFGStudent(Student):

# adding the parent class's attributes as well as creating new ones where average mark and subjects can be stored.
    def __init__(self, name, age, id):
        super().__init__(name, age, id)
        self.average_mark = 0
        self.subjects = None

# a method that adds the student's subjects.
    def add_subject(self, subjects):
        self.subjects = subjects
        return self.subjects

# a method that can remove a student's subject.
    def remove_subject(self, subject):
        subjects_dict = self.subjects
        subjects_dict.pop(subject)
        return self.subjects

# a method that allows us to see the subjects that the student is currently enrolled in.
    def view_subject(self):
        subjects_dict = self.subjects
        subjects = list(dict.keys(subjects_dict))
        print(f"{self.name} is studying: ")
        for subject in subjects:
            print(subject)

# a method that calculates a student's average mark in their subjects.
    def calc_overall_mark(self):
        subjects_dict = self.subjects
        subjects_values = subjects_dict.values()
        average_mark = sum(subjects_values)/len(subjects_values)
        self.average_mark = average_mark
        return self.average_mark

# a method that allows us to view a student's average mark
    def view_average_mark(self):
        print(f"Your average mark is: {self.average_mark}")

# EXAMPLE RUN
cfgstudent = CFGStudent('Autumn', 26, 3)
cfgstudent.add_subject({'Python': 70, 'SQL': 67, 'Javascript': 58, 'HTML': 30, 'Java': 50})
cfgstudent.view_subject()
cfgstudent.remove_subject('Javascript')
cfgstudent.view_subject()
cfgstudent.calc_overall_mark()
cfgstudent.view_average_mark()
