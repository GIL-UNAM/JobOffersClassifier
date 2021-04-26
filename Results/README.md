# Resultados

* Se utilizaron 2 arquitecturas de redes neuronales para realizar la clasificación: LSTM y CNN.
* Se utilizó validación cruzada estratificada para evaluar el rendimiento del clasificador.

## LSTM
#### Resultados con backtranslation
| class | precision | recall | f1-score |
| --- | --- | --- | --- | 
| Administración | 0.662 | 0.702 | 0.678 |
| Call center | 0.676 | 0.72 | 0.696 |
| Comercio exterior | 0.96 | 0.928 | 0.936 |
| Comunicación | 0.938 | 0.906 | 0.916 | 
| Construcción | 0.972 | 0.916 | 0.944 | 
| Diseño | 0.884 | 0.846 | 0.856 | 
| Educación	| 0.848 | 0.936 | 0.886 | 
| Finanzas | 0.528 | 0.448 | 0.478 |
| Gastronomía | 0.63 | 0.56 | 0.582 |
| Gerencia | 0.934 | 0.916 | 0.916 |
| Ingeniería | 0.946 | 0.816 | 0.862 |
| Legales | 0.974 | 0.934 | 0.948 |
| Logística | 0.6 | 0.614 | 0.6 |
| Mercadotecnia | 0.548 | 0.546 | 0.536 |
| Minería | 0.936 | 0.928 | 0.926 |
| Oficios | 0.488 | 0.464 | 0.472 |
| Producción | 0.464 | 0.464 | 0.452 |
| Recursos humanos | 0.666 | 0.626 | 0.642 |
| Salud | 0.674 | 0.624 | 0.632 |
| Secretaria | 0.62 | 0.584 | 0.596 |
| Seguros | 0.952 | 0.924 | 0.934 |
| Tecnología | 0.722 | 0.752 | 0.73 |
| Ventas | 0.71 | 0.71 | 0.71 |	
| accuracy | | |0.788 |
| macro | 0.754 | 0.732 | 0.736 |
| weighted | 0.804 | 0.788 | 0.79 |

#### Resultados sin backtranslation
|class | precision | recall | f1-score |
| --- | --- | --- | --- |
| Administración | 0.7 | 0.7 | 0.698 |
|Call center | 0.694 | 0.704 | 0.698 |
|Comercio exterior | 0.512 | 0.326 | 0.384 |
|Comunicación | 0.264 | 0.244 | 0.25 |
|Construcción | 0.55 | 0.612 | 0.578 |
|Diseño | 0.67 | 0.62 | 0.642 |
|Educación | 0.738 | 0.674 | 0.7 |
|Finanzas | 0.514 | 0.452 | 0.48 |
|Gastronomía | 0.638 | 0.558 | 0.59 |
|Gerencia | 0.252 | 0.196 | 0.22 |
|Ingeniería | 0.354 | 0.368 | 0.36 |
|Legales | 0.72 | 0.636 | 0.672 |
|Logística | 0.624 | 0.592 | 0.606 |
|Mercadotecnia | 0.56 | 0.566 | 0.56 |
|Minería | 0.594 | 0.428 | 0.466 |
|Oficios | 0.488 | 0.474 | 0.478 |
|Producción | 0.496 | 0.47 | 0.48 |
|Recursos humanos | 0.682 | 0.638 | 0.658 |
|Salud | 0.71 | 0.632 | 0.67 |
|Secretaria | 0.578 | 0.588 | 0.582 |
|Seguros | 0.482 | 0.38 | 0.42 |
|Tecnología | 0.77 | 0.768 | 0.768 |
|Ventas | 0.688 | 0.742 | 0.712 |
|accuracy |  |  | 0.652 |
|macro | 0.578 | 0.538 | 0.55 |
|weighted | 0.652 | 0.652 | 0.652 |


## CNN
#### Resultados con backtranslation
| class | precision | recall | f1-score |
| --- | --- | --- | --- | 
|Administración | 0.718 | 0.74 | 0.726 |
|Call center | 0.71 | 0.72 | 0.708 |
|Comercio exterior | 0.95 | 0.91 | 0.924 |
|Comunicación | 0.898 | 0.906 | 0.89 |
|Construcción | 0.97 | 0.912 | 0.938 |
|Diseño | 0.86 | 0.854 | 0.838 |
|Educación | 0.874 | 0.91 | 0.884 |
|Finanzas | 0.626 | 0.442 | 0.516 |
|Gastronomía | 0.704 | 0.592 | 0.642 |
|Gerencia | 0.922 | 0.892 | 0.902 |
|Ingeniería | 0.922 | 0.814 | 0.856 |
|Legales | 0.97 | 0.94 | 0.954 |
|Logística | 0.696 | 0.58 | 0.628 |
|Mercadotecnía | 0.628 | 0.548 | 0.582 |
|Minería | 0.96 | 0.846 | 0.888 |
|Oficios | 0.528 | 0.522 | 0.518 |
|Producción | 0.542 | 0.492 | 0.472 |
|Recursos humanos | 0.728 | 0.68 | 0.7 |
|Salud | 0.732 | 0.642 | 0.676 |
|Secretaria | 0.644 | 0.612 | 0.626 |
|Seguros | 0.916 | 0.922 | 0.912 |
|Tecnología | 0.802 | 0.78 | 0.788 |
|Ventas | 0.698 | 0.776 | 0.732 |
accuracy |  |  | 0.798 |
macro | 0.782 | 0.74 | 0.754 |
weighted | 0.814 | 0.798 | 0.8 |


#### Resultados sin backtranslation
|class | precision | recall | f1-score |
| --- | --- | --- | --- |
| Administración | 0.738 | 0.75 | 0.744 |
|Call center | 0.73 | 0.74 | 0.732 |
|Comercio exterior | 0.648 | 0.394 | 0.468 |
|Comunicación | 0.438 | 0.232 | 0.292 |
|Construcción | 0.698 | 0.606 | 0.646 |
|Diseño | 0.74 | 0.626 | 0.674 |
|Educación | 0.8 | 0.728 | 0.76 |
|Finanzas | 0.592 | 0.47 | 0.522 |
|Gastronomía | 0.692 | 0.608 | 0.644 |
|Gerencia | 0.622 | 0.198 | 0.284 |
|Ingeniería | 0.492 | 0.318 | 0.38 |
|Legales | 0.754 | 0.704 | 0.726 |
|Logística | 0.692 | 0.582 | 0.63 |
|Mercadotecnia | 0.648 | 0.568 | 0.6 |
|Minería | 0.84 | 0.384 | 0.478 |
|Oficios | 0.49 | 0.58 | 0.526 |
|Producción | 0.58 | 0.472 | 0.516 |
|Recursos humanos | 0.758 | 0.69 | 0.72 |
|Salud | 0.724 | 0.684 | 0.7 |
|Secretaria | 0.69 | 0.606 | 0.644 |
|Seguros | 0.592 | 0.384 | 0.464 |
|Tecnología | 0.806 | 0.788 | 0.796 |
|Ventas | 0.706 | 0.796 | 0.744 |
accuracy |  |  | 0.696 |
macro | 0.674 | 0.56 | 0.594 |
weighted | 0.698 | 0.696 | 0.692 |
