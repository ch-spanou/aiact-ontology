from rdflib import Graph, Namespace, RDF, RDFS, OWL, Literal, URIRef

# Load the uploaded ontology file
ontology_path = r"C:\Users\hspan\Desktop\ontology.owl"
g = Graph()
g.parse(ontology_path)

# Define namespaces
EX = Namespace("https://w3id.org/dpv/legal/eu/aiact")
g.bind("ex", EX)
g.bind("owl", OWL)
g.bind("rdfs", RDFS)

# Define key classes
classes = {
    "AICategory": ["Prohibited", "HighRisk", "TransparencyOnly", "GeneralPurpose"],
    "Actor": ["Provider", "Deployer", "Importer", "Distributor"],
    "Documentation": ["TechDoc", "RiskFile", "TransparencyReport", "GPAIDoc"],
    "ProhibitedPractice": ["SocialScoring", "EmotionRecognition", "RemoteBiometricID", "CriminalRiskAssessment", "BiometricCategorization", "Manipulation", "Scraping"],
    "Exclusion": ["OpenSourceExclusion", "MilitaryUse", "IPProtectedUse"],
    "Guideline": ["ProhibitedAI", "AISystemDefinition", "GPAIGuidance"],
}

# Create classes and instances
for class_name, instances in classes.items():
    class_uri = EX[class_name]
    g.add((class_uri, RDF.type, OWL.Class))
    for instance in instances:
        instance_uri = EX[instance]
        g.add((instance_uri, RDF.type, class_uri))

# Define properties
properties = {
    "provides": (EX.Actor, EX.AICategory),
    "deploys": (EX.Actor, EX.AICategory),
    "mustHaveDoc": (EX.AICategory, EX.Documentation),
    "prohibitedBy": (EX.AICategory, EX.ProhibitedPractice),
    "excludedFrom": (EX.AICategory, EX.Exclusion),
    "clarifiedBy": (EX.AICategory, EX.Guideline),
    "entryIntoForceDate": (EX.AICategory, None),
    "complianceDeadline": (EX.AICategory, None),
}

# Create object and datatype properties
for prop, (domain, range_) in properties.items():
    prop_uri = EX[prop]
    g.add((prop_uri, RDF.type, OWL.ObjectProperty if range_ else OWL.DatatypeProperty))
    g.add((prop_uri, RDFS.domain, domain))
    if range_:
        g.add((prop_uri, RDFS.range, range_))

# Save updated ontology
updated_ontology_path = r"C:\Users\hspan\Desktop\ontology2.0.owl"
g.serialize(destination=updated_ontology_path, format="xml")
updated_ontology_path
