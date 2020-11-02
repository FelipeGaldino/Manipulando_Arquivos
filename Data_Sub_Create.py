import os
import pandas as pd 

# Padroniza os Arquivos
def novoarquivo(Ativo,TipoBarra,SizeCandle):
    
    # Altera a versao do arquivo para UTF-8 e separa por virgulas
    df = pd.read_csv(f"Data_Sub_Folder/{SizeCandle}/{TipoBarra}_CandlesTicks_{SizeCandle}.csv",encoding="utf-16",sep ="\t")
    
    # Exclui a coluna tipo_barra
    del df['tipo_barra']
    
    # Renomeia as Colunas 
    df.rename(columns={'id': 'timestamp','abertura': 'open','minimo': 'low',
                       'maximo': 'high','fechamento': 'close','volume': 'volume'}, inplace=True)
   
    # Converte as Colunas do tipo inteiro em Float
    df['open']   = df['open'].astype(float)
    df['low']    = df['low'].astype(float)
    df['high']   = df['high'].astype(float)
    df['close']  = df['close'].astype(float)
    df['volume'] = df['volume'].astype(float)

    # Altera o tipo da Data no arquivo
    df['timestamp'] = df['timestamp'].apply(lambda x: x.replace('.', ''))
    df['timestamp'] = df['timestamp'].apply(lambda x: x.replace(':', ''))
    df['timestamp'] = df['timestamp'].apply(lambda x: x.replace(' ', ''))
    df['timestamp'] = pd.to_datetime(df['timestamp'],format='%Y%m%d%H%M%S')
    
    # Salva em CSV
    df.to_csv(f'Data_Sub_Folder_New/{SizeCandle}/{Ativo}_{TipoBarra}_{SizeCandle}.csv',index=False, sep=",",encoding="utf-8")

# Cria Arquivos
def CriaArquivos(Ativo,TipoBarra):
    novoarquivo(Ativo,TipoBarra,100)
    novoarquivo(Ativo,TipoBarra,200)

if __name__ == '__main__':
    
    # Tipo Candle
    Ativo = input("Digite o ativo WINJ20 WIN$N : ")

    # Cria Diretorios
    diretorio = f'Data_Sub_Folder_New/100'
    os.makedirs(diretorio)
    diretorio = f'Data_Sub_Folder_New/200'
    os.makedirs(diretorio)
    
    # Salva os arquivos
    TipoBarra = "Ask"
    CriaArquivos(Ativo,TipoBarra)

    # Salva os arquivos
    TipoBarra = "Bid"
    CriaArquivos(Ativo,TipoBarra)

    # Salva os arquivos
    TipoBarra = "Last"
    CriaArquivos(Ativo,TipoBarra)