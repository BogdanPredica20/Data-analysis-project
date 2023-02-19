import pandas as pd

def functieCitireCSV():
    df = pd.read_csv('csvFilePsw.csv')
    print(df)

#functieCitireCSV()

# accesarea datelor cu loc şi iloc;
# ---afisarea hotelurilor din Bucharest
def functieAfisareDateFiltrate():
    print('\nAfisarea hotelurilor din Bucuresti\n')
    df = pd.read_csv('csvFilePsw.csv')
    print(df.loc[(df['Locatie'] == 'Bucuresti' ), 'Hotel' : 'Locatie'])
# ---afisarea hotelului, locatiei acestuia, funrnizorul si articolul achizitionat de la randurile 4-10
    print('\nAfisarea hotelului, locatiei acestuia, funrnizorul si articolul achizitionat de la randurile 4-10\n')
    print(df.iloc[4:10, 1:5])
    print('\n')
#functieAfisareDateFiltrate()


# Tratarea valorilor lipsă
def functieTratareValoriLipsa():
    df = pd.read_csv('csvFilePsw.csv')
    print('\nTratarea valorilor lipsa\n')
    print(df['Feedback clienti'])
    print('\nDupa inlocuire\n')
    print(df['Feedback clienti'].fillna(0))
#functieTratareValoriLipsa()


# modificarea preturilor unitare de la articole in functie de numarul bucatilor cumparate
def modificarePreturiUnitare():
    df = pd.read_csv('csvFilePsw.csv')
    df1=df.copy()
    print('\nValorile inainte de scaderea pretului unitar')
    print(df1.loc[(df1['Nr. Buc.']>0),
          ['Hotel', 'Locatie', 'Articol', 'Pret unitar', 'Nr. Buc.']])

    df1.loc[(df1['Nr. Buc.']>50 ), 'Pret unitar'] -= 5

    print('\nValorile dupa scaderea pretului')
    print(df1.loc[(df1['Nr. Buc.'] > 0),
                  ['Hotel', 'Locatie', 'Articol', 'Pret unitar', 'Nr. Buc.']])
#modificarePreturiUnitare()


#  Ștergerea de coloane şi înregistrări
# ---stergerea din df1 a coloanelor Nr. crt., Feedback clienti si Rating
def functieStergeColoaneSiInregistrari():
    print('\nTabel fara coloanele Nr. Crt., Feedback clienti si Rating\n')
    df = pd.read_csv('csvFilePsw.csv')
    df2 = df.drop("Nr. Crt.", axis=1).drop("Feedback clienti",axis = 1).drop("Rating", axis = 1)
    print(df2.head())
    print('-'*40)

    #--- stergere inregistrari
    print('\nTabel fara inregistrarile 3,5,9,10\n')
    df3 = df.drop([3,5,9,10], axis=0)
    print(df3.head(10))
functieStergeColoaneSiInregistrari()


