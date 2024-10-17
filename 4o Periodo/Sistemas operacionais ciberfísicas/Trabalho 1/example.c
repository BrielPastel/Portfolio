

#Trabalho feito por: Gabriel Berto Beckauser e Arthur Capellazzi Fontana Amaral


#include <stdio.h>
#include <string.h>
#include <time.h>
#include "FreeRTOS.h"
#include "task.h"
#include "semphr.h"

#define MAX_DISPLAY_LENGTH 100
#define MAX_TEMP 40.0

char display[MAX_DISPLAY_LENGTH];
SemaphoreHandle_t displayMutex;

void vTask1(void* pvParameters);
void vTask2(void* pvParameters);
void vTask3(void* pvParameters);

// Tarefa 1
void vTask1(void* pvParameters)
{
    int taskId = *(int*)pvParameters;
    char buffer[MAX_DISPLAY_LENGTH];

    for (;;)
    {
        time_t now = time(NULL);
        struct tm* tm_struct = localtime(&now);
        strftime(buffer, sizeof(buffer), "%d/%m/%Y", tm_struct);

        if (xSemaphoreTake(displayMutex, portMAX_DELAY) == pdTRUE)
        {
            snprintf(display, MAX_DISPLAY_LENGTH, "Task %d: Data: %s", taskId, buffer);
            printf("%s\n", display);
            xSemaphoreGive(displayMutex);
        }

        vTaskDelay(pdMS_TO_TICKS(1000));
    }
}

// Tarefa 2
void vTask2(void* pvParameters)
{
    int taskId = *(int*)pvParameters;
    char buffer[MAX_DISPLAY_LENGTH];

    for (;;)
    {
        time_t now = time(NULL);
        struct tm* tm_struct = localtime(&now);
        strftime(buffer, sizeof(buffer), "%H:%M:%S", tm_struct);

        if (xSemaphoreTake(displayMutex, portMAX_DELAY) == pdTRUE)
        {
            snprintf(display, MAX_DISPLAY_LENGTH, "Task %d: Hora: %s", taskId, buffer);
            printf("%s\n", display);
            xSemaphoreGive(displayMutex);
        }

        vTaskDelay(pdMS_TO_TICKS(1000));
    }
}

// Tarefa 3
void vTask3(void* pvParameters)
{
    int taskId = *(int*)pvParameters;
    const char* cidade = "Curitiba";

    for (;;)
    {
        float temperatura = ((float)rand() / RAND_MAX) * MAX_TEMP;

        if (xSemaphoreTake(displayMutex, portMAX_DELAY) == pdTRUE)
        {
            snprintf(display, MAX_DISPLAY_LENGTH, "Task %d: Cidade: %s, Temperatura: %.1f�C", taskId, cidade, temperatura);
            printf("%s\n", display);
            xSemaphoreGive(displayMutex);
        }

        vTaskDelay(pdMS_TO_TICKS(1000));
    }
}

int main(void)
{
    displayMutex = xSemaphoreCreateMutex();

    if (displayMutex != NULL)
    {
        int task1Id = 1, task2Id = 2, task3Id = 3;

        xTaskCreate(vTask1, "Task1", configMINIMAL_STACK_SIZE, &task1Id, 1, NULL);
        xTaskCreate(vTask2, "Task2", configMINIMAL_STACK_SIZE, &task2Id, 1, NULL);
        xTaskCreate(vTask3, "Task3", configMINIMAL_STACK_SIZE, &task3Id, 1, NULL);

        vTaskStartScheduler();
    }

    for (;;);
    return 0;
}