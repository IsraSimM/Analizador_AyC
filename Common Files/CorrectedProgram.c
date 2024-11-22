#include <stdio.h>
#include <math.h>

int main() {
    float comision, sueldo_diario, sueldo_semanal, sueldos_totales[50];
    int no_empleado, edad, faltas, c;
    char categoria;
    float suma_total = 0;

    for (c = 1; c <= 50; c++) {
        printf("Escribe tu numero de empleado: ");
        scanf(" %d", &no_empleado);

        printf("Escribe tu edad: ");
        scanf(" %d", &edad);
        
        printf("Escribe tu categoría: ");
        getchar();
        scanf(" %c", &categoria);

        if (categoria == 'a') {
            comision = 0.2;
        } else {
            comision = 0.1;
        }

        printf("Escribe tu sueldo diario: ");
        scanf("%f", &sueldo_diario);

        printf("Escribe las faltas: ");
        scanf("%d", &faltas);

        sueldo_semanal = (sueldo_diario * 7) + (sueldo_diario*comision*7) - (faltas * 650.45);
        sueldos_totales[c-1] = sueldo_semanal;
        suma_total += sueldo_semanal;

        printf("\nNo. de empleado: %d\n", no_empleado);
        printf("Su edad es: %d\n", edad);
        printf("Su sueldo semanal es: %.2f\n", sueldo_semanal);
    }

    printf("\nDetalle de sueldos de todos los empleados:\n");
    for (c = 0; c < 50; c++) {
        printf("Empleado %d: $%.2f\n", c+1, sueldos_totales[c]);
    }

    printf("\nEl monto total de sueldos es: %.2f\n", suma_total);

    return 0;
}