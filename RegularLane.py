from Lane import Base_Lane
from constants import MAX_REGULAR_LANE_CUSTOMERS
from LaneInterface import LaneInterface
class RegularLane(Base_Lane,LaneInterface):
    def __init__(self,lane_id) -> None:
        super().__init__()
        self.lane_id = lane_id
        self.name = "Reg"
        self.capacity = MAX_REGULAR_LANE_CUSTOMERS
    
    #add customer
    def add_customer(self, customer):
        if len(self.customers) < self.capacity:
            self.customers.append(customer)
            self.open_lane()
        else:
            print(f"Lane {self.name} is full. Cannot add more customers.")
    
    # display lane status
    def display_lane(self,lane_id):
        stars = "closed" if self.customer_count>0  else '* '* self.customer_count
        print(f"L{lane_id} ({self.name})-> {stars}")
        
    def get_lane_status(self):
        if self.customer_count  >= self.capacity:
            self.is_opened = False
        return self.is_opened
    