# Proyecto de Grado  
# Perfil Auditivo: Un enfoque analítico para la elección de audífonos

---

## 📋 Tareas

- [x] Descargar datos  
- [x] Consolidar datos  
- [x] Limpiar datos (remover duplicados)  
- [x] Crear base de datos de marcas  
- [ ] Obtener información adicional de referencias (link, imagen, precio, calificación de usuarios)  
- [x] Crear modelo de datos (Explode de Audífonos)  
- [x] Medida para identificar curvas más similares a Harman  
- [ ] Elaborar mockup (colores, fuentes, esquema visual)  
- [ ] Desarrollar el dashboard  

---

## Paso 1: Descarga de Datos

Se descargaron los datos desde:  
🔗 [Repositorio AutoEq en GitHub](https://github.com/jaakkopasanen/AutoEq/tree/master)

Para facilitar su manejo, el archivo se renombró como `DataSet.xlsx`.  
Se creó el primer notebook llamado `1.Consolidar.ipynb`, donde se agrupan todos los archivos en uno solo, exportando el archivo `naming.csv`.

Posteriormente, se realizaron ajustes manuales como la separación entre marca y referencia (basados en un ejercicio previo realizado el año pasado), y se generó el archivo final `Base 2025.xlsx`.

---

## Paso 2: Limpieza de Duplicados

Se desarrolló el notebook `Naming CleanUp.ipynb`, donde se carga el archivo `Base 2025.xlsx` y se ejecutan dos procesos principales para la eliminación de análisis duplicados en la respuesta en frecuencia:

1. Se separa el dataset en tres subconjuntos: referencias únicas, referencias duplicadas una vez, y referencias duplicadas dos o más veces.  
2. Para las referencias duplicadas más de dos veces:
   - Se promedian todos los valores de respuesta en frecuencia.
   - Se calcula la distancia de cada versión a la media y se conserva únicamente la más cercana.  
3. Para las referencias duplicadas una sola vez:
   - Se genera un ranking de evaluadores basado en la cantidad de evaluaciones presentes en el dataset.
   - Se conserva la evaluación del evaluador mejor posicionado en el ranking.

De este proceso se exporta el archivo `df_unicos_nuevo.csv`, y se identifican algunas referencias que fueron corregidas manualmente bajo el mismo criterio.  
También se genera un archivo `Marcas.csv` con la lista consolidada de marcas únicas.

---

## Paso 3: Información Útil de las Marcas

Con base en el archivo `Marcas.csv`, y usando ChatGPT como apoyo, se recopila información complementaria de cada marca:

- Enfoque principal (Audiophile, profesional, usuario estándar, etc.)
- País de origen
- Página web oficial

Posteriormente se realiza una limpieza manual eliminando marcas cuyas páginas no ofrecen información o aquellas que ya no existen, removiendo también sus audífonos relacionados.  
Se descargan los logos de las marcas activas para integrarlos al modelo visual.

---

## Paso 4: Modelo de Datos – Explode de Audífonos

Para estructurar correctamente el modelo, se generan dos archivos:  
- Uno con las referencias únicas (`Dataset_Unicos.csv`)  
- Otro con las frecuencias y respuestas expandidas por audífono (`Dataset_Expandido.csv`), donde cada fila representa una frecuencia específica de un modelo.

---

## Paso 5: Comparación con la Curva Harman

Desde la misma fuente (AutoEq), se descargan dos curvas objetivo de Harman: una para audífonos **in-ear** y otra para **over-ear**.  
Se vincula cada audífono con su tipo correspondiente, y se compara la respuesta en frecuencia contra la curva ideal en cada punto.  
A partir de esta comparación se calculan dos métricas:

- **MAE** (Mean Absolute Error): error medio absoluto en dB.  
- **RMSE** (Root Mean Squared Error): sensibilidad al error acumulado.

Con base en estas métricas, se creó un índice denominado **Affinity**, que expresa en una escala de 0 a 100 qué tan parecida es la curva de un audífono a la curva Harman.  
Esto permite clasificar de forma más intuitiva los audífonos más cercanos a una experiencia de escucha equilibrada.  
Este índice será clave para las fases de clusterización y visualización final.

---

## Paso 6: Construcción de Curvas Proxy por Género Musical y Uso

Para complementar el análisis basado en la curva Harman, se construyeron curvas "proxy" representativas para diferentes géneros musicales y tipos de contenido, como Electrónica, Clásica, Hip-Hop, Rock, Gaming, Podcast, Reguetón, Trap, entre otros.

El proceso consistió en definir manualmente un conjunto de puntos clave de frecuencia (por ejemplo: 20 Hz, 60 Hz, 1 kHz, 10 kHz) junto con valores estimados de ganancia en decibeles (dB) que reflejan el perfil tonal típico de cada género. Estas definiciones se basaron en múltiples fuentes de referencia: artículos técnicos, recomendaciones de ecualización comunitarias y análisis auditivos documentados.

A partir de esos puntos, se generaron curvas completas de 695 valores usando interpolación lineal (`scipy.interpolate.interp1d`), alineadas exactamente con la resolución de frecuencia del dataset original. Esto permite comparar cualquier audífono contra cada curva proxy de forma precisa, calculando métricas como similitud o error medio, para identificar qué modelos son más aptos para cada tipo de contenido.  
Este conjunto de curvas ampliadas será clave para enriquecer la recomendación en el dashboard final.

---

## Paso 7: Preparación de Datos para el Web Scraping

Como parte del análisis del perfil auditivo, se incorporarán variables complementarias a las técnicas ya consideradas, incluyendo el **precio**, la **calificación promedio de usuarios**, la **imagen principal del producto** y los **enlaces comerciales** desde plataformas como **Amazon** y **AliExpress**.

Actualmente se cuenta con un total de **1.169 referencias únicas de audífonos**, las cuales fueron segmentadas en **12 archivos `.csv`** mediante un script en Python. Cada archivo agrupa un subconjunto de 100 audífonos, lo cual facilita tanto el proceso de búsqueda como el almacenamiento y posterior integración de los datos recolectados.

El objetivo de este paso es obtener y almacenar las siguientes variables por cada referencia:

- Indicador de disponibilidad (flag) en Amazon y AliExpress  
- URL directa al producto (por plataforma)  
- Imagen principal del producto  
- Precio estimado en USD  
- Calificación promedio de usuarios (estrellas)  

Esta información se integrará posteriormente en los modelos de **clusterización** (como K-Means), permitiendo segmentar los audífonos no solo por su respuesta en frecuencia, sino también por criterios de mercado y percepción del usuario.

---

### Pasos siguientes

Actualmente se están evaluando diferentes metodologías para realizar el scraping de forma eficiente y respetando las políticas de uso de cada plataforma. Entre las opciones consideradas se encuentran:

- **Scripts en Python** utilizando librerías como `Selenium` o `BeautifulSoup`, que permiten mayor control pero implican una ejecución más manual.  
- **Herramientas no-code** como **Octoparse**, que podrían acelerar el proceso con menor esfuerzo técnico, especialmente útil para lotes grandes.

Una vez recolectada y validada la información, se aplicarán técnicas de **clusterización avanzada** y se implementará una infraestructura de datos en **Databricks**, con el fin de contar con un **data warehouse robusto y escalable**. Este repositorio será consumido desde **Power BI**, donde se construirá la interfaz visual del usuario final.



## 📝 Necesidades

- Adquirir una suscripción paga de ChatGPT para agilizar el proceso de recolección de información y no depender de la versión gratuita.

---

# ✨ Notas extra

- Asegurarte de estandarizar los nombres de archivos (`Base 2025.xlsx`, `DataSet.xlsx`, etc.) para evitar confusiones.
- Documentar también las decisiones visuales cuando empieces el mockup (tipografías, paleta de colores, etc.).
