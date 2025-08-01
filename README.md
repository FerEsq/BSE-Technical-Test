# BSE Technical Test
## 📜 Descripción
La solución a la prueba técnica incluye el procesamiento (limpieza y validación) de un archivo csv con más de 1.7 registros, la creación de un API REST para la obtención de información de dicho csv y la normalización del csv para la creación de una base ded adatos.


## 📦 Dependencias Principales
Las principales dependencias del proyecto incluyen:
* [![Python][Python]][Python-url]
* [![Markdown][Markdown]][Markdown-url]


## 👥 Developer

<a href="https://github.com/FerEsq">
  <img width='175' src="https://github.com/FerEsq/FerEsq/blob/main/assets/headset.png" alt="Fernanda Esquivel" />
</a>

* [![Linkedin][Linkedin]][Linkedin-fer]
* [![GitHub][GitHub]][GitHub-fer]


## 📞 Contacto
Si tienes preguntas o comentarios, puedes contactarme a traves de:

* [![Website][Website]][Website-fer]
* [![Mail][Mail]][Mail-fer]


## 💻 Instrucciones de Ejecución
### Clonar el repositorio
En la carpeta de su preferencia, abrir una terminal y ejecutar el comando:
```bash
gh repo clone FerEsq/BSE-Technical-Test
```

### Instalación de dependencias
En la carpeta de raiz, abrir una terminal y ejecutar el comando:
```bash
pip install -r requirements.txt
```

### Preprocesamiento
Primero, se debe ejecutar el código de [dataProcessing.ipynb](https://github.com/FerEsq/BSE-Technical-Test/blob/main/dataProcessing.ipynb). Para ello, puedes utilizar el IDE de tu preferencia o ejecutar el comando:
```bash
jupyter notebook dataProcessing.ipynb
```
Se creará el archivo `polizas_clean.csv` dentro de la carpeta `data` con el csv procesado.


### API REST
Para poder acceder al API, se debe ejecutar el código de [API.py](https://github.com/FerEsq/BSE-Technical-Test/blob/main/API.py), para ello, ejecuta el comando:
```bash
uvicorn API:app --reload
```
Luego, accede a Swager UI para poder poner a prueba los endpoints:
```
http://127.0.0.1:8000/docs
```


### Base de Datos
Finalmente, se debe ejecutar el código de [database.ipynb](https://github.com/FerEsq/BSE-Technical-Test/blob/main/database.ipynb). Para ello, puedes utilizar el IDE de tu preferencia o ejecutar el comando:
```bash
jupyter notebook database.ipynb
```
Con eso podrás acceder a la base de datos normalizada dentro de la carpeta `data/database`


## 📐 Diagrama Entidad-Relación
![ER](https://github.com/FerEsq/BSE-Technical-Test/blob/main/ER.png)

### Descripción de las tablas
* Polizas: Contiene información de las polizas (correlativo, fecha, aduana, regimen y tipo de cambio).
* Importaciones: Contiene información de las importaciones (correlativo, sac, país, unidad de medida, tasa y valor del impuesto, valor CIF, etc...)
* Aduanas: Contiene todas las aduanas.
* Regimenes: Contiene todos los tipos de régimen.
* SAC: Contiene todos los SAC.
* Paises: Contiene todos los países.
* Unidades_Medida: Contiene todas las unidades de medida.

<!-- MARKDOWN LINKS & IMAGES -->
[Python]: https://img.shields.io/badge/Python-4B8BBE?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org
[Markdown]: https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white
[Markdown-url]: https://www.markdownguide.org
[Vite]: https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=Vite&logoColor=white
[Vite-url]: https://vite.dev
[Mongo]: https://img.shields.io/badge/-MongoDB-13aa52?style=for-the-badge&logo=mongodb&logoColor=white
[Mongo-url]: https://www.mongodb.com
[Linkedin-fer]: https://www.linkedin.com/in/feresq
[Linkedin-monti]: https://www.linkedin.com/in/andrés-montoya-8a0743287/
[Linkedin]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[Github-fer]: https://github.com/FerEsq
[Github-monti]: https://github.com/Montoya086
[GitHub]: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white
[Github-url]: https://github.com
[Website]: https://img.shields.io/badge/Website-226946?style=for-the-badge&logo=opera&logoColor=white
[Website-fer]: https://fer-esq.web.app
[Mail]: https://img.shields.io/badge/Gmail-DC143C?style=for-the-badge&logo=gmail&logoColor=white
[Mail-fer]: mailto:feresq.gt@gmail.com
