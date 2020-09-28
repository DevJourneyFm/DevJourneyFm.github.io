#!/usr/bin/python
import sys
import os 

# Usage
# CreateGuest.py '114' 'Kemdi Ebi' 'Nov 04' 'title_without_number'

def loadIndex(path):
    indexFile = open(os.path.dirname(os.path.realpath(__file__)) + "\\" + path,'r')
    return indexFile.read()
    
def CreateFile(pagecontent, args):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # FileFormat Number_FirstNameLastName.html"
    number = args[1]
    nameWOSpaces = args[2].replace(" ", "")

    path = dir_path + "\\Guests\\" + number + "-" + nameWOSpaces + ".html"
    htmlFile = open(path, 'w')
    htmlFile.write(pagecontent)
    htmlFile.close()

    # FileFormat Number_FirstNameLastNameTx.html"
    pathTx = dir_path + "\\Guests\\Transcripts\\" + number + "-" + nameWOSpaces + "Tx.html"
    htmlTxFile = open(pathTx, 'w')
    htmlTxFile.write("<span></span>")
    htmlTxFile.close()

def overwriteFile(path, content):
    htmlFile = open(os.path.dirname(os.path.realpath(__file__)) + "\\" + path, 'w')
    htmlFile.write(content)
    htmlFile.close()

if(len(sys.argv) != 5):
    print("CreateGuest.py '114' 'Kemdi Ebi' 'Nov 04' 'title_without_number'")
    exit()

print("Creating pages for Guest: " + sys.argv[2])

GUEST_PAGE = """---
layout: default
comments: true
title: #NUMBER FIRSTNAME LASTNAME
description: #TITLE_WITHOUT_HASH
---
<h1>#TITLE_WITHOUT_HASH</h1>
<script type='text/javascript' charset='utf-8' src='https://www.buzzsprout.com/190346.js?player=small&artist=Timoth%C3%A9e%20Bourguignon,%20FIRSTNAME%20LASTNAME'></script>

<!--
<div>
        <h2>Transcript</h2>
        <p><i>
                The following transcript was automatically generated. </br>
                Help us out, <a
                    href="https://github.com/DevJourneyFm/DevJourneyFm.github.io/tree/master/Guests/Transcripts/NUMBER-FIRSTNAMELASTNAMETx.html">Submit
                    a pull-request</a> to correct potential mistakes
            </i></p>

        {% include_relative Transcripts/NUMBER-FIRSTNAMELASTNAMETx.html %}
    </div>
-->

{% if page.comments %}  
{% include disqus.html %}
{% endif %}"""

number = sys.argv[1]
guestname = sys.argv[2]
firstname = sys.argv[2].split(" ")[0]
lastname = sys.argv[2].split(" ")[1]
date = sys.argv[3]
title = sys.argv[4]

GUEST_PAGE = GUEST_PAGE.replace("NUMBER", number)
GUEST_PAGE = GUEST_PAGE.replace("FIRSTNAME", firstname)
GUEST_PAGE = GUEST_PAGE.replace("LASTNAME", lastname)
GUEST_PAGE = GUEST_PAGE.replace("TITLE_WITHOUT_HASH", number + " " + title)

CreateFile(GUEST_PAGE, sys.argv)

SLUG_TO_FIND = "<!-- insert here -->"
SLUG_TO_REPLACE = """<!-- insert here -->
        <li>DATE, 2020: <a href="/Guests/NUMBER-FIRSTNAMELASTNAME.html">#TITLE_WITHOUT_HASH</a></li>"""
SLUG_TO_REPLACE = SLUG_TO_REPLACE.replace("NUMBER", number)
SLUG_TO_REPLACE = SLUG_TO_REPLACE.replace("FIRSTNAME", firstname)
SLUG_TO_REPLACE = SLUG_TO_REPLACE.replace("LASTNAME", lastname)
SLUG_TO_REPLACE = SLUG_TO_REPLACE.replace("DATE", date)

emboldenedTitle = title.replace(guestname, "</br><b>" + guestname + "</b>")

SLUG_TO_REPLACE = SLUG_TO_REPLACE.replace("TITLE_WITHOUT_HASH", number + " " + emboldenedTitle)

content = loadIndex("index.html")
content = content.replace(SLUG_TO_FIND, SLUG_TO_REPLACE)

overwriteFile("index.html", content)