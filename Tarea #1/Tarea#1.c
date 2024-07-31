#include <stdio.h>

int main() {
    int max_minutes_per_month = 450;
    int minutes_per_day = 15;
    int days_per_month = max_minutes_per_month / minutes_per_day;
    int months_with_enough_days = 0;
    int month;

    // Array de los días en cada mes (suponiendo que no es año bisiesto)
    int days_in_month[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    // Contar cuántos meses tienen menos de `days_per_month + 1` días
    for (month = 0; month < 12; month++) {
        if (days_in_month[month] <= days_per_month) {
            months_with_enough_days++;
        }
    }

    printf("Facundo puede tomar cafe %d meses al ano sin que le descuenten dinero del sueldo.\n", months_with_enough_days);

    return 0;
}
