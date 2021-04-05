import pandas as pd

minority_classes = ['Minería', 'Comercio Exterior', 'Gerencia', 'Comunicación', 'Seguros',
                    'Construcción', 'Legales', 'Diseño', 'Educación', 'Ingeniería']

augmented_columns = ['back_en', 'back_te', 'back_zh', 'back_ro', 'back_ar', 'back_ja',
                     'back_jv', 'back_ko', 'back_vi', 'back_tr', 'back_yo']

AUGMENTED_DATA_PATH = './Data/Class augmented/'
DATA_PATH = './Data/Data_For_Backtranslation.csv'

df = pd.read_csv(DATA_PATH)

for min_class in minority_classes:
    path = AUGMENTED_DATA_PATH + '{}.xlsx'.format(min_class)
    min_df = pd.read_excel(path)
    classes = []
    texts = []
    for col in augmented_columns:
        for text in min_df[col]:
            texts.append(text)
        for element in min_df['clase']:
            classes.append(element)
    augmented_df = pd.DataFrame()
    augmented_df['texto'] = texts
    augmented_df['clase'] = classes
    df = df.append(augmented_df, ignore_index=True)

print(df['clase'].value_counts())
df.to_csv('./Data/Augmented_data.csv', index=False)  
        
