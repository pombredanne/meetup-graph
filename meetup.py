#!/usr/bin/env python
# encoding: utf-8
"""
meetup.py

Created by mark henderson on 2013-02-19.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""
import os
import re
from tornado import httpserver, ioloop, web
from neo4jrestclient.client import Relationship
import util


class Application(web.Application):    
    def __init__(self):
        settings = {
            'debug': True,
            'autoescape': None,
            'static_path': os.path.join(os.path.dirname(__file__), 'static'),
        }

        routes = [
            (r'/', PageHandler),
            (r'/search', SearchHandler),
            (r'/node/(\d+)', NodeHandler),
        ]
        web.Application.__init__(self, routes, **settings)

class PageHandler(web.RequestHandler):
    def get(self):
        self.render('template/base.html')
        
class NodeHandler(web.RequestHandler):
    def get(self, node_id):
        node = util.get(node_id)
        others = []
        likes = []
        dislikes = []

        if node:
            for rel in node.relationships.all():
                if rel.end != node:
                    if rel.type == 'likes':
                        likes.append(rel.end)
                    elif rel.type == 'dislikes':
                        dislikes.append(rel.end)
                    else:
                        others.append(rel.end)
        print likes, others
        self.write({
            'results': self.render_string('template/detail.html', node=node, others=others, likes=likes, dislikes=dislikes)
        })
        
class SearchHandler(web.RequestHandler):
    def get(self):
        """figure out the type of search that was performed
        
        if it has the words like or dislike, capture the word after 
            and do a search
        if it contains <--> capture the words before and after and do
            a degree search
        """
        nodes = []
        results = ''
        search = str(self.get_argument('search', ''))
        bacon = False
        template = 'template/node.html'
        
        if '<-->' in search:
            r = re.search('(.*?)<\-\->(.*)\W*', search)
            bacon = True
            
            if r:
                left = r.group(1)
                right = r.group(2)
                nodes = util.degree(left, right, 'likes')
        elif 'likes' in search:
            r = re.search('(?:dis)?likes\s(\w+)', search)
            feels = 'likes'
            
            if 'dislikes' in search:
                feels = 'dislikes'

            if r:
                nodes = util.search(r.group(1), feels)

        for n in nodes:
            if bacon:
                if isinstance(n, Relationship):
                    template = 'template/relationship.html'
                    print '[[[[]', n.type
                else:
                    template = 'template/node.html'
                results += self.render_string(template, node=n, klass='relationship_node')
            else:
                results += self.render_string(template, node=n, klass="")
            
        self.write({
            'results': results
        })
            
if __name__ == '__main__':
    """Start the application"""
    http_server = httpserver.HTTPServer(Application())
    http_server.listen(9003)
    ioloop.IOLoop.instance().start()
