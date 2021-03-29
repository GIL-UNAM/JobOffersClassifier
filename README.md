# Clasificador de ofertas de trabajo
Proyecto de clasificación multiclase de ofertas de trabajo utilizando aprendizaje de máquina

## Conjuntos de datos
* El conjunto de datos después de aplicar backtranslation está disponible [aquí](https://drive.google.com/drive/folders/1qRtoGDDpmrms8CiLaQ2HrgLORq7Y5XBr?usp=sharing)

## Backtranslation
Para llevar a cabo el proceso de backtranslation se utilizó el traductor de Google y la herramienta de Google sheets como se indica [aquí](https://amitness.com/2020/02/back-translation-in-google-sheets/)

Para realizar esta etapa, se convirtió el texto a minusculas, se eliminó el aviso de privacidad y re removieron las ofertas repetidas, los datos obtenidos fueron los siguientes:

| Clase | Instancias |
| --- | --- |
| Ventas | 13721 |
| Administración | 9028 |
| Call Center | 8876 |
| Tecnología | 5951 |
| Oficios | 4094 |
| Recursos Humanos | 2429 |
| Logística | 2321 |
| Mercadotecnia | 1746 |
| Salud | 1644 |
| Finanzas | 1373 |
| Gastronomía | 1363 |
| Secretaria | 1281 |
| Producción | 1174 |
| Ingeniería | 911 |
| Educación | 720 |
| Diseño | 685 |
| Legales | 684 |
| Construcción | 650 |
| Seguros | 602 |
| Comunicación | 429 |
| Gerencia | 282 |
| Comercio Exterior | 233 |
| Minería | 47 |

## Word embeddings
Se utilizó un modelo pre-entrenado en español de word2vec disponible [aquí](http://crscardellino.github.io/SBWCE/)
