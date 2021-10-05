# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bibWrQLv_P-j9x_4ZsAu3uJhLBOuBvEQ

**Task 07: Querying RDF(s)**
"""

!pip install rdflib 
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

for subj, pred, obj in g:
  print(subj,pred,obj)

"""**TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**"""

# TO DO
# Visualize the results
from rdflib.plugins.sparql import prepareQuery

VCARD = Namespace("http://www.w3.org/2000/01/rdf-schema#")
ns = Namespace("http://somewhere#")

q1=prepareQuery('''
  SELECT ?Subclass WHERE {
    ?Subclass vcard:subClassOf+ ?Class .
  }
  ''',
  initNs = { "vcard": VCARD}
)

for r in g.query(q1, initBindings = {'?Class': ns.Person }):
  print(r.Subclass)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

# TO DO
# Visualize the results

ns0 = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

q2=prepareQuery('''
  SELECT ?Subject WHERE {
    ?Subclass vcard:subClassOf* ?Class .
    ?Subject ns0:type ?Subclass .
  }
  ''',
  initNs = { "vcard": VCARD, "ns0": ns0}
)

for r in g.query(q2, initBindings = {'?Class': ns.Person }):
  print(r.Subject)

"""**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**

"""

# TO DO
# Visualize the results

q3=prepareQuery('''
  SELECT ?Subject ?Properties ?Value WHERE {
    ?Subclass vcard:subClassOf* ?Class .
    ?Subject ns0:type ?Subclass .
    ?Subject ?Properties ?Value.
  }
  ''',
  initNs = { "vcard": VCARD, "ns0": ns0}
)

for r in g.query(q3, initBindings = {'?Class': ns.Person }):
  print(r.Subject, r.Properties, r.Value)