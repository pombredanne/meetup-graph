#!/usr/bin/env python
# encoding: utf-8
"""
script.py

Created by mark henderson on 2013-02-19.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""
from util import add, connect

#create the main node
meetup = add(name='meetup')


#add everyone 
mark = add(name='mark')
patrick = add(name='patrick')
greg = add(name='greg')
joel = add(name='joel')
leila = add(name='leila')
howard = add(name='howard')
henry = add(name='henry')
brandon = add(name='brandon')
chris = add(name='chris')
kevin = add(name='kevin')
will = add(name='will')
mike = add(name='mike')
kathleen = add(name='kathleen')
foster = add(name='foster')
jeff = add(name='jeff')
matt = add(name='matt')
david = add(name='david')
vijay = add(name='vijay')



#add things
python = add(name='python')
php = add(name='php')
js = add(name='javascript')
pizza = add(name='pizza')
beer = add(name='beer')
cleaning = add(name='cleaning')
interning = add(name='interning')



#add what people like
connect(meetup, python, 'likes')
connect(meetup, beer, 'likes')
connect(meetup, patrick, 'organizer')
connect(mike, cleaning, 'likes')
connect(mike, kathleen, 'married')
connect(kathleen, cleaning, 'likes')
connect(mark, python, 'likes')
connect(mark, php, 'likes')
connect(mark, js, 'likes')
connect(kevin, interning, 'dislikes')
connect(kevin, beer, 'likes')


