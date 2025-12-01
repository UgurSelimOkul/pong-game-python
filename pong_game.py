import pygame
import random

# --- BAŞLANGIÇ AYARLARI ---
pygame.init()

# Ekran Boyutları
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Single Player Pong - Menu Control")

# Renkler
WHITE = (255, 255, 255)
RED = (255, 50, 50)
BLUE = (50, 50, 255)
BLACK = (20, 20, 20)
GREEN = (50, 255, 50)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 0)

# Oyun Saati
clock = pygame.time.Clock()
FPS = 60

# Fontlar
font_large = pygame.font.Font(None, 60)
font_small = pygame.font.Font(None, 40)

# --- OYUN DEĞİŞKENLERİ ---
# Raket
rect_width = 100
rect_height = 15
rect_speed = 7
p1_x = (WIDTH - rect_width) // 2
p1_y = HEIGHT - 40

# Top
ball_radius = 10
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = 0
ball_dy = 0

# Oyun Durumu
difficulty_multiplier = 0 
running = True
game_active = False
score = 0
high_score = 0

def reset_game_state():
    global ball_x, ball_y, ball_dx, ball_dy, p1_x, score
    p1_x = (WIDTH - rect_width) // 2
    score = 0
    
    # Topu merkeze al
    ball_x = WIDTH // 2
    ball_y = HEIGHT // 2
    
    # Top Hızı ve Yönü
    # X ekseni: Rastgele sağ veya sol
    ball_dx = random.choice([-1, 1]) * difficulty_multiplier
    
    # Y ekseni: DAİMA YUKARI (Negatif Y yukarı demektir)
    ball_dy = -1 * difficulty_multiplier

def draw_text_centered(text, font, color, y_offset=0):
    surface = font.render(text, True, color)
    rect = surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
    screen.blit(surface, rect)

def main_menu():
    global difficulty_multiplier, running, game_active
    menu_running = True
    
    # Menü Seçenekleri
    options = ["Kolay", "Orta", "Zor"]
    # Zorluk çarpanları (Kolay:4, Orta:6, Zor:9)
    multipliers = [4, 6, 9] 
    
    selected_index = 1 # Varsayılan olarak "Orta" seçili başlasın
    
    while menu_running and running:
        screen.fill(BLACK)
        
        draw_text_centered("PONG GAME", font_large, BLUE, -150)
        draw_text_centered("Zorluk Sec:", font_small, GRAY, -80)
        
        # Seçenekleri çizdir
        for i, option in enumerate(options):
            # Eğer seçili indekste ise Rengi SARI yap, değilse BEYAZ
            color = YELLOW if i == selected_index else WHITE
            # Seçili ise yanına ok koy
            prefix = "> " if i == selected_index else "  "
            
            text_surface = font_small.render(prefix + option, True, color)
            rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + (i * 50)))
            screen.blit(text_surface, rect)

        draw_text_centered("Secim: YUKARI/ASAGI - Onay: ENTER", pygame.font.Font(None, 24), GRAY, 200)

        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                menu_running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    # Modulo operatörü (%) ile liste içinde döngü sağlarız
                    selected_index = (selected_index - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected_index = (selected_index + 1) % len(options)
                elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE: # Enter veya Space
                    difficulty_multiplier = multipliers[selected_index]
                    reset_game_state()
                    game_active = True
                    menu_running = False

# --- OYUN DÖNGÜSÜ ---
main_menu()

while running:
    # 1. Event (Olay) Kontrolü
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Oyun bittiyse (Game Over) tuş kontrolleri
        if not game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: # Restart
                    reset_game_state()
                    game_active = True
                elif event.key == pygame.K_m: # Menüye Dön
                    main_menu()
                elif event.key == pygame.K_q: # Çıkış
                    running = False

    if game_active:
        # 2. Klavye Hareket
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and p1_x > 0:
            p1_x -= rect_speed
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and p1_x < WIDTH - rect_width:
            p1_x += rect_speed

        # 3. Top Hareketi
        ball_x += ball_dx
        ball_y += ball_dy

        # 4. Duvar Çarpışmaları
        # Sağ ve Sol duvarlar
        if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
            ball_dx *= -1 
        
        # Üst Duvar (Sektirme)
        if ball_y - ball_radius <= 0:
            ball_dy *= -1 

        # Alt Duvar (Oyun Biter)
        if ball_y > HEIGHT:
            game_active = False
            if score > high_score:
                high_score = score
        
        # 5. Raket Çarpışması
        # Top raketin içine mi girdi?
        if (p1_y < ball_y + ball_radius < p1_y + rect_height) and (p1_x < ball_x < p1_x + rect_width):
            # Topu yukarı sekti (Y hızını negatife çevir)
            ball_dy = -abs(ball_dy) 
            
            # Topun raketin içine sıkışmasını önlemek için biraz yukarı at
            ball_y = p1_y - ball_radius - 2
            
            # Hızı biraz artır (Zorlaştırma) - Opsiyonel
            # ball_dx *= 1.05
            # ball_dy *= 1.05
            
            score += 10 # Puan ver

    # --- ÇİZİM ---
    screen.fill(BLACK)
    
    if game_active:
        # Raket ve Top
        pygame.draw.rect(screen, BLUE, (p1_x, p1_y, rect_width, rect_height))
        pygame.draw.circle(screen, WHITE, (int(ball_x), int(ball_y)), ball_radius)
        
        # Skor Tablosu
        score_text = font_small.render(f"Skor: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        
        hiscore_text = font_small.render(f"En Yuksek: {high_score}", True, GRAY)
        hiscore_rect = hiscore_text.get_rect(topright=(WIDTH - 10, 10))
        screen.blit(hiscore_text, hiscore_rect)
        
    else:
        # GAME OVER EKRANI
        draw_text_centered("KAYBETTIN!", font_large, RED, -50)
        draw_text_centered(f"Skorun: {score}", font_small, WHITE, 10)
        draw_text_centered("Tekrar Oyna: 'R'", font_small, GREEN, 60)
        draw_text_centered("Menu: 'M'", font_small, YELLOW, 100)
        draw_text_centered("Cikis: 'Q'", font_small, GRAY, 140)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()