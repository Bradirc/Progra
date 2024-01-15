import openai

openai.api_base = "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"
system_rol = '''Haz de cuanta que eres un analizador de sentimientos.
                 Yo te paso sentimientos y tu anlizas el sentimiento de los mensajes
                 y me das una repuesta con al menos 1 caracter y como maximo 4 caracteres 
                 SOLO RESPUESTAS NUMERICAS. donde -1 es negatividas maxima, 0 es neutral y 1 es positividad maxima.
                 Puedes ir entre estos rangos, es decir 0.3, -0.5 etc también son válidos.
                 (Puedes responder solo con ints o floats)'''

mensajes = [{"role": "sytem", "content": system_rol}]

class Sentimiento:
    def __init__ (self, nombre, color):
        self.nombre = nombre 
        self.color = color
    
    def __str__(self):
        return "\x1b[1;{}m{}\x1b[0;37m".format(self.color,self.nombre)


class AnalizadorDeSentiemientos:
    def __init__(self, rangos):
       self.rangos = rangos

    def analizar_sentimiento(self, polaridad):   
        for rango, sentimiento in self.rangos:
            if rango[0] < polaridad <= rango[1]:
                return sentimiento
        return Sentimiento("Muy negativo", "31") 

rangos = [
    ((-0,6),(-0,3), Sentimiento("Negativo", "31")),
    ((-0,3),(-0,1), Sentimiento("algo negativo", "31")),
    ((-0,1),(0,1), Sentimiento("Neutral", "33")),
    ((0,1),(0,4), Sentimiento("algo positivo", "32")),
    ((0,4),(0,9), Sentimiento("positivo", "32")),
    ((0.9,1), Sentimiento("muy positivo", "32")),
]   


        
analizador = AnalizadorDeSentiemientos(rangos)

while True:
    user_prompt = input("1x1b[1;33m" + "\nDime Algo: " + "\x1b[0;37m")
    mensajes.append({"role": "user", "content": user_prompt})

    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = mensajes,
        max_tokens = 8
    )

    respuesta = completion.choices[0].messages["content"]
    mensajes.append({"role": "assistant", "content": respuesta })

    sentimiento = analizador.analizar_sentimiento(float(respuesta))
    print(sentimiento)    
        