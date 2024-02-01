from datetime import datetime
from LaneTypeEnum import LaneType
from constants import MAX_ITEMS_IN_BASKET, REG_FIXED_TIME,SLF_FIXED_TIME
from Utils import get_random,generate_unique_id

class Customer:
    # items and lottery is private as we are generating lottery ticket from it.
    def __init__(self) -> None:
        self.__items = get_random(1,MAX_ITEMS_IN_BASKET)
        # lane_type = get_random(0,len(self.available_lanes)-1)
        self.id = generate_unique_id()
        self.created = int(datetime.now().timestamp())
        # self.lane = lane_name
        # self.lane_id = lane_type
        # self.lane_assigned = False
        self.lane_id = LaneType.REG
        self.__lottery = get_random(1,10)
        self.lane_assigned = False
        
    # get the no of items in basket
    def get_items_count_in_basket(self):
        return self.__items
    
    # get the checkout time based on lane and no of items
    def get_checkout_time(self):
        if self.lane_id == LaneType.REG:
            return REG_FIXED_TIME * self.__items + self.created
        return SLF_FIXED_TIME * self.__items + self.created
    
    # generating lottery randomly 
    def hasLottery(self):
        return self.__items >= 10 and  True if self.__lottery % 5 else False
    
    #get and display basket size of customers and processing time
    def display_basket_details(self):
        if self.hasLottery(): 
           print("items in your basket: ",self.get_items_count_in_basket()," You won a lottery ticket!")
        else:
           print("You have items in your basket: ",self.get_items_count_in_basket(),". Unlucky, no lottery ticket this time ")
        print("time to process basket at cashier till: ",self.get_items_count_in_basket()*REG_FIXED_TIME)
        print("time to process basket at self-service till: ",self.get_items_count_in_basket()*SLF_FIXED_TIME)
        


        
    