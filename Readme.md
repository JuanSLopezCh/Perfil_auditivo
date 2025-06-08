# Proyecto de Grado
# Perfil Auditivo: Un enfoque analítico para la elección de audífonos

---

## 📋 Tareas

- [x] Descargar datos
- [x] Consolidar datos
- [x] Limpiar datos (remover duplicados)
- [x] Crear base de datos de marcas
- [ ] Obtener información adicional de referencias (link, imagen, precio, calificación de usuarios)
- [ ] Crear modelo de datos
- [ ] Elaborar mockup (colores, fuentes, esquema visual)
- [ ] Desarrollar el dashboard

---

## Paso 1: Descarga de Datos

Se descargaron los datos desde:  
🔗 [Repositorio AutoEq en GitHub](https://github.com/jaakkopasanen/AutoEq/tree/master)

Para mejor identificación, el archivo se nombró como `DataSet.xlsx`.  
Se creó el primer código llamado `1.Consolidar.ipynb`, donde se agrupan todos los archivos en uno solo, exportando un archivo denominado `naming.csv`.

Posteriormente, se realizaron ajustes manuales, como la separación de marca y referencia (basados en un ejercicio previo realizado el año pasado), y se generó el archivo final `Base 2025.xlsx`.

---

## Paso 2: Limpieza de Duplicados

Se creó el archivo de código `Naming CleanUp.ipynb`, donde se carga el último archivo de Excel (`Base 2025.xlsx`) y se ejecutan dos procesos principales para la eliminación de análisis duplicados en la respuesta en frecuencia:

1. Se separa el dataset en tres subconjuntos: referencias únicas, referencias duplicadas una vez, y referencias duplicadas dos o más veces.
2. Para las referencias duplicadas más de dos veces:
   - Se promedian todos los valores de respuesta en frecuencia.
   - Se calcula la distancia de cada versión a la media y se conserva únicamente la más cercana.
3. Para las referencias duplicadas una sola vez:
   - Se genera un ranking de evaluadores basado en la cantidad de evaluaciones presentes en el dataset.
   - Se conserva la evaluación del evaluador mejor posicionado en el ranking.

De este proceso se exporta el archivo `df_unicos_nuevo.csv`, donde se identificaron algunas referencias que se corrigieron manualmente siguiendo el mismo principio.

Además, se exportó un dataset de marcas únicas llamado `Marcas.csv`.

---

## Paso 3: Información Útil de las Marcas

Para construir un modelo de datos más completo, utilizando el archivo `Marcas.csv`, se obtuvo mediante ChatGPT información adicional como:

- Enfoque de la marca (Audiophile, usuario estándar, profesional, etc.)
- País de origen
- Página web oficial

Se hace luego una limpieza manual de las marcas cuyas paginas web no retornaban ninguna información para finalmente eliminar las marcas que ya no existen y sus audifonos relacionados.

Se descargan Los logos de las marcas.

---

## 💡 Ideas

- Descargar el logo de cada marca para incluirlo en el dashboard.

---

## 📝 Necesidades

- Adquirir una suscripción paga de ChatGPT para agilizar el proceso de recolección de información y no depender de la versión gratuita.

---

# ✨ Notas extra

- Asegurarte de estandarizar los nombres de archivos (`Base 2025.xlsx`, `DataSet.xlsx`, etc.) para evitar confusiones.
- Documentar también las decisiones visuales cuando empieces el mockup (tipografías, paleta de colores, etc.).
