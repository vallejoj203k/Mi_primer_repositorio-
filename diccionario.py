meme_dict = {
  "CRINGE" :"Algo que causa mucha pena o embarazoso",
  "LOL": "Una respuesta comun a algo gracioso",
  "ROLF": "Se utiliza como reaccion a algo gracioso, similar a LOL"
}

word = input ("Escribe una palabra moderna que no entiendas (¡Utiliza Mayusculas!): ")

if word in meme_dict.keys():
  print(meme_dict[word])

else:
  print("Todavia no tenemos esa palabra... Pero estamos trabajando en ella. ")
