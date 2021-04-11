
__author__ = "Luciano Ramalho"

class Bicho:
    def fazer_barulho(self, som, vezes):
        barulho = f'{som}!'.replace("ar", 'u')
        return (f"{barulho} "*vezes).strip()

    def __getattr__(self, name):
        def sonar(vezes=1):
            return self.fazer_barulho(name, vezes)
        return sonar
