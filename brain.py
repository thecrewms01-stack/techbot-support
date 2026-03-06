# brain.py
from openai import OpenAI
import config

# Connexion au client
client = OpenAI(
    base_url=config.GROQ_URL,
    api_key=config.GROQ_API_KEY
)

def analyser_et_repondre(message_client, historique=[]):
    """
    Cette fonction prend le message du client et l'historique (si conversation),
    et retourne la réponse de l'IA.
    """
    
    # Construction de la conversation pour l'IA
    messages = [
        {"role": "system", "content": config.SYSTEM_PROMPT}
    ]
    
    # On ajoute l'historique (pour se souvenir de ce qu'on a dit avant)
    for tour in historique:
        messages.append({"role": "user", "content": tour["user"]})
        messages.append({"role": "assistant", "content": tour["ia"]})
    
    # On ajoute le nouveau message
    messages.append({"role": "user", "content": message_client})

    try:
        # Appel à l'IA (Groq)
        response = client.chat.completions.create(
            model=config.MODEL_NAME,
            messages=messages,
            temperature=0.7 # Un peu de créativité, mais pas trop
        )
        
        # On récupère juste le texte
        return response.choices[0].message.content
        
    except Exception as e:
        return f"Erreur critique dans le cerveau : {e}"