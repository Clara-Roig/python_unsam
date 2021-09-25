
import csv


def parse_csv (nombre_archivo, select = None, types = None, has_headers = True, silence_errors = False):
    
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    
    
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        
        
######## opción sin headers:
        
        if has_headers == False:
            
            if select != None:
                raise RuntimeError ("para seleccionar se necesita un archivo con encabezados")
            
            else:
                registros = []
                                
                for f, row in enumerate(rows):
                    
                    if not row:  #saltea las filas sin datos
                        continue
                
            # convertir a los tipos indicados:
                    if types:
                        
                        try:
                            row = [func(val) for func, val in zip(types, row)]
                            
                        except ValueError as e:
                            
                            if silence_errors == False:
                                print (f'Fila {f}: No pude convertir {row}')
                                print (f'Fila {f}: Motivo: {e}')
                                
                            else:
                                pass
                
            
            # armar el diccionario:
                    registro = tuple(row)
                    registros.append(registro)
                    
                    
            
            return registros
            
        
        
        
########################      opción con headers:
    
        else:
            headers = next(rows)   #leer los encabezados
        
            if select:
                indices = [headers.index(nombre_columna) for nombre_columna in select]
            
            else:
                indices = []
        
        
            registros = []
            for f, row in enumerate(rows):
                if not row:  #saltea las filas sin datos
                    continue
            
            # filtrar la fila si se especificaron columnas:
                if indices:
                    row = [row[index] for index in indices]
                
                
            # convertir a los tipos indicados:
                if types:
                    
                    try:
                        row = [func(val) for func, val in zip(types, row)]
                        
                    except ValueError as e:
                        
                        if silence_errors == False:
                            print (f'Fila {f}: No pude convertir {row}')
                            print (f'Fila {f}: Motivo: {e}')
                            
                        else:
                            pass
                
            
            # armar el diccionario:
                registro = dict(zip(headers, row))
                registros.append(registro)
            
            
        return registros



camion = parse_csv('../Data/missing.csv', types = [str, int, float], silence_errors = True)

print(camion)
