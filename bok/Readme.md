# Body of knowledge management


Store
* Your GROBID-processed articles in a zip file in data/
* Your bibliography in biblio.XXX

# Installing GROBID
 
[https://grobid.readthedocs.io/en/latest/Grobid-docker/]()
 
Current latest version:
```
> docker pull grobid/grobid:0.7.2
```

* Run the container:
```
> docker run --rm --gpus all -p 8070:8070 grobid/grobid:0.7.2
```
