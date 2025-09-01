from rdflib import Graph, Namespace, RDF, RDFS, OWL, URIRef, Literal

# Load the ontology
g = Graph()
input_path = r"C:\Users\hspan\Desktop\ontology.owl"


# Namespace definition
BASE = Namespace("https://w3id.org/dpv/legal/eu/aiact#")
g.bind("ai", BASE)

# Class creation
def create_class(uri, label, parent_uri):
    g.add((uri, RDF.type, OWL.Class))
    g.add((uri, RDFS.label, Literal(label)))
    g.add((uri, RDFS.subClassOf, parent_uri))

# Subclass creation
def add_class_hierarchy(parent_uri, children_labels):
    for label in children_labels:
        uri = BASE[label.replace(" ", "_").replace("-", "").lower()]
        create_class(uri, label, parent_uri)

# Hierchy base
regulation_uri = BASE["regulation_eu"]
create_class(regulation_uri, "REGULATION (EU)", OWL.Class)

# Preamble και Recitals
preamble_uri = BASE["preamble"]
create_class(preamble_uri, "preamble", regulation_uri)

create_class(BASE["citation"], "citation", preamble_uri)
recitals = [f"recital {i}" for i in range(1, 181)]
add_class_hierarchy(preamble_uri, recitals)

# Enacting terms
enacting_terms_uri = BASE["enacting_terms"]
create_class(enacting_terms_uri, "enacting terms", regulation_uri)

# Chapter and article structure
structure = {
    "chapter_1": {
    "label": "chapter I - GENERAL PROVISIONS",
    "articles": [
      "article 1 - Subject matter",
      "article 2 - Scope",
      "article 3 - Definitions",
      "article 4 - AI literacy"
    ]
  },
  "chapter_2": {
    "label": "chapter II - PROHIBITED AI PRACTICES",
    "articles": [
      "article 5 - Prohibited AI practices"
    ]
  },
  "chapter_3": {
    "label": "chapter III - HIGH-RISK AI SYSTEMS",
    "sections": {
      "section_1": {
        "label": "section 1 - Classification of high-risk AI systems",
        "articles": [
          "article 6 - Classification rules for high-risk AI systems",
          "article 7 - Amendments to Annex III"
        ]
      },
      "section_2": {
        "label": "section 2 - Requirements for high-risk AI systems",
        "articles": [
          "article 8 - Compliance with the requirements",
          "article 9 - Risk management system",
          "article 10 - Data and data governance",
          "article 11 - Technical documentation",
          "article 12 - Record-keeping",
          "article 13 - Transparency and provision of information to users",
          "article 14 - Human oversight",
          "article 15 - Accuracy, robustness and cybersecurity"
        ]
      },
      "section_3": {
        "label": "section 3 - Obligations of economic operators and other stakeholders",
        "articles": [
          "article 16 - Obligations of providers",
          "article 17 - Quality management system",
          "article 18 - Documentation obligations",
          "article 19 - Automatic monitoring and control systems",
          "article 20 - Corrective actions",
          "article 21 - Cooperation with national authorities",
          "article 22 - Authorised representatives",
          "article 23 - Obligations of importers",
          "article 24 - Obligations of distributors",
          "article 25 - Responsibilities of operators placing on the market in third countries",
          "article 26 - Obligations of users",
          "article 27 - Fundamental rights impact assessments"
        ]
      },
      "section_4": {
        "label": "section 4 - Notifying and registration",
        "articles": [
          "article 28 - Notifying high-risk AI systems",
          "article 29 - Application of simplified procedure",
          "article 30 - Notification by providers",
          "article 31 - Requirements for notifying bodies",
          "article 32 - Presumption of conformity",
          "article 33 - Subsidiaries of providers",
          "article 34 - Operational cooperation",
          "article 35 - Identification of notified bodies",
          "article 36 - Changes to notified bodies’ designation",
          "article 37 - Challenge to the designation",
          "article 38 - Coordination of notified bodies",
          "article 39 - Conformity assessment procedures"
        ]
      },
      "section_5": {
        "label": "section 5 - Standards, harmonised specifications and CE marking",
        "articles": [
          "article 40 - Harmonised standards",
          "article 41 - Common specifications",
          "article 42 - Presumption of conformity",
          "article 43 - Conformity assessment modules",
          "article 44 - Certificates issued by notified bodies",
          "article 45 - Information exchange on standards",
          "article 46 - Derogation from conformity with harmonised standards",
          "article 47 - EU declaration of conformity",
          "article 48 - CE marking",
          "article 49 - Registration in the EU database"
        ]
      }
    }
  },
  "chapter_4": {
    "label": "chapter IV - TRANSPARENCY OBLIGATIONS FOR PROVIDERS OF GENERAL-PURPOSE AI SYSTEMS",
    "articles": [
      "article 50 - Transparency obligations"
    ]
  },
  "chapter_5": {
    "label": "chapter V - GENERAL-PURPOSE AI SYSTEMS",
    "sections": {
      "section_1": {
        "label": "section 1 - Classification rules",
        "articles": [
          "article 51 - Classification of general-purpose AI systems",
          "article 52 - Procedure"
        ]
      },
      "section_2": {
        "label": "section 2 - Obligations for providers",
        "articles": [
          "article 53 - Obligations for providers of general-purpose AI systems",
          "article 54 - Authorised representatives"
        ]
      },
      "section_3": {
        "label": "section 3 - Obligations of users",
        "articles": [
          "article 55 - Obligations of users of general-purpose AI systems"
        ]
      },
      "section_4": {
        "label": "section 4 - Codes of practice",
        "articles": [
          "article 56 - Codes of practice"
        ]
      }
    }
  },
  "chapter_6": {
    "label": "chapter VI - MEASURES IN SUPPORT OF INNOVATION",
    "articles": [
      "article 57 - AI regulatory sandboxes",
      "article 58 - Detailed rules for sandboxes",
      "article 59 - Further processing of data",
      "article 60 - Testing of AI systems",
      "article 61 - Informed consent to use of data",
      "article 62 - Measures for small and medium-sized enterprises",
      "article 63 - Derogations for certain AI systems"
    ]
  },
  "chapter_7": {
    "label": "chapter VII - GOVERNANCE",
    "sections": {
      "section_1": {
        "label": "section 1 - Governance at Union level",
        "articles": [
          "article 64 - AI Office",
          "article 65 - Establishment and composition of the European AI Board",
          "article 66 - Tasks of the Board",
          "article 67 - Advisory forum",
          "article 68 - Scientific panel of the Board",
          "article 69 - Access to the pool of experts"
        ]
      },
      "section_2": {
        "label": "section 2 - National competent authorities",
        "articles": [
          "article 70 - Designation of national competent authorities"
        ]
      }
    }
  },
  "chapter_8": {
    "label": "chapter VIII - EU DATABASE FOR HIGH-RISK AI SYSTEMS",
    "articles": [
      "article 71 - EU database for high-risk AI systems"
    ]
  },
  "chapter_9": {
    "label": "chapter IX - POST-MARKET MONITORING, SURVEILLANCE AND ENFORCEMENT",
    "sections": {
      "section_1": {
        "label": "section 1 - Post-market monitoring",
        "articles": [
          "article 72 - Post-market monitoring obligations"
        ]
      },
      "section_2": {
        "label": "section 2 - Sharing of information",
        "articles": [
          "article 73 - Reporting of serious incidents and malfunctioning"
        ]
      },
      "section_3": {
        "label": "section 3 - Enforcement",
        "articles": [
          "article 74 - Market surveillance authorities",
          "article 75 - Mutual assistance, cooperation and exchange of information",
          "article 76 - Supervision of providers and users",
          "article 77 - Powers of national authorities",
          "article 78 - Confidentiality",
          "article 79 - Procedure at national level",
          "article 80 - Procedure for implementing Union safeguard clause",
          "article 81 - Union safeguard",
          "article 82 - Compliance AI tools",
          "article 83 - Formal notices and penalties",
          "article 84 - Union AI testing and evaluation"
        ]
      },
      "section_4": {
        "label": "section 4 - Remedies",
        "articles": [
          "article 85 - Right to lodge a complaint",
          "article 86 - Right to an effective remedy",
          "article 87 - Reporting of …"
        ]
      },
      "section_5": {
        "label": "section 5 - Supervision, monitoring and coordination",
        "articles": [
          "article 88 - Enforcement of the …",
          "article 89 - Monitoring actions",
          "article 90 - Alerts of systemic …",
          "article 91 - Power to request …",
          "article 92 - Power to conduct …",
          "article 93 - Power to request …",
          "article 94 - Procedural rights …"
        ]
      }
    }
  },
  "chapter_10": {
    "label": "chapter X - CODES OF CONDUCT AND GUIDELINES",
    "articles": [
      "article 95 - Codes of conduct",
      "article 96 - Guidelines from the …"
    ]
  },
  "chapter_11": {
    "label": "chapter XI - DELEGATION OF POWER",
    "articles": [
      "article 97 - Exercise of the …",
      "article 98 - Committee procedure"
    ]
  },
  "chapter_12": {
    "label": "chapter XII - PENALTIES",
    "articles": [
      "article 99 - Penalties",
      "article 100 - Penalties"
    ]
  },
  "chapter_13": {
    "label": "chapter XIII - FINAL PROVISIONS",
    "articles": [
      "article 101 - Final provisions"
    ]
  }
}

# Insert to the data structure
for ch_key, ch_data in structure.items() :
    ch_uri = BASE[ch_key]
    create_class(ch_uri, ch_data["label"], enacting_terms_uri)
    if "sections" in ch_data:
        for sec_key, sec_data in ch_data["sections"].items():
            sec_uri = BASE[f"{ch_key}_{sec_key}"]
            create_class(sec_uri, sec_data["label"], ch_uri)
            add_class_hierarchy(sec_uri, sec_data["articles"])
    else:
        add_class_hierarchy(ch_uri, ch_data["articles"])

# Concluding formulas & Annexes
create_class(BASE["concluding_formulas"], "Concluding formulas", regulation_uri)
add_class_hierarchy(regulation_uri, [f"annex {i}" for i in range(1, 14)])

# Save as an OWL file
g.serialize(destination=r"C:\Users\hspan\Desktop\ontology4.0.owl", format="xml")
print("Ontology updated and saved to 'updated_ontology.owl'")
