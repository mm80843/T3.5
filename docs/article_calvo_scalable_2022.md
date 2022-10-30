# Article: __Scalable IoT Architecture for Monitoring IEQ Conditions in Public and Private Buildings__ (calvo_scalable_2022)

* [10.3390/en15062270](https://doi.org/10.3390/en15062270)
* Cluster: [building-space](cluster_7)


## Keywords

[ieq](keyword_ieq), [iot](keyword_iot)

## Abstract

This paper presents a scalable IoT architecture based on
the edge–fog–cloud paradigm for monitoring the Indoor
Environmental Quality (IEQ) parameters in public buildings.
Nowadays, IEQ monitoring systems are becoming important for
several reasons: (1) to ensure that temperature and
humidity conditions are adequate, improving the comfort and
productivity of the occupants; (2) to introduce actions to
reduce energy consumption, contributing to achieving the
Sustainable Development Goals (SDG); and (3) to guarantee
the quality of the air—a key concern due to the COVID-19
worldwide pandemic. Two kinds of nodes compose the proposed
architecture; these are the so-called: (1) smart IEQ sensor
nodes, responsible for acquiring indoor environmental
measures locally, and (2) the IEQ concentrators,
responsible for collecting the data from smart sensor nodes
distributed along the facilities. The IEQ concentrators are
also responsible for configuring the acquisition system
locally, logging the acquired local data, analyzing the
information, and connecting to cloud applications. The
presented architecture has been designed using low-cost
open-source hardware and software—specifically, single
board computers and microcontrollers such as Raspberry Pis
and Arduino boards. WiFi and TCP/IP communication
technologies were selected, since they are typically
available in corporative buildings, benefiting from already
available communication infrastructures. The application
layer was implemented with MQTT. A prototype was built and
deployed at the Faculty of Engineering of Vitoria-Gasteiz,
University of the Basque Country (UPV/EHU), using the
existing network infrastructure. This prototype allowed for
collecting data within different academic scenarios.
Finally, a smart sensor node was designed including
low-cost sensors to measure temperature, humidity, eCO2,
and VOC.


## Concepts

 ![](imgs/article_calvo_scalable_2022.jpg)

### References 

* [Continuous IEQ monitoring system: Context and
development](article_parkinson_continuous_2019)
* [The ventilation of buildings and other mitigating measures
for COVID-19: a focus on wintertime](article_burridge_ventilation_2021)

### Cited by 


