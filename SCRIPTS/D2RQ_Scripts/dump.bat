

::  
:: TO RUN THE SCRIPT::
:: DUMP.BAT <D2RQBASE DIRECTORY> <OUTPUTDIR> <MAPPINGDIR>
:: EXAMPLE DUMP.BAT "C:\Users\alberto.traverso\Workspace_RO\SW\d2rq-0.8.1" "C:\Users\alberto.traverso\Workspace_RO\Data\RDFOutput" "C:\Users\alberto.traverso\Workspace_RO\Scripts\D2RQ\MappingScripts" 
:: MOVING TO DIRECTORY WHERE D2RQ IS INSTALLED
cd %1
:: JUST DELETING PRINT OF COMMANDS FROM WINDOWS
@ECHO OFF
SET OUTPUTDIR=%2
SET MAPPINGDIR=%3
ECHO "FEATURETABLE"
CALL dump-rdf -b http://albertotraverso.maaastro.nl/rdf/ -o %OUTPUTDIR%\featuretable_out.ttl %MAPPINGDIR%\FeatureTable.ttl
ECHO "CALCULATION RUN TABLE"
CALL dump-rdf -b http://albertotraverso.maaastro.nl/rdf/ -o %OUTPUTDIR%\calculationruntable_out.ttl %MAPPINGDIR%\CalculationRunTable.ttl
ECHO "SOFTWARE TABLE"
CALL dump-rdf -b http://albertotraverso.maaastro.nl/rdf/ -o %OUTPUTDIR%\softwaretable_out.ttl %MAPPINGDIR%\SoftwareTable.ttl
ECHO "FEATURE PARAMETER SPACE TABLE"
CALL dump-rdf -b http://albertotraverso.maaastro.nl/rdf/ -o %OUTPUTDIR%\featureparameterspacetable_out.ttl %MAPPINGDIR%\FeatureParameterSpaceTable.ttl
ECHO "FEATURE SPECIFIC PARAMETER TABLE"
CALL dump-rdf -b http://albertotraverso.maaastro.nl/rdf/ -o %OUTPUTDIR%\featurespecificparametertable_out.ttl %MAPPINGDIR%\FeatureSpecificParameterTable.ttl
ECHO "DISCRETIZATION TABLE"
CALL dump-rdf -b http://albertotraverso.maaastro.nl/rdf/ -o %OUTPUTDIR%\discretizationtable_out.ttl %MAPPINGDIR%\DiscretizationTable.ttl
ECHO "INTERPOLATION TABLE"
CALL dump-rdf -b http://albertotraverso.maaastro.nl/rdf/ -o %OUTPUTDIR%\interpolationtable_out.ttl %MAPPINGDIR%\InterpolationTable.ttl
ECHO "RESEGMENTATION TABLE"
CALL dump-rdf -b http://albertotraverso.maaastro.nl/rdf/ -o %OUTPUTDIR%\resegmentationtable_out.ttl %MAPPINGDIR%\ResegmentationTable.ttl
ECHO "MORPHOLOGICAL FEATURES TABLE"
CALL dump-rdf -b http://albertotraverso.maaastro.nl/rdf/ -o %OUTPUTDIR%\morphtable_out.ttl %MAPPINGDIR%\MorphTable.ttl
ECHO "GLCM FEATURES TABLE"
CALL dump-rdf -b http://albertotraverso.maaastro.nl/rdf/ -o %OUTPUTDIR%\glcmtable_out.ttl %MAPPINGDIR%\glcmTable.ttl
ECHO "GLRLM FEATURES TABLE"
CALL dump-rdf -b http://albertotraverso.maaastro.nl/rdf/ -o %OUTPUTDIR%\glrlmtable_out.ttl %MAPPINGDIR%\glrlmTable.ttl
ECHO "GLDZM FEATURES TABLE"
CALL dump-rdf -b http://albertotraverso.maaastro.nl/rdf/ -o %OUTPUTDIR%\gldzmtable_out.ttl %MAPPINGDIR%\gldzmTable.ttl
ECHO "NGTDM FEATURES TABLE"
CALL dump-rdf -b http://albertotraverso.maaastro.nl/rdf/ -o %OUTPUTDIR%\ngtdmtable_out.ttl %MAPPINGDIR%\ngtdmTable.ttl
ECHO "NGLDM FEATURES TABLE"
CALL dump-rdf -b http://albertotraverso.maaastro.nl/rdf/ -o %OUTPUTDIR%\ngldmtable_out.ttl %MAPPINGDIR%\ngldmTable.ttl
ECHO "INT VOL HIST FEATURES TABLE"
CALL dump-rdf -b http://albertotraverso.maaastro.nl/rdf/ -o %OUTPUTDIR%\intvolhisttable_out.ttl %MAPPINGDIR%\intvolhistTable.ttl
ECHO "FILTER SPACE TABLE"
CALL dump-rdf -b http://albertotraverso.maaastro.nl/rdf/ -o %OUTPUTDIR%\filterspacetable_out.ttl %MAPPINGDIR%\FilterSpaceTable.ttl
ECHO "WAVELET FILTER TABLE"
CALL dump-rdf -b http://albertotraverso.maaastro.nl/rdf/ -o %OUTPUTDIR%\waveletfiltertable_out.ttl %MAPPINGDIR%\WaveletFilterTable.ttl
ECHO "IMAGE SPACE TABLE"
CALL dump-rdf -b http://albertotraverso.maaastro.nl/rdf/ -o %OUTPUTDIR%\imagespacetable_out.ttl %MAPPINGDIR%\ImageSpaceTable.ttl
ECHO "IMAGE VOLUME SPACE TABLE"
CALL dump-rdf -b http://albertotraverso.maaastro.nl/rdf/ -o %OUTPUTDIR%\imagevolumespacetable_out.ttl %MAPPINGDIR%\ImageVolumeSpaceTable.ttl
ECHO "ROI MASK TABLE"
CALL dump-rdf -b http://albertotraverso.maaastro.nl/rdf/ -o %OUTPUTDIR%\roimasktable_out.ttl %MAPPINGDIR%\ROIMaskTable.ttl
ECHO "SEGMENTATION TABLE"
CALL dump-rdf -b http://albertotraverso.maaastro.nl/rdf/ -o %OUTPUTDIR%\segmentationtable_out.ttl %MAPPINGDIR%\SegmentationTable.ttl
ECHO "POST PROCESSING TABLE"
CALL dump-rdf -b http://albertotraverso.maaastro.nl/rdf/ -o %OUTPUTDIR%\postprocessingtable_out.ttl %MAPPINGDIR%\PostProcessingTable.ttl
ECHO "SCAN TABLE"
CALL dump-rdf -b http://albertotraverso.maaastro.nl/rdf/ -o %OUTPUTDIR%\scantable_out.ttl %MAPPINGDIR%\ScanTable.ttl
ECHO "VOXEL DIMENSION TABLE"
CALL dump-rdf -b http://albertotraverso.maaastro.nl/rdf/ -o %OUTPUTDIR%\voxeldimension_out.ttl %MAPPINGDIR%\VoxelDimensionTable.ttl
ECHO "MAPPING DONE"








