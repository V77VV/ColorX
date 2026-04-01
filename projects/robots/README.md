# Robots

Robotics projects — from simple Arduino bots to Python-controlled autonomous systems.

## Projects

| Folder | Description |
|--------|-------------|
| `arduino/` | Low-level motor control, sensors, embedded C++ |
| `python-controller/` | High-level Python control via serial or WiFi |

## Hardware This Works With

- Arduino Uno / Nano / Mega
- Raspberry Pi (for Python controller)
- L298N or similar motor driver
- HC-SR04 ultrasonic sensor (obstacle avoidance)
- MPU6050 IMU (orientation)
- Servo motors

## Quick Start: Arduino

1. Open `arduino/basic_bot/basic_bot.ino` in the Arduino IDE
2. Connect your motor driver to the pins defined at the top of the file
3. Upload to your Arduino board
4. The robot will drive forward, detect obstacles, and turn

## Quick Start: Python Controller

```bash
cd python-controller
pip install -r requirements.txt

# Find your serial port (Arduino connected via USB)
python find_port.py

# Run the controller
python controller.py --port /dev/ttyUSB0
```

## Project Structure

```
robots/
├── arduino/
│   └── basic_bot/
│       ├── basic_bot.ino     # Main Arduino sketch
│       └── motor.h           # Motor helper functions
├── python-controller/
│   ├── controller.py         # Send commands to Arduino over serial
│   ├── find_port.py          # Detect which serial port Arduino is on
│   └── requirements.txt
└── README.md
```

## Wiring Reference

```
Arduino Pin  →  Component
D3, D4       →  Motor A (IN1, IN2 on L298N)
D5, D6       →  Motor B (IN3, IN4 on L298N)
D9, D10      →  Motor speed (ENA, ENB)
D7           →  HC-SR04 Trigger
D8           →  HC-SR04 Echo
5V / GND     →  Sensor power
```

## License

MIT
