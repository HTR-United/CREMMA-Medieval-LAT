import glob
import lxml.etree as et
import os

manifests = {
  "@context": "http://iiif.io/api/presentation/2/context.json", 
  "@id": "http://iiif.io/api/presentation/2.0/example/fixtures/1/manifest.json", 
  "@type": "sc:Manifest", 
  "label": "CREMMA Medii Aevi", 
  "within": "http://iiif.io/api/presentation/2.0/example/fixtures/collection.json", 
  "sequences": [
    {
      "@type": "sc:Sequence", 
      "canvases": []
    }
  ]
}

i = 0
for directory in glob.glob("../data/*"):
    for file in glob.glob(f"{directory}/*.mufichecker.xml"):
        i += 1
        xml = et.parse(file)
        image_name = str(xml.findall("//{*}fileName")[0].text)
        image_page = os.path.join(os.path.dirname(file), image_name)
        page = xml.findall("//{*}Page")[0]
        width, height = int(page.attrib["WIDTH"]), int(page.attrib["HEIGHT"])
        manifests["sequences"][0]["canvases"].append(
            {
              "@id": f"http://iiif.io/api/presentation/3.0/example/fixtures/canvas/1/c{i}.json", 
              "@type": "sc:Canvas", 
              "label": image_name, 
              "height": height, 
              "width": width,
              "images": [
                {
                  "@type": "oa:Annotation", 
                  "motivation": "sc:painting", 
                  "resource": {
                    "@id": image_page, 
                    "@type": "dctypes:Image", 
                    "height": height, 
                    "width": width
                  }
                }
              ],
              "seeAlso": [{
                "@id":  file, 
                "format": "application/xml+alto",
                "profile": "http://www.loc.gov/standards/alto/ns-v4#",
                "label": "OCR text"
              }]
            }
        )
    #break

import json
with open(f"simple_manifest.json", "w") as f:
    json.dump(manifests, f)
