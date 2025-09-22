import os
import RPi.GPIO as GPIO
import time

def set_dc(pwm_gpio):
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pwm_gpio[0], GPIO.OUT)

        # frequencia = 10 hertz => a rapidez com que o ciclo PWM se repete. Então um ciclo - que demora um periodo 1/f - 0,.1s
        p = GPIO.PWM(pwm_gpio[0], 0.5)
        # dc = duty cycle => porcentagem de tempo do ciclo (ou seja, do período) em que o sinal fica em HIGH
        p.start(0)

        p.ChangeFrequency(10)

        p.changeDutyCycle(50)
        p.changeFrequency(50)
        
        input("Pressione qualquer tecla para continuar...")

    except KeyboardInterrupt:
        p.stop()
        print(f"Programa interrompido")
        print("Pressione qualquer tecla para continuar...")
        input()
        print("Fechando o bar...")
        GPIO.cleanup()

    finally:
        p.stop()
        print("Fechando o bar...")
        GPIO.cleanup()

def vary_dc(pwm_gpio):
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pwm_gpio[0], GPIO.OUT)

        # frequencia = 10 hertz => a rapidez com que o ciclo PWM se repete. Então um ciclo - que demora um periodo 1/f - 0,.1s
        p = GPIO.PWM(pwm_gpio[0], 0.5)
        # dc = duty cycle => porcentagem de tempo do ciclo (ou seja, do período) em que o sinal fica em HIGH
        p.start(0)

        p.ChangeFrequency(10)

        while True:
            # eu demoro 20 segundos para colocar o duty cycle no estado ligado 100% do tempo
            # como ajustar a frequência para ter o visual de aumento progressivo no dashboard? Aumentando a frequência? Desse jeito eu tenho mais ciclos por segundo, o que deve me dar mais vizualizaççoes 
            for dc in range(0, 101, 5):
                print(f"Subindo - duty cycle em: {dc}")
                p.ChangeDutyCycle(dc)
                time.sleep(1)

            for dc in range(100, 0, -5):
                print(f"Descendo - duty cycle em: {dc}")
                p.ChangeDutyCycle(dc)
                time.sleep(1)

    except KeyboardInterrupt:
        print(f"Programa interrompido")
        print("Pressione qualquer tecla para continuar...")
        input()
        print("Fechando o bar...")
        GPIO.cleanup()

def main():
    leds_gpio = (7, 8, 12, 19, 25, 26)
    pwm_gpio = (23, 24)

    while True:
        try:
            print("\n 1 - Definir um duty cycle fixo")
            print(" 2 - Variar um duty cycle")
            print("-1 - Sair")
            
            option = int(input("O que deseja fazer? "))
        
            if option == 1:
                set_dc(p)
            elif option == 2:
                vary_dc(p)
            elif option == -1:
                break

        except RuntimeError as e:
                print(f"Erro: {e}")
                print("Pressione qualquer tecla para continuar")
                input()
                os.system("clear")
        
if __name__ == '__main__':
    main()