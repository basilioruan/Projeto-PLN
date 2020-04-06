import spacy
import random
import plac
from spacy.lang.pt.examples import sentences
from spacy import displacy
nlp = spacy.load('pt_core_news_sm')

doc = nlp("Gostei do produto, tudo ok como o esperado")
#doc2 = nlp("Quando eu chegar em casa falo com voce, beijos")
#print(doc2.text)

#for token in doc2:
#    print(token.text, token.pos_, token.dep_)

#print("\n")

for token in doc:
    print(token.text, token.pos_, token.dep_)

displacy.serve(doc,style='dep')