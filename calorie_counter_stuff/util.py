import json
from menu_info import calories_dict, combos_dict, meal_price_dict, combo_price_dict

def cal_count(*meals):
    
    count = 0

    for meal in meals:
        if meal in calories_dict:
            count += calories_dict[meal]
    
        else:
            try:
                    combo_meal = combos_dict[meal]
                    for meal in combo_meal:
                        if meal in calories_dict:
                            count += calories_dict[meal]  
            except KeyError: 
                print ("Food not found in our DataBase") 
    return count
            
def price_count(*meals):
    
    count = 0

    for meal in meals:
        if meal in meal_price_dict:
            count += meal_price_dict[meal]
    
        else:
            try:
                    combo_meal = combo_price_dict[meal]
                    if meal in combo_price_dict:
                        count += combo_price_dict[meal]  
            except KeyError: 
                print ("Food not found in our DataBase") 
    return count
