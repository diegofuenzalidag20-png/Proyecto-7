# app.py (CÓDIGO CORREGIDO Y COMPLETO)
from flask import Flask, jsonify, request
import pandas as pd
import joblib
import json
import numpy as np
import warnings
from sklearn.exceptions import InconsistentVersionWarning

# Ignorar advertencias de versiones de Scikit-learn
warnings.filterwarnings("ignore", category=InconsistentVersionWarning)

app = Flask(__name__)

# Rutas de archivos (SE CARGAN UNA SOLA VEZ AL INICIAR LA APP)
MODEL_PATH = 'aspirations_classifier_final.pkl'
FEATURES_PATH = 'feature_names.json'

classifier = None
model_features = []

try:
    # Cargar el modelo y las features al inicio de la app
    classifier = joblib.load(MODEL_PATH)
    with open(FEATURES_PATH, 'r') as f:
        model_features = json.load(f)
    print("Modelos y features cargados exitosamente.")
except Exception as e:
    # Si esta carga inicial falla, la app fallará inmediatamente.
    print(f"ERROR: No se pudieron cargar los archivos del modelo. Detalle: {e}")

@app.route('/predict_aspirations', methods=['POST'])
def predict():
    if classifier is None:
        return jsonify({"error": "El modelo no esta disponible en el servidor."}), 500
        
    try:
        # 1. Obtener los datos de entrada como JSON
        json_data = request.get_json(force=True)
        
        # 2. Adaptar la entrada y crear un DataFrame de 1 fila
        processed_data = {k: [v] if not isinstance(v, list) else v for k, v in json_data.items()}
        query_df = pd.DataFrame(processed_data)

        # 3. Preprocesamiento: Aplicar One-Hot Encoding
        query_encoded = pd.get_dummies(query_df, drop_first=True)

        # 4. Alinear las columnas: Crear un DataFrame con las 49 columnas esperadas
        final_query = pd.DataFrame(columns=model_features, data=np.zeros((1, len(model_features))))

        # Rellenar solo las columnas presentes en la consulta codificada
        for col in query_encoded.columns:
            if col in final_query.columns:
                final_query[col] = query_encoded[col].values[0]

        # 5. Realizar la prediccion y obtener la probabilidad
        probabilities = classifier.predict_proba(final_query)[0]
        max_prob_index = np.argmax(probabilities)
        
        prediction_class = classifier.classes_[max_prob_index]
        confidence = probabilities[max_prob_index] * 100

        # 6. Devolver la respuesta en formato JSON
        response = {
            "prediction_aspirational_path": prediction_class,
            "confidence_percentage": f"{confidence:.2f}%",
            "message": "Prediccion generada por el modelo de Aspiraciones de la Gen Z. (Precision general del 30% debido a datos limitados)."
        }
        
        return jsonify(response)

    except Exception as e:
        # Manejo de errores detallado
        return jsonify({"error": "Error interno al procesar la solicitud.", "detail": str(e)}), 500

if __name__ == "__main__":
    # HOST='127.0.0.1' es para correrlo localmente en tu PC
    app.run(host='127.0.0.1', port=8000, debug=False)