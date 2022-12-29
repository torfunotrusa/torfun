import json
from woocommerce import API

wcapi = API(
    url="https://staging-otrusa.kinsta.cloud/",
    consumer_key="ck_822523119e6eb530d372231aae1c45bff22329bb",
    consumer_secret="cs_ae2f4bd88b9af2e70bb948ed82c512ac545e28fd",
    version="wc/v3"
)

# deleted_id = [707380,843232,843295,843330,843333,843608,843863,843864,843873,843932,843933,844144,844450,844660,844711,844999,845067,845102,845107,845182,845258,845336,845350,845407,845466,845609,845863,845879,846271,846296,846525,846540,846545,846731,846891,846942,847048,847060,847101,847105,847131,847258,847181,847299,847337,847485,847493,847601,847643,847646,847954,848016]

deleted_id = [845079]

for i in deleted_id:
    respond = (wcapi.delete(f"products/{i}", params={"force":False}).json())
    respond_name = respond["name"]
    respond_id = respond["id"]
    print(f"Product ID: {respond_id} Name: {respond_name} Has been moved to trash")
   