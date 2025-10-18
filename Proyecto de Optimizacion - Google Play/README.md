# 🚀 Proyecto 2: Optimización de la Clasificación de Apps de Google Play

## 🎯 Objetivo de Optimización
Superar la baja precisión del 30% del Proyecto 1, logrando una clasificación de alto rendimiento mediante la aplicación de técnicas avanzadas de preprocesamiento, balanceo de clases y modelado avanzado.

## 🛠️ Estrategia de Optimización

1.  **Ingeniería de Features Avanzada:** Creación de variables clave como `Mean_Sentiment_Polarity` (a partir de las reseñas de usuarios) y `Review_Install_Ratio`.
2.  **Reducción de Cardinalidad:** Agrupación de las 33 categorías originales en 25 grupos para simplificar el modelo.
3.  **Balanceo de Clases (Solución Clave):** Uso de la técnica **SMOTE** para crear datos sintéticos, llevando el dataset de entrenamiento a un balance perfecto (5,914 vs. 5,914).
4.  **Modelado de Alto Rendimiento:** Uso del algoritmo **XGBoost Classifier** para el entrenamiento.

## 📈 Resultados de la Evaluación (XGBoost + SMOTE)

El modelo fue evaluado en el conjunto de prueba original (sin SMOTE) de 2,710 muestras:

| Métrica | Clase 0 (No Popular) | Clase 1 (Popular) |
| :--- | :--- | :--- |
| **Precision** | **0.83** | **0.61** |
| **Recall** | **0.87** | **0.53** |
| **F1-Score** | **0.85** | **0.57** |

| Métrica General | Valor |
| :--- | :--- |
| **Accuracy General** | **0.78** (78%) |
| **Área bajo la curva ROC (AUC-ROC)** | **0.7859** |

**Conclusión:** La estrategia de optimización elevó la precisión general del $30\%$ al $\mathbf{78\%}$, y el *Recall* de la clase minoritaria (**$0.53$**) valida que el modelo ahora es efectivamente capaz de identificar las aplicaciones populares, cumpliendo el objetivo del proyecto de optimización.