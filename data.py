import os
import pandas as pd

input_folder = "block"
output_folder = "output"
txt_files = ["names/game_names.txt", "names/ia_names.txt", "names/meme_names.txt", "names/rwa_names.txt"]

categories_mapping = {
    "names/game": 1,
    "names/ia": 2,
    "names/meme": 3,
    "names/rwa": 4
}

categories = {}
for file in txt_files:
    category = file.split("_")[0]
    with open(file, 'r', encoding='utf-8') as f: 
        lines = f.readlines()
        for line in lines:
            symbol, name = line.strip().split(" - ")
            categories[symbol] = categories_mapping[category]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for file_name in os.listdir(input_folder):
    if file_name.endswith(".csv"):
        input_file = os.path.join(input_folder, file_name)
        output_file = os.path.join(output_folder, file_name)
        
        df = pd.read_csv(input_file)
        
        df['categoria'] = df['token'].apply(lambda x: categories.get(x, 0))
        
        df.to_csv(output_file, index=False)

print("Proceso completado. Los archivos CSV modificados se han guardado en la carpeta 'output'.")
