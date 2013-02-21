# Facebook-like Graph Search

This is the web site that was used during the February Baltimore Python Meetup group presentation.

## Requirements

* Neo4j (http://www.neo4j.org/install)
* Python >= 2.6
* virtualenv

## Usage

Download and run Neo4j (by default this will run at http://localhost:7474)

```
cd /path/to/neo4j/bin
./neo4j start
```

Download this project and create a virtual environment for it.

```
cd /path/to/meetup
virutalenv .
```

Start the environment

```
. bin/activate
```

Install dependencies with Pip. This simply installs Tornadoweb and neo4jrestclient

```
pip install -r requirements.txt
```

Run the script.py. This creates all of the nodes and funny connections.

```
python script.py
```

Start the webserver (this is defaulted to port 9003)

```
python meetup.py
```

## What you can do with the search box

Point your browser to http://localhost:9003

Find out who likes and dislikes nodes by typing in

```
likes node_name

dislikes node_name
```

Get the shortest path (six degrees of Kevin Bacon) between two nodes

```
nodeName<-->nodeName2
```

Click on a node to see all of its connections

### Have fun
