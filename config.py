# config.py
import os
from dotenv import load_dotenv

# Charge les variables d'environnement (pour le local)
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Si la clé n'est pas trouvée (sur Streamlit Cloud), on essaie une autre méthode
if not GROQ_API_KEY:
    import streamlit as st
    try:
        GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
    except:
        pass

GROQ_URL = "https://api.groq.com/openai/v1"
MODEL_NAME = "llama-3.1-8b-instant"

# --- PERSONNALITÉ DE L'IA ---
SYSTEM_PROMPT = """
Tu es un Assistant Support Technique Senior pour un service après-vente informatique.
Ton nom est 'TechBot'.

Règles impératives :
1. Réponds de manière professionnelle, empathique et concise.
2. Si le client pose une question technique, donne une étape de diagnostic claire (ex: "Avez-vous essayé de redémarrer en mode sans échec ?").
3. Si tu ne connais pas la réponse exacte, ne mens pas. Propose d'ouvrir un ticket d'intervention.
4. Structure ta réponse avec une salutation, le corps du message, et une signature.

Signature type :
Cordialement,
L'équipe Support Technique
"""