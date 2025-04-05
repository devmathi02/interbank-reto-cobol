import csv #importamos la libreria csv que esta incluida en el lenguaje (no hace falta instalarla)

archivo_csv = 'data.csv' #decidi procesar el nombre del archivo en una variable

def procesar_transacciones (archivo_csv): #definimos la funcion que se encarga de leer el archivo csv
    credito = debito = max_monto = 0 # acumuladores de los montos
    cont_credito = cont_debito = 0 # contadores de operaciones
    id_max_monto = None # almacena el id del monto más grande

    #abre el archivo csv con codificacion utf-8 para manejar BOM si existe
    with open(archivo_csv, mode='r', encoding='utf-8-sig') as archivo: 

        for transaccion in csv.DictReader(archivo): #lee el archivo como diccionario 
            try:
                #convertimos el monto a float y normalizamos el tipo, osea pasamos a minusculas y sin espacios
                monto = float(transaccion['monto'])
                tipo = transaccion['tipo'].strip().lower()
                id_trans = transaccion['id']

                #clasifica las transacciones, suma el total de cada tipo y los cuenta 
                if tipo in ('crédito', 'credito'):
                    credito += monto
                    cont_credito += 1
                elif tipo in ('débito', 'debito'):
                    debito += monto
                    cont_debito += 1
                
                #actualiza la transaccion con mayor monto
                if monto > max_monto:
                    max_monto, id_max_monto = monto, id_trans

            except ValueError: #capturamos el error si en caso el monto es un de tipo numerico
                print(f"Error en el Id {transaccion.get('id', 'N/A')}: monto invalido")

    #generamos el reporte 
    print("=" * 47)
    print("Reporte de Transacciones")
    print("=" * 47)
    print(f"- Balance Final: {credito - debito:.2f}")# creditos - debitos para hallar el balance final, el .2f es para mostrar los valores en decimales
    print(f"- Transacciones de Mayor Monto: Id: {id_max_monto} | monto: {max_monto:.2f}")# la transaccion más grande con su id y el monto
    print("Conteo de Transacciones:") #totalees de creditos y debitos
    print(f"    => Crédito: {cont_credito}")
    print(f"    => Débito: {cont_debito}\n")

procesar_transacciones(archivo_csv)#ejecutamos la funcion    