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
 Por consola debera ejecutar esta instrucción:
``` 
$ python generarJsonUsers.py -f example -r 2000
``` 
Te generará un archivo example.json en la misma carpeta raiz que esta ejecutando el archivo
Luego, ab


### Screenshot(s):
<p align="center">
<img src="http://www.seguridadsistema.com.ve/ggithub/zendesk/users/img/csv.png" />
</p>

<p align="center">
<img src="http://www.seguridadsistema.com.ve/ggithub/zendesk/users/img/console1.png" />
</p>

## Autor (Author)

  Jesus Maria Lobaton Escobar < jesuslobaton@gmail.com >

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

