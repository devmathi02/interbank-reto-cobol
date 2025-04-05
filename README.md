# Solución Reto Técnico: Procesamiento de Transacciones Bancarias (CLI)

## Introduccion:

Este proyecto es la solución al Reto Técnico Cobol, mi solucion analiza el reporte de las transacciones financieras en formato CSV. El proposito es calcular el balance final, encontrar la transaccion con el monto mayor y contar la cantidad de transacciones que hay del tipo Crédito y Débito.

Se hizo un fork como se pidio en las instrucciones del repositorio base:
`https://github.com/codeableorg/interbank-academy-25`

---

## Instrucciones de Ejecucion

1. **Lenguaje y Dependencias**  
   El lenguaje a utilizar es Python, para ellos debe asegurarse de tenerlo instalado o actualizado en su sistema, para ello le adjunto el link de la pagina oficial si en caso no lo tuviera: 
   `https://www.python.org/downloads/`

   Tambien mencionar que la libreria a utilizar en CSV, no es necesaria su instalación ya que viene incluida en Python.


2. **Ejecucion del Programa**  
   - Cambie y Guarde el archivo de las transacciones en formato CSV en la misma ruta dónde se encuentra el archivo `reto-tecnico-cobol.py`.
   - En el archivo  `reto-tecnico-cobol.py` cambie la variable de `data.csv` por el nombre del archivo que guardo anteriormente, guarde los cambios y ejecute el programa.
   

3. **Enfoque y Solución**  
   El código realiza los siguientes pasos:
   

   1. Carga los datos del archivo CSV usando la `codificación utf-8-sig`, permitiendo manejar el archivo en caso de tener BOM.

   2. Se usan los acumuladores (credito, debito) para calcular el total de cada tipo de transaccion y contadores (cont_credito, cont_debito) para llevar el registro de la cantidad de operaciones, por ultimo la variable (id_max_monto) para encontrar la transaccion más alta.

   3. se corre cada fila del archivo como un diccionario, donde se convierten el monto a float y normlaiza el campo tipo, clasificamos las transacciones como crédito o débito, actuliazando los acumuladores y contadores, luego se verifica el monto actual es mayor que el maximo encontrado hasta ahora, si lo es se actualiza el valor con su id.

   4. Utilizamos un try-except para capturar errores en la conversion de monto, por ejemplo si no es un número valido.

   5. Por ultimo se imprime el reporte con el balace final (créditos - débitos), la transaccion con el monto mayor y su id y el conteo de las transacciones por su tipo.

4. **Estructura del Proyecto**  
   ```sh
   /data.csv                  
   /README.md                 
   /reto-tecnico-cobol.py     
   ```

5. **Documentacion y Calidad del código**  
   - Los comentarios realizados en el código son utiles y ayudan a entender la funcion del script.
   - Trabajan con variables que poseen nombres descriptivos, que facilitan su proposito.
   - El código realiza buenas practicas, tanto en el uso de `with open` que asegura el script cierre correctamente, normalización de datos con `strip y lower` y manejo de errores con `try-except`. 

