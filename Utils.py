import random
import uuid

def get_random(start,end):
    return random.randint(start, end)

def generate_unique_id():
    unique_id = uuid.uuid4()
    return str(unique_id)
# from datetime import datetime, timedelta
# def add_to_time(date_time, seconds):
#     new_datetime = date_time + timedelta(seconds)
# def date_to_int(date):
    
# # Create a datetime object
# current_datetime = datetime.now()
# print("Current Datetime:", current_datetime)

# # Add time to the datetime object
# time_to_add = timedelta(hours=2, minutes=30)
# new_datetime = current_datetime + time_to_add
# print("New Datetime (after adding time):", new_datetime)

# # Convert a datetime object to an integer timestamp (Unix timestamp)
# timestamp = int(new_datetime.timestamp())
# print("Timestamp:", timestamp)

    
