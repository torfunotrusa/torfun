import json
from woocommerce import API

wcapi = API(
    url="https://www.otrusa.com/",
    consumer_key="ck_345a09819d5dc2ad29f36fc23088076cacdbc085",
    consumer_secret="cs_440a066d02641852054093c9dd70f2cbc1b92436",
    version="wc/v3"
)

print(wcapi.get("products/847337", params={"per_page": 20}).json())

# First Batch
# deleted_id = [843295,843330,843333,843608,843863,843864,843873,843932,843933,844144,844450,844660,844711,844999,845067,845102,845107,845182,845258,845336,845350,845407,845466,845609,845863,845879,846271,846296,846525,846540,846545,846731,846891,846942,847048,847060,847101,847105,847131,847258,847181,847337,847485,847493,847601,847643,847646,847954,848016]

# Duplicate
# deleted_id = [842326,653622,660141,591024,706809,750477,751139,751201,751247,751288,751595,751640,751823,751881,752000,752459,843976,844708,846274,845146,653808]

for i in deleted_id:
    respond = (wcapi.delete(f"products/{i}", params={"force":False}).json())
    respond_name = respond["name"]
    respond_id = respond["id"]
    print(f"Product ID: {respond_id} Name: {respond_name} Has been moved to trash")
   