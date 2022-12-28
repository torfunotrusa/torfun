import json
from woocommerce import API

wcapi = API(
    url="https://www.otrusa.com/",
    consumer_key="ck_345a09819d5dc2ad29f36fc23088076cacdbc085",
    consumer_secret="cs_440a066d02641852054093c9dd70f2cbc1b92436",
    version="wc/v3"
)

deleted_id = [707380,843232,843295,843330,843333,843608,843863,843864,843873,843932,843933,844144,844450,844660,844711,844999,845067,845102,845107,845182,845258,845336,845350,845407,845466,845609,845863,845879,846271,846296,846525,846540,846545,846731,846891,846942,847048,847060,847101,847105,847131,847258,847181,847299,847337,847485,847493,847601,847643,847646,847954,848016]

for i in deleted_id:
    # print (i)
   x = (wcapi.get(f"products/{i}").json())
   y = x["name"]
   print(y)

# product_data = wcapi.delete("products/652084").json()
# product_deleted_name = product_data["name"]

# print(f"this product has been deleted > {product_deleted_name}")
