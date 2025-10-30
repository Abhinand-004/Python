from tracker import create_record
from datetime import datetime
import json
records = [
    create_record("Bali", "05-06-2022", "Enjoyed the beaches and sunsets."),
    create_record("Rome", "14-09-2023", "Loved the ancient architecture."),
    create_record("Sydney", "20-12-2024", "Amazing New Year fireworks!")
]
for record in records:
    date_obj = datetime.strptime(record["date"], "%d-%m-%Y")
    record["date"] = date_obj.strftime("%B %d, %Y") 
json_data = json.dumps(records)
print(json_data)
parsed_records = json.loads(json_data)
for rec in parsed_records:
    print(rec)
