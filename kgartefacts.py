import pandas as pd
import os, json

from owlready2 import *



def getNameLabel(x):
    try :
        b = x.label[0]
    except:
        b = str(x)
    return b


def createIndex(onto,K):
    HOME = "https://pbn-t3-5.streamlit.app/"
    k = eval("onto."+K)
    print(K)
    IDX = "[Source]("+HOME+")"
    IDX += "\n\n# "+str(K)+" -- "+str(len(k.instances()))+ " instances.\n\n"
    BB = list(k.instances())
    BB = [x for x in BB if x.label]
    BB.sort(key=lambda x: x.label[0].lower())
    for i in BB: 
        I = str(i).split(".")[-1]

        II = "_".join(I.split("PBN__")[1].split("_")[:-1])
        N = I.split("_")[-1]
        A = i.label[0]
        if K == "Article":
            A = " ".join(list(set(A.split(" ")))).replace("nan","").strip()
        if "Nan" not in A:
            if "----" not in A:
                IDX += "* ["+A+"]("+HOME+"?category="+K+"&id="+str(N)+")\n" 
    return IDX

def createPage(onto,obj,uid,orderedJson):
    HOME = "https://pbn-t3-5.streamlit.app/"
    K = obj
    i = eval("onto.PBN__"+obj+"_"+str(uid))
    print("onto.PBN__"+obj+"_"+str(uid),i)
    MD = "[Home]("+HOME+") >> Class: ["+K+"]("+HOME+"?category="+K+")"+" >> Individual ID:"+str(uid)+" \n\n"

    if i.label:
        MD += "\n\n# "+i.label[0]+"\n\n"
    else:
        MD += "\n\n# "+str(i)+"\n\n"

    A = list(i.get_properties())
    a = [str(x).split(".")[-1] for x in A]


    for prop in orderedJson[K]:

        if prop in a:
            p = eval("onto."+prop)
            P = prop
            #print(prop,P)
            OBJ = "onto."+str(i.name)+"."+str(P)
            OB = eval(OBJ) # OBJ is the way to get the list of label of the object
            E = eval(OBJ)[0] # Getting first
            if not (OB == [onto.nan]):
                if not P == "label":
                    #print("P",P,p)
                    # Label of the property
                    if not p.label:
                        # Unnamed properties
                        MD += "### Property: "+P+"\n\n"
                    else:
                        # Named properties
                        MD += "### "+str(p.label[0])+"\n\n"
                
                    if type(E) is str:
                        # Only one thing to print
                        MD += E + "\n\n"
                    else:
                        A = [x.get_name() for x in OB]
                        B = [x.label[0] for x in OB]
                        #B.sort(key=lambda x: getNameLabel(x))
                        C = zip(A, B)
                        C = sorted(C, key = lambda x: x[0])
                        #print("C",list(C))
                        for c in C:
                            if c[1] not in ["None","Nan"]:
                                N = c[0][5:].split("_")[-1]
                                cat = "_".join(c[0][5:].split("_")[:-1])
                                linetoadd = "* ["+c[1]+"](?category="+cat+"&id="+str(N)+")\n"
                                MD += linetoadd
                        MD += "\n" 
        elif prop.startswith("# "):
            MD += "\n\n#"+prop+"\n\n"
        else:
            print("Unseen category")
    return MD