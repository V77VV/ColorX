"""
Control your Arduino robot from Python over serial.
Upload basic_bot.ino first, then run:
  python controller.py --port /dev/ttyUSB0   (Linux/Mac)
  python controller.py --port COM3            (Windows)

Commands: w=forward  s=backward  a=left  d=right  x=stop  q=quit
"""

import argparse
import serial
import time


COMMANDS = {
    "w": b"F",   # Forward
    "s": b"B",   # Backward
    "a": b"L",   # Left
    "d": b"R",   # Right
    "x": b"S",   # Stop
}


def main(port: str, baud: int = 9600):
    print(f"Connecting to {port}...")
    try:
        ser = serial.Serial(port, baud, timeout=1)
    except serial.SerialException as e:
        print(f"Could not open port: {e}")
        print("Run find_port.py to see available ports.")
        return

    time.sleep(2)  # wait for Arduino reset
    print("Connected. Controls: W/A/S/D = move, X = stop, Q = quit\n")

    try:
        while True:
            key = input("Command: ").strip().lower()
            if key == "q":
                break
            if key in COMMANDS:
                ser.write(COMMANDS[key])
                print(f"  → Sent: {COMMANDS[key].decode()}")
            else:
                print("  Unknown command. Use W A S D X or Q.")
    finally:
        ser.write(b"S")  # stop motors on exit
        ser.close()
        print("Disconnected.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", required=True, help="Serial port (e.g. /dev/ttyUSB0 or COM3)")
    parser.add_argument("--baud", type=int, default=9600)
    args = parser.parse_args()
    main(args.port, args.baud)
