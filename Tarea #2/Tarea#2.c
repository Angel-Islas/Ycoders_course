#include <stdio.h>
#include <math.h>

int main() {
    int angry_days = 0;
    int days_per_month[] = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int number_of_months = sizeof(days_per_month) / sizeof(days_per_month[0]);
    int month = 0;
    
    // Calcular días enfadada al año
    for (int x = 0; x < 12; x++) {
        if (x % 2 == 1) {
            angry_days += (int)ceil(days_per_month[x] * 0.7);
        } else {
            angry_days += (int)ceil(days_per_month[x] * 0.35);
        }
    }

    printf("La cantidad de dias que pasa enfadada en el ano es de: %d\n", angry_days);

    int date_to_avoid = angry_days / 2;
    angry_days = 0;

    // Encontrar el mes a partir del cual se debe evitar a la jefa
    for (int x = 0; x < 12; x++) {
        if (x % 2 == 1) {
            angry_days += (int)ceil(days_per_month[x] * 0.7);
        } else {
            angry_days += (int)ceil(days_per_month[x] * 0.35);
        }

        if (angry_days > date_to_avoid) {
            month = x + 1;  
            break;
        }
    }

    printf("Debe evitar a su jefa en el mes %d\n", month);
    
    return 0;
}
