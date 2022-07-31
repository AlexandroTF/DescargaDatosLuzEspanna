import requests
import pandas as pd
from datetime import timedelta, datetime

print('The oldest possible date is 1st April of 2014')
annoInicio = int(input('start date(year): '))
mesInicio = int(input('start date(month): '))
diaInicio = int(input('start date(day): '))
inicioDescargas = datetime(annoInicio,mesInicio,diaInicio)
finhoy = input('End the range of dates today? (Yes/Y/Si/S)')
if (finhoy == 'Yes' or finhoy == 'YES' or finhoy == 'yes' or finhoy == 'Y' or finhoy == 'y' or finhoy == 'Si' or finhoy == 'SI' or finhoy == 'si' or finhoy == 'S' or finhoy == 's' or finhoy == ''):
    finalDescargas = datetime.today()
else:
    annoFin = int(input('start date(year): '))
    mesFin = int(input('start date(month): '))
    diaFin = int(input('start date(day): '))
    finalDescargas = datetime(annoFin,mesFin,diaFin)



nDiasDescargas = (finalDescargas - inicioDescargas).days

columnas = ['Dia', 'Hora', 'Peaje', 'Periodo', 'Termino energia PVPC FEU = TEU + TCU €/MWh consumo', 'Peajes y cargos TEU €/MWh consumo', 'Precio producción TCU = CP x(1+PERD/100) €/MWh consumo', '% coeficiente pérdidas PVPC PERD', '% coeficiente pérdidas estándar', 'Coste producción CP €/MWh bc', 'Total OC €/MWh bc', 'Financiación OS €/MWh bc', 'Financiación OM €/MWh bc', 'Cargo capacidad €/MWh bc', 'Servicio interrumpibilidad €/MWh bc', 'Excedente o deficit subastas renovables €/MWh bc', 'CCVh coste comercialización  RCVtovph €/MWh bc', 'CCVh coste comercialización RFE €/MWh bc', 'CCVh coste comercialización  RMRv €/MWh bc', 'CCVh coste comercialización  Runitaria €/MWh bc', 'Total SAH €/MWh bc', 'Otros sistema €/MWh bc', 'Coste desvíos €/MWh bc', 'Coste banda €/MWh bc', 'Coste reserva €/MWh bc', 'Coste restricciones tecnicas diario €/MWh bc', 'Total PMH €/MWh bc', 'Componente intradiario 1 €/MWh bc', 'Mercado diario €/MWh bc', 'Coeficiente perfilado']
columnasAntiguas = ['Dia', 'Hora', 'Peaje', 'Periodo', 'Termino energia PVPC FEU = TEU + TCU €/MWh consumo', 'Peajes y cargos TEU €/MWh consumo', 'Precio producción TCU = CP x(1+PERD/100) €/MWh consumo', '% coeficiente pérdidas PVPC PERD', '% coeficiente pérdidas estándar', 'Coste producción CP €/MWh bc', 'Total OC €/MWh bc', 'Financiación OS €/MWh bc', 'Financiación OM €/MWh bc', 'Cargo capacidad €/MWh bc', 'Servicio interrumpibilidad €/MWh bc', 'CCVh coste comercialización  RCVtovph €/MWh bc', 'CCVh coste comercialización RFE €/MWh bc', 'CCVh coste comercialización  RMRv €/MWh bc', 'CCVh coste comercialización  Runitaria €/MWh bc', 'Total SAH €/MWh bc', 'Otros sistema €/MWh bc', 'Coste desvíos €/MWh bc', 'Coste banda €/MWh bc', 'Coste reserva €/MWh bc', 'Coste restricciones tecnicas diario €/MWh bc', 'Total PMH €/MWh bc', 'Componente intradiario 1 €/MWh bc', 'Mercado diario €/MWh bc', 'Coeficiente perfilado']
columnasMasAntiguas = ['Dia', 'Hora', 'Peaje', 'Periodo', 'Termino energia PVPC FEU = TEU + TCU €/MWh consumo', 'Peajes y cargos TEU €/MWh consumo', 'Precio producción TCU = CP x(1+PERD/100) €/MWh consumo', '% coeficiente pérdidas PVPC PERD', '% coeficiente pérdidas estándar', 'Coste producción CP €/MWh bc', 'Total OC €/MWh bc', 'Financiación OS €/MWh bc', 'Financiación OM €/MWh bc', 'Cargo capacidad €/MWh bc', 'Servicio interrumpibilidad €/MWh bc', 'Total SAH €/MWh bc', 'Otros sistema €/MWh bc', 'Coste desvíos €/MWh bc', 'Coste banda €/MWh bc', 'Coste reserva €/MWh bc', 'Coste restricciones tecnicas diario €/MWh bc', 'Total PMH €/MWh bc', 'Componente intradiario 1 €/MWh bc', 'Mercado diario €/MWh bc', 'Coeficiente perfilado']
columnasNuevas = ['Dia', 'Hora', 'Peaje', 'Periodo', 'Termino energia PVPC FEU = TEU + TCU €/MWh consumo', 'Peajes y cargos TEU €/MWh consumo', 'Precio producción TCU = CP x(1+PERD/100) €/MWh consumo', '% coeficiente pérdidas PVPC PERD', '% coeficiente pérdidas estándar', 'Coste producción CP €/MWh bc', 'Total OC €/MWh bc', 'Financiación OS €/MWh bc', 'Financiación OM €/MWh bc', 'Cargo capacidad €/MWh bc', 'Servicio interrumpibilidad €/MWh bc', 'Excedente o deficit subastas renovables €/MWh bc', 'CCVh coste comercialización  RCVtovph €/MWh bc', 'CCVh coste comercialización RFE €/MWh bc', 'CCVh coste comercialización  RMRv €/MWh bc', 'CCVh coste comercialización  Runitaria €/MWh bc', 'Total SAH €/MWh bc', 'Otros sistema €/MWh bc', 'Coste desvíos €/MWh bc', 'Coste banda €/MWh bc', 'Coste reserva €/MWh bc', 'Coste restricciones tecnicas diario €/MWh bc', 'Total PMH €/MWh bc', 'Componente intradiario 1 €/MWh bc', 'Mercado diario €/MWh bc', 'Coeficiente perfilado', 'Coste de produccion']
#Un bucle para pasar por todos los días
for dia_unico in (inicioDescargas + timedelta(n) for n in range(nDiasDescargas)):
    yyyy = dia_unico.year
    mm = dia_unico.month
    dd = dia_unico.day
    fecha = str(yyyy) + '-' + str(mm) + '-' + str(dd)
    try:
        link = "https://api.esios.ree.es/archives/71/download?date=" + fecha
        r = requests.get(link, allow_redirects=True)
        df = pd.read_excel(r.content)

        df = df.drop(df.columns[-1:], axis=1)
        try:
            df.columns = columnasNuevas
            df = df[4:-1]
        except:
            try:
                df.columns = columnas
                ##df = df[4:-1]
            except:
                try:
                    df.columns = columnasAntiguas
                except:
                    try:
                        df.columns = columnasMasAntiguas
                    except:
                        print('ERROR FATAL')
                    df['CCVh coste comercialización  RCVtovph €/MWh bc'] = 'null'
                    df['CCVh coste comercialización RFE €/MWh bc'] = 'null'
                    df['CCVh coste comercialización  RMRv €/MWh bc'] = 'null'
                    df['CCVh coste comercialización  Runitaria €/MWh bc'] = 'null'
                df['Excedente o deficit subastas renovables €/MWh bc'] = 'null'
            df['Coste de produccion'] = 'null'
            df = df[columnasNuevas]
            df = df[4:-3]
            
        nombreArchivo = 'Datos/' +  fecha + 'preciosLuz' + '.csv'
        df.to_csv(nombreArchivo, encoding='utf-8', sep=';', index='')
    except Exception as e:
        print(e)
        print('')
        pass
        