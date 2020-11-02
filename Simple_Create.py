import os
import pandas as pd 

dir_data = "Simple_Data/"
new_dir  = "Simple_Data_New/"

list_files = os.listdir(dir_data)

for file in list_files:
    if file.endswith(".csv"):

        # Altera a versao do arquivo para UTF-8 e separa por virgulas
        name_file = dir_data + file
        df = pd.read_csv(name_file,encoding="utf-16",sep ="\t")
        
        # Altera o tipo da Data no arquivo
        df['timestamp'] = df['timestamp'].apply(lambda x: x.replace('.', ''))
        df['timestamp'] = df['timestamp'].apply(lambda x: x.replace(':', ''))
        df['timestamp'] = df['timestamp'].apply(lambda x: x.replace(' ', ''))
        df['timestamp'] = pd.to_datetime(df['timestamp'],format='%Y%m%d%H%M%S')
                
        # Salva novo arquivo
        new_file = new_dir + file
        df.to_csv(new_file,index=False, sep=",",encoding="utf-8")