# Volume: Find the total volume for the station Foster NB for Sept 21, 2011.

import pymongo
import time

client = pymongo.MongoClient("mongodb+srv://admin:admin@cs488p3-o8kgj.gcp.mongodb.net/cs488?retryWrites=true&w=majority")
db = client.cs488
co = db.freeway_loopdata
co1 = db.freeway_detectors

start_time = time.time()

station = "Foster NB"
total = 0

for x in co1.find({"locationtext": station}):
        result = co.aggregate([{"$match": {"detectorid": x["detectorid"]}},
                       {"$match": {"starttime": {"$gte": "2011-09-21 00:00:00", "$lt": "2011-09-22 00:00:00"}}},
                       {"$group": {"_id": "$detectorid", "total": {"$sum": "$volume"}}}])

        for x in result:
            total += x["total"]
print("Total volume for station %s for Sept 21, 2011 is %s" % (station, total))

print("")
print("--- query execution time: %s seconds ---" % (time.time() - start_time))
client.close()


