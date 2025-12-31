# Ejercicio-Docker-Humai
Definir un cluster en Docker Compose que contenga:
  - Un contenedor con PostgreSQL con un punto de montaje en el directorio local en el cual se guarden los datos de la Base de Datos.
  - Un contenedor con pgAdmin con un volumen nombrado en el cual se guarden las conexiones a las Bases de Datos.
Mediante el pgAdmin conectarse al PostgreSQL y crear una Base de Datos llamada bank
Si detenemos el cluster y lo volvemos a levantar con docker-compose up deberiamos seguir viendo la conexion a la base de datos y la base de datos bank
Definir un script de Python que mediante Pandas lea el CSV guardado en https://storage.googleapis.com/humai-datasets/aws_s3/python_dev/5_Docker/ejercicios/bank-additional-full.csv y lo escriba en una tabla llamada clients en la Base de Datos bank
Definir un Dockerfile que contenga ese script y todas sus dependencias, cada vez que se lance el contenedor debe sobreescribir la tabla.
