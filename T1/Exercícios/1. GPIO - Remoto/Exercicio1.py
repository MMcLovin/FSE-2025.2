import os
import RPi.GPIO as GPIO
import time

def setup():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)

def ligar_led(led_pin):
    try:
        setup()
        GPIO.setup(led_pin, GPIO.OUT)

        print(f"Usando o GPIO {led_pin}")

        while(True):
            flag = int(input())
            if flag == 1:
                # define o sinal a ser mandado pelo pino configurado como output
                GPIO.output(led_pin, GPIO.HIGH)
                print("LED aceso")
            elif flag == 0:
                print("LED apagado")
                # define o sinal a ser mandado pelo pino configurado como output
                GPIO.output(led_pin, GPIO.LOW)

    except KeyboardInterrupt:
        print("\nPrograma interrompido")
        print("Fechando o bar...")
        GPIO.output(led_pin, GPIO.LOW)
        GPIO.cleanup()
        return

    except RuntimeError as e:
        print(f"Algo deu errado ao ligar um led: {e}")
        print("Pressione qualquer tecla para continuar")
        input()

def temporizar_led(led_pin):
    try:
        setup()
        # pino para mandar um sinal
        GPIO.setup(led_pin, GPIO.OUT)

        print(f"Usando o GPIO {led_pin}")

        # de quais formas eu posso alternar um valor em python?
        # posso ter uma variavel, ir somando 1 e quando for par, eu faço uma coisa, quando for impar, eu faço outra coisa
        flag = 0

        while(True):
            if flag == 1000:
                flag = 0
            if flag % 2 == 0:
                # define o sinal a ser mandado pelo pino configurado como output
                GPIO.output(led_pin, GPIO.HIGH)
                print("LED aceso")
            else:
                print("LED apagado")
                # define o sinal a ser mandado pelo pino configurado como output
                GPIO.output(led_pin, GPIO.LOW)
            time.sleep(2)
            flag += 1

    except KeyboardInterrupt:
        print("\nPrograma interrompido")
        print("Fechando o bar...")
        GPIO.output(led_pin, GPIO.LOW)
        GPIO.cleanup()
        return

    except RuntimeError as e:
        print(f"Algo deu errado ao temporizar o led: {e}")
        print("Pressione qualquer tecla para continuar")
        input()

def ligar_todos_leds(gpios):
    try:
        setup()
        for led in gpios:
            GPIO.setup(led, GPIO.OUT)
    
        while True:
            for led in gpios:
                print(f"Usando o GPIO {led}")
                GPIO.output(led, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(led, GPIO.LOW)

    except KeyboardInterrupt:
            print("\nPrograma interrompido")
            print("Fechando o bar...")
            for led in gpios:
                GPIO.output(led, GPIO.LOW)
            GPIO.cleanup()
            return

    except RuntimeError as e:
        print(f"Algo deu errado ao temporizar o led: {e}")
        print("Pressione qualquer tecla para continuar")
        input()

    finally:
        print("\nComeçando de novo\n")

def main():
    leds_gpio = (7, 8, 12, 19, 25, 26)

    while True:
        try:
            
            # vamos usar a numeração GPIOX 
            GPIO.setmode(GPIO.BCM)

            print("\n 1 - Ligar e desligar um LED")
            print(" 2 - Ligar e desligar um LED usando temporizador")
            print(" 3 - Ligar e desligar os LEDs em sequência")
            print("-1 - Sair")
            
            option = int(input("O que deseja fazer? "))
        
            if option == 1:
                ligar_led(leds_gpio[0])
            elif option == 2:
                temporizar_led(leds_gpio[0])
            elif option == 3:
                ligar_todos_leds(leds_gpio)
            elif option == -1:
                break

        except RuntimeError as e:
                print(f"Erro: {e}")
                print("Pressione qualquer tecla para continuar")
                input()
                os.system("clear")
        
if __name__ == '__main__':
    main()