# T3.5 Knwoledge Graph -- TODOs

* [ ] TODO
* [x] DONE
* [L] Later

### 20240204

* [x] Add license
* [x] Add descriptions to Interventions 
* [x] New method to calculate IDs of objects
* [ ] Add CAO items to subgroups (people, techs, risks, internvetions) - see 20240128
* [ ] Create Mitigation subgroups (Intervention -> _Subgroup_ -> Mitig)
* [ ] Use BOK for extracting more benefits from articles
* [ ] Search app: 
  * [ ] (Stakeholder, technology) -> Top 3 risks, interventions, benefits

### 20240201

* [x] Risk, Tech, Stakeholder (sub) groups descriptions based on BOK -- use property has_desc
* [x] Labels for classes (in the indexes)
* [x] Removing Nans or strings with only '------'
* [x] Cleanup: if item starts with '*', remove the star
* [x] Add note : property has_note
* [x] Export to TTL

### 20240128

* [x] Reroute in KG articles with 'nan' to reroute to good articles like https://pbn-t3-5.streamlit.app/?category=Article&id=304
* [ ] ISO Mapping (scale impact purpose) for risks groups
* [ ] ISO Mapping (scale impact purpose) for blueprints
* [x] App links in same tab : `st.markdown('<a href="/?key=value" target="_self">View all</a>',unsafe_allow_html=True)`

### 20240122

* [x] Rerun classification ([Step1](rdf/work/work_on_0.3/04.Add_Classification_Step1.ipynb) & [Step2](rdf/work/work_on_0.3/04.Add_Classification_Step2.ipynb))
* [x] Add Articles to groups
* [x] Missing orders in [orders.json](rdf/support/order.json) (check from logs from streamlit app)
* [x] Missing labels for relations (check from logs from streamlit app)
* [x] City Anatomy Mapping
* [L] Solving top-x grouping with synonyms
* [L] Destroy all relationships when starting Step2
* [x] Clean up Stakeholders (appearing in subgroups)

#### To check

- [x] Property not in order.json: has_StakeholderGroup_RiskGroup_Subject for StakeholderGroup (uid 3 )
- [x] Property not in order.json: has_StakeholderGroup_RiskGroup_Owner for StakeholderGroup (uid 3 )
- [x] Property not in order.json: has_StakeholderGroup_RiskSubgroup_Subject for StakeholderSubgroup (uid 3 )
- [x] Property not in order.json: has_StakeholderGroup_RiskSubgroup_Owner for StakeholderSubgroup (uid 3 )

- [x] Property without a label: has_TechGroup_StakeholderSubgroup for TechGroup (uid 3 )

- Stuff to categorize
  - Mitig -->
  - Risk -->
  - People -->
  - Tech --> 
- String:
  - List for the groups and subgroups

- Article: missing people at risk and owners

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
* [x] Add simplification mechanisms (centrality of items?)
* [x] Tools in a library
  * [x] KG."Simplify" --> KG -> KG
  * [x] KG."Modularize" --> KG -> (KG,KG)
  * [x] KG."Aggregate"  --> (KG,KG) -> KG
* [x] Update the technical note on KG - updated.
* [x] Update graph of the technical note.
* [x] Do a new release

### 20231217

* [x] Add ChromaDB of articles -> _done, in documentation/_
  * [x] Add caching of questions.
* [x] Article: 
  * [x] Generate paper without background
  * [x] Generate paper and add bakcground, EU flag and disclaimer
