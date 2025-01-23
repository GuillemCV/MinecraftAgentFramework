import random
import time
from framework.MinecraftAgentFramework import MinecraftAgent, executable
import framework.mcpi.block as block


class OracleAgent(MinecraftAgent):
    def __init__(self, name, active, mc):
        info = ("Agente que muestra preguntas de cultura general y da la respuesta a la pregunta que escoja el jugador. "
                "Argumentos: ninguno")
        super().__init__(name, active, info, mc)

    # Sobreescribir el método main_execute:
    def main_execute(self, *args):
        # Mostramos las preguntas y esperamos a que el jugador escoja una
        self.show_questions()

        # Bucle hasta que el jugador escoja una pregunta
        correct_question_number = False
        while not correct_question_number:
            # Se obtiene la respuesta del jugador
            question_number = self.receive_message()

            # Se comprueba que el número de pregunta sea correcto
            correct_question_number = self.check_question_number(question_number)
                
            # Esperamos medio segundo
            time.sleep(0.5)

    def show_questions(self):
        """
        Muestra las preguntas de cultura general al jugador.
        """
        self.send_message("Escoge una pregunta del 1 al 25 para saber la respuesta:")
        for question, answer in self.questions_and_answers:
            self.send_message(question)

    def check_question_number(self, question_number) -> bool:
        """
        Comprueba que el número de pregunta introducido sea un número entero entre 1 y 25.

        :param question_number: Número de pregunta introducido por el jugador.
        :return: True si el número es correcto, False en caso contrario.
        """

        correct = False
        # Si se ha escrito algo
        if not question_number == "":
            # Se comprueba que la respuesta sea un número entre 1 y 25
            try:
                question_number = int(question_number)
                if 1 <= question_number <= 25:
                    # Se obtiene la respuesta correcta
                    question, answer = self.questions_and_answers[question_number - 1]
                    self.send_message(f"La respuesta a la pregunta {question} es: {answer}")
                    correct = True
                else:
                    # Si el número no está entre 1 y 25
                    self.send_message("Por favor, escoge un numero entre 1 y 25")
                    correct = False
            except ValueError:
                # Si no se ha introducido un número
                self.send_message("Por favor, introduce un numero")
                correct = False

        return correct

    
    # Lista de preguntas y respuestas
    questions_and_answers = [
    ("1. Cual es el planeta mas grande del sistema solar?", "Jupiter"),
    ("2. En que continente se encuentra Egipto?", "Africa"),
    ("3. Quien Pinto la Mona Lisa?", "Leonardo da Vinci"),
    ("4. Cual es el oceano mas grande del mundo?", "Pacifico"),
    ("5. Que pais tiene forma de bota?", "Italia"),
    ("6. Quien escribio Don Quijote de la Mancha?", "Miguel de Cervantes"),
    ("7. Cual es el metal mas ligero?", "Litio"),
    ("8. Cual es el animal mas rapido del mundo?", "Guepardo"),
    ("9. Que instrumento mide los terremotos?", "Sismografo"),
    ("10. En que ano llego el hombre a la Luna?", "1969"),
    ("11. Que gas respiramos para vivir?", "Oxigeno"),
    ("12. Cual es el rio mas largo del mundo?", "Nilo"),
    ("13. Que idioma se habla en Brasil?", "Portugues"),
    ("14. Quien es el padre de la teoria de la relatividad?", "Albert Einstein"),
    ("15. Que numero romano representa el 100?", "C"),
    ("16. Cual es la capital de Japon?", "Tokio"),
    ("17. Que tipo de animal es una ballena?", "Mamifero"),
    ("18. Cual es el pais mas grande del mundo?", "Rusia"),
    ("19. En que ano comenzo la Segunda Guerra Mundial?", "1939"),
    ("20. Que elemento quimico tiene el simbolo H?", "Hidrogeno"),
    ("21. Cuantos lados tiene un hexagono?", "Seis"),
    ("22. Quien es conocido como el rey del rock and roll?", "Elvis Presley"),
    ("23. Que pais es famoso por su torre inclinada?", "Italia"),
    ("24. Que planeta se conoce como el planeta rojo?", "Marte"),
    ("25. Quien fue el primer presidente de los Estados Unidos?", "George Washington")
    ]
