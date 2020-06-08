# Route Finding: Find a route from Johnson Creek to Columbia Blvd on I-205 NB using the upstream and downstream fields.

import pymongo
import time

client = pymongo.MongoClient("mongodb+srv://admin:admin@cs488p3-o8kgj.gcp.mongodb.net/cs488?retryWrites=true&w=majority")
db = client.cs488
co = db.freeway_stations

start_time = time.time()

start = "Johnson Cr NB"
end = "Columbia to I-205 NB"

station = co.find_one({"locationtext": start})

print("The route from %s to %s is: " % (start, end))
print(station["locationtext"])

flag = 1
while flag:
        next_station = co.find_one({"stationid": station["downstream"]})
        print(next_station["locationtext"])
        station = next_station
        if next_station["locationtext"] == end:
            flag = 0


print("")
print("--- query execution time: %s seconds ---" % (time.time() - start_time))

client.close()
