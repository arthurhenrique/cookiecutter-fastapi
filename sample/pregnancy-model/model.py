import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

def train_and_save_model():
    # Gerando dados fictícios sobre bem-estar durante a gravidez
    np.random.seed(42)
    num_samples = 500
    data = {
        'horas_sono': np.random.randint(4, 10, num_samples),
        'alimentacao_saudavel': np.random.randint(0, 10, num_samples),
        'nivel_estresse': np.random.randint(0, 10, num_samples),
        'exercicio': np.random.randint(0, 5, num_samples),
        'bem_estar': np.random.choice([0, 1], num_samples)
    }
    df = pd.DataFrame(data)

    # Separando features e target
    X = df[['horas_sono', 'alimentacao_saudavel', 'nivel_estresse', 'exercicio']]
    y = df['bem_estar']

    # Dividindo em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Normalizando os dados
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Treinando o modelo
    rf_model = RandomForestClassifier(n_estimators=100, max_depth=4, random_state=42)
    rf_model.fit(X_train, y_train)

    # Salvando o modelo no seu ambiente
    model_data = {
        "model": rf_model,
        "scaler": scaler
    }

    joblib.dump(rf_model, "pregnancy_model_local.joblib")
    print("Modelo treinado e salvo com sucesso!")

def predict_wellness(horas_sono, alimentacao_saudavel, nivel_estresse, exercicio):
    # Carregando o modelo salvo
    model = joblib.load("pregnancy_model_local.joblib")
    # model = model_data["model"]
    # scaler = model_data["scaler"]

    # Criando entrada formatada
    input_data = np.array([[horas_sono, alimentacao_saudavel, nivel_estresse, exercicio]])
    # input_data_scaled = scaler.transform(input_data)

    # Fazendo a previsão
    prediction = model.predict(input_data)
    return "Bem-estar Positivo" if prediction[0] == 1 else "Bem-estar Negativo"

if __name__ == "__main__":
    train_and_save_model()

    # Exemplo de previsão
    resultado = predict_wellness(0, 0, 3, 2)
    print(f"Previsão de bem-estar: {resultado}")
