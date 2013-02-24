#!/usr/bin/env python
# encoding: utf-8
"""
util.py

Created by mark henderson on 2013-02-19.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""
from neo4jrestclient.client import GraphDatabase, Node, Relationship
from neo4jrestclient.query import Q
from neo4jrestclient.request import Request
import json

neo = GraphDatabase('http://localhost:7474/db/data')
name_index = neo.nodes.indexes.create('NAME', type='fulltext', provider='lucene')

def get(id):
    return neo.nodes.get(id)

def add(**kwargs):
    node = neo.nodes.create(**kwargs)
    name_index.add('NAME', 'name', node)
    return node 

def connect(right, left, name, **kwargs):
    #duplex relationships so that we can traverse in both directions
    right.relationships.create(name, left, **kwargs)
    left.relationships.create(name, right, **kwargs)
    
def search(connection, feels='likes'):
    lookup = Q('name', exact=connection)
    node = neo.nodes.filter(lookup)[-1]
    nodes = []

    for rel in node.relationships.all(types=[feels]):
        ends = [rel.start, rel.end]
        i = 0
        
        if ends[0] == node:
            i = 1
        
        rel_node = ends[i]
        
        if rel_node not in nodes:
            nodes.append(rel_node)
            
    return nodes


def degree(right, left, connection):
    lookup = Q('name', exact=right)
    start = neo.nodes.filter(lookup)[-1]

    lookup2 = Q('name', exact=left)
    end = neo.nodes.filter(lookup2)[-1]

    r = Request()
    d = {
        "to" : "http://localhost:7474/db/data/node/%s" % end.id,
        "max_depth" : 30,
        "relationships" : {
            "type" : connection,
            "direction" : "out"
        },
        "algorithm" : "shortestPath"
    }
    
    response, content = r.post("http://localhost:7474/db/data/node/%s/paths" % start.id, d)    
    print response, content, d

    content = json.loads(content)   
    if len(content) == 0:
        return []
    
    objs = []
    last = len(content[0]['nodes'])
    nodes = content[0]['nodes']
    relationships = content[0]['relationships']
    
    for k, v in enumerate(nodes):
        objs.append(Node(v))
        if(k != last - 1):
            objs.append(Relationship(relationships[k]))
            
    return objs