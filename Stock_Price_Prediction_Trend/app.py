import joblib
import pandas as pd
import streamlit as st
import tensorflow as tf
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from datetime import timedelta

# Charger les modèles
ml_model = joblib.load('ml_model.pkl')  # Charger le modèle de machine learning sauvegardé
lstm_model = None
try:
    lstm_model_path = 'my_model.keras'
    lstm_model = tf.keras.models.load_model(lstm_model_path)  # Charger LSTM sauvegardé
except Exception as e:
    print(f"Error loading LSTM model: {e}")

# Titre de l'application Streamlit
st.title("Stock Prediction App")

# Option pour choisir entre les deux modèles
option = st.selectbox("Choose the model", ("Machine Learning", "LSTM"))

# Entrée de texte pour le ticker de l'action
stock_ticker = st.text_input("Enter Stock Ticker", "AAPL")

# Entrée de date pour la date de début
start_date = st.date_input("Start Date", pd.to_datetime("2020-01-01"))

# Entrée de date pour la date de fin
end_date = st.date_input("End Date", pd.to_datetime("today"))

# Bouton pour obtenir les données
if st.button("Get Data"):
    global predictions
    # Télécharger les données de Yahoo Finance
    data = yf.download(stock_ticker, start=start_date, end=end_date)

    # Afficher les données téléchargées
    st.write(f"Data for {stock_ticker} from {start_date} to {end_date}")
    st.write(data)

    # Prévoir pour demain
    tomorrow_date = end_date + timedelta(days=1)
    st.write(f"Predicting for {tomorrow_date}")

    # Faire des prédictions avec le modèle choisi
    if option == "Machine Learning":
        if ml_model is not None:
            try:
                # Préparer les données pour le modèle de machine learning
                features = data[['Close', 'Volume']].values
                predictions = ml_model.predict(features)
                # Afficher les prédictions
                st.write(f"Predicted Close Price for {tomorrow_date} (Machine Learning): ${predictions[0]:.2f}")
            except Exception as e:
                st.error(f"Error during Machine Learning prediction: {e}")
        else:
            st.error("Machine Learning model is not loaded. Please check the model file and try again.")
    elif option == "LSTM":
        if lstm_model is not None:
            # Préparer les données pour le modèle LSTM
            scaler = MinMaxScaler(feature_range=(0, 1))  # Normalisation Min-Max
            # Utiliser les données de clôture pour prédire demain
            close_today = data['Close'].iloc[-1]  # Dernier prix de clôture
            features = scaler.fit_transform(data[['Close']])  # Normaliser les données
            features = features[-1].reshape((1, 1, features.shape[1]))  # Reshape pour LSTM
            try:
                predictions = lstm_model.predict(features)
                # Inverser la normalisation pour obtenir les prédictions réelles
                predictions = scaler.inverse_transform(predictions.reshape(-1, 1))
                st.write(f"Predicted Close Price for {tomorrow_date}: ${predictions[0][0]:.2f}")
            except Exception as e:
                st.error(f"Error during prediction: {e}")
        else:
            st.error("LSTM model is not loaded. Please check the model file and try again.")
