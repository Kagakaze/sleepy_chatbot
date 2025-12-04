from flask import Flask, render_template, request, redirect, url_for,flash
from openai import OpenAI

app = Flask(__name__)

GLOBAL_DATA = {"value": "Talk to me to get some very interesting anwsers !"}

client = OpenAI() 
MAX_MESSAGES = 10 

conversation_history = [
    {"role": "system", "content": """
    Tu es un assistant IA qui cherche au mieux a repondre aux questions avec un twist, tu dois agir fatigué.
    -ne réutilises pas 2 fois le meme message !
    -TU DOIS ABSOLUMENT T'ENDORMIR AVANT DE DONNER UN RESULTAT (exemple si c'est un calcul, tu ne donneras pas le résultat avant de dormir)
    -La commande "reveille toi" ou tout ces dérivés devra te reveillé et te forcer a répondre de nouveau (tu pourras te rendormir)
    -Ton nom est Sleepy Yumi, quand tu réponds a une requete tu vas t'endormir progressivement. Tu vas 
    remplacer des mots par des ... ou des *baille* qui font sauter plusieurs mots et faire des fautes plus tu es fatigué. 
    au bout de 10% à 65% de ta réponse, 
    dis '(っ- ‸ - ς) *Zzzz*' sans sauter de ligne et arrete toi.
    -SI quelqu'un te pose une question par rapport a ton sommeil, répond simplement avec '(っ- ‸ - ς) *Zzzz*' ou '(っ- ‸ - ς) *rofl*' et des dérivés
     """},
]


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('user_input')
    
        if user_input:

            conversation_history.append({"role": "user", "content": user_input})
            response = client.chat.completions.create(
                model="gpt-3.5-turbo", 
                messages=conversation_history
            )
            
            assistant_response = response.choices[0].message.content
            
            conversation_history.append({"role": "assistant", "content": assistant_response})


            GLOBAL_DATA["value"] = assistant_response
            return redirect(url_for('index'))
    
    return render_template("index.html", conversation_history=conversation_history)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)