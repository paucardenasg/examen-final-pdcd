# Examen Final Proyecto de Ciencia de Datos
## Paula Daniela Cárdenas Gallardo | `733720`
### Viernes 25 de noviembre de 2022

Este repositorio contiene el examen final de la materia Proyecto en Ciencia de Datos. Dentro de él se encuentra la solución de un problema donde se busca crear un modelo que clasifique si un proyecto recibirá fondos o no. Dichos proyectos son de escuelas de Estados Unidos desarrollados por maestros para mejorar las condiciones de los estudiantes, resolver problemáticas como el bullying, mejorar el prendizaje, etc.
Para la solución se realizó:
+ Análisis Exploratorio de Datos (EDA por sus siglas en inglés)
+ Ingeniería de Características (Data Wrangling)
+ Entrenamiento, validación, evaluación y selección del modelo de clasificación
+ Microservicio (API) para servir el modelo
+ Creación de imagen para dicha API
  + Explicación del procedimiento utilizado para crear la imagen y correr el contenedor
  + Imágenes como prueba del funcionamiento del contenedor de la API
+ Interpretación de resultados y conclusiones
  
Lo anterior se encuentra en un archivo .ipynb con su respectivo archivo `requirements.txt` para no tener problemas en la ejecución de la solución. Además, en la carpeta de `API` se encuentra el arvhico .py con el código necesario para ejecutarla, el `requirements.txt` y el `Dockerfile` para el desarrollo del proyecto. De la misma manera, este repositorio contiene este `README.md` y un archivo `.gitignore` para no tener archivos que no son necesarios, como los checkpoints de Jupyer Notebook. Únicamente hay una rama en este repositorio, la `main`.

En cuanto al conjunto de datos que se utilizarán, se obtuvieron a través de un [enlace](https://drive.google.com/file/d/1sQ7Fw0tO9GV-qnErJTQEbnqAACcPc18Q/view). Cuenta con las siguientes variables:
+ `Project Title` $\Rightarrow$ Nombre del proyecto
+ `Project Short Description` $\Rightarrow$ Descripción corta del proyecto
+ `Project Subject Category Tree` $\Rightarrow$ Taxonomía que indica el área al que pertenece el proyecto
+ `Project Cost` $\Rightarrow$ Cantidad de fondos solicitados
+ `Project Current Status` $\Rightarrow$ Si el proyecto fue fondedado o no (Variable de respuesta)
