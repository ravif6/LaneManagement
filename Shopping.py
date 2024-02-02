from collections import deque
from Customer import Customer
from RegularLane import RegularLane
from SelfServiceLane import SelfServiceLane
from LaneTypeEnum import LaneType
from constants import MAX_REGULAR_LANE,MAX_REGULAR_LANE_CUSTOMERS,MAX_SELF_SERVICE,MAX_SELF_SERVICE_CUSTOMERS
class Shopping:
    def __init__(self) -> None:
        self.available_lanes=set([0,5])
        self.lanes = deque([RegularLane()]*5 + [SelfServiceLane()])
        self.customer = [0]*(MAX_SELF_SERVICE*MAX_SELF_SERVICE_CUSTOMERS + MAX_REGULAR_LANE*MAX_REGULAR_LANE_CUSTOMERS)
        self.available_customers
        
    def check():
        pass
    def display_lane_status(self):
        for lane_id in range(len(self.lanes)):
            current_lane = self.lanes[lane_id]
            stars = "closed" if current_lane.customer_count == 0 else '* '* current_lane.customer_count
            print(f"L{lane_id} ({current_lane.name})-> {stars}")
    def assign_customer_to_lane(self,customer:Customer):
        for current_lane in self.available_lanes[customer.Lane]:
                if self.lanes[current_lane].is_open():
                    self.lanes[current_lane].customer_count +=1
                    customer.Lane_id = current_lane
                    self.lanes[current_lane].customers.append(customer)
                    return True
        return False 
    # def allocate_to_lane(self,lane_type:LaneType):
    #     for current_lane in self.available_lanes[lane_type]:
    #             if self.lanes[current_lane].is_open():
    #                 self.lanes[current_lane].customer_count +=1
    #                 return True 
                
    def remove_customer_from_lane(self,customer:Customer):
        self.lanes[customer.Lane_id].customer_count-=1
        self.customer-=1