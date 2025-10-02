# Configurando a Placa

- **IP:** `15.0.93.161`
- Comando para listar GPIOs:  
    ```bash
    gpioinfo
    ```

## Controle do LED

Para acender o LED:
```bash
gpioset gpiochip0 17=1
```

Para apagar o LED:
```bash
gpioset gpiochip0 17=0
```

> **Observação:**  
> No nosso caso, o LED era meio "bootleg" e algumas coisas vieram invertidas de fábrica.

---

*Obs.: Foram passados alguns comandos Bash que pareciam ser de algum slide. Preciso encontrar isso depois.*
