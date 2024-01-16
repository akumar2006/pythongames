import pygame
import sys
import itertools
import random
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
DOT_RADIUS = 10
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

def distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)


def total_distance(path):
    total = 0
    for i in range(len(path) - 1):
        total += distance(path[i], path[i + 1])
    return total


def draw_dots_and_lines(screen, dots, path, draw_text=True):
    screen.fill(BLACK)

    for dot in dots:
        pygame.draw.circle(screen, WHITE, dot, DOT_RADIUS)

    for i in range(len(path) - 1):
        pygame.draw.line(screen, WHITE, path[i], path[i + 1])

    if draw_text:
        font = pygame.font.Font(None, 36)
        text = font.render(f"Total Distance: {total_distance(path):.2f}", True, WHITE)
        screen.blit(text, (10, 10))

    pygame.display.flip()


dots = [(random.randint(DOT_RADIUS, WIDTH - DOT_RADIUS), random.randint(DOT_RADIUS, HEIGHT - DOT_RADIUS)) for _ in range(5)]


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Traveling Salesman Game")

    clock = pygame.time.Clock()

    path = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                path.append(event.pos)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                draw_dots_and_lines(screen, dots, path, draw_text=False)
                print(f"Your path: {path}")
                print(f"Your total distance: {total_distance(path):.2f}")

                optimal_path = min(itertools.permutations(dots), key=total_distance)

                # Display the optimal path and its total distance
                draw_dots_and_lines(screen, dots, optimal_path, draw_text=False)
                print(f"Optimal path: {optimal_path}")
                print(f"Optimal total distance: {total_distance(optimal_path):.2f}")

        # Draw dots and lines
        draw_dots_and_lines(screen, dots, path)

        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()