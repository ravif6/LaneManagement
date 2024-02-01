from Shopping import Shopping
from Customer import Customer
from Utils import get_random
from constants import MAX_ITEMS_IN_BASKET
from LaneTypeEnum import LaneType
from datetime import datetime

def main():
    while True:
        shop = Shopping()
        for i in range(10):
            items = get_random(1,MAX_ITEMS_IN_BASKET)
            lane_type = get_random(1,2)
            # checking criteria is it feasible to join SLF or not 
            if lane_type == LaneType.SLF (items >10 or shop.lanes[shop.available_lanes[LaneType.SLF]].is_open()):
                lane_type == LaneType.REG
                
            customer = Customer(items,lane_type)
            shop.assign_customer_to_lane(customer)
            # if not shop.assign_customer_to_lane(customer):
            #     return "Saturation point"
            
        