from tripdata import get_trip as get_tripdata
from datetime import datetime
import json
trips=[
    get_tripdata("New York", "25-12-2022"),
    get_tripdata("Los Angeles","10-09-2024"),
    get_tripdata("Chicago", "15-05-2023")
]
for trip in trips:
    date_obj=datetime.strptime(trip["date"], '%d-%m-%Y')
    trip["date"] = date_obj.strftime("%B %d, %Y")
trips_json = json.dumps(trips,indent=4)
print(trips_json)