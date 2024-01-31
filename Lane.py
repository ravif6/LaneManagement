from collections import deque
from Customer import Customer

class Base_Lane():
    # generate a lane constructor
    def __init__(self) -> None:
        self.customer_count = 1
        self.is_opened = True
        self.customers :deque[Customer]= deque([])
        self.end_time = 0
        # self.capacity = capacity
    
    #remove customer from a lane
    def remove_customer(self):
        if self.customers:
            self.customers.popleft()
        if not self.customers:
           self.close_lane()
    
    #open the lane
    def open_lane(self):
        self.is_opened = True
    
    #close the lane
    def close_lane(self):
        self.is_opened = False
        




    
        