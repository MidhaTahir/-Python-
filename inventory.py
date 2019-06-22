#inventory using functions
def order():
    print("Each box price is Rs.3000/-")
    enter = int(input("Enter how many boxes you want to order: "))
    return enter
def bill(box):
    unit_cost = 3000
    price = box * unit_cost
    return price
def discount(offer):
    if offer >= 50000:
        user_discount= 0.5*offer
        new_price = offer - user_discount
        print("You are offered a discount of: "+str(user_discount)+" The new price of your order is :"+str(new_price))
    elif offer >=25000:
        user_discount= 0.25*offer
        new_price = offer - user_discount
        print("You are offered a discount of: "+str(user_discount)+" The new price of your order is :"+str(new_price))
    else:
        print("No Discount!")
user_order = order()
user_bill = bill(user_order)
print("Your bill is :" + str(user_bill))
user_discount = discount(user_bill)

    