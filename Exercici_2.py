def main():
    alumnos = list()
    print("**************************BIENVENIDO********************************")
    alum = int(input("Introduce el número de alumnos: "))
    while alum < 1:  # Validación del valor
        alum = int(input("¿Como? ¿Tienes alumnos negativos?\nIntroduce el número real de alumnos: "))
    for x in range(alum):
        alumnos.append(int(input("Introduce la nota del alumno: ")))
        if alumnos[x] < 0 or alumnos[x] > 10:
            del alumnos[x]
            alumnos.append(int(input("La nota ha de que ser entre 0 y 10.\nVuelve a introducirla: ")))
    aprobados = list()
    suspensos = list()
    aprob = suspe = 0
    for x in alumnos:
        if x < 5:
            suspensos.append(x)
        else:
            aprobados.append(x)
    for x in aprobados:
        aprob += x #Si quisieramos calcular la media de la CANTIDAD de aprobados, substituiriamos la "x" por "1".
    for x in suspensos:
        suspe += x #Si quisieramos calcular la media de la CANTIDAD de aprobados, substituiriamos la "x" por "1".
    print("La media de aprobados es: ", aprob / alum)
    print("La media de suspensos es: ", suspe / alum)
    print("La cantidad de aprobados es: ", len(aprobados))
    print("La cantidad de suspensos es: ", len(suspensos))


if __name__ == '__main__':
    main()
