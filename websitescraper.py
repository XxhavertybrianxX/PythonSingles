import requests
import html,http
from html import parser

import xml.etree.ElementTree as ET
sess = requests.session()

sitenm = "https://www.tmobile.careers/job-search?e=Mid-Career&dd=e"



with sess.request('GET', sitenm) as req:
    parser = ET.XMLParser(target=req.content,encoding=req.encoding)
    print(parser.buffer_text)
    et.

