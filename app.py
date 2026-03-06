import streamlit as st
import os 
import brain
import config

# Configuration de la page
st.set_page_config(page_title="TechBot Assistant", page_icon="🤖")

# Titre
st.title("🤖 TechBot : Assistant Support IT")
st.markdown(f"**Modèle actuel :** `{config.MODEL_NAME}`")
st.write("---")

# Zone de texte pour le mail client
mail_client = st.text_area(
    "📧 Collez ici le mail du client :", 
    height=150,
    placeholder="Ex: Bonjour, mon PC fait du bruit..."
)

# Bouton de génération
if st.button("🚀 Générer une réponse"):
    if mail_client:
        with st.spinner("Analyse du problème en cours..."):
            # On appelle ton cerveau (brain.py)
            reponse = brain.analyser_et_repondre(mail_client)
            
            # On affiche le résultat
            st.success("Réponse prête !")
            st.markdown("### ✉️ Réponse suggérée :")
            st.info(reponse)
    else:
        st.warning("Merci d'entrer un message client.")

# Petit pied de page
st.write("---")
st.caption("Développé par [Ton Nom] - MVP V1")