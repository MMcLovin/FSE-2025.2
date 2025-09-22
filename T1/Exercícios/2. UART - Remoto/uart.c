#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>
#include <fcntl.h>
#include <unistd.h>
#include <termios.h>

#define UART_DEV "/dev/serial0" 
#define BAUDRATE B115200

uint8_t matricula[4] = {2, 1, 6, 2}; // Ultimos 4 digitos 

#define MSG_SOLICITA_LEN 5

int solicitar_int();
int solicitar_float();
int solicitar_string();

int enviar_int(int dado);
int enviar_float(float dado);
int enviar_string(const uint8_t* dado);

// Funcao para configurar a porta serial. Essa função foi 100% copiada do gepeto
int setup_uart(int fd) {
    struct termios tty;
    // Pega os atributos atuais da porta
    if (tcgetattr(fd, &tty) != 0) {
        perror("Erro de tcgetattr");
        return -1;
    }

    // Define o baudrate
    cfsetospeed(&tty, BAUDRATE);
    cfsetispeed(&tty, BAUDRATE);

    // Seta o modo de operacao para 8N1 (8 bits de dados, sem paridade, 1 bit de parada)
    tty.c_cflag &= ~PARENB; // Sem paridade
    tty.c_cflag &= ~CSTOPB; // 1 bit de parada
    tty.c_cflag &= ~CSIZE;  // Limpa o numero de bits
    tty.c_cflag |= CS8;     // Seta 8 bits de dados
    tty.c_cflag &= ~CRTSCTS; // Desativa o controle de fluxo de hardware
    tty.c_cflag |= CREAD | CLOCAL; // Habilita a leitura e ignora as linhas de controle do modem

    // Desativa os modos de entrada e saida de software
    tty.c_iflag &= ~(IXON | IXOFF | IXANY);
    tty.c_iflag &= ~(IGNBRK|BRKINT|PARMRK|ISTRIP|INLCR|IGNCR|ICRNL);

    // Desativa o modo de saida
    tty.c_oflag &= ~OPOST;

    // Desativa o modo de entrada
    tty.c_lflag &= ~(ICANON | ECHO | ECHOE | ISIG);

    // Configura o timeout
    tty.c_cc[VMIN] = 0;
    tty.c_cc[VTIME] = 10; // Timeout de 1 segundo (em 100ms)

    // Aplica as configuracoes
    if (tcsetattr(fd, TCSANOW, &tty) != 0) {
        perror("Erro de tcsetattr");
        return -1;
    }
    return 0;
}

int solicitar_int() {
    int fd;
    int valor_inteiro;

    // Abre a porta serial
    // O_RDWR: Abre para leitura e escrita
    // O_NOCTTY: Não faz da porta o terminal de controle
    // O_NDELAY: Faz uma chamada não bloqueante => ainda não entendi o pq, mas se eu usar o O_NDELAY, a leitura não funciona.
    fd = open(UART_DEV, O_RDWR | O_NOCTTY);

    if (fd == -1) {
        perror("Erro ao abrir a porta serial");
        return -1;
    }

    if (setup_uart(fd) != 0) {
        close(fd);
        return -1;
    }

    uint8_t mensagem[MSG_SOLICITA_LEN];
    mensagem[0] = 0xA1; // comando para solicitar int
    mensagem[1] = matricula[1];
    mensagem[2] = matricula[2];
    mensagem[3] = matricula[3];
    mensagem[4] = matricula[4];

    // Envia a mensagem
    ssize_t bytes_escritos = write(fd, mensagem, MSG_SOLICITA_LEN);
    if (bytes_escritos < 0) {
        perror("Erro ao escrever na porta serial");
        close(fd);
        return -1;
    }

    printf("Mensagem de solicitação de um inteiro enviada. %ld bytes escritos.\n", bytes_escritos);
    usleep(100000); // 100ms recomendados pelo enunciado 

    tcflush(fd, TCIFLUSH); // Limpa o buffer de entrada

    // Lendo a resposta
    ssize_t bytes_lidos = read(fd, &valor_inteiro, sizeof(valor_inteiro));
    if (bytes_lidos < 0) {
        perror("Erro ao ler da porta serial");
        close(fd);
        
        sleep(6); // Espera 6 segundos para a gnt ter tempo de ver o valor
        
        return -1;
    }

    printf("Valor inteiro recebido: %d\n", valor_inteiro);

    close(fd);
    sleep(6); // Espera 6 segundos para a ter tempo de ver o valor

    return 0;
}

int main(){
    // Minha matricula: 222022162
    // Solicitação de dados pela porta serial deve seguir o padrão: comando + 4 ultimos dígitos da matrícula
    // Envio de dado pela porta serial deve seguir o padrão: Comando + dado + 4 ultimos dígitos da matrícula
    // Leitura de dados pela porta serial deve seguir o padrão: Comando + dado + 4 ultimos dígitos da matrícula

    // Menu de opções
    int opcao;
    char buffer[256];
    do {
        printf("Menu de Opções:\n");
        printf("1. Solicitar Dado\n");
        printf("2. Enviar Dado\n");
        printf("3. Sair\n");
        printf("Escolha uma opção: ");
        scanf("%d", &opcao);
        
        switch (opcao) {
            case 1:
            // tipo do dado a ser solicitado
                system("clear");
                fflush(stdout);
                printf("1. Solicitar um inteiro\n");
                printf("2. Solicitar um float\n");
                printf("3. Solicitar uma string\n");
                printf("Escolha o tipo de dado: ");
                int tipo_dado;
                scanf("%d", &tipo_dado);

                switch (tipo_dado) {
                    case 1:
                        solicitar_int();
                        break;
                    case 2:
                        //solicitar_float();
                        break;
                    case 3:
                        //solicitar_string();
                    default:
                        break;
                }
                break;
                
            case 2:
                // tipo do dado a ser enviado
                system("clear");
                fflush(stdout);
                printf("1. Enviar um inteiro\n");
                printf("2. Enviar um float\n");
                printf("3. Enviar uma string\n");
                printf("Escolha o tipo de dado: ");
                int tipo_dado_envio;
                scanf("%d", &tipo_dado_envio);

                switch (tipo_dado_envio) {
                    case 1:
                        //solicitar_int();
                        break;
                    case 2:
                        //solicitar_float();
                        break;
                    case 3:
                        //solicitar_string();
                    default:
                        break;
                }
                break;

            case 3:
                printf("Saindo...\n");
                sleep(1);
                break;
            default:
                printf("Opção inválida. Tente novamente.\n");
        }
        // limpar o terminal
        fflush(stdout);
        system("clear");

    } while (opcao != 3);

    return 0;
}
