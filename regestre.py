import re

exemple = '''
P1 est un produit composé de P2 et P3
P2 est un produit élémentaire
P5 est un produit composé de P1 et P4
P4 est un produit élémentaire
P9 est un produit composé de P1, P6 et P4
P10 est un produit composé de P3 et P5
P11 est un produit composé de P5 et P3
'''

produits_elementaires = re.findall(r'\b(\w+)\s+est\s+un\s+produit\s+élémentaire\b', exemple)

produits_composes_trois = re.findall(r'\b(\w+)\s+est\s+un\s+produit\s+composé\s+de\s+(\w+)\s+et\s+(\w+)\b', exemple)

produits_composes_P3_P5 = re.findall(r'\b(\w+)\s+est\s+un\s+produit\s+composé\s+de\s+P3\s+et\s+P5\b', exemple)

produits_composes_sans_P2 = re.findall(r'\b(\w+)\s+est\s+un\s+produit\s+composé\s+(?!de\s*P2)\b', exemple)

produits_composants_P9 = re.findall(r'\bP9\s+est\s+un\s+produit\s+composé\s+de\s+([\w\s,]+)\b', exemple)

print("1. Produits élémentaires:", produits_elementaires)
print("2. Produits composés de trois produits:", produits_composes_trois)
print("3. Produits composés de P3 et P5:", produits_composes_P3_P5)
print("4. Produits composés sans P2:", produits_composes_sans_P2)
print("5. Produits qui composent P9:", produits_composants_P9)