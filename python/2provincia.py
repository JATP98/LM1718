from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')
localidad= doc.findall('provincia/localidades/localidad')
for nombre in localidad:	
	print(nombre.text)
