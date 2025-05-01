import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

MODEL_FILE = "pregnancy_model_local.joblib"

# tabela embutida como string
x = """idade_mae,horas_sono,alimentacao_saudavel,nivel_estresse,atividade_fisica_semana,renda_familiar,apoio_social,bem_estar
28,6,8,2,3,3500,8,1
32,7,6,5,1,4500,6,0
30,7.5,9,1,4,5000,9,1
25,5,4,7,0,2000,5,0
35,8,7,2,3,6000,7,1
29,6.5,5,6,2,3000,6,0
33,7,8,3,5,7000,8,1
31,6,6,4,1,4000,5,0
27,7.2,9,1,6,5500,9,1
26,5.5,3,8,0,1800,4,0"""

def carregar_dados():
    from io import StringIO
    data = pd.read_csv(StringIO(x))
    print("dados carregados da variável embutida")
    return data

def treinar_modelo(data):
    X = data.drop('bem_estar', axis=1)
    y = data['bem_estar']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    if len(data) > 10:
        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    else:
        X_train, y_train = X_scaled, y
        X_test, y_test = X_scaled, y

    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)

    return rf, scaler, X_test, y_test

def avaliar_modelo(model, X_test, y_test):
    y_pred = model.predict(X_test)
    print("\n== Random Forest ==")
    print(classification_report(y_test, y_pred))
    auc = roc_auc_score(y_test, model.predict_proba(X_test)[:,1])
    print(f"AUC: {auc:.2f}")

def save_model(model, scaler):
    model_data = {
        "model": model,
        "scaler": scaler
    }
    joblib.dump(model_data, MODEL_FILE)
    print(f"modelo salvo como {MODEL_FILE}")

def main():
    data = carregar_dados()
    rf_model, scaler, X_test, y_test = treinar_modelo(data)

    avaliar_modelo(rf_model, X_test, y_test)
    save_model(rf_model, scaler)

if __name__ == "__main__":
    main()