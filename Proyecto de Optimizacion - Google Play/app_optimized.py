import joblib
import pandas as pd
import json
from flask import Flask, request, jsonify

# --- Inicialización y Carga de Componentes ---
app = Flask(__name__)
# Nota: La API solo necesita cargar el modelo y el preprocesador.
try:
    # Cargar el modelo XGBoost
    model = joblib.load('xgb_model_optimized.pkl')
    # Cargar el objeto ColumnTransformer para preprocesar los datos de entrada
    preprocessor = joblib.load('preprocessor_optimized.pkl')
    # Cargar la lista de features de entrada original para alinear los datos
    with open('input_features_list.json', 'r') as f:
        input_features = json.load(f)
    print("Componentes de la API cargados exitosamente.")

except Exception as e:
    print(f"ERROR al cargar componentes: {e}")
    model = None
    preprocessor = None

# --- Función de Predicción ---
@app.route('/predict_popularity', methods=['POST'])
def predict():
    if model is None or preprocessor is None:
        return jsonify({"error": "Modelo o preprocesador no cargados. Revisar logs."}), 500

    try:
        # 1. Recibir los datos de la solicitud (debe ser un JSON)
        data = request.get_json()
        
        # 2. Crear un DataFrame con las features originales esperadas
        # Aseguramos que el DF tenga las mismas columnas que se usaron en el entrenamiento.
        input_df = pd.DataFrame(data, index=[0])
        
        # 3. Aplicar el Preprocesador
        # El preprocesador (ColumnTransformer) escala los numéricos y hace OHE a los categóricos.
        # Las features deben estar en el orden correcto, pero ColumnTransformer lo maneja.
        processed_data = preprocessor.transform(input_df)
        
        # 4. Predicción del Modelo (XGBoost)
        # Predicción de probabilidad para la clase 1 (Popular)
        probability_popular = model.predict_proba(processed_data)[0][1]
        
        # Predicción binaria (0 o 1)
        prediction_int = model.predict(processed_data)[0]
        prediction_label = "Popular (Rating >= 4.5)" if prediction_int == 1 else "No Popular (Rating < 4.5)"

        # 5. Respuesta JSON
        response = {
            "prediction_label": prediction_label,
            "is_popular": int(prediction_int),
            "confidence_score": f"{probability_popular*100:.2f}%",
            "accuracy_general": "78%", # Dato del Paso 8 para contexto
            "message": "Predicción generada por el modelo XGBoost optimizado con SMOTE."
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({"error": f"Error en la predicción: {str(e)}"}), 400

# --- Ejecución de la API ---
if __name__ == '__main__':
    # Usamos un puerto diferente para que no choque con el Proyecto 1 (Puerto 5000)
    app.run(debug=True, port=8001)