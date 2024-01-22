import streamlit as st
import os, json
from zipfile import ZipFile
import kgartefacts as c
from owlready2 import *

README = """# Required
* setup.sh helps to load files in the folder
* onto.zip -- for loading the KG
* order.json -- for label orders
"""

st.set_page_config(layout="wide")

st.sidebar.write("ST version: "+str(st.__version__))

@st.cache_resource
def readOnto():
    if not os.path.isfile("data/onto.owl"):
        if os.path.isfile("data/onto.zip"):
            pathZip = "data/onto.zip"
        else:
            pathZip = "../rdf/pbn_t3_5.owl.zip"
        st.write("Creating the ontology")
        with ZipFile(pathZip) as myzip:
            print(myzip.namelist())
            m = myzip.extract(myzip.namelist()[0], path="data/")
        os.rename(m,"data/onto.owl")
    onto = get_ontology("data/onto.owl").load()
    st.sidebar.write("Ontology loaded")

    with open("data/order.json", "r") as f:
        orderedJson = json.loads(f.read())

    return onto, orderedJson
 


onto, orderedJson = readOnto()

st.sidebar.write("Onto version:",onto.metadata.comment[13])
PARAMS = st.query_params.to_dict()


if ("category" in PARAMS) and ("id" in PARAMS):
    md = c.createPage(onto,PARAMS["category"],PARAMS["id"],orderedJson)
    st.write(md)
elif ("category" in PARAMS) and not ("id" in PARAMS):
    md = c.createIndex(onto,PARAMS["category"])
    st.write(md)
else:
    md = c.createMainIndex(onto)
    st.write(md)