""" This compiles alto files into XML files.

They need to be mufichecked before hand with 

>>> chocomufin -n NFD convert table.csv data/*/*.xml --parser alto

"""

import lxml.etree as ET
import glob

for file in sorted(glob.glob("data/*/*.mufichecker.xml")):
    xml = ET.parse(file)
    with open(file.replace(".mufichecker.xml", ".txt"), "w") as f:
        f.write(
            "\n".join([line.attrib["CONTENT"] for line in xml.findall("//{*}TextLine/{*}String")])
        )
