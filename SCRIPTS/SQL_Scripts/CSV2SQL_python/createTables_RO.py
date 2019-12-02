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
#featuretable_splits = 64 # Use 0 to keep only one table. Use a positive number to split it into multiple tables named "featuretable1", "featuretable2", etc.
featuretable_splits = 0
# B. CONNECTION TO THE DATABASE
conn = psycopg2.connect(f"host={host} dbname={dbname} user={user} password={password} port=5432")
cur = conn.cursor()



# --> CREATING TABLES

# CREATING SCHEMA
cur.execute(f"CREATE SCHEMA IF NOT EXISTS {schema}")
conn.commit()

# 1. Feature_table
if featuretable_splits > 0:
    for t in range(featuretable_splits):
        cur.execute(f"""
        	CREATE TABLE IF NOT EXISTS {schema}.featuretable{str(t+1)} (
            patientid text,
            patientlabel text,
            featurename text,
        	featurevalue numeric,
        	unit text,
        	imagespacename text,
        	featureparameterspace text,
            calculationrunspace text
        	)
        	""")
        conn.commit()
else:
    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {schema}.featuretable (
        patientid text,
        patientlabel text,
        featurename text,
        featurevalue numeric,
        unit text,
        imagespacename text,
        featureparameterspace text,
        calculationrunspace text
        )
        """)
    conn.commit()


# 2. ImageSpace_table
cur.execute(f"""
	CREATE TABLE IF NOT EXISTS {schema}.imagespacetable (
    imagespacename text,
    imagevolume text,
    roimask text
	)
	""")
conn.commit()

# 3. ImageVolume_table
cur.execute(f"""
	CREATE TABLE IF NOT EXISTS {schema}.volumespacetable (
    imagevolume text,
    imagevolumelabel text,
    dimensionx text,
    dimensiony text,
    dimensionz text,
    scan text,
    postprocessing text
	)
	""")
conn.commit()

# 4. VoxelDimension_table
cur.execute(f"""
	CREATE TABLE IF NOT EXISTS {schema}.voxeldimensiontable (
    dimensionname text,
	dimensionvalue numeric,
	unit text
	)
	""")
conn.commit()

# 5. Scan_table
cur.execute(f"""
	CREATE TABLE IF NOT EXISTS {schema}.scantable (
    scan text,
	patientid text,
	patientlabel text,
    imagingmodality text,
    dicomspace text
	)
	""")
conn.commit()

# 6. PostAcquisitionProcessing_table
cur.execute(f"""
	CREATE TABLE IF NOT EXISTS {schema}.postprocessingtable (
    processing text,
	pvecorrection text,
	noisereduction text,
    nonuniformitycorrection text
	)
	""")
conn.commit()

# 7. ROImask_table
cur.execute(f"""
	CREATE TABLE IF NOT EXISTS {schema}.roimasktable (
    roimask text,
	roimasklabel text,
	roitype text,
    roitypelabel text,
    dimensionx text,
    dimensiony text,
    dimensionz text,
    segmentation text
	)
	""")
conn.commit()

# 8. SegmentationMethod_table
cur.execute(f"""
	CREATE TABLE IF NOT EXISTS {schema}.segmentationtable (
    segmentation text,
    segmethod text
	)
	""")
conn.commit()

# 9. FeatureParameterSpace_table
cur.execute(f"""
	CREATE TABLE IF NOT EXISTS {schema}.featureparameterspacetable(
    featureparameterspace text,
    aggregationparameter text,
    filtername text,
    interpolation text,
    resegmentation text,
    discretization text,
    featurespecific text
	)
	""")
conn.commit()

# 10. ImageFilterSpace_table
cur.execute(f"""
    CREATE TABLE IF NOT EXISTS {schema}.imagefilterspacetable(
    filterspace text,
    waveletfilterpar text
    )
    """)
conn.commit()

# 11. InterpolationParameters_table
cur.execute(f"""
	CREATE TABLE IF NOT EXISTS {schema}.interpolationtable(
    interpolation text,
    interpolationvalue numeric,
    interpolationunit text,
    imagevolumemethod text,
    glroundvalue numeric,
    glroundunit text,
    roimethod text,
    pvcutoff numeric
	)
	""")
conn.commit()

# 12. ReSegmentationParameters_table
cur.execute(f"""
	CREATE TABLE IF NOT EXISTS {schema}.resegmentationtable(
    resegmentation text,
    resegminvalue numeric,
    resegminunit text,
    resegmaxvalue numeric,
    resegmaxunit text,
    outlierremovalthreshold numeric
	)
	""")
conn.commit()

# 13. DiscretisationParameters_table
cur.execute(f"""
	CREATE TABLE IF NOT EXISTS {schema}.discretisationtable(
    discretisation text,
    equalisationbins integer,
    algorithm text,
    algorithmvalue numeric,
    algorithmunit text,
    discretisationminvalue numeric,
    discretisationminunit text
	)
	""")
conn.commit()

# 14. FeatureSpecificParameters_table
cur.execute(f"""
	CREATE TABLE IF NOT EXISTS {schema}.featurespecifictable(
    featurespecific text,
    morphpar text,
    glcmpar text,
    glrlmpar text,
    gldzmpar text,
    ngtdmpar text,
    ngldmpar text,
    intvolhistpar text
	)
	""")
conn.commit()

# 15. morphParameters_table
cur.execute(f"""
	CREATE TABLE IF NOT EXISTS {schema}.morphtable(
    morphpar text,
    morphmethod text,
    morphvalue numeric
	)
	""")
conn.commit()

# 16. glcmParameters_table
cur.execute(f"""
	CREATE TABLE IF NOT EXISTS {schema}.glcmtable(
    glcmpar text,
    symmetry text,
    distancemethod text,
    distancevalue numeric,
    distanceunit text,
    distancefunction text
	)
	""")
conn.commit()

# 17. glrlmParameters_table
cur.execute(f"""
	CREATE TABLE IF NOT EXISTS {schema}.glrlmtable(
    glrlmpar text,
    distancefunction text
	)
	""")
conn.commit()

# 18. gldzmParameters_table
cur.execute(f"""
	CREATE TABLE IF NOT EXISTS {schema}.gldzmtable(
    gldzmpar text,
    distancemethod text,
    distancevalue numeric,
    distanceunit text
	)
	""")
conn.commit()

# 19. ngtdmParameters_table
cur.execute(f"""
    CREATE TABLE IF NOT EXISTS {schema}.ngtdmtable(
    ngtdmpar text,
    distancemethod text,
    distancevalue numeric,
    distanceunit text,
    distancefunction text
    )
    """)
conn.commit()

# 20. ngldmParameters_table
cur.execute(f"""
    CREATE TABLE IF NOT EXISTS {schema}.ngldmtable(
    ngldmpar text,
    coarsenessvalue numeric,
    distancemethod text,
    distancevalue numeric,
    distanceunit text
    )
    """)
conn.commit()

# 21. intVolHistParameters_table
cur.execute(f"""
    CREATE TABLE IF NOT EXISTS {schema}.intvolhisttable(
    intvolhistpar text,
    minboundvalue numeric,
    minboundunit text,
    maxboundvalue numeric,
    maxboundunit text
    )
    """)
conn.commit()

# 22. CalculationRunSpace_table
cur.execute(f"""
    CREATE TABLE IF NOT EXISTS {schema}.calculationruntable(
    calculationrunspace text,
    timestamp text,
    software text
    )
    """)
conn.commit()

# 23. Software_table
cur.execute(f"""
    CREATE TABLE IF NOT EXISTS {schema}.softwaretable(
    software text,
    softwarelabel text,
    versionname text,
    programminglanguage text,
    institution text
    )
    """)
conn.commit()


# LAST TABLES --> FILTERS
# 24. WaveletFilterParameters_table
cur.execute(f"""
    CREATE TABLE IF NOT EXISTS {schema}.waveletfiltertable(
    waveletfilterpar text,
    basisfunction text,
    waveletdirection text
    )
    """)
conn.commit()


# --> CLOSING CONNECTION
conn.close()
