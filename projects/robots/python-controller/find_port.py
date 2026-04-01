"""
List available serial ports to help you find where your Arduino is connected.
Run: python find_port.py
"""

import serial.tools.list_ports

ports = list(serial.tools.list_ports.comports())
if not ports:
    print("No serial ports found. Is the Arduino plugged in?")
else:
    print("Available serial ports:")
    for p in ports:
        print(f"  {p.device}  —  {p.description}")
