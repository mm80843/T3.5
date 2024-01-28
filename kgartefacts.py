import pandas as pd
import os, json

from owlready2 import *

from dotenv import load_dotenv



def getNameLabel(x):
    try :
        b = x.label[0]
    except:
        b = str(x)
    return b


def createIndex(onto,K):
    load_dotenv()
    location = os.getenv('WHERE')
    if location:
        HOME = ""
    else:
        HOME = "https://pbn-t3-5.streamlit.app/"

    k = eval("onto."+K)
    print(K)
    IDX = "[Source]("+HOME+")"
    IDX += "\n\n# "+str(K)+" -- "+str(len(k.instances()))+ " instances.\n\n"
    if "Subgroup" in K:
        subindex = dict()
        for w in list(k.instances()):
            try:
                SPACE = K.replace("Subgroup","")
                GROUP =  "w.has_Subgroup"+SPACE+"[0].has_"+SPACE+"Group[0].name"
                GROUP = eval(GROUP)
                SUBGROUP = w.name
                if GROUP not in subindex.keys():
                    subindex[GROUP] = []
                subindex[GROUP].append(SUBGROUP)
            except:
                print("Error with",k)
                pass
        for GR in subindex.keys():
            G = str(GR)
            n = G.split("_")[-1]
            c = G.replace("_"+str(n),"")[5:]
            #print(G,"==>",GR)
            m = eval("onto."+G+".label[0]")
            #print(m)
            IDX += "\n#### <a href='"+HOME+"?category="+c+"' target='_self'>"+m+"</a>"
            #IDX += ("\n### ["+m+"]("+HOME+"?category="+c+"&id="+n+")")
            for items in subindex[GR]:
                s = str(items)
                n = s.split("_")[-1]
                c = s.replace("_"+str(n),"")[5:]
                IDX += "\n* <a href='"+HOME+"?id="+n+"&category="+c+"' target='_self'>"+eval("onto."+items+".label[0]")+"</a>"
                #IDX += "\n* ["+eval("onto."+items+".label[0]")+"]("+HOME+"?category="+c+"&id="+n+")"
    else:

        BB = list(k.instances())
        BB = [x for x in BB if x.label]
        BB.sort(key=lambda x: x.label[0].lower())
        for i in BB: 
            I = str(i).split(".")[-1]

            II = "_".join(I.split("PBN__")[1].split("_")[:-1])
            N = I.split("_")[-1]
            A = i.label[0]
            IDX += "\n * <a href='"+HOME+"?category="+K+"&id="+str(N)+"' target='_self'>"+A+"</a>"
            #IDX += "* ["+A+"]("+HOME+"?category="+K+"&id="+str(N)+")\n" 
    return IDX


def createPage(onto,obj,uid,orderedJson):
    load_dotenv()
    location = os.getenv('WHERE')
    if location:
        HOME = ""
    else:
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
            a.remove(prop)
            p = eval("onto."+prop)
            P = prop
            #print(prop,P)
            OBJ = "onto."+str(i.name)+"."+str(P)
            OB = eval(OBJ) # OBJ is the way to get the list of label of the object
            E = eval(OBJ)[0] # Getting first
            propType = eval("onto."+str(P))
            if not (OB == [onto.nan]):
                if not P == "label":
                    #print("P",P,p)
                    # Label of the property
                    if not p.label:
                        # Unnamed properties
                        MD += "### Property: "+P+"\n\n"
                        print("Property without a label:",prop,"for",obj,"(uid",uid,")")
                
                    else:
                        # Named properties
                        MD += "### "+str(p.label[0])+"\n\n"
                        
                    if propType.get_range() == [str]:
                        # Only one thing to print
                        # @TODO check if p is data_property : DataProperty
                        #MD += "\n\n"+str(eval(OBJ))+"\n\n"
                        MD += "\n"
                        for strItem in OB:
                            MD += "* "+strItem+"\n"
                        MD += "\n"
                    else:
                        print("->",OB)
                        A = [x.get_name() if (type(x) != str) else str(x) for x in OB ]
                        B = [x.label[0] if (type(x) != str) else str(x) for x in OB ]
                        #B = [x.label[0] for x in OB]
                        #B.sort(key=lambda x: getNameLabel(x))
                        C = zip(A, B)
                        C = sorted(C, key = lambda x: x[0])
                        #print("C",list(C))
                        for c in list(set(C)):
                            if c[1] not in ["None","Nan"]:
                                N = c[0][5:].split("_")[-1]
                                cat = "_".join(c[0][5:].split("_")[:-1])
                                if cat and N:
                                    linetoadd = "\n * <a href='"+HOME+"?category="+cat+"&id="+str(N)+"' target='_self'>"+c[1]+"</a>"
                                else:
                                    linetoadd = "\n * "+c[1]+""
                                #linetoadd = "* ["+c[1]+"]("+HOME+"?category="+cat+"&id="+str(N)+")\n"
                                MD += linetoadd
                        MD += "\n" 
        elif prop.startswith("# "):
            MD += "\n\n#"+prop+"\n\n"
        else:
            print("Property not used:",prop,"for",obj,"(uid",uid,")")

    if len(a):
        MD += "\n\n# Other properties\n\n"
        for prop in a:
            print("Missing in order.json:",a)
            p = eval("onto."+prop)
            P = prop
            #print(prop,P)
            OBJ = "onto."+str(i.name)+"."+str(P)
            OB = eval(OBJ) # OBJ is the way to get the list of label of the object
            E = eval(OBJ)[0] # Getting first
            propType = eval("onto."+str(P))
            if not (OB == [onto.nan]):
                if not P == "label":
                    #print("P",P,p)
                    # Label of the property
                    if not p.label:
                        # Unnamed properties
                        MD += "### Property: "+P+"\n\n"
                        print("Property without a label:",prop,"for",obj,"(uid",uid,")")
                
                    else:
                        # Named properties
                        MD += "### "+str(p.label[0])+"\n\n"
                        
                    if propType.get_range() == [str]:
                        # Only one thing to print
                        # @TODO check if p is data_property : DataProperty
                        #MD += "\n\n"+str(eval(OBJ))+"\n\n"
                        MD += "\n"
                        for strItem in OB:
                            MD += "* "+strItem+"\n"
                        MD += "\n"
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
                                linetoadd = "\n * <a href='"+HOME+"?category="+cat+"&id="+str(N)+"' target='_self'>"+c[1]+"</a>"
                                #linetoadd = "* ["+c[1]+"]("+HOME+"?category="+cat+"&id="+str(N)+")\n"
                                MD += linetoadd
                        MD += "\n" 
    return MD

def createMainIndex(onto):
    IDX = ""
    IDX += "# Welcome on T3.5 knowledge graph explorer\n\n"
    IDX += "References to the original work is [there on github](https://github.com/mm80843/T3.5)\n\n"

    load_dotenv()
    location = os.getenv('WHERE')
    if location:
        HOME = ""
    else:
        HOME = "https://pbn-t3-5.streamlit.app/"
        
    BB = list(onto.classes())
    BB.sort(key=lambda x: str(x).lower())
    for k in BB:
        if len(k.instances()):
            MM = str(k).split(".")[-1]
            if (not MM == "RiskMitigation") and (not MM == "PBNThing"):
                #IDX += "* _["+MM+"]("+HOME+"?category="+MM+")_ "
                IDX += "* <a href='"+HOME+"?category="+MM+"' target='_self'>"+MM+"</a>"
                IDX += "-- "+str(len(k.instances()))+ " instances.\n"

    return IDX
