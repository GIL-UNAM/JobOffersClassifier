from BackTranslation import BackTranslation
import pandas as pd

class Backtranslator:
  def __init__(self):
    self.translator = BackTranslation(url=['translate.google.com','translate.google.co.kr',])
    self.temp_languages = ['af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca',
                           'ceb', 'ny', 'zh-cn', 'zh-tw', 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et',
                           'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'ha', 'haw', 
                           'he', 'hi','hmn','hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jw', 'kn', 
                           'kk', 'km','ko', 'ku', 'ky', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg',
                           'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'or', 'ps', 'fa',
                           'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si',
                           'sk', 'sl', 'so', 'su', 'sw', 'sv', 'tg', 'ta', 'te', 'th', 'tr', 'uk',
                           'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu']
  
  def backtranslate(self, text_list, src, limit):
    backtranslated_texts = []
    for temp_lan in self.temp_languages:
      for text in text_list:
        result = self.translator.translate(text, src=src, tmp=temp_lan, sleeping=5)
        backtranslated_texts.append(result.result_text)
        if len(backtranslated_texts) == limit:
          return backtranslated_texts
    return backtranslated_texts

"""
Ventas               13019
Administración        8740
Call Center           8459
Tecnología            5564
Oficios               3977
Recursos Humanos      2362
Logística             2209
Mercadotecnia         1667
Salud                 1613
Gastronomía           1346
Finanzas              1269
Secretaria            1239
Producción            1130
Ingeniería             881
Educación              702
Diseño                 661
Legales                646
Construcción           623
Seguros                573
Comunicación           418
Gerencia               272
Comercio Exterior      228
Minería                 41
"""

backtranslator = Backtranslator()

minority_classes = ['Minería', 'Comercio Exterior', 'Gerencia', 'Comunicación', 'Seguros',
                    'Construcción', 'Legales', 'Diseño', 'Educación', 'Ingeniería',
                    'Producción', 'Secreataría', 'Finanzas', 'Gastronomía', 'Salud', 
                    'Mercadotecnia', 'Logística', 'Recursos Humanos', 'Oficios','Tecnología',
                    'Call Center', 'Administración']

DATA_PATH = './Data/Data_For_Backtranslation.csv'
df = pd.read_csv(DATA_PATH, encoding='utf8')

AUGMENTED_DATA_PATH = './Data/Augmented_'
for min_class in minority_classes:
  print('Clase: {}'.format(min_class))
  df_class = df[(df['clase'] == min_class)]
  lim = 13019 - df_class['texto'].size
  augmented_data = backtranslator.backtranslate(text_list=df_class['texto'],src='es',limit=lim)
  df_augmented = pd.DataFrame()
  df_augmented['texto'] = augmented_data
  df_augmented['clase'] = [min_class]*len(augmented_data)
  df_augmented.to_csv(AUGMENTED_DATA_PATH+'{}.csv'.format(min_class),encoding='utf8',index=False)


  