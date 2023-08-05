# Gotta go get rest cause I didnt sleep while making this, will finish the afterwards
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import json
import openai


class Search():

    def __init__(self) -> None:

        with open("Embed_data4.json", 'r') as f:
            s = f.read()
            self.embed_data = json.loads(s)
            self.embeddings = []
            for key in list(self.embed_data.keys()):
                self.embeddings.append(self.embed_data[key])
    def query(self, embs):
        probs = cosine_similarity([embs], self.embeddings)
        return probs

def get_embedding(text, model="text-embedding-ada-002"):
   text = text.replace("\n", " ")
   return openai.Embedding.create(input = [text], model=model)['data'][0]['embedding']
if __name__ == "__main__":

    with open("Data2.json",'r') as f:
        s = f.read()
        data = json.loads(s)

    openai.api_key = "<openai api>"

    embs = get_embedding("Hey, I've been seeing dreams in which I am chased by big scary monsters, I am unable to sleep because of it.")

    searcher = Search()
    probs = searcher.query(embs)
    idx = np.argmax(probs)
    print(idx)
    keys = list(searcher.embed_data.keys())
    print(data[keys[idx]])
    
        
