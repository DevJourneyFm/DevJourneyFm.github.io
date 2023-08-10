#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import io

# Usage
# CreateGuest.py '114' 'Kemdi Ebi' 'Nov 04' 'title_without_number'

def loadIndex(path):
    indexFile = open(os.path.dirname(os.path.realpath(__file__)) + "//" + path,'r', encoding='utf-8')
    return indexFile.read()
    
def CreateFile(pagecontent, args):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # FileFormat Number_FirstNameLastName.html"
    number = args[1]
    nameWOSpaces = args[2].replace(" ", "")

    path = dir_path + "//Guests//" + number + "-" + nameWOSpaces + ".html"
    htmlFile = open(path, 'w', encoding='utf-8')
    htmlFile.write(pagecontent)
    htmlFile.close()

    # FileFormat Number_FirstNameLastNameTx.html"
    pathTx = dir_path + "//Guests//Transcripts//" + number + "-" + nameWOSpaces + "Tx.html"
    htmlTxFile = open(pathTx, 'w', encoding='utf-8')
    htmlTxFile.write("<span></span>")
    htmlTxFile.close()

def overwriteFile(path, content):
    htmlFile = open(os.path.dirname(os.path.realpath(__file__)) + "//" + path, 'w', encoding='utf-8')
    htmlFile.write(content)
    htmlFile.close()

if(len(sys.argv) != 5):
    print("CreateGuest.py '114' 'Kemdi Ebi' 'Nov 04' 'title_without_number'")
    exit()

print("Creating pages for Guest: " + sys.argv[2])

GUEST_PAGE = """---
layout: default
comments: true
title: "#NUMBER FIRSTNAME LASTNAME"
description: "#TITLE_WITHOUT_HASH"
---
<h1>#TITLE_WITHOUT_HASH</h1>
<script type='text/javascript' charset='utf-8' src='https://www.buzzsprout.com/190346.js?player=small&artist=Timoth%C3%A9e%20Bourguignon,%20FIRSTNAME%20LASTNAME'></script>

<div><h2>Resources</h2>
    <ul>
        <li></li>
        <li>Cover <a href="https://freemusicarchive.org/music/Blue_Dot_Sessions/Zander/Campfire_Rounds">Campfire Rounds</a> by <a href="https://freemusicarchive.org/music/Blue_Dot_Sessions#contact-artist">Blue Dot Sessions</a> is licensed <a href="http://creativecommons.org/licenses/by-nc-nd/4.0/">CC BY-NC-ND 4.0.</a></li>
    </ul>
</div>

<div><h2>Highlights</h2>
    <p>

    </p>
</div>

<div>
    <h2>Enjoyed the Podcast?</h2>
    If you did, make sure to <a href="https://devjourney.info/subscribe">subscribe</a> and share it with your friends!<br/><br/>
    <b>Post a review and share it!</b> If you enjoyed tuning in, leave us a review. You can also share this podcast with your friends and family and share lessons on software development.<br/><br/>
    <b>Become a supporter of the show.</b> Head over to <a href="https://www.patreon.com/timbourguignon">Patreon</a> or on <a href="https://www.buzzsprout.com/190346/support">Buzzsprout</a>.<br/><br/>
    <b>Got any questions?</b> You can connect with me, Timothée (Tim) Bourguignon, on <a href="https://www.linkedin.com/in/timbourguignon/">LinkedIn</a>, per <a href="mailto:info@devjourney.info">email</a>, or via my <a href="https://timbourguignon.fr">homepage</a>.<br/><br/>
    Thank you for tuning in!
</div>

<div><h2>Transcript</h2>
    <p><i>
            ⚠ The following transcript was automatically generated. </br>
            ❤ Help us out, <a
                href="https://github.com/DevJourneyFm/DevJourneyFm.github.io/tree/master/Guests/Transcripts/NUMBER-FIRSTNAMELASTNAMETx.html">Submit
                a pull-request</a> to correct potential mistakes
        </i></p>

    {% include_relative Transcripts/NUMBER-FIRSTNAMELASTNAMETx.html %}
</div>

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
        <li><a href="/Guests/NUMBER-FIRSTNAMELASTNAME.html">#TITLE_WITHOUT_HASH</a> - DATE, 2023</li>"""
SLUG_TO_REPLACE = SLUG_TO_REPLACE.replace("NUMBER", number)
SLUG_TO_REPLACE = SLUG_TO_REPLACE.replace("FIRSTNAME", firstname)
SLUG_TO_REPLACE = SLUG_TO_REPLACE.replace("LASTNAME", lastname)
SLUG_TO_REPLACE = SLUG_TO_REPLACE.replace("DATE", date)

emboldenedTitle = title.replace(guestname, "<b>" + guestname + "</b>")

SLUG_TO_REPLACE = SLUG_TO_REPLACE.replace("TITLE_WITHOUT_HASH", number + " " + emboldenedTitle)

content = loadIndex("index.html")
content = content.replace(SLUG_TO_FIND, SLUG_TO_REPLACE)

overwriteFile("index.html", content)