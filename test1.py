import os
import datetime
import pytz

ist = pytz.timezone('Asia/Kolkata')
timestamp_ist = datetime.datetime.now(ist).strftime("%Y%m%d%H%M%S")
print(f"Current Data & Time: {timestamp_ist}")
print("Test1")
print("This is branch_1")
print("This is branch_1_tag_V1.0.0")
print("THis is release V1.0.1")
print("THis is release V2.0.0")