import json

# 1 - Strings para Dicionário 
person =  '{"name": "Rodrigo", "languagens": ["Python", "Javascript"]}' 
person_dict = json.loads(pessoa)
print(person_dict)
print(person_dict['languagens'])

# 2 - Lendo json externo
with open('iris.json', 'r') as f:
  data = json.load(f)
print(data)

# 3 - Convertendo dicionário para json
person_json = json.dumps(person_dict)
print(person_json)

# 4 - Formatando json
print(json.dumps(person_dict, indent = 4, sort_keys=True))

# 5 - Salvando json em txt
with open('person.txt', 'w') as json_file:
   json.dump(person_dict, json_file)
