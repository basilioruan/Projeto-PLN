import emoji #Biblioteca com funções para converter emoji em seu código

#Discionário para trocar o resultado da função por uma expressão
discEmoji = {
    ':thumbsup:' : '*aprovação*',
    ':muscle:' : '*músculo*',
    ':clown_face:' : '*palhaço*'
}

#TO DO: verificar variação do código em emojis
texto = 'O de hoje tá pago 💪'
#'Na vida, às vezes é preciso ser meio palhaço 🤡'
#'O de hoje tá pago 💪🏽'

texto = emoji.demojize(texto, use_aliases=True)

resultado = ""

#Convertendo a frase em uma lista
texto = texto.split(" ")
for i in range (len(texto)):
    if(texto[i] in discEmoji):
        texto[i] = discEmoji[texto[i]]
    resultado = resultado + str(texto[i]) + " "

print (resultado)


    
