# Author- Amit Raj
# Description- search a string in InLine post-functions of JIRA workflow.
# Use Case- you would like to search a password string or a userid which is used in InLine groovy scripts
#         - print all the groovy scripts from a workflow xml file, this will decode the encoded inline post-functions
#
import xml.etree.ElementTree as ET
import base64

Search_String = '<search string here>'
tree = ET.parse(r'C:\Users\admin\Desktop\sample workflow 1.5.xml')  # path of your workflow xml file
root = tree.getroot()

for i in root.iter('step'):
    print(i.attrib['id'], i.attrib['name'])
    for j in i.findall('./actions/'):
        print(" --", j.get('name'))
        for k in j.findall('./results/'):
            for l in k.findall('./post-functions/'):
                for m in l.findall('./arg'):
                    if m.attrib['name'] == 'FIELD_INLINE_SCRIPT':
                        data = base64.b64decode(m.text).decode("utf-8")
                        # print(data) # uncomment if you would like to print the inline groovy script
                        if Search_String in data:
                            print("      *******", m.attrib['name'], ":found:", Search_String)