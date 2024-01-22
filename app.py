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

    with open("order.json", "r") as f:
        orderedJson = json.loads(f.read())

    return onto, orderedJson
 


onto, orderedJson = readOnto()

PARAMS = st.query_params.to_dict()


if ("category" in PARAMS) and ("id" in PARAMS):
    st.write("Object detected")
    md = c.createPage(onto,PARAMS["category"],PARAMS["id"],orderedJson)
    st.write(md)
st.write(PARAMS)

st.write("[link](?test=TESTVAL)")