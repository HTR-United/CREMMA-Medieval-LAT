""" This script simply compiles the main metadata file (data-registry.csv) 
        into a readable Markdown Table
"""
import csv
import tabulate


header = ["Shelfmark", "Folder", "Biblissima", "Pages", "Type", "Century", "Color", "Script", "Content"]

table = [
    header
]
with open("data-registry.csv") as f:
    for line in csv.DictReader(f):
        print(line)
        table.append(
            [
                f"[{line['Shelfmark ID']}]({line['Link']})",
                f"[🔗]({line['Folder']})",
                f"[→]({line['Biblissima']})" if line["Biblissima"] else "",
                line["Pages"],
                line["Type"],
                str((int(line["notBefore"]) + int(line["notAfter"])) // 200 + 1 ),
                "✓" if line["Status"] == "Color" else "✗",
                line["Script"],
                line["Content"]
            ]
        )


print(tabulate.tabulate(table, tablefmt="github", headers="firstrow"))