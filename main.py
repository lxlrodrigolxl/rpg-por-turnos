import random
import pygame

class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome

    def get_vida(self):
        return self.__vida

    def get_nivel(self):
        return self.__nivel

    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}"

    def receber_ataque(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0

    def atacar(self, alvo):
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4)
        alvo.receber_ataque(dano)
        print(f"\n{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")


class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\n"

    def ataque_especial(self, alvo):
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 8)
        alvo.receber_ataque(dano)
        print(f"\n{self.get_nome()} usou a habilidade especial '{self.get_habilidade()}' em {alvo.get_nome()} e causou {dano} de dano!")

    def defender(self):
        print(f"\n{self.get_nome()} defendeu e bloqueou o ataque de dano!")


class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}\n"


class Jogo:
    """Classe orquestradora do jogo"""
    def __init__(self) -> None:
        self.heroi = Heroi(nome="Link", vida=100, nivel=5, habilidade="Jump with Sword")
        self.inimigo = Inimigo(nome="Dark Link", vida=80, nivel=5, tipo="Boss")

    def tocar_musica(self):
        try:
            pygame.mixer.init()
            pygame.mixer.music.load('musica.mp3')
            pygame.mixer.music.play(-1)
        except Exception as e:
            print(f"(Aviso de áudio: {e})")

    def iniciar_batalha(self):
        self.tocar_musica()
        print("Iniciando Batalha!")
        
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos personagens:")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("Pressione Enter para continuar...")
            escolha = input("Escolha (1 - Ataque, 2 - Defesa, 3 - Ataque especial, 4 - Sair): ")

            if escolha == '1':
                self.heroi.atacar(self.inimigo)
            elif escolha == '2':
                self.heroi.defender()
            elif escolha == '3':
                self.heroi.ataque_especial(self.inimigo)
            elif escolha == '4':
                print("\nVocê saiu do jogo!")
                break
            else:
                print("\nOpção inválida. Escolha novamente.")

            if self.inimigo.get_vida() > 0 and escolha in ['1', '2', '3']:
                self.inimigo.atacar(self.heroi)

        if self.heroi.get_vida() > 0 and escolha != '4':
            print(f"\nParabéns, você venceu a batalha!")
            print("Você salvou o reino de Hyrule!")
        elif self.inimigo.get_vida() > 0 and escolha != '4':
            print(f"\nVocê foi derrotado!")

        try:
            pygame.mixer.music.stop()
        except:
            pass
        print("\nFim do jogo!")


if __name__ == "__main__":
    jogo = Jogo()
    jogo.iniciar_batalha()
