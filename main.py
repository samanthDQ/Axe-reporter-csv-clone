import json
import pandas as pd
import os
import csv

all_records = []
all_rule_ids = {}

all_records_lib = {
  "nested-interactive": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "4.1.2 Name, Role, Value",
    "Section 508 Paragraph": ""
  },
  "color-contrast": {
    "Standard": "WCAG 2.0 Level AA",
    "WCAG 2 Success Criteria": "1.4.3 Contrast (Minimum)",
    "Section 508 Paragraph": ""
  },
  "area-alt": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "1.1.1 Non-text Content, 2.4.4 Link Purpose (In Context), 4.1.2 Name, Role, Value",
    "Section 508 Paragraph": "Paragraph A - Equivalent alternatives for non-text elements"
  },
  "aria-command-name": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "4.1.2 Name, Role, Value",
    "Section 508 Paragraph": ""
  },
  "aria-input-field-name": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "4.1.2 Name, Role, Value",
    "Section 508 Paragraph": ""
  },
  "aria-meter-name": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "1.1.1 Non-text Content",
    "Section 508 Paragraph": ""
  },
  "aria-progressbar-name": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "1.1.1 Non-text Content",
    "Section 508 Paragraph": ""
  },
  "aria-required-children": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "1.3.1 Info and Relationships",
    "Section 508 Paragraph": ""
  },
  "aria-required-parent": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "1.3.1 Info and Relationships",
    "Section 508 Paragraph": ""
  },
  "aria-roledescription": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "4.1.2 Name, Role, Value",
    "Section 508 Paragraph": ""
  },
  "aria-tooltip-name": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "4.1.2 Name, Role, Value",
    "Section 508 Paragraph": ""
  },
  "audio-caption": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "1.2.1 Audio-only and Video-only (Prerecorded)",
    "Section 508 Paragraph": "Paragraph A - Equivalent alternatives for non-text elements"
  },
  "blink": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "2.2.2 Pause, Stop, Hide",
    "Section 508 Paragraph": "Paragraph J - Screen flicker in range of 2 - 55 Hz"
  },
  "button-name": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "4.1.2 Name, Role, Value",
    "Section 508 Paragraph": "Paragraph A - Equivalent alternatives for non-text elements"
  },
  "definition-list": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "1.3.1 Info and Relationships",
    "Section 508 Paragraph": ""
  },
  "dlitem": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "1.3.1 Info and Relationships",
    "Section 508 Paragraph": ""
  },
  "frame-focusable-content": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "2.1.1 Keyboard",
    "Section 508 Paragraph": ""
  },
  "frame-title": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "2.4.1 Bypass Blocks, 4.1.2 Name, Role, Value",
    "Section 508 Paragraph": "Paragraph I - Title frames/iframes to facilitate frame identification and navigation"
  },
  "html-xml-lang-mismatch": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "3.1.1 Language of Page",
    "Section 508 Paragraph": ""
  },
  "input-image-alt": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "1.1.1 Non-text Content",
    "Section 508 Paragraph": "Paragraph A - Equivalent alternatives for non-text elements"
  },
  "marquee": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "2.2.2 Pause, Stop, Hide",
    "Section 508 Paragraph": ""
  },
  "meta-refresh": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "2.2.1 Timing Adjustable, 2.2.4 Interruptions, 3.2.5 Change on Request",
    "Section 508 Paragraph": ""
  },
  "object-alt": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "1.1.1 Non-text Content",
    "Section 508 Paragraph": "Paragraph A - Equivalent alternatives for non-text elements"
  },
  "role-img-alt": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "1.1.1 Non-text Content",
    "Section 508 Paragraph": "Paragraph A - Equivalent alternatives for non-text elements"
  },
  "scrollable-region-focusable": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "2.1.1 Keyboard",
    "Section 508 Paragraph": ""
  },
  "server-side-image-map": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "2.1.1 Keyboard",
    "Section 508 Paragraph": "Paragraph F - Convert server-side image maps to client-side image maps"
  },
  "svg-img-alt": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "1.1.1 Non-text Content",
    "Section 508 Paragraph": "Paragraph A - Equivalent alternatives for non-text elements"
  },
  "td-headers-attr": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "1.3.1 Info and Relationships",
    "Section 508 Paragraph": "Paragraph G - Row and column headers for data tables"
  },
  "th-has-data-cells": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "1.3.1 Info and Relationships",
    "Section 508 Paragraph": "Paragraph G - Row and column headers for data tables"
  },
  "video-caption": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "1.2.2 Captions (Prerecorded)",
    "Section 508 Paragraph": "Paragraph A - Equivalent alternatives for non-text elements"
  },
  "valid-lang": {
    "Standard": "WCAG 2.0 Level AA",
    "WCAG 2 Success Criteria": "3.1.2 Language of Parts",
    "Section 508 Paragraph": ""
  },
  "aria-allowed-attr": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "4.1.2 Name, Role, Value",
    "Section 508 Paragraph": ""
  },
  "aria-hidden-body": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "4.1.2 Name, Role, Value",
    "Section 508 Paragraph": ""
  },
  "aria-hidden-focus": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "4.1.2 Name, Role, Value, 1.3.1 Info and Relationships",
    "Section 508 Paragraph": ""
  },
  "aria-required-attr": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "4.1.2 Name, Role, Value",
    "Section 508 Paragraph": ""
  },
  "aria-roles": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "4.1.2 Name, Role, Value",
    "Section 508 Paragraph": ""
  },
  "aria-toggle-field-name": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "4.1.2 Name, Role, Value",
    "Section 508 Paragraph": ""
  },
  "aria-valid-attr": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "4.1.2 Name, Role, Value",
    "Section 508 Paragraph": ""
  },
  "aria-valid-attr-value": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "4.1.2 Name, Role, Value",
    "Section 508 Paragraph": ""
  },
  "bypass": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "2.4.1 Bypass Blocks",
    "Section 508 Paragraph": "Paragraph O - Repetitive navigation links"
  },
  "document-title": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "2.4.2 Page Titled",
    "Section 508 Paragraph": ""
  },
  "duplicate-id": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "4.1.1 Parsing",
    "Section 508 Paragraph": ""
  },
  "duplicate-id-active": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "4.1.1 Parsing",
    "Section 508 Paragraph": ""
  },
  "duplicate-id-aria": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "4.1.1 Parsing",
    "Section 508 Paragraph": ""
  },
  "form-field-multiple-labels": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "3.3.2 Labels or Instructions",
    "Section 508 Paragraph": ""
  },
  "html-has-lang": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "3.1.1 Language of Page",
    "Section 508 Paragraph": ""
  },
  "html-lang-valid": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "3.1.1 Language of Page",
    "Section 508 Paragraph": ""
  },
  "image-alt": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "1.1.1 Non-text Content",
    "Section 508 Paragraph": "Paragraph A - Equivalent alternatives for non-text elements"
  },
  "input-button-name": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "4.1.2 Name, Role, Value",
    "Section 508 Paragraph": "Paragraph A - Equivalent alternatives for non-text elements"
  },
  "label": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "4.1.2 Name, Role, Value, 1.3.1 Info and Relationships",
    "Section 508 Paragraph": "Paragraph N - Electronic forms"
  },
  "link-name": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "4.1.2 Name, Role, Value, 2.4.4 Link Purpose (In Context)",
    "Section 508 Paragraph": "Paragraph A - Equivalent alternatives for non-text elements"
  },
  "list": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "1.3.1 Info and Relationships",
    "Section 508 Paragraph": ""
  },
  "listitem": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "1.3.1 Info and Relationships",
    "Section 508 Paragraph": ""
  },
  "select-name": {
    "Standard": "WCAG 2.0 Level A",
    "WCAG 2 Success Criteria": "4.1.2 Name, Role, Value, 1.3.1 Info and Relationships",
    "Section 508 Paragraph": "Paragraph N - Electronic forms"
  }
}


def get_tags(tags_array=None):
    if type(tags_array) != list or tags_array == None:
        return ""
    string = ""
    for tag in tags_array:
        string = string + tag + ', '
    return string[:-2]

# Get a list of all JSON files in the directory

# get ruleset-lib

# create a rule library
# path_to_csv = 'december-file.csv'
#
# with open(path_to_csv, encoding="utf8") as f:
#     DictReader_obj = csv.DictReader(f)
#     for item_dict in DictReader_obj:
#         item = dict(item_dict)
#         rule = item["Rule iD"]
#         if rule not in all_rule_ids.keys():
#             all_rule_ids[rule] = {"Standard": item['Standard'],
#                                   'WCAG 2 Success Criteria': item['WCAG 2 Success Criteria'],
#                                   'Section 508 Paragraph': item['Section 508 Paragraph']
#                                   }


path_to_json = 'results/'
json_files = [f for f in os.listdir(path_to_json) if f.endswith('.json')]
# Loop through each JSON file and append the data to the DataFrame
for file in json_files:
    with open(os.path.join(path_to_json, file), 'r', encoding="utf8") as f:
        data = json.load(f)
    df = pd.json_normalize(data)
    d = df.to_dict(orient='records')

    violations = d[0]["findings.violations"]
    passes = d[0]["findings.passes"]
    incomplete = d[0]["findings.incomplete"]
    inapplicable = d[0]["findings.inapplicable"]
    timestamp = d[0]["findings.timestamp"]
    version = d[0]["findings.testEngine.version"]

    for violation in violations:
        violation_nodes = violation['nodes']
        Standard = ''
        SC: ''
        Section: ''
        if violation["id"] in all_records_lib.keys():
            Standard = all_records_lib[violation["id"]]["Standard"]
            SC = all_records_lib[violation["id"]]["WCAG 2 Success Criteria"]
            Section = all_records_lib[violation["id"]]["Section 508 Paragraph"]
        else:
            print("Missing Violation id in library:", violation["id"])

        for node in violation_nodes:
            node_impact = node["impact"].title() if node["impact"] is not None else ''
            new_dict = {"Page URL": d[0]["testSubject.fileName"], "Page title": d[0]["id"], "Outcome": "Failed",
                        "Impact": node_impact, "Code Snippet": node["html"], "Selector": node["target"][0],
                        "Remediation": node["failureSummary"], "Manual": "FALSE",
                        "Rule iD": violation["id"], "Help": violation["help"],
                        "Description": violation["description"], "Help URL": violation["helpUrl"],
                        "Standard": Standard,
                        "WCAG 2 Success Criteria": SC,
                        "Section 508 Paragraph": Section,
                        "Tags": get_tags(violation["tags"]), "Date": timestamp, "Axe-core": version
                        }
            all_records.append(new_dict)

    for pass_rec in passes:
        pass_nodes = pass_rec['nodes']
        for node in pass_nodes:
            node_impact = node["impact"].title() if node["impact"] is not None else ''
            new_dict = {"Page URL": d[0]["testSubject.fileName"], "Page title": d[0]["id"], "Outcome": "Passed",
                        "Impact": node_impact, "Code Snippet": node["html"], "Selector": node["target"][0],
                        "Remediation": "", "Manual": "FALSE",
                        "Rule iD": pass_rec["id"], "Help": pass_rec["help"],
                        "Description": pass_rec["description"], "Help URL": pass_rec["helpUrl"],
                        "Standard": all_records_lib[pass_rec["id"]]["Standard"],
                        "WCAG 2 Success Criteria": all_records_lib[pass_rec["id"]]["WCAG 2 Success Criteria"],
                        "Section 508 Paragraph": all_records_lib[pass_rec["id"]]["Section 508 Paragraph"],
                        "Tags": get_tags(pass_rec["tags"]), "Date": timestamp, "Axe-core": version
                        }
            all_records.append(new_dict)

    for incomplete_rec in incomplete:
        incomplete_nodes = incomplete_rec['nodes']
        for node in incomplete_nodes:
            node_impact = node["impact"].title() if node["impact"] is not None else ''
            new_dict = {"Page URL": d[0]["testSubject.fileName"], "Page title": d[0]["id"],
                        "Outcome": "Needs review",
                        "Impact": node_impact, "Code Snippet": node["html"], "Selector": node["target"][0],
                        "Remediation": node["failureSummary"], "Manual": "FALSE",
                        "Rule iD": incomplete_rec["id"], "Help": incomplete_rec["help"],
                        "Description": incomplete_rec["description"], "Help URL": incomplete_rec["helpUrl"],
                        "Standard": all_records_lib[incomplete_rec["id"]]["Standard"],
                        "WCAG 2 Success Criteria": all_records_lib[incomplete_rec["id"]]["WCAG 2 Success Criteria"],
                        "Section 508 Paragraph": all_records_lib[incomplete_rec["id"]]["Section 508 Paragraph"],
                        "Tags": get_tags(incomplete_rec["tags"]), "Date": timestamp, "Axe-core": version
                        }
            all_records.append(new_dict)

    for not_applicable_rec in inapplicable:
        new_dict = {"Page URL": d[0]["testSubject.fileName"], "Page title": d[0]["id"], "Outcome": "Inapplicable",
                    "Impact": "", "Code Snippet": "", "Selector": "",
                    "Remediation": "", "Manual": "FALSE",
                    "Rule iD": not_applicable_rec["id"], "Help": not_applicable_rec["help"],
                    "Description": not_applicable_rec["description"], "Help URL": not_applicable_rec["helpUrl"],
                    "Standard": all_records_lib[not_applicable_rec["id"]]["Standard"],
                    "WCAG 2 Success Criteria": all_records_lib[not_applicable_rec["id"]]["WCAG 2 Success Criteria"],
                    "Section 508 Paragraph": all_records_lib[not_applicable_rec["id"]]["Section 508 Paragraph"],
                    "Tags": get_tags(not_applicable_rec["tags"]), "Date": timestamp, "Axe-core": version
                    }
        all_records.append(new_dict)

data_frame = pd.DataFrame.from_dict(all_records)

data_frame.to_csv(r'axe-devtools-results.csv', index=False, header=True)
