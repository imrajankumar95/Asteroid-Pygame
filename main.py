import pygame
from constants import *
from logger import log_state
from player import Player

def main():
    
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS, 0)
        player.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        #print(dt)


if __name__ == "__main__":
    main()
