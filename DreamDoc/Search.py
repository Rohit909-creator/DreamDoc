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
    # print(keys[idx])
    print(data[keys[idx]])
    # for key in list(embed_data.keys()):
    #     # self.embeddings.append(embed_data[key])
    #     print(f"{key}:{len(embed_data[key])}")
        

























# import pinecone
# import json

# with open("Embed_data2.json",'r') as f:
#     s = f.read()
#     embed_data = json.loads(s)

# print(embed_data.keys())

# pinecone.init(api_key="8ed2c79c-fdd2-45a0-a9c0-5ebb610223fe", environment="asia-southeast1-gcp-free")

# l = pinecone.list_indexes()
# print(l)

# # pinecone.delete_index('dreamdata')

# # pinecone.create_index(name="dreamdata",dimension=1538, metric='cosine')
# index = pinecone.Index('dreamdata')

# data = []

# for key in list(embed_data.keys()):
#     data.append((key, embed_data[key]))
#     break
# # print(data)
# print("Uploading....")
# index.upsert(data)

# index.upsert()





















# from fuzzywuzzy import fuzz



# class KeySearch():

#     def __init__(self):
#         pass

#     def search(self,key):

#         result = []
#         R = fuzz.token_sort_ratio(s1.lower(), s2.lower())

#         return result


# if __name__ == "__main__":

    
#     r = search(L)

#     # with open('FETCHDAT.txt','r') as f:
        
