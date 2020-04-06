import re
import itertools
import nltk
import emoji

discAbreviacoes = {
    'vc' : 'você'
}

discEmoji = {
    ':thumbsup:' : '*aprovação*',
    ':muscle:' : '*músculo*',
    ':clown_face:' : '*palhaço*'
}

# Separa palavras que estejam com letras maisculas (ex: Quem disse isso foi NicolasCage -> Quem disse isso foi Nicolas Cage)
def tratamentoPalavrasJuntas (texto):
    retorno = " ".join(re.findall('[A-Z][^A-Z]*', texto))
    return (retorno)

# Tira a repetição de caracteres desnecessarios (ex: Ameeeeeeei o produto -> Amei o produto)
def tratamentoRepeticao (texto):
    retorno = "".join("".join(s)[:1] for _, s in itertools.groupby(texto))
    return retorno

# Substitui abreviacoes por suas correspondentes
def tratamentoAbreviacoes (texto):
    lista = nltk.word_tokenize(texto)
    retorno = ""
    for i in range (len(lista)):
        if (lista[i] in discAbreviacoes):
            lista[i] = discAbreviacoes[lista[i]]
        retorno += lista[i] + " "
    return retorno

# Trata os emojis substituindo-os por ações descritas no discionário
def tratamentoEmojis (texto):
    texto = emoji.demojize(texto, use_aliases=True)
    lista = nltk.word_tokenize(texto)
    retorno = ""

    for i in range (len(lista)):
        if(lista[i] in discEmoji):
            lista[i] = discEmoji[lista[i]]
        retorno += lista[i] + " "

    return retorno

fraseOriginal = "Ameeeeeei o produto, vc gostou? Até o MikeShinoda comprou 💪"

frase = tratamentoPalavrasJuntas(fraseOriginal)

frase = tratamentoRepeticao(frase)

frase = tratamentoAbreviacoes(frase)

frase = tratamentoEmojis(frase)

print(frase)