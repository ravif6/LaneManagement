from collections import deque
import threading
import time
from typing import Dict
from Customer import Customer
from LaneTypeEnum import LaneType
from RegularLane import RegularLane
from SelfServiceLane import SelfServiceLane
from datetime import datetime
# from Shopping import Shopping
from Utils import get_random
from constants import MAX_ITEMS_IN_BASKET, MAX_REGULAR_LANE,MAX_REGULAR_LANE_CUSTOMERS,MAX_SELF_SERVICE,MAX_SELF_SERVICE_CUSTOMERS

class Simulation:
    def __init__(self,simulation_time) -> None:
        # set up lanes
        self.stop_event = threading.Event()
        self.regular_lanes = [RegularLane(lane_id) for lane_id in range(5)]
        self.self_service_lane = SelfServiceLane(5)
        self.open_lanes = [self.regular_lanes[0], self.self_service_lane]
       
        self.lanes = self.regular_lanes + [self.self_service_lane]
       # self.customer = [Customer()]*(MAX_SELF_SERVICE*MAX_SELF_SERVICE_CUSTOMERS + MAX_REGULAR_LANE*MAX_REGULAR_LANE_CUSTOMERS)
        self.customer_count = 0
        self.customers :Dict[str, Customer] ={}
        self.simulation_time_limit = simulation_time
        
    def assign_customer_to_lane(self):
        current_customers = self.customers.copy()
        if not self.customers:
            return
        for customer_id in current_customers:
           # print("entered to assign ------ ",len(list(self.customers.keys())))
            customer = self.customers[customer_id]
            if customer.lane_assigned:
                print("already assigned")
                continue
            # print(customer.created)
            #current_lane : RegularLane | SelfServiceLane = \
            current_lane = None
            if customer.get_items_count_in_basket() < 10 and self.self_service_lane.get_lane_status():
                self.self_service_lane.add_customer(customer)
                current_lane = self.self_service_lane
            else:
                for lane in self.regular_lanes:
                    if lane.is_opened:
                        current_lane = lane
                        lane.add_customer(customer)
                        break  # Assign to the first available regular lane
            if current_lane:
                customer.created = max(int(current_lane.end_time),int(datetime.now().timestamp()))
                current_lane.customer_count +=1
                current_lane.end_time = customer.get_checkout_time()
                customer.lane_assigned = True

    def generate_more_customers(self):
        for _ in range(10):
            customer = Customer()
            self.customers[customer.id] = customer
        self.customer_count=10
        print("Generated new set of customers and items. ")
        while True and self.customer_count <= 40:
            time.sleep(3)
            customer = Customer()
            self.customers[customer.id] = customer
            self.customer_count+=1
            self.assign_customer_to_lane()
            print("customers = ",self.customer_count)
            
            
    
    def manage_lanes(self):
        for lane in self.open_lanes:
            current_lane:RegularLane | SelfServiceLane = self.lanes[lane]
            max_customers =  MAX_REGULAR_LANE_CUSTOMERS if current_lane.name == LaneType.REG else MAX_SELF_SERVICE_CUSTOMERS 
            if current_lane.customer_count >= max_customers:
                current_lane.close_lane()
            else:
                current_lane.open_lane()
        for lane in range(len(self.lanes)):
            if lane not in self.open_lanes:
                self.open_lanes.append(lane)
                break
            
    def manage_customers(self):
        for lane in self.open_lanes:
            for customer_id in lane.customers:
                customer = self.customers[customer_id]
                current_lane : RegularLane | SelfServiceLane = self.lanes[lane]
                print(" customer ==========         ", customer.created,int(datetime.now().timestamp()))
                if customer.get_checkout_time() >= int(datetime.now().timestamp()):
                    current_lane.customers.popleft()
                    current_lane.customer_count-=1
                    del self.customers[customer_id]
                    self.customer_count-=1
                    break
    
    def display_simulation_state(self):
        # Display simulation state at intervals
        while True and self.customer_count<15: #check it
            time.sleep(10)  # Adjust the interval for displaying simulation state
            print("\nSimulation State:")
            
            # for lane_id,lane in enumerate(self.lanes):
            #     print(lane.lane_id,lane,lane_id)
            #     lane.display_lane(lane_id)
            for lane_id,lane in enumerate(self.regular_lanes):
                lane.display_lane(lane_id)
            self.self_service_lane.display_lane(5)
            print(f"Total customers waiting at {time.strftime('%H:%M:%S')} is {self.customer_count}")
            for customer in self.customers.values():
                customer.display_basket_details()

    def run_simulation(self):
        # Run the simulation
        generate_customers_thread = threading.Thread(target=self.generate_more_customers)
        assign_customers_thread = threading.Thread(target=self.assign_customer_to_lane)
        manage_lanes_thread = threading.Thread(target=self.manage_lanes)
        manage_customers_thread = threading.Thread(target=self.manage_customers)
        display_state_thread = threading.Thread(target=self.display_simulation_state)
        
        self.regular_lanes[0].open_lane()
        self.self_service_lane.open_lane()
        assign_customers_thread.start()
        generate_customers_thread.start()
        manage_lanes_thread.start()
        manage_customers_thread.start()
        display_state_thread.start()

        # Keep the simulation running for a limited time
        time.sleep(self.simulation_time_limit)

        # End the simulation
        assign_customers_thread.join()
        generate_customers_thread.join()
        manage_lanes_thread.join()
        manage_customers_thread.join()
        if self.customer_count> 35:
            self.stop_event.set()
        display_state_thread.join()
        while(True):
            if (self.customer_count>3):
                self.stop_event.set()

if __name__ == "__main__":
    import threading
    simulation = Simulation(30)
    simulation.run_simulation()