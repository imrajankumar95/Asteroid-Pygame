# Asteroids Pygame

A classic Asteroids arcade game implementation using Python and Pygame. Control your spaceship, destroy asteroids by shooting them, and avoid collisions to survive as long as possible.

## Overview

This project recreates the iconic Asteroids arcade game where players control a triangular spaceship in a 2D environment filled with asteroids. The game features collision detection, shooting mechanics, and increasingly challenging gameplay as you progress.

## Features

- **Player Controls**: Rotate and move your spaceship across the screen
- **Shooting Mechanics**: Fire shots at asteroids with a cooldown system
- **Asteroid Physics**: Asteroids spawn continuously and move across the screen
- **Collision Detection**: Detect collisions between player and asteroids, and between shots and asteroids
- **Game Logging**: Event and state logging for game analytics and debugging
- **Screen Wrapping**: Objects wrap around screen edges for continuous gameplay

## Requirements

- Python 3.12 or higher
- Pygame 2.6.1

## Installation

1. Clone the repository:
```bash
git clone https://github.com/imrajankumar95/Asteroid-Pygame.git
cd Asteroid-Pygame
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

Or if using uv:
```bash
uv pip install pygame==2.6.1
```

## Usage

Run the game:
```bash
python main.py
```

## Game Controls

- **Arrow Keys (← →)**: Rotate your spaceship left and right
- **Arrow Key (↑)**: Move forward in the direction your spaceship is facing
- **Space**: Fire a shot at asteroids
- **Close Window**: Exit the game

## Game Mechanics

### Player
- Triangular spaceship centered on screen
- Rotates based on player input (300°/second turn speed)
- Moves forward at a constant speed (200 pixels/second)
- Can shoot with a 0.3-second cooldown between shots

### Asteroids
- Spawn continuously at a rate of one every 0.8 seconds
- Three different sizes (ranging from 20 to 60 pixel radius)
- Move in random directions across the screen
- Wrap around screen edges

### Shots
- Travel at 500 pixels/second
- Have a 5-pixel radius
- Disappear when they hit an asteroid

### Game Over
- The game ends immediately if an asteroid collides with the player
- Score is tracked through event logging

## Project Structure

- `main.py` - Main game loop and collision detection
- `player.py` - Player spaceship class and controls
- `asteroid.py` - Asteroid class and behavior
- `asteroidfield.py` - Manages asteroid spawning
- `shot.py` - Projectile class
- `circleshape.py` - Base class for circular game objects
- `constants.py` - Game configuration values
- `logger.py` - Event and state logging
- `pyproject.toml` - Project metadata and dependencies

## Game Configuration

Game parameters can be adjusted in `constants.py`:

- `SCREEN_WIDTH` (1280) and `SCREEN_HEIGHT` (720) - Game window size
- `PLAYER_RADIUS` (20) - Player spaceship size
- `PLAYER_SPEED` (200) - Player movement speed
- `PLAYER_TURN_SPEED` (300) - Player rotation speed
- `ASTEROID_SPAWN_RATE_SECONDS` (0.8) - How often asteroids spawn
- `ASTEROID_MIN_RADIUS` (20) - Smallest asteroid size
- `PLAYER_SHOOT_COOLDOWN_SECONDS` (0.3) - Time between shots

## Logging

The game logs events and game state:

- `game_events.jsonl` - Records game events (player hit, asteroid destroyed)
- `game_state.jsonl` - Records game state snapshots

This data can be used for gameplay analysis and debugging.

## License

This project is open source and available under the MIT License.

## Author

Created by [imrajankumar95](https://github.com/imrajankumar95)
