from django.db import models

# Create your models here.
'''

https://medicinaysaludpublica.com/categoria/articulos/

https://medicinaysaludpublica.com/categoria/noticias/

Modelos:
Se añade de un CSV
Foro:
    -ID
    -Nombre

WebScrapping
Tema:
    -Título
    -Autor puede ser nulo si la noticia es de web scrapping
    -NumRespuestas
    -Fecha última respuesta
    -Foro al que pertenece

WebScrapping    
Respuesta:
    -Autor
    -Fecha y hora
    -Texto
    -Tema al que responde


Usuario:
    -Nombre
    -Apellido
    -Email
    -Nombre de usuario
    -Contraseña
'''