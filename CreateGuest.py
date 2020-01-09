#!/usr/bin/python
import sys
import os 

def loadIndex(path):
    indexFile = open(os.path.dirname(os.path.realpath(__file__)) + "\\" + path,'r')
    return indexFile.read()
    
def CreateFile(pagecontent, args):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    path = dir_path + "\\Guests\\" + args[1] + "_" + args[2] + args[3] + ".html"
    htmlFile = open(path, 'w')
    htmlFile.write(pagecontent)
    htmlFile.close()

def overwriteFile(path, content):
    htmlFile = open(os.path.dirname(os.path.realpath(__file__)) + "\\" + path, 'w')
    htmlFile.write(content)
    htmlFile.close()

if(len(sys.argv) != 5):
    print("CreateGuest.py 74 Kemdi Ebi 'Nov 04' 'title_without_#'")
    exit()

print("Creating pages for Guest: " + sys.argv[2] + " " + sys.argv[3])

GUEST_PAGE = """---
layout: default
comments: true
title: NUMBER FIRSTNAME LASTNAME
description: TITLE_WITHOUT_HASH
---
<h1>#TITLE_WITHOUT_HASH</h1>
<script type='text/javascript' charset='utf-8' src='https://www.buzzsprout.com/190346.js?player=small&artist=Timoth%C3%A9e%20Bourguignon,%20FIRSTNAME%20LASTNAME'></script>

{% if page.comments %}  
{% include disqus.html %}
{% endif %}"""

GUEST_PAGE = GUEST_PAGE.replace("NUMBER", sys.argv[1])
GUEST_PAGE = GUEST_PAGE.replace("FIRSTNAME", sys.argv[2])
GUEST_PAGE = GUEST_PAGE.replace("LASTNAME", sys.argv[3])
GUEST_PAGE = GUEST_PAGE.replace("TITLE_WITHOUT_HASH", sys.argv[4])

CreateFile(GUEST_PAGE, sys.argv)

SLUG_TO_FIND = "<!-- insert here -->"
SLUG_TO_REPLACE = """<!-- insert here -->
        <li>DATE, 2020: <a href="/Guests/NUMBER_FIRSTNAMELASTNAME.html">#NUMBER FIRSTNAME LASTNAME</a></li>"""
SLUG_TO_REPLACE = SLUG_TO_REPLACE.replace("NUMBER", sys.argv[1])
SLUG_TO_REPLACE = SLUG_TO_REPLACE.replace("FIRSTNAME", sys.argv[2])
SLUG_TO_REPLACE = SLUG_TO_REPLACE.replace("LASTNAME", sys.argv[3])
SLUG_TO_REPLACE = SLUG_TO_REPLACE.replace("DATE", sys.argv[4])

content = loadIndex("index.html")
content = content.replace(SLUG_TO_FIND, SLUG_TO_REPLACE)

overwriteFile("index.html", content)