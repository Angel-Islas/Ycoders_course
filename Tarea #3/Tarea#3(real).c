#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

int main() {
    time_t current_time;
    struct tm * time_info;
    int start_hour = 8; // hora de inicio de la jornada
    int end_hour = 21; // hora de finalización de la jornada
    int end_minute = 0; // minuto de finalización de la jornada

    // Generar un número aleatorio entre 10 y 60 minutos
    srand(time(NULL));
    int extra_minutes = rand() % 51 + 10;
    end_minute += extra_minutes;

    // Ajustar las horas si los minutos exceden 60
    if (end_minute >= 60) {
        end_hour += end_minute / 60;
        end_minute = end_minute % 60;
    }

    printf("La jornada laboral termina a las %02d:%02d\n", end_hour, end_minute);
    
    while (1) {
        current_time = time(NULL);
        time_info = localtime(&current_time);
        
        int current_hour = time_info->tm_hour;
        int current_minute = time_info->tm_min;

        // Verificar si es hora de terminar la jornada laboral
        if (current_hour > end_hour || (current_hour == end_hour && current_minute >= end_minute)) {
            printf("¡La jornada laboral ha terminado! Buen trabajo.\n");
            break;
        }

        // Calcular el tiempo restante
        int hours_left = end_hour - current_hour;
        int minutes_left = end_minute - current_minute;
        if (minutes_left < 0) {
            hours_left--;
            minutes_left += 60;
        }

        // Mostrar el tiempo restante
        printf("Tiempo restante para finalizar la jornada: %02d:%02d\n", hours_left, minutes_left);

        sleep(60); // esperar un minuto
    }

    return 0;
}
