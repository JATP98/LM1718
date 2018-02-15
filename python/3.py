from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')
provincia= doc.findall('provincia/nombre')
for nombre in provincia:	
	print(nombre.text)
nmunicipio= doc.findall('provincia/localidades/localidad')
#for nombre1 in nmunicipio:	
	print(len(nmunicipio))