// Basic obstacle-avoiding robot
// Motor driver: L298N
// Sensor: HC-SR04 ultrasonic

// --- Pin definitions ---
#define MOTOR_A_IN1  3
#define MOTOR_A_IN2  4
#define MOTOR_A_SPD  9   // ENA (PWM)

#define MOTOR_B_IN3  5
#define MOTOR_B_IN4  6
#define MOTOR_B_SPD  10  // ENB (PWM)

#define TRIG_PIN     7
#define ECHO_PIN     8

#define OBSTACLE_CM  20   // stop and turn if obstacle within this distance
#define SPEED        180  // 0-255

void setup() {
  pinMode(MOTOR_A_IN1, OUTPUT);
  pinMode(MOTOR_A_IN2, OUTPUT);
  pinMode(MOTOR_A_SPD, OUTPUT);
  pinMode(MOTOR_B_IN3, OUTPUT);
  pinMode(MOTOR_B_IN4, OUTPUT);
  pinMode(MOTOR_B_SPD, OUTPUT);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  Serial.begin(9600);
  Serial.println("Robot ready.");
}

void loop() {
  long dist = getDistance();
  Serial.print("Distance: ");
  Serial.print(dist);
  Serial.println(" cm");

  if (dist > 0 && dist < OBSTACLE_CM) {
    stopMotors();
    delay(300);
    turnRight();
    delay(600);
  } else {
    driveForward();
  }
  delay(100);
}

// --- Motor control ---

void driveForward() {
  analogWrite(MOTOR_A_SPD, SPEED);
  analogWrite(MOTOR_B_SPD, SPEED);
  digitalWrite(MOTOR_A_IN1, HIGH);
  digitalWrite(MOTOR_A_IN2, LOW);
  digitalWrite(MOTOR_B_IN3, HIGH);
  digitalWrite(MOTOR_B_IN4, LOW);
}

void turnRight() {
  analogWrite(MOTOR_A_SPD, SPEED);
  analogWrite(MOTOR_B_SPD, SPEED);
  digitalWrite(MOTOR_A_IN1, HIGH);
  digitalWrite(MOTOR_A_IN2, LOW);
  digitalWrite(MOTOR_B_IN3, LOW);
  digitalWrite(MOTOR_B_IN4, HIGH);
}

void stopMotors() {
  analogWrite(MOTOR_A_SPD, 0);
  analogWrite(MOTOR_B_SPD, 0);
}

// --- Ultrasonic sensor ---

long getDistance() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  long duration = pulseIn(ECHO_PIN, HIGH, 30000);
  if (duration == 0) return -1;
  return duration * 0.034 / 2;
}
