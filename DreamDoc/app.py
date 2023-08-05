from flask import Flask, render_template, request, jsonify
import Search
import numpy as np
import json
import openai
app = Flask(__name__)


lock = False
fact = None
search = Search.Search()
D = ""
with open('Data2.json','r') as f:
    s = f.read()
    data = json.loads(s)

openai.api_key = "<openai api>"


@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    global lock
    global fact
    global D
    user_message = request.json.get('user_message')

    if lock != True:
        print("Describe block")
        embs = Search.get_embedding(user_message)
        probs = search.query(embs)
        idx = np.argmax(probs)
        # print(idx)
        keys = list(search.embed_data.keys())
        # print(keys[idx])
        fact = data[keys[idx]]
        D = f"""-Fact-
    {fact}
    Procedures-
nterpreting Dream Symbols: I can provide explanations of common dream symbols and their potential meanings based on psychological theories and popular interpretations.
Offering General Insights: I can give general insights into the possible emotions and themes that may be present in a dream. For example, I can suggest that a dream about falling may relate to a feeling of lack of control or insecurity in waking life.
Highlighting Patterns: By analyzing recurring dreams or themes, I can point out potential patterns that may warrant further exploration or reflection.
Providing Context: If the dreamer shares relevant details about their life or current situation, I can try to contextualize the dream's symbolism within that framework.
Encouraging Self-Reflection: I can prompt the dreamer to reflect on the dream's content, emotions, and potential connections to their waking life.
Follow the facts and give dream based psychoanalysis on a person, help him understand his dreams.Follow the procedures to get to know more about the user chatting, try to make him/her say whats troubling, use the prefix "AI:" for response, don't make stuff up
user: {user_message}
"""
    else:
        print("Normal Chat block")
        
        D += f"user:{user_message}\n"
        
    lock = True
    resp = openai.Completion.create(
                        engine="text-davinci-003",
                        prompt=D,
                        temperature=0.7,
                        top_p=1.0,
                        max_tokens=200,
                        frequency_penalty=0.5,
                        presence_penalty=0.0,
                        stop=["You:"]
    )
    response = resp['choices'][0]['text']
    # response = "sample response"
    # Simulate a simple chatbot response
    chatbot_response = response
    D += f"\nAI:{chatbot_response}\n"
    print(D)    
    return jsonify({'chatbot_response': chatbot_response})

if __name__ == '__main__':
    app.run()
