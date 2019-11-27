# -*- coding: utf-8 -*-
"""
Created on 2019-02-24

@author: Martin Vallières
"""


import psycopg2

# A. CONNECTION OPTIONS
host = 'localhost'
dbname = 'Radiomics_Ontology'
user = 'postgres'
password = 'postgres'
schema = 'public'
featuretable_splits = 0 # Use 0 to keep only one table. Use a positive number to split it into multiple tables named "featuretable1", "featuretable2", etc.

# B. CONNECTION TO THE DATABASE
conn = psycopg2.connect(f"host={host} dbname={dbname} user={user} password={password} port=5432")
cur = conn.cursor()



# --> CLEANING TABLES
if featuretable_splits > 0:
	for t in range(featuretable_splits):
		cur.execute(f"DROP TABLE IF EXISTS {schema}.featuretable{str(t+1)}")
		conn.commit()
else:
	cur.execute(f"DROP TABLE IF EXISTS {schema}.featuretable")
	conn.commit()	


cur.execute(f"DROP TABLE IF EXISTS {schema}.imagespacetable")
conn.commit()  

cur.execute(f"DROP TABLE IF EXISTS {schema}.volumespacetable")
conn.commit()  

cur.execute(f"DROP TABLE IF EXISTS {schema}.voxeldimensiontable")
conn.commit()  

cur.execute(f"DROP TABLE IF EXISTS {schema}.scantable")
conn.commit()  

cur.execute(f"DROP TABLE IF EXISTS {schema}.postprocessingtable")
conn.commit()   

cur.execute(f"DROP TABLE IF EXISTS {schema}.roimasktable")
conn.commit()   

cur.execute(f"DROP TABLE IF EXISTS {schema}.segmentationtable")
conn.commit()    

cur.execute(f"DROP TABLE IF EXISTS {schema}.featureparameterspacetable")
conn.commit()  

cur.execute(f"DROP TABLE IF EXISTS {schema}.imagefilterspacetable")
conn.commit()   

cur.execute(f"DROP TABLE IF EXISTS {schema}.interpolationtable")
conn.commit()    

cur.execute(f"DROP TABLE IF EXISTS {schema}.resegmentationtable")
conn.commit()   

cur.execute(f"DROP TABLE IF EXISTS {schema}.discretisationtable")
conn.commit()  

cur.execute(f"DROP TABLE IF EXISTS {schema}.featurespecifictable")
conn.commit()  

cur.execute(f"DROP TABLE IF EXISTS {schema}.morphtable")
conn.commit()   

cur.execute(f"DROP TABLE IF EXISTS {schema}.glcmtable")
conn.commit()   

cur.execute(f"DROP TABLE IF EXISTS {schema}.glrlmtable")
conn.commit()  

cur.execute(f"DROP TABLE IF EXISTS {schema}.gldzmtable")
conn.commit()  

cur.execute(f"DROP TABLE IF EXISTS {schema}.ngtdmtable")
conn.commit()   

cur.execute(f"DROP TABLE IF EXISTS {schema}.ngldmtable")
conn.commit()    

cur.execute(f"DROP TABLE IF EXISTS {schema}.intvolhisttable")
conn.commit()  

cur.execute(f"DROP TABLE IF EXISTS {schema}.calculationruntable")
conn.commit()

cur.execute(f"DROP TABLE IF EXISTS {schema}.softwaretable")
conn.commit()

cur.execute(f"DROP TABLE IF EXISTS {schema}.waveletfiltertable")
conn.commit()


# --> CLOSING CONNECTION
conn.close()