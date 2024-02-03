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

    if not os.path.isfile("data/full.owl"):
        pathZip = "data/full.zip"
        st.write("Creating the ontology")
        with ZipFile(pathZip) as myzip:
            print(myzip.namelist())
            m = myzip.extract(myzip.namelist()[0], path="data/")
        os.rename(m,"data/full.owl")
    onto = get_ontology("data/full.owl").load()
    
    st.sidebar.write("Big Onto .. OK")

    with open("data/order.json", "r") as f:
        orderedJson = json.loads(f.read())

    return onto, orderedJson
 


onto, orderedJson = readOnto()

st.sidebar.write("#### Details")
st.sidebar.write("Onto version:",onto.metadata.comment[1])
st.sidebar.write(onto.metadata.comment[5]) #date
PARAMS = st.query_params.to_dict()


if ("category" in PARAMS) and ("id" in PARAMS):
    md = c.createPage(onto,PARAMS["category"],PARAMS["id"],orderedJson)
    st.markdown(md,unsafe_allow_html=True)
elif ("category" in PARAMS) and not ("id" in PARAMS):
    md = c.createIndex(onto,PARAMS["category"])
    st.markdown(md,unsafe_allow_html=True)
else:
    md = c.createMainIndex(onto)
    st.markdown(md,unsafe_allow_html=True)