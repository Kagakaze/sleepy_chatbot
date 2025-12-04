from openai import OpenAI
import os

from openai import OpenAI
import json
# Instanciation de votre client OpenAI
client = OpenAI() 

# Le seuil après lequel nous déclenchons le résumé (simplification)
MAX_MESSAGES = 10 

conversation_history = [
    {"role": "system", "content": """
    Tu es un assistant IA qui cherche au mieux a repondre aux questions avec un twist, tu dois agir fatigué.
    Ton nom est Sleepy Yumi, quand tu réponds a une requete tu vas t'endormir progressivement. Tu vas 
    
     """},
]

# Le "Prompt" que nous utiliserons pour demander le résumé à l'IA
SUMMARY_PROMPT = "Veuillez résumer la conversation précédente en une phrase concise et informative pour servir de contexte futur."

while True:
    user_input = input("Vous: ")
    if user_input.lower() in ["quitter", "exit"]:
        print("Fin de la conversation.")
        break
    
    conversation_history.append({"role": "user", "content": user_input})
    
    try:
        # 3. Appel de l'API avec l'historique optimisé
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=conversation_history
        )
        
        assistant_response = response.choices[0].message.content
        
        # 4. Ajouter la réponse de l'assistant à l'historique
        conversation_history.append({"role": "assistant", "content": assistant_response})
        
        print(f"Bot: {assistant_response}")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        # Retirer le dernier message utilisateur pour éviter de boucler sur l'erreur
        conversation_history.pop()