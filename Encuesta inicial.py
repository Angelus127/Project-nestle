def realizar_encuesta():
    print("Bienvenid@ a la encuesta de producto nestle. Por favor, responde las preguntas a continuación.\n")
    
    # Lista de preguntas de calificación
    preguntas_calificacion = [
        "¿Qué tan satisfech@ estás con el sabor del producto de kit kat?",
        "¿Qué tan satisfech@ estás con la calidad del producto?",
        "¿Qué tan satisfech@ estás con la presentacion del producto?",
        "¿Qué tan satisfech@ estás con la innovacion del producto?",
        "¿Qué tan probable es que recomiendes nuestro producto a un amig@?",
        "¿Qué tan satisfech@ estás con los precios de nuestros productos kitkat?",
        "¿Qué tan satisfech@ estás con nuestra política de devoluciones?",
        "¿Qué tan satisfech@ estás con las promociones y descuentos ofrecidos?",
        "¿Qué tan satisfech@ estás con nuestra variedad de productos?",
        "¿Qué tan satisfech@ estás con la claridad de la información sobre el producto?",
    ]
    
    respuestas = {}

    # Preguntas de calificación
    for i, pregunta in enumerate(preguntas_calificacion, start=1):
        while True:
            try:
                respuesta = int(input(f"{i}. {pregunta} (1 a 5 estrellas): "))
                if respuesta < 1 or respuesta > 5:
                    raise ValueError("La calificación debe estar entre 1 y 5 estrellas")
                respuestas[f"Pregunta {i}"] = respuesta
                break
            except ValueError as e:
                print(f"Entrada inválida: {e}. Intenta de nuevo.")

    # Pregunta abierta
    respuesta_abierta = input("\n11. ¿Que crees que podemos mejorar en nuestro producto?: ")
    respuestas["Comentario adicional"] = respuesta_abierta
    
    print("\n¡Gracias por completar la encuesta! Tus respuestas han sido registradas.\n")
    return respuestas


# Ejecutar la encuesta
respuestas_encuesta = realizar_encuesta()
print("Respuestas registradas:")
for pregunta, respuesta in respuestas_encuesta.items():
    print(f"{pregunta}: {respuesta}")
