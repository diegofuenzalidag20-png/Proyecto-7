# 📊 Repositorio de Proyectos de Ciencia de Datos y Machine Learning

Este repositorio contiene la implementación de dos proyectos de Machine Learning desarrollados bajo el enfoque de **Modelo Base** y **Optimización**. El objetivo principal es demostrar la capacidad de construir soluciones predictivas completas, desde la limpieza inicial de datos hasta el despliegue final en una API REST, resolviendo desafíos de rendimiento y calidad de datos.

-----

## 🧭 Índice de Contenidos

1.  [Enfoque: Modelo Base y Optimización](https://www.google.com/search?q=%231-enfoque-modelo-base-y-optimizacion)
2.  [Proyecto 1: Modelo Base (Aspiraciones Generación Z)](https://www.google.com/search?q=%232-proyecto-1-modelo-base-aspiraciones-generacion-z)
3.  [Proyecto 2: Optimización (Popularidad de Apps en Google Play)](https://www.google.com/search?q=%233-proyecto-2-optimizacion-popularidad-de-apps-en-google-play)
4.  [Tecnologías Clave](https://www.google.com/search?q=%234-tecnologias-clave)

-----

## 1\. Enfoque: Modelo Base y Optimización

Este repositorio está estructurado en torno a dos proyectos con el propósito de demostrar la **mejora iterativa** en el desarrollo de soluciones de Machine Learning.

| Fase | Objetivo | Resultado |
| :--- | :--- | :--- |
| **Proyecto 1: Modelo Base** | Establecer una línea de base (baseline) de rendimiento y exponer los desafíos iniciales del dataset (principalmente el desbalance de clases). | Precisión inicial de **\~30%**. |
| **Proyecto 2: Optimización** | Aplicar técnicas avanzadas (Ingeniería de Features, SMOTE, XGBoost) para superar las deficiencias del modelo base, logrando un rendimiento superior y un modelo desplegable de alto valor. | Precisión general de **78%**. |

-----

## 2\. Proyecto 1: Modelo Base (Aspiraciones Generación Z)

Este proyecto se centró en predecir las aspiraciones profesionales de la Generación Z.

  * **Dataset:** `Aspiraciones profesionales de la generación Z`.
  * **Problema:** Clasificación Multiclase.
  * **Modelo:** Random Forest.
  * **Desafío Principal:** El dataset presentaba un **desbalance de clases severo**, lo que limitó la capacidad predictiva del modelo.

| Métrica | Valor |
| :--- | :--- |
| **Precisión (Accuracy)** | **\~30%** |

### Archivos Clave

  * [**Carpeta del Proyecto 1**](https://www.google.com/search?q=./Aspiraciones%2520profesionales%2520de%2520la%2520generaci%25C3%25B3n%2520Z%2520\(30%2525\)/README.md)
  * **API de Despliegue:** Desplegado mediante **Flask** para predicciones en tiempo real.

-----

## 3\. Proyecto 2: Optimización (Popularidad de Apps en Google Play)

Para esta fase, se eligió un nuevo dataset y se aplicó una estrategia de optimización para lograr un modelo robusto y de alto rendimiento. El objetivo fue predecir si una aplicación es "Popular" (`Rating >= 4.5`).

  * **Dataset:** Google Play Apps (`googleplaystore.csv` y `googleplaystore_user_reviews.csv`).
  * **Problema:** Clasificación Binaria (`Is_Popular` vs. `No_Popular`).
  * **Modelo:** **XGBoost Classifier**.

### 🛠️ Estrategia de Optimización Implementada

| Técnica | Justificación |
| :--- | :--- |
| **Ingeniería de Features** | Creación de métricas como `Mean_Sentiment_Polarity` (integrando reseñas) y `Review_Install_Ratio`. |
| **Visualización** | Análisis de distribuciones (`Rating`, `Installs`, `Price`) para justificar la limpieza de datos. |
| **Balanceo de Clases** | Uso de **SMOTE** (Synthetic Minority Over-sampling Technique) para balancear la clase minoritaria ("Popular"), resolviendo el problema central del Proyecto 1. |

### 📈 Resultados de la Optimización

La aplicación de estas técnicas resultó en una mejora drástica en el rendimiento predictivo:

| Métrica | Proyecto 1 (Base) | Proyecto 2 (Optimizado) | Mejora |
| :--- | :--- | :--- | :--- |
| **Precisión General** | $30\%$ | **$78\%$** | **+48 puntos porcentuales** |
| **AUC-ROC** | N/A | **$0.7859$** | Alto poder de discriminación del modelo. |

### Archivos Clave

  * [**Carpeta del Proyecto 2**](https://www.google.com/search?q=./Proyecto%2520de%2520Optimizacion%2520-%2520Google%2520Play/README.md)
  * **Modelo Persistido:** `xgb_model_optimized.pkl` y `preprocessor_optimized.pkl`.
  * **API de Despliegue:** Desplegado mediante **Flask** en el puerto 8001.

-----

## 4\. Tecnologías Clave

  * **Lenguaje:** Python 3.x
  * **Análisis y Procesamiento:** Pandas, NumPy
  * **Visualización:** Matplotlib, Seaborn
  * **Modelado:** Scikit-learn, **XGBoost**
  * **Optimización:** **imbalanced-learn (SMOTE)**
  * **Despliegue:** **Flask**, Joblib (Persistencia)
  * **Control de Versiones:** Git / GitHub