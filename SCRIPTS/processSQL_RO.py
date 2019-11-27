# -*- coding: utf-8 -*-
"""
Created on 2019-02-24

@author: Martin Vallières
"""


import os
import time
import psycopg2

# A. CONNECTION OPTIONS
host = 'localhost'
dbname = 'Radiomics_Ontology'
user = 'postgres'
password = 'postgres'
schema = 'public'

# B. CONNECTION TO THE DATABASE
conn = psycopg2.connect(f"host={host} dbname={dbname} user={user} password={password} port=5432")
cur = conn.cursor()

# C. TEMPORARY PATH TO FILES
pathTables = "/Users/martin/Desktop/ONTOLOGY_STUDY/FEATURES/ONTOLOGY/"
#pathTables = "/Users/martin/Desktop/WORKSPACE_ONTOLOGY/ONTOLOGY/" # Full tables with 12,000,000 feature table rows
#pathTables = "/Users/martin/Desktop/WORKSPACE_ONTOLOGY/ONTOLOGY_SPLIT/" # Full tables with 12,000,000 feature table rows -- SPLITTED TABLES


# D. DEFINIING TABLES TO CONVERT
def table_to_sql(file_path, table_name, schema):
    "Convert csv to sql"
    table_to_sql_dict = {
        'Feature_table': f"COPY {schema}.featuretable FROM {file_path} DELIMITER ',' CSV HEADER;",
        'ImageSpace_table': f"COPY {schema}.imagespacetable FROM {file_path} DELIMITER ',' CSV HEADER;",
        'ImageVolume_table': f"COPY {schema}.volumespacetable FROM {file_path} DELIMITER ',' CSV HEADER;",
        'VoxelDimension_table': f"COPY {schema}.voxeldimensiontable FROM {file_path} DELIMITER ',' CSV HEADER;",
        'Scan_table': f"COPY {schema}.scantable FROM {file_path} DELIMITER ',' CSV HEADER;",
        'PostAcquisitionProcessing_table': f"COPY {schema}.postprocessingtable FROM {file_path} DELIMITER ',' CSV HEADER;",
        'ROImask_table': f"COPY ro.roimasktable FROM {file_path} DELIMITER ',' CSV HEADER;",
        'SegmentationMethod_table': f"COPY {schema}.segmentationtable FROM {file_path} DELIMITER ',' CSV HEADER;",
        'FeatureParameterSpace_table': f"COPY {schema}.featureparameterspacetable FROM {file_path} DELIMITER ',' CSV HEADER;",
        'ImageFilterSpace_table': f"COPY {schema}.imagefilterspacetable FROM {file_path} DELIMITER ',' CSV HEADER;",
        'InterpolationParameters_table': f"COPY {schema}.interpolationtable FROM {file_path} DELIMITER ',' CSV HEADER;",
        'ReSegmentationParameters_table': f"COPY {schema}.resegmentationtable FROM {file_path} DELIMITER ',' CSV HEADER;",
        'DiscretisationParameters_table': f"COPY {schema}.discretisationtable FROM {file_path} DELIMITER ',' CSV HEADER;",
        'FeatureSpecificParameters_table': f"COPY {schema}.featurespecifictable FROM {file_path} DELIMITER ',' CSV HEADER;",
        'morphParameters_table': f"COPY {schema}.morphtable FROM {file_path} DELIMITER ',' CSV HEADER;",
        'glcmParameters_table': f"COPY {schema}.glcmtable FROM {file_path} DELIMITER ',' CSV HEADER;",
        'glrlmParameters_table': f"COPY {schema}.glrlmtable FROM {file_path} DELIMITER ',' CSV HEADER;",
        'gldzmParameters_table': f"COPY {schema}.gldzmtable FROM {file_path} DELIMITER ',' CSV HEADER;",
        'ngtdmParameters_table': f"COPY {schema}.ngtdmtable FROM {file_path} DELIMITER ',' CSV HEADER;",
        'ngldmParameters_table': f"COPY {schema}.ngldmtable FROM {file_path} DELIMITER ',' CSV HEADER;",
        'intVolHistParameters_table': f"COPY {schema}.intvolhisttable FROM {file_path} DELIMITER ',' CSV HEADER;",
        'CalculationRunSpace_table': f"COPY {schema}.calculationruntable FROM {file_path} DELIMITER ',' CSV HEADER;",
        'Software_table': f"COPY {schema}.softwaretable FROM {file_path} DELIMITER ',' CSV HEADER;",
        'WaveletFilterParameters_table': f"COPY {schema}.waveletfiltertable FROM {file_path} DELIMITER ',' CSV HEADER;"}

    # Loading table
    if 'Feature_table' in table_name:
        print('')
        print(f"COPY {schema}.featuretable{table_name[13:]} FROM {file_path} DELIMITER ',' CSV HEADER;")
        cur.execute(f"COPY {schema}.featuretable{table_name[13:]} FROM {file_path} DELIMITER ',' CSV HEADER;")
        conn.commit()
        print('')
    else:
        print('')
        print(f"""{table_to_sql_dict[table_name]}""")
        print('')
        cur.execute(f"""{table_to_sql_dict[table_name]}""")
        conn.commit()



# E. MAIN
if __name__ == "__main__":
    start = time.time()
    print('\n---Converting from CSV to SQL---\n')
    # PATH = '/tmp' + '/CSV/'
    # PATH = os.getcwd() + '/CSV/'
    # PATH = '/home/picare/Desktop' + '/CSV/'
    PATH = pathTables
    cvs_files = os.listdir(PATH)
    list_cvs_files = []
    for file in cvs_files:
        if file.endswith('.csv'):
            list_cvs_files.append(file)

    file_path_string = ''
    print('Loading into data base\n')
    for file in list_cvs_files:
        file_path_string = "'" + PATH + file + "'"
        table_to_sql(file_path_string, file[:-4], schema)

    conn.close()
    print('DONE!')
    print('Execution Time: ', time.time() - start)