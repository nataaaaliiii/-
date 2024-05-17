import pygame
import sys

# Ініціалізація Pygame
pygame.init()

# Кольори
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SALAD = (100, 200, 100)  # Салатовий колір

# Розміри вікна
WIDTH = 700
HEIGHT = 400

# Розміри блоку лабіринту
BLOCK_SIZE = 20

# Ініціалізація екрану
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Лабіринт")

# Завантаження фонового зображення
background_image = pygame.image.load("background.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Розмір лабіринту
level = [
    "WWWWWWWWWWWWWWWWWWWW",
    "W     W       W    W",
    "W WWW W WWWWW W WW W",
    "W W   W     W W W  W",
    "W W WWW WWW W W W WW",
    "W W     W W W W W  W",
    "W WWWWW W W W W W WW",
    "W     W W W W W W  W",
    "W WWWWW W W W W WWWW",
    "W     W   W W W    W",
    "W WWW WWWWW W WWWW W",
    "W W       W W    W W",
    "W W WWWWW WWWWW WW W",
    "W W     W       W  W",
    "W WWWWWWWWWWWWWWWWWW",
    "W                  F",
    "WWWWWWWWWWWWWWWWWWWW",
]

# Клас гравця
class Player:
    def __init__(self):
        self.x = 1 * BLOCK_SIZE
        self.y = 1 * BLOCK_SIZE
        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE
        self.vel = BLOCK_SIZE

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))

    def move(self, dx, dy):
        if level[int((self.y + dy) // BLOCK_SIZE)][int((self.x + dx) // BLOCK_SIZE)] != "W":
            self.x += dx
            self.y += dy

# Функція для відображення лобі
def show_lobby():
    screen.fill(WHITE)  # Білий фон
    font = pygame.font.SysFont(None, 50)
    start_text = font.render("Натисніть 'A' для початку гри", True, SALAD)  # Салатовий колір
    exit_text = font.render("Натисніть 'Q' для виходу", True, SALAD)  # Салатовий колір
    screen.blit(start_text, (WIDTH // 4, HEIGHT // 3))
    screen.blit(exit_text, (WIDTH // 4, HEIGHT // 2))
    pygame.display.update()

# Клас гри
class Game:
    def __init__(self):
        self.player = Player()
        self.show_lobby = True

    def draw_level(self):
        for y, row in enumerate(level):
            for x, col in enumerate(row):
                if col == "W":
                    pygame.draw.rect(screen, GREEN, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                elif col == "F":
                    pygame.draw.rect(screen, BLUE, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def run(self):
        pygame.mixer.music.load("music.mp3")  # Завантаження музики
        pygame.mixer.music.play(-1)  # Відтворення музики в безкінечному циклі
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a and self.show_lobby:
                        self.show_lobby = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_UP:
                        self.player.move(0, -self.player.vel)
                    elif event.key == pygame.K_DOWN:
                        self.player.move(0, self.player.vel)
                    elif event.key == pygame.K_LEFT:
                        self.player.move(-self.player.vel, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.player.move(self.player.vel, 0)

            # Оновлення екрану фону
            screen.blit(background_image, (0, 0))

            if not self.show_lobby:
                self.draw_level()
                self.player.draw()
                # Перевірка зіткнення гравця з синім блоком
                if level[int((self.player.y + self.player.height) // BLOCK_SIZE)][int((self.player.x + self.player.width) // BLOCK_SIZE)] == "F":
                    font = pygame.font.SysFont(None, 50)
                    congrats_text = font.render("Молодець!!!", True, RED)
                    screen.blit(congrats_text, (WIDTH // 2 - 100, HEIGHT // 2))

            if self.show_lobby:
                show_lobby()

            pygame.display.flip()

# Запуск гри
if __name__ == "__main__":
    game = Game()
    game.run()
