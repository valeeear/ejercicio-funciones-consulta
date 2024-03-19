import os
con_odontologia = 0
con_ginecologia = 0
con_consultorioGeneral = 0
con_maternidad = 0
con_infancia = 0

sw = True
def fnt_selector(op):
    global con_odontologia 
    global con_ginecologia
    global con_consultorioGeneral
    global con_maternidad 
    global con_infancia 
    if op == 1:
        con_odontologia += 1
    if op == 2:
         con_ginecologia += 1
    if op == 3:
        con_consultorioGeneral += 1
    if op == 4:
        con_maternidad += 1
    if op == 5:
        con_infancia += 1
    
os.system('cls')   
def fnt_reporte(): 
    print('               >>>REPORTE<<<')
    print('La cantidad de registros en odontologia fueron:      ' , con_odontologia)
    print('La cantidad de registros en ginecologia fueron:      ' , con_ginecologia)
    print('La cantidad de registros en consulta General fueron: ', con_consultorioGeneral)
    print('La cantidad de registros en maternidad fueron:       '  , con_maternidad)
    print('La cantidad de registros en infancia fueron:         '     , con_infancia)
                
       
while sw == True:
    import os
    op = int(input('¿A cuál especialidad vas a asistir?\n1. Odontologia\n2. Ginecologia\n3. Consultorio General\n4. Maternidad\n5. Infancia\n6. Reporte\n->'))
    os.system('cls')
    fnt_selector(op)
    if op <= 0 or op >= 7:
        print('Elija una opción valida')
    if op == 6:    
        fnt_reporte()
        break
    

    
    