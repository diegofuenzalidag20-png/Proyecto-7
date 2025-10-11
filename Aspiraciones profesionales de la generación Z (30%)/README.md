# 📁 Proyecto 1: Modelo Base de Aspiraciones Profesionales de la Generación Z

## 🎯 Objetivo
El objetivo principal de este proyecto fue implementar el **ciclo de vida completo de Machine Learning (ML)**, desde el preprocesamiento hasta el despliegue de un modelo predictivo como una **API REST**.

El modelo está diseñado para clasificar la ruta de aspiración profesional más probable de un individuo de la Gen Z en una de las 7 categorías disponibles, basándose en sus respuestas a una encuesta.

---

## 📊 Resultado y Análisis Crítico

| Métrica | Valor | Conclusión |
| :--- | :--- | :--- |
| **Modelo Usado** | Random Forest Classifier | Robustez para datos categóricos y bajo volumen. |
| **Precisión (Accuracy)** | **30%** | Resultado bajo, pero superior a una predicción al azar (14.3%). |
| **Predicción de Prueba** | Business/Ops/Sales | (Basado en el `payload.json`) |

### Justificación de la Baja Precisión (30%)

La baja precisión es un resultado esperado, sirviendo como **análisis base** para las mejoras del Proyecto 2. Las principales causas son:

1.  **Desbalance de Clases:** La variable objetivo (Aspiración Profesional) presenta una distribución muy desigual, lo que provoca que el modelo tenga un fuerte **sesgo** hacia las clases mayoritarias.
2.  **Bajo Volumen de Datos vs. Alta Dimensionalidad:** Se partió de $\approx 300$ muestras. Al aplicar **One-Hot Encoding** a las 12 preguntas categóricas, se generaron $\approx 50$ *features*. La escasez de datos en relación al alto número de *features* generó un alto riesgo de **sobreajuste** (*overfitting*).

---

## 🛠️ Estructura del Proyecto y Despliegue

Este proyecto implementa un **pipeline de producción** con los siguientes componentes:

### Archivos Clave

| Archivo | Descripción |
| :--- | :--- |
| `Proyecto7.ipynb` | Notebook de Jupyter con la Exploración de Datos, Preprocesamiento y Entrenamiento del modelo. |
| `aspirations_classifier_final.pkl` | Archivo binario que contiene el **Modelo de Random Forest entrenado**. |
| `feature_names.json` | Contiene la lista de las **49 *features*** esperadas, crucial para alinear la entrada de la API con las columnas de entrenamiento. |
| `app.py` | Servidor Flask que expone el modelo como API REST. |
| `payload.json` | Ejemplo de cuerpo de solicitud POST para probar la API. |

### 🚀 Instrucciones de Despliegue (API REST)

Para levantar el servicio de predicción localmente:

1.  **Instalar dependencias:**
    ```bash
    pip install pandas joblib scikit-learn flask
    ```
2.  **Iniciar el Servidor Flask:**
    Asegúrese de estar en la carpeta `/Aspiraciones profesionales de la generación Z (30%)` y ejecute:
    ```bash
    python app.py
    ```
3.  **Realizar una Predicción (desde otra terminal):**
    Utilice `curl` para enviar los datos de prueba definidos en `payload.json` al *endpoint*:
    ```bash
    curl -X POST -H "Content-Type: application/json" -d "@payload.json" [http://127.0.0.1:8000/predict_aspirations](http://127.0.0.1:8000/predict_aspirations)
    ```

**Respuesta Esperada:**
```json
{
"confidence_percentage": "23.76%", 
"message": "Prediccion generada por el modelo de Aspiraciones de la Gen Z. (Precision general del 30% debido a datos limitados).", 
"prediction_aspirational_path": "Business/Ops/Sales"
}