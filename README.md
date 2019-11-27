# RadiomicsOntologyIBSI
## Radiomics Ontology and IBSI radiomics standard reporting
This is the repository for the radiomics ontology (RO) and the project with IBSI (Image Biomarker Standardization Iniative) for standardized reporting in radiomics computation. The aim of the project is to provide the radiomics community with a set of tools and guidlines to improve the actual quality of reporting of radiomics studies. Finally, the projects aims at providing FAIR (Findable Accessible Interoperable Reusable) tools to boost the access and reproducibility of radiomics studies.

In particular, we developed a complete workflow that allows standardizing the reporting of radiomics computations.
The workflow is composed by the following steps:
1) **Template tables for standardized reporting**: report of radiomics computations by filling a set of template tables. These template tables contain information about radiomic features, their values, units and all other details related to their computation. The tables have been created to guarantee broad coverage of all the steps in the radiomic workflow, as explained in details in the IBSI reference guide (https://arxiv.org/abs/1612.07003). A set of rules is provided to facilitate the filling of the tables. Small example tables are provided too.
2) **Radiomics ontology (RO)**: the radiomics ontology aims to cover the radiomics feature domain, as well as the full spectrum of radiomics computational details identified by the IBSI. The current version of the RO includes all the possible steps that should be documented when poerforming a radiomic study. The ontology URIs (Unique Resource Identifiers) are the same as in the IBSI reference manual. The ontology is used to transform the tables from the previous point as FAIR (Find Accessible Interoperable Reusable) compliant data, by producing RDF (Resource Description Framework) triples, published  the Semantic Web and making them querable using a dedicated language. The latest version of the ontology is always published on BioPortal (https://bioportal.bioontology.org/ontologies/RO), on this gitHub [here] (https://github.com/albytrav/RadiomicsOntologyIBSI/tree/master/Ontology/Protege) and it is permanently hosted on www.radiomics.org/RO. Users can tansverse the ontology tree by typing directly the address associated with a specific concept in the ontology (e.g. www.radiomics.org/RO/RNU0 will show the morpohological feature Volume).
3) **D2rq conversion scripts**: these scripts are used to convert from databases to RDF triples, so that row, columns and values in the database are mapped to the concepts and predicates in the ontology. The mapping is made via dedicated scripts based on the D2RQ mapping language (http://d2rq.org/). The results of this output is a set of RDF triples, which express the content of mapped tables, but as FAIR-compliant objects
4) **Query of RDF triples via Semantic Web**: RDF triples are then made avaialble via the Semantic Web and deoposited on a dedicated SPARQL endpoint. They can be queried using a dedicate language, which is called SPARQL (https://www.w3.org/TR/rdf-sparql-query/). To perform queries, web interfaces (being the SPARQL endpoint hosted on a public IP) such as Blazegraph (https://www.blazegraph.com/) or GraphDb (http://graphdb.ontotext.com/)

In this [wiki](https://github.com/albytrav/RadiomicsOntologyIBSI/wiki), we make available all the tools and provide you with a small guide to convert your radiomics studies with our pipeline. 



