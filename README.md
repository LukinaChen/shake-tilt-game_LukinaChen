# 🎮 Shake & Tilt Game — ESP32-C3 + ADXL345 + OLED + NeoPixel
Motion-controlled handheld game using ESP32-C3, ADXL345, OLED, and NeoPixel. Includes tilt/shake detection, rotary-encoder UI, 10 levels, and 3 difficulty modes.

## 📌 Overview

Shake & Tilt is a handheld game powered by the ESP32-C3 microcontroller.
Players complete gesture sequences (tilt left/right/forward/back + shake) within a time limit. The difficulty increases over 10 levels with faster timing and longer sequences.

This project was built for TECHIN 512 A Au 25: Introduction To Sensors And Circuits at the University of Washington GIX.


## 🧩 Features

### 1. Three Difficulty Modes
  - Easy (1 move/level, 2.0s limit)

  - Medium (1–2 moves/level, 1.2s limit)

  - Hard (1–3 moves/level, 0.7s limit)
 
### 2.  Motion Input

  - Tilt: left / right / forward / backward

  - Shake detection

### 3.  Rotary Encoder

  - Select difficulty

  - Press to start/restart

## 📁 Repository Structure
```
shake-tilt-game/
│
├── src/                       # All CircuitPython code
│   ├── code.py
│   ├── game_state.py
│   ├── motion_utils.py
│   ├── display_utils.py
│   ├── encoder_utils.py
│   ├── pixel_utils.py
│   ├── check_move.py
│   └── move_utils.py
│
├── Documentation/             # Engineering diagrams
│   ├── circuit_diagram.kicad_sch
│   └── system_block_diagram.png/pdf
│
├── README.md
└── LICENSE (optional)
```
## 🔧 Hardware Used

  - ESP32-C3 Super Mini
  
  - ADXL345 3-axis accelerometer
  
  - SSD1306 128×64 I²C OLED display
  
  - Rotary encoder with push button
  
  - NeoPixel RGB LED
  
  - Jumper wires, breadboard, USB-C cable
