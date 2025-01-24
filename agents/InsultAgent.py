import random
from framework.MinecraftAgentFramework import MinecraftAgent, executable


class InsultAgent(MinecraftAgent):
    def __init__(self, name, active, mc):
        info = ("Agente que escribe tantos insultos aleatorios en el chat como se le indique. " 
                "Argumentos: numero de insultos a escribir (int)")
        super().__init__(name, active, info, mc)

    # Sobreescribir el método main_execute:
    def main_execute(self, *args):
        # Se comprueba que se haya pasado al menos un argumento
        if len(args) < 1:
            raise ValueError("Se necesita al menos un argumento: numero de insultos a escribir (int)")

        # Se obtiene el argumento
        try:
            num_insults = int(args[0])
        except ValueError:
            raise ValueError("El argumento debe ser un numero entero")

        for _ in range(num_insults):
            self.random_insult()

    # Definir otros métodos si es necesario, para ser llamados desde main_execute i/o
    # ser ejecutados mediante comandos des del chat del juego (decorator @executable):

    @executable
    def random_insult(self):
        """
        Escribe en el chat un insulto aleatorio de la lista de insultos.

        """

        return self.send_message(random.choice(self.insults))

    # Se define una lista de insultos
    insults = [
    "Youre as sharp as a marble.",
    "Youre slower than a snail on vacation.",
    "Your jokes are older than the internet.",
    "Youre proof that dinosaurs had bad taste.",
    "Youre the kind of person who claps when the plane lands.",
    "You bring everyone so much joy... when you leave the room.",
    "Your brain is like a web browser with 50 tabs open... and none of them is responding.",
    "Youre like a cloud when you disappear, its a beautiful day.",
    "Youre the reason they put instructions on shampoo bottles.",
    "Youre so indecisive that even your shadow hesitates to follow you.",
    "Your cooking is the reason for microwave dinners.",
    "Youre like a broken pencil completely pointless.",
    "Youre slower than a turtle in reverse.",
    "Youd argue with a stop sign if it gave you the chance.",
    "Youre not stupid, you just have bad luck thinking.",
    "Your WiFi signal is stronger than your arguments.",
    "Youre like a software update nobody wants you, but were stuck with you.",
    "Youre so lazy, even your dreams take naps.",
    "Youre like a USB port always the wrong way on the first try.",
    "Youre the human version of autocorrect always wrong.",
    "Youre so extra, even a spreadsheet cant handle you.",
    "Youre like a sandwich with no filling kind of pointless.",
    "Youre like a popup ad nobody wants to see you.",
    "Youre the reason I keep my phone on silent.",
    "Youre so basic, even your passwords are password123.",
    "Your search history must be as boring as your jokes.",
    "Youre like a math problem difficult and unnecessary.",
    "Youre so random, even Google cant autocomplete you.",
    "Youre the reason the mute button was invented.",
    "Youre as useful as a chocolate teapot.",
    "Youre like a selfie stick nobody really needs you.",
    "Youre like an old app irrelevant and full of bugs.",
    "Youre like a WiFi signal in a basement completely useless.",
    "Youre the kind of person who laughs at their own jokes... alone.",
    "Youre like an expired coupon no value anymore.",
    "Youre the human version of buffering.",
    "Youre like a weather forecast always wrong but pretending to know.",
    "Youre like a printer always out of order when needed.",
    "Youd be great at hideandseek because no ones looking for you.",
    "Youre like an elevator that skips your floor.",
    "Youre like a TikTok trend fun for five seconds, then annoying.",
    "Youre like a check engine light confusing and ignored.",
    "Youre like a loading bar stuck at 99 percent so close, yet so far.",
    "Youre as predictable as a Hallmark movie.",
    "Youre so dramatic, even reality TV would reject you.",
    "Youre like decaf coffee whats the point?",
    "Youre like a typo in an important email completely unnecessary.",
    "Youre like a pop quiz nobody asked for you.",
    "Youre like a phone at 1 percent battery barely hanging on.",
    "Youre the human version of a CAPTCHA annoying and unnecessary."
    ]


