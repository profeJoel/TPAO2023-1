import pygame

pygame.init()

ventana = pygame.display.set_mode((500,500))
pygame.display.set_caption("El juego de ejemplo en PyGame")

# Ciclo de eventos
infinito = True
while infinito:
    pygame.time.delay(100)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: # Es el botón de cierre del programa (botón rojo)
            # Evento es capturado
            infinito = False # Acción sobre el evento
            # El evento es manejado

pygame.quit()