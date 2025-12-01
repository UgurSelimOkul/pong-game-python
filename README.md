# pong-game-python
A fast-paced single-player arcade game developed with Python and Pygame. Unlike the classic 2-player Pong, this version challenges you to keep the ball in play against gravity, featuring a robust menu system, difficulty levels, and high-score tracking.

## 🎮 Features

* **Interactive Menu System:** Navigate through options to start the game.
* **3 Difficulty Levels:**
    * **Easy:** Slower ball speed for beginners.
    * **Medium:** Balanced speed for casual play.
    * **Hard:** Fast-paced challenge for reflexes.
* **High Score Tracking:** The game remembers your best performance during the session.
* **Game State Management:** Seamless transitions between Menu, Gameplay, and Game Over screens.
* **Dual Controls:** Supports both Arrow Keys and WASD for player movement.

## 🛠️ Technologies Used

* **Python 3.x**
* **Pygame** (Library for graphics and game physics)
* **Random Module** (For unpredictable ball movements)

## 📸 Concept Art

![Pong Game Concept Art](pong_gmae.jpeg)

## ⚙️ Installation & How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/UgurSelimOkul/pong-game-python.git](https://github.com/UgurSelimOkul/pong-game-python.git)
    cd pong-game-python
    ```

2.  **Install the required library:**
    You need `pygame` to run this game.
    ```bash
    pip install pygame
    ```

3.  **Run the game:**
    ```bash
    python main.py
    ```

## 🕹️ Controls

### Menu Controls
| Key | Action |
| :--- | :--- |
| **⬆️ Up / ⬇️ Down** | Change Difficulty |
| **Enter / Space** | Start Game |

### In-Game Controls
| Key | Action |
| :--- | :--- |
| **⬅️ Left / 🅰️ A** | Move Paddle Left |
| **➡️ Right / 🇩 D** | Move Paddle Right |

### Game Over Controls
| Key | Action |
| :--- | :--- |
| **R** | Restart Game (Quick Retry) |
| **M** | Return to Main Menu |
| **Q** | Quit Game |

## 🧩 How It Works

The game utilizes a main loop that handles event processing, logic updates, and rendering (drawing) separately. It calculates collisions between the ball and the paddle or walls. The ball's angle changes dynamically based on where it hits, and the difficulty multiplier adjusts the physics speed.

---

### 👨‍💻 Author

**Uğur Selim Okul**
* [GitHub Profile](https://github.com/UgurSelimOkul)
