############## PREPROCESAMIENTO DE DATOS ##################
import pandas as pd
import joblib

data = pd.read_excel("dataset.xlsx") #cargamos el dataset
data.dropna(inplace=True) #eliminar filas que contengan valores nulos (inplace = no crear copia)

from sklearn.preprocessing import LabelEncoder #codificar etiquetas categoricas en valores numericos
label_encoder = LabelEncoder() #instancia de labelEncoder
data["tipo_encoded"] = label_encoder.fit_transform(data["Tipo"]) #visual, auditivo y cinestesico ahora son 0, 1 y 2
print(label_encoder.classes_)
print(data["tipo_encoded"])

#importar funciones de NLTK para el procesamiento de lenguaje natural
from nltk.tokenize import word_tokenize #divir texto en palabras o tokens
from nltk.corpus import stopwords #palabras vacias ("el", "la", "y", "en", etc)
from nltk.stem import PorterStemmer #algoritmo de lematizacion de palabras (lemas)

stop_words = set(stopwords.words("es")) #conjunto de palabras vacias
stemmer = PorterStemmer() #instancia del algoritmo de lema

#preprocesamiento de texto (funcion para una descripción de texto (Sentencia))
def preprocess_text(text):
    tokens = word_tokenize(text.lower()) #se convierte todo a minusculas y se divide en tokens
    tokens = [token for token in tokens if token not in stop_words] #si un token es una palabra vacia, se elimina
    tokens = [stemmer.stem(token) for token in tokens] #a cada token no eliminado se aplica stemmer
    return " ".join(tokens) #tokens procesados en una cadena de texto separados por un espacio en blanco

data["Sentencia"] = data["Sentencia"].apply(preprocess_text) #aplicando la funcion a cada fila de la columna "Sentencia"

############## SELECCION DE CARACTERISTICAS ##################
from sklearn.feature_extraction.text import TfidfVectorizer #transformar texto en representaciones numericas utilizando TF-IDF
tfidf_vectorizer = TfidfVectorizer() #instancia TF-IDF limitado a 1000 caracteristicas (para mejorar eficiencia)
X = tfidf_vectorizer.fit_transform(data["Sentencia"]) #representacion numerica de las descripciones (matriz)


############## MODELADO DEL DATASET (entrenamiento y prueba) ##################
from sklearn.model_selection import train_test_split #division de manera aleatoria
X_train, X_test, y_train, y_test = train_test_split(X, data["tipo_encoded"], test_size=0.3, random_state=10) #10 es un valor arbitrario

#conjuntos de datos
#X_train: Conjunto de caracteristicas de entrenamiento.
#X_test: Conjunto de caracteristicas de prueba.
#y_train: Conjunto de etiquetas de entrenamiento.
#y_test: Conjunto de etiquetas de prueba.

from sklearn.svm import SVC #Support Vector Machine, es un clasificador 
clasificador = SVC() #instancia de SVC

clasificador.fit(X_train, y_train) #aprende la relacion entre las caracteristicas y las etiquetas, para poder realizar predicciones


############## EVALUACION DE MODELO ##################
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
y_pred = clasificador.predict(X_test)
print("Exactitud:", accuracy_score(y_test, y_pred))
print("Reporte de clasificación:\n", classification_report(y_test, y_pred))
print("Matriz de confusión:\n", confusion_matrix(y_test, y_pred))


joblib.dump(clasificador, 'clasificador_entrenado.pkl')
# Guardar el vectorizador TF-IDF
joblib.dump(tfidf_vectorizer, 'tfidf_vectorizer.pkl')



