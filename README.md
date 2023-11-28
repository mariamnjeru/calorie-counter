# Order and Calorie Counting

## Introduction

This Python code implements an Order class that manages customer orders for meals and combos from a menu. It allows customers to place two separate orders, calculates the total calories and price for each order, and provides information on the order status.

## Files

1. **menu_info.py**
   - Contains information about available meals and combos in the menu.

2. **util.py**
   - Provides utility functions for calculating the total calories and price of ordered items.

3. **classes.py**
   - Implements the Order class, allowing customers to place orders, checks for order acceptance based on calorie limits, and provides order details.

## Usage

1. **Importing Dependencies**
   - The code imports necessary modules and initializes the Order class.

2. **Order Class Overview**
   - The `Order` class has attributes, properties, and methods to manage and process customer orders.

   - Attributes:
     - `order_id`: A unique identifier for the order.
     - `order_accepted`: Indicates whether the order was accepted.
     - `order_refused_reason`: The reason for refusing the order.
     - `date`: The date and time of the order.
     - `items`: A list of item IDs for the ordered items.

   - Properties:
     - `calories`: The total calories for the order.
     - `price`: The total price for the order.

   - Class Attributes:
     - `order_counter`: A counter for generating unique order IDs.

   - Methods:
     - `place_order()`: Prompts the user to place two separate orders and checks if the ordered items are in the menu. If valid, it adds the items to the order.
     - `accept_order()`: Accepts or declines the order based on the total calories. If the total calories exceed 2000, the order is declined with a calorie limit exceeded reason.

3. **Example Usage**
   - An example of using the `Order` class is provided, where an order is placed, its acceptance is determined, and order details are printed.

   ```python
   order = Order()
   order.place_order()
   order.accept_order()
   print(f"Order Number: {order.order_id}")
   print(order.order_refused_reason)
   print("Total Calories:", order.calories)
   print("Total Price:", order.price)
