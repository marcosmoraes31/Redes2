from gpio import *
from time import *


def main():
    pinMode(0, IN)
    pinMode(4, OUT)
    pinMode(1, IN)
    pinMode(5, OUT)

    while True:
        if digitalRead(0) == HIGH:
            digitalWrite(4, HIGH)
        else:
            digitalWrite(4, LOW)

        if digitalRead(1) == HIGH:
            customWrite(5, '2')

        else:
            customWrite(5, '0')

    delay(100)


if __name__ == "__main__":
    main()
