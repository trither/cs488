# Count high speeds: Find the number of speeds > 100 in the data set.

import pymongo
import time

client = pymongo.MongoClient("mongodb+srv://admin:admin@cs488p3-o8kgj.gcp.mongodb.net/cs488?retryWrites=true&w=majority")
db = client.cs488
co = db.freeway_loopdata

start_time = time.time()

result = co.find({"speed": {"$gt": 100}}).count()
print("Number of speeds > 100 in the data set: ", result)

print("")
print("--- query execution time: %s seconds ---" % (time.time() - start_time))
client.close()
