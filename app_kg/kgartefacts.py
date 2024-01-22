import pandas as pd
import os, json

from owlready2 import *



def getNameLabel(x):
    try :
        b = x.label[0]
    except:
        b = str(x)
    return b


def createPage(onto,obj,uid,orderedJson):

    K = obj
    i = eval("onto.PBN__"+obj+"_"+str(uid))
    print("onto.PBN__"+obj+"_"+str(uid),i)
    MD = "[Home](https://github.com/mm80843/T3.5/blob/pages/index.md) >> Class: ["+K+"](https://github.com/mm80843/T3.5/tree/pages/docs/"+K+"/index.md)"+" >> Individual ID:"+str(uid)+" \n\n"

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