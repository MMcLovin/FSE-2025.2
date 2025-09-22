import os
import RPi.GPIO as GPIO
import time

def polling(btns_gpio):

    try:
        btn = btns_gpio[1]
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(btn, GPIO.IN)
        
        print(f"Polling no botão de GPIO {btn}")

        estado = GPIO.input(btn)

        print(f"estado inicial: {estado}")

        while True:
            # estado inicial -> estado_novo
            if estado != GPIO.input(btn):
                print(f"{estado} -----> {GPIO.input(btn)}")
                estado = GPIO.input(btn)

            time.sleep(0.01)

    except KeyboardInterrupt:

        print(f"\nPrograma interrompido")
        print("Pressione qualquer tecla para continuar...")
        input()
        print("Fechando o bar...")
        GPIO.cleanup()

    finally:

        print("Fechando o bar...")
        GPIO.cleanup()

def main():
    leds_gpio = (7, 8, 12, 19, 25, 26)
    pwm_gpio = (23, 24)
    btns_gpio = (22, 27)

    while True:
        try:
            print("\n 1 - Polling de um botão")
            print(" 2 - Debounce de um botão")
            print("-1 - Sair")
            
            option = int(input("O que deseja fazer? "))
        
            if option == 1:
                polling(btns_gpio)
            elif option == 2:
                pass
                #debouncing(btns_gpio)
            elif option == -1:
                break

        except RuntimeError as e:
                print(f"Erro: {e}")
                print("Pressione qualquer tecla para continuar")
                input()
                os.system("clear")
        
if __name__ == '__main__':
    main()