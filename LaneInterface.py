from collections import deque
from abc import ABC, abstractmethod

# abstract class with abstract and concrete methods
class LaneInterface(ABC):
    # generate a lane constructor
    # def __init__(self) -> None:
    #     self.customer_count = 0
    #     self.is_opened = False
    #     self.customers :deque[Customer]= deque([])
    #     self.end_time = 0
        # self.capacity = capacity
    
    #add customer to lane
    @abstractmethod
    def add_customer(self, customer):
        pass
    
    @abstractmethod
    def display_lane(lane_id):
        pass
    
    @abstractmethod
    def display_lane(self,lane_id):
        pass