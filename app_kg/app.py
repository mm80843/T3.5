import streamlit as st
import os, json
from zipfile import ZipFile
from owlready2 import *


st.set_page_config(layout="wide")

st.write(st.__version__)

@st.cache_resource
def readOnto():
    if not os.path.isfile("onto.owl"):
        if os.path.isfile("onto.zip"):
            pathZip = "onto.zip"
        else:
            pathZip = "../rdf/work/currentWIP/WIP_w_SPARQL.zip"
        st.write("Creating the ontology")
        with ZipFile(pathZip) as myzip:
            print(myzip.namelist())
            m = myzip.extract(myzip.namelist()[0], path="./")
        os.rename(m,"onto.owl")
    onto = get_ontology("onto.owl").load()
    st.write("Ontology loaded")
    return onto

README = """# Required
* RDF file (zipped for size) -- for loading the KG
* order.json -- for label orders
"""

onto = readOnto()

PARAMS = st.query_params.to_dict()


st.write(PARAMS)

st.write("[link](?test=TESTVAL)")