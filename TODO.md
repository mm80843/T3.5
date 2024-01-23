# TODOs


### 20240122

* [ ] Rerun classification ([Step1](rdf/work/work_on_0.3/04.Add_Classification_Step1.ipynb) & [Step2](rdf/work/work_on_0.3/04.Add_Classification_Step2.ipynb))
* [ ] Add Articles to groups
* [ ] Missing orders in [orders.json](rdf/support/order.json)
* [ ] Missing labels for relations
* [ ] City Anatomy Mapping
* [ ] ISO Mapping for risks
* [ ] ISO Mapping for blueprints
* [ ] Synonyms
* [ ] Solving top-x grouping with synonyms
* [ ] Destroy all relationships when starting Step1

### 20231223

* [L] Add a "to-remove" class
* [x] Add risks families
* [x] Add stakeholders families
* [x] Add technologies families

### 20231218

* [x] Module approach
  * [x] Litterature KG
  * [x] Blueprints
  * [x] Merge ontos
* [x] New articles
  * [x] Add mechanisms to parse papers (post grobid) - Risks
  * [x] Add papers to the KG based on DOIs obtained
  * [x] Add risks to the KG
* [ ] Add simplification mechanisms (centrality of items?)
* [x] Tools in a library
  * [x] KG."Simplify" --> KG -> KG
  * [x] KG."Modularize" --> KG -> (KG,KG)
  * [x] KG."Aggregate"  --> (KG,KG) -> KG
* [x] Update the technical note on KG - updated.
* [ ] Update graph of the technical note.
* [ ] Do a new release

### 20231217

* [x] Add ChromaDB of articles -> _done, in documentation/_
  * [x] Add caching of questions.
* [x] Article: 
  * [x] Generate paper without background
  * [x] Generate paper and add bakcground, EU flag and disclaimer
