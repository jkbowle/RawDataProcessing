from sqlalchemy import create_engine
from pandas import DataFrame

# an Engine, which the Session will use for connection
# resources
some_engine = create_engine('ibm_db_sa://id19868:Idm183qk@x1dbd225:50000/SIEBEL')
connection = some_engine.connect()
location = r'D:\Documents\workspaces\OERawDataProcessing\test_sql\test.sql'

with open (location,"r") as myfile:
    sql=myfile.read().replace('\n','')


#result = connection.execute("SELECT * FROM CCDB2.KAX_ESTIMATE a WHERE SEQ_NBR = 100540")
result = connection.execute(sql)
keys = result.keys()

df = DataFrame(result.fetchall())
#for row in result:
#    #print row['file_name']
#    #print row.keys()
#    print row.items()

df.to_csv("test.csv",header=keys)

connection.close()