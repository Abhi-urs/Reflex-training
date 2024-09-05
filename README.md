# Reflex-training Game

Reflex-training is a reflex-testing game built using Pygame, a popular Python library for game development. The game challenges players to click on targets that appear on the screen, testing both their reflexes and aiming accuracy.

## Key Components

### 1. Pygame Initialization
- **Libraries Imported:** math, random, pygame, and time.
- **Setup:** Initializes Pygame with `pygame.init()`, sets the display size to 800x600 pixels, and names the window "AIM Building".
- **Display Creation:** Uses `pygame.display.set_mode((w, h))` to create the game window.

### 2. Target Class
- **Attributes:** Targets are represented as circles with an initial size of 0 that grows until it reaches a maximum size (30 units).
- **Methods:**
  - `update()`: Manages the target’s growth and shrinking.
  - `draw()`: Renders multiple concentric circles for a target-like appearance.
  - `collide()`: Checks if the user’s click intersects with the target.

### 3. Game Display
- **Rendering:** The `draw()` function renders targets on a dark blue background.
- **Top Bar:** The `draw_top_bar()` function displays game statistics, including elapsed time, hits, speed, and remaining lives.

### 4. Game Logic (Main Loop)
- **Core Loop:** Managed by the `main()` function, running at 60 FPS with `clock.tick(60)`.
- **Update & Input Handling:** Updates targets, processes user input, and checks for collisions each frame.
- **Scoring:** On clicking a target, the target is removed, and the player gains points. The game tracks total clicks and missed targets.
- **Lives:** Players start with 3 lives; running out results in a game over and the display of an end screen.

### 5. Timer and Custom Events
- **Target Creation:** Uses a timer (`pygame.time.set_timer(TARGET_EVENT, TARGET_INCREMENT)`) to spawn new targets at regular intervals at random positions.

### 6. End Screen
- **Game Over:** When lives are depleted, the end screen displays statistics such as total time, hits, speed (targets per second), and accuracy.

## How to Run

1. **Install Dependencies:** Ensure you have Pygame installed. You can install it via pip:
   ```bash
   pip install pygame
2. **Execute the Game:**
   ```bash
   python -u ./Reflex_training.py

## Game Preview

- ### In Game:
<div align="center">
    <img src="https://github.com/user-attachments/assets/34aa36fa-1a64-4246-9f98-8767c25204cb" width="500"/>
</div>

- ### Result:
<div align="center">
    <img src="https://github.com/user-attachments/assets/5c345acd-210a-44d7-bae3-6c9dc9a5d6a4" width="500"/>
</div>
