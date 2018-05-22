# zendesk_json_users
Bash que permite generar un archivo JSON a partir de un archivo CSV, para poder importarlo a la API Console de Zendesk v2

## Dependencias:

* python >=  2.7.12

## Explicación:
* Archivo:
```
generarJsonUsers.py
```

* Parametros de entradas:
```
   -f  :  Nombre de archivo CSV a procesar (sin la extención)
   -r  :  Cuantos Registros se va a Generar por archivo
```

## Como usarlo:
 Por consola deberá ejecutar esta instrucción:
``` 
$ python generarJsonUsers.py -f example -r 2000
``` 

 Si no muestra algún error, te mostrará información acerca del nombre de los archivos generado
<p align="center">
<img src="http://www.seguridadsistema.com.ve/github/zendesk/users/img/console1.png" />
</p>

 Luego abrir la pagina de Api Console de Zendesk
 ```
 https://developer.zendesk.com/requests/new
```
 Deberá personalizar la conexión en el cual, van a cargar los datos que se va a migrar, [más información](https://)
 
 
## Screenshot(s):
### Imagen de muestra del Archivo example.csv
<p align="center">
<img src="http://www.seguridadsistema.com.ve/github/zendesk/users/img/csv.png" />
</p>
### Imagen de muestra Cuando se genera


## Autor (Author)

  Jesus Maria Lobaton Escobar < jesuslobaton@gmail.com >

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

