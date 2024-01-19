![GitHub repo size](https://img.shields.io/github/repo-size/mm80843/T3.5?style=plastic)
![GitHub language count](https://img.shields.io/github/languages/count/mm80843/T3.5?style=plastic)
![GitHub top language](https://img.shields.io/github/languages/top/mm80843/T3.5?style=plastic)
![GitHub last commit](https://img.shields.io/github/last-commit/mm80843/T3.5?color=red&style=plastic)
[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)](http://commonmark.org)




# Creating Knowledge graphs from the literature: the case of health resilience in Green Building Neighbourhoods

### Introduction

The Horizon 2020 PROBONO project (Grant agreement 101037075) aims at demonstrating 
_"strong examples of how Green Building Neighbourhoods (GBNs) technological and social innovations can be applied, with a vision focused on building infrastructure and a renewed focus on people and sustainability, taking full advantage of digitization and smart technologies for the benefit of society"_. 
The Task 3.5 of this projects aims at reviewing ”Interventions to mitigate diseases outbreaks”.

In this document, we summarize how we used new technologies, including Large Language Models (LLMs), to consolidate a knowledge graph of (KG) this topic, based on the literature, to demonstrate the feasibility of building a body of knowledge pertaining to a certain domain, with a specific angle.
This opens the door to more opportunities the growing space existing between LLMs and KGs.

### Objective

The main objective of the task is to review the scientific literature to identify key risks, stakeholders, technologies and mitigations measures both at building and neighbourhood scales.

### Technical details

The present knowledge graph has been created using new tools, helping to streamline, faster and more consistently, information from the literature:
* Parsing of the literature was done with GROBID. This provided structured text (XML) from the article PDFs;
* The data was processed and structured in an RDF that was produced with the Owlready2 python library;
* Vector embedding based on Pinecone because of the early possibility to integrate with Langchain, and because of its ease of use.

Once the data was prepared, information structuring was done using different solutions:
* NLTK was used to extract topics and themes of the articles;
* Spacy was used for entity recognition, and CoreferenceResolver to tackle disambiguation ;
* Text was processed using a combination of OpenAI API (both using GPT3.5 and GPT4 endpoints) as well as running local models (NOUS/LLaMa), using the python requests or langchain libraries.


### Results

#### Overview 

We started with defining a basic ontology based on classes of interest for mitigation measures, namely ’Risks’, ’Mitigations’, ’People’, and ’Technologies’. These constitute an initial body of knowledge, which is then used to build ’Blueprints’, possible interventions to mitigate diseases outbreaks.

To date, the Knowledge Graph (v0.3) contains information on 376 articles, from which were programmaticaly derived 3418 risks, 5295 mitigation measures, 2640 stakeholders and 3915 technologies. 
The team used these to build 24 blueprints manually, and automated the production of 50 others.

We hope that releasing the knowledge graph under an open-source license (CC BY-NC-SA) will drive use of this knowledge graph and that health professionals can use this to derive useful, professionally-approved mitigation measures.

#### Materials produced

This repository contains:
* A [zipped knowledge graph](rdf/pbn_t3_5.zip)
  * [Support materials](/rdf/support/)
  * [Examples of work](/rdf/work/currentWIP/02.Add_RisksAssessments.ipynb) on the knowledge graph
  * Example of [SPARQL queries](/rdf/work/currentWIP/04.Add_Classification_Step2.ipynb)
* Helper tools to
  * [manage the knowledge graph](/utils/rdfutils.py)
  * [work with LLMs](/utils/llm.py)
* Tools to [process data](/bok/data/) from a body of knowledge
* A [technical note](/documentation/article/T3_5.pdf) describing the work

### Next steps

This activity yielded expected outcomes, consisting in mapping out risks, technologies and stakeholders, as well as suggesting mitigation measures.

This however is an asset that has a highly reusable potential, and this list, albeit listing possible actions from a project perspective, could be undertaken by other parties:

* We plan on integrating more robust graph management solutions, possibly Neo4j or similar, to continually review and enrich the knowledge graph;
* We would want to enrich the semantic content of the graph to make it more usable and possible an input to KG-backed LLMs;
* Reusing existing semantic assets (eg Wikidata) might help structure
* Connect this knowledge graph to other KGs or ontologies.


### Disclaimer

Please note that this document is a research-based exploration compiled by knowledge management researchers, not medical professionals. 
Our findings are presented with the intention to inform and contribute to the dialogue on public health strategies. 
They are indicative and should serve as a preliminary guide. 
We encourage all readers to consult with qualified health professionals for expert advice and to confirm and enrich these insights.


## Technicalities

* Environment is defined in the requirements.txt
* Using python 3.10.2 (TBC)