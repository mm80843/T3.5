import pandas as pd
import os, json
from owlready2 import *

import owlready2


def checkOnto(path,debug = True):
    onto = owlready2.get_ontology(path).load()


    print("\n# Overview\n")
    for k in onto.classes():
        if len(k.instances()):
            print("* ","_"+str(k).split(".")[-1]+"_"," -- ",len(k.instances()), "instances.")
    if debug:
        print("\n# Details\n")
        for k in onto.classes():
            K = str(k).split(".")[-1]
            if K not in ["Qid","PBNThing"]:
                print("## ",K," -- ",len(k.instances()), "instances.")
                for i in k.instances()[:2]: 
                    I = str(i).split(".")[-1]
                    if K == "Qid":
                        if len(i.has_Qid_alias) > 0:
                            print("### ",I," -> ",i.has_Qid_alias[0])
                        else:
                            print("### ",I)
                        for p in list(i.get_properties()):
                            P = str(p).split(".")[-1]
                            OBJ = "onto."+str(I)+"."+str(P)
                            if not P == "label":
                                print("* ","pbn_t3_5."+str(I)+"."+str(P),": ",eval(OBJ))
                    else:
                        print("### ",I," -> ",i.label[0])
                        for p in list(i.get_properties()):
                            P = str(p).split(".")[-1]
                            OBJ = "onto."+str(I)+"."+str(P)
                            if not P == "label":
                                print("* ","pbn_t3_5."+str(I)+"."+str(P),": ",eval(OBJ))



def getNameLabel(x):
    try :
        b = x.label[0]
    except:
        b = str(x)
    return b

def getRosettaOnto(onto):
    NAMES = {}
    for k in onto.classes():
        K = str(k).split(".")[-1]
        if K not in ["PBNThing"]:
            for i in k.instances():
                NAMES[i.get_name()] = getNameLabel(i)
    return NAMES

def saveRosettaOnto(NAMES,path):
    with open(path,"w") as f:
        f.write(json.dumps(NAMES))
    return "Saved at "+str(path)

def loadRosettaOnto(path):
    with open(path,"r") as f:
        NAMES = json.loads(f.read())
    return NAMES


def onto_noBP(pathrdfin,pathrdfout):

    onto = owlready2.get_ontology(pathrdfin).load()
    onto.metadata.comment[5] = 'limited to PROBONO blueprints'

    for k in onto.classes():
        I = k.instances()
        if len(I):
            K = str(k).split(".")[-1]
            if K.startswith("Blueprint"):
                for i in I:
                    owlready2.destroy_entity(i)
                owlready2.destroy_entity(k)
        else:
            owlready2.destroy_entity(k)
                
    onto.save(file = pathrdfout)
    onto.destroy()
    return "File saved at "+pathrdfout


def onto_BP(pathrdfin,pathrdfout):

    onto = owlready2.get_ontology(pathrdfin).load()
    onto.metadata.comment[5] = 'limited to blueprints'

    with onto:
        for k in onto.classes():
            I = k.instances()
            if len(I):
                K = str(k).split(".")[-1]
                if not( (K.startswith("Blueprint") or K.startswith("BP_") or K == "PBNThing" ) ):
                    for i in I:
                        owlready2.destroy_entity(i)
                    owlready2.destroy_entity(k)

    onto.save(file = pathrdfout)
    onto.destroy()
    return "File saved at "+pathrdfout

def checkComments(onto):
    for k in range(len(onto.metadata.comment)):
        print("ID:",k,"\t",onto.metadata.comment[k])
    return onto.metadata.comment

def createDict(onto):
    dIDct = {}
    for C in onto.classes():
        CLASS = str(C).split(".")[-1]
        print(CLASS)
        dIDct[CLASS] = {} 
        for k in C.instances():
            try:
                dIDct[CLASS][k.label[0]] = int(str(k).split(".")[-1].split("_")[-1])
            except:
                dIDct[CLASS][str(k)] = int(str(k).split(".")[-1].split("_")[-1])
    return dIDct


def addItem(itemClass, itemDescription, dIDct, onto ):
    itemDescription = str(itemDescription).replace("\n"," ").replace("\\"," ").replace("e.g."," ").replace("("," ").replace(")"," ")
    itemDescription = itemDescription.replace("\b"," ")
    itemDescription = re.sub(' +', ' ',  str(itemDescription)).strip().capitalize()
    if itemClass not in dIDct.keys():
        dIDct[itemClass] = {}
    if itemDescription in dIDct[itemClass].keys():
        ID = dIDct[itemClass][itemDescription]
        EXP = "onto."+itemClass+'("PBN__'+itemClass+"_"+str(ID)+'")'
        OBJ = eval(EXP)
        eval("OBJ.label.append('"+itemDescription.replace("'","’")+"')")
        OBJ.label = list(set(OBJ.label))
        return OBJ
    else:
        ID = len(dIDct[itemClass])
        dIDct[itemClass][itemDescription] = ID
        EXP = "onto."+itemClass+'("PBN__'+itemClass+"_"+str(ID)+'")'
        OBJ = eval(EXP)
        eval("OBJ.label.append('"+itemDescription.replace("'","’")+"')")
        NAM = list(set(OBJ.label))
        if "Nan" in NAM:
            NAM.remove("Nan")
        OBJ.label = NAM
        
        return OBJ