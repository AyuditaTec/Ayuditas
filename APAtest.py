print("Bienvenido a Bibliografía APA tipo PrepaTec. Comenzaré haciendo preguntas ahre.")
print()
print("Qué tipo de fuente estás usando?")
print()
print("1 : Página de Internet")
print()
print("2 :  Fotos e Imágenes de Internet")
print()
print("3 : Libros")
print()
print("4 : Fuentes de Consulta (ej. Diccionarios, encyclopedias, constituciones)")
print()
print("5 : Periódicos")
print()
print("6 : Medios Audiovisuales")
print("A continuación, escribe el número de tu elección")
opcion = int (input())
##Página de internet##
						
if opcion == 1:
	print("Tu fuente tiene autor? (Normalmente se encuentra al final o al principio de la página; pero no uses apodos)")
	print("1 : Sí		2: No")
	eleccion1 = int (input())
							##Con Autor##
if eleccion1 == 1:
	print("Escribe su apellido completo a continuación. Recuerda que si es nombre de autor hispano, son dos apellidos.")
	apellidos = str (input())
	print("Escribe la primera letra de su primer nombre.")
	nombre = str (input())
	print("Tu fuente tiene fecha?")
	print("1 : sí			2 : No")
	eleccion12 = int(input())
	if eleccion12 == 1:
		print("Escribe el año.")
		fecha = str (input())
	if eleccion12 == 2:
		fecha = "s. f."
		print( "Está bien, continuemos")
	print("Cómo se llama el artículo? (este es el título de la página, pero no el nombre como tal.)")
	print("Por ejemplo, el título puede ser 'Salvar Tortugas' pero la página se llama BBC o Wikipedia.")
	titulo = str (input())
	print("Perfecto, ya casi acabamos")
	print("Cómo se llama la página?")
	pagina = str (input())
	print("Para terminar, proporcióname con el URL")
	url = str (input())
	print()
	print(apellidos + ", " + nombre + ". " + "(" + fecha + ")" + ". " + titulo + ". " + pagina + ". Recuperado de " + url)
	
							##Sin Autor##
	
if eleccion1 == 2:
	print("Está bien, continuemos")
	print("Tu fuente tiene fecha?")
	print("1 : sí			2 : No")
eleccion12 = int(input())
if eleccion12 == 1:
	print("Escribe el año.")
	fecha = str (input())
if eleccion12 == 2:
	fecha = "s. f."
	print( "Está bien, continuemos")
print("Cómo se llama el artículo? (este es el título de la página, pero no el nombre como tal.)")
print("Por ejemplo, el título puede ser 'Salvar Tortugas' pero la página se llama BBC o Wikipedia.")
titulo = str (input())
print("Perfecto, ya casi acabamos")
print("Cómo se llama la página?")
pagina = str (input())
print("Para terminar, proporcióname con el URL")
url = str (input())
print()
print(titulo + ". (" + fecha + ")" + ". " + pagina + ". Recuperado de " + url)