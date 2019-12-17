# Rest-HTTP

Rest-http is a presto connector able to take in REST api's as a data source.

## Setup

Build the required .jar files for the plugin using the following command in the current directory

```bash
mvn package
```

To locate the built .jar files, type the following command

```
cd src/target
unzip presto-rest-http-0.230-SNAPSHOT.zip
cd presto-rest-http-0.230-SNAPSHOT
```

When installing the rest-http connector, presto requires a new directory for the .jar files in the plugins folder. For the folder structure, enquire the following visual and the presto documentation: https://prestodb.io/docs/current/installation/deployment.html 

```
unpacked presto-server-*.tar.gz
./
|-- bin
|-- lib
|-- plugin
|   |-- rest-http
|   |-- ...
```

## Catalog Configuration

In a INSERT_NAME.properties file, add the following properties required for the rest-http connector. The connector requires a uri to a json representation of the api schema. 

```
connector.name=rest-http
metadata-uri=http://example.com/
```