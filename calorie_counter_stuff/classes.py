from menu_info import meals, combos
from util import cal_count, price_count
import datetime
import itertools

"""
This code defines an Order class to manage and process customer orders for meals and combos from a menu. It allows customers to place two separate orders and calculates the total calories and price for each order. If the total calories of an order exceed 2000, the order is declined with a reason.

The Order class has the following attributes and properties:

Attributes:
    - order_id (int): A unique identifier for the order.
    - order_accepted (bool): Indicates whether the order was accepted.
    - order_refused_reason (str): The reason for refusing the order.
    - date (datetime): The date and time of the order.
    - items (list): A list of item IDs for the ordered items.

Properties:
    - calories (int): The total calories for the order.
    - price (int): The total price for the order.

Class Attributes:
    - order_counter (itertools.count): A counter for generating unique order IDs.

Methods:
    - place_order(): Prompts the user to place two separate orders and checks if the ordered items are in the menu. If valid, it adds the items to the order.
    - accept_order(): Accepts or declines the order based on the total calories. If the total calories exceed 2000, the order is declined with a calorie limit exceeded reason.

The code initializes an Order instance, allows customers to place orders, checks for order acceptance, and provides order details, including the order number, refusal reason, total calories, and total price.

Example usage:
order = Order()
order.place_order()
order.accept_order()
print(f"Order Number: {order.order_id}")
print("Order Refused Reason:", order.order_refused_reason)
print("Total Calories:", order.calories)
print("Total Price:", order.price)
"""


class Order:
    classmethod
    order_counter = itertools.count(1)

    def __init__(self, order_id: str = "", order_accepted: bool = False, order_refused_reason: str = ""):
        self.order_id = next(self.order_counter)
        self.order_accepted = order_accepted
        self.order_refused_reason = order_refused_reason
        self.date = datetime.datetime.now()
        self.items = []

    def place_order(self):
        cust_input1 = input("Place your first order(Enter id): ")
        cust_input2 = input("Place your second order(Enter id): ")
        
        if any(item["id"] == cust_input1 for item in meals) or any(item["id"] == cust_input1 for item in combos):
            print(f"Your first order is {cust_input1}")
            self.items.append(cust_input1)
        else:
            print("First order Declined. Item not in menu")

        if any(item["id"] == cust_input2 for item in meals) or any(item["id"] == cust_input2 for item in combos):
            print(f"Your second order is {cust_input2}")
            self.items.append(cust_input2)
        else:
            print("Second order Declined. Item not in menu")

    def accept_order(self):
        total_calories = cal_count(*self.items)
        if total_calories <= 2000:
            self.order_accepted = True
            print("Order Accepted")
        else:
            self.order_refused_reason = "Calorie limit exceeded"
            print("Order Declined")

    @property
    def calories(self):
        return cal_count(*self.items)

    @property
    def price(self):
        return price_count(*self.items)

order = Order()
order.place_order()
order.accept_order()
print(f"Order Number: {order.order_id}")
print(order.order_refused_reason)
print("Total Calories:", order.calories)
print("Total Price:", order.price)
