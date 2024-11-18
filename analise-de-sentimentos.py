import requests
import pandas as pd
import torch
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
import re

nltk.download('stopwords')
nltk.download('punkt')


ACCESS_TOKEN = "Q1didzWENybkYxWW1PQWsyaDQZD" # Substitua pelo seu token de acesso
INSTAGRAM_MEDIA_ID = "175165" # Substitua pelo ID da postagem no Instagram


def get_instagram_comments(access_token, media_id):
    url = f"https://graph.instagram.com/{media_id}/comments?fields=text&access_token={access_token}"
    response = requests.get(url)
    if response.status_code == 200:
        comments = response.json().get('data', [])
        return [comment['text'] for comment in comments]
    else:
        print(f"Erro ao obter comentários: {response.status_code}")
        return []


def preprocess_comments(comments):
    stop_words = set(stopwords.words('portuguese'))
    cleaned_comments = []
    for comment in comments:
        
        comment = re.sub(r"http\S+|www\S+|https\S+", "", comment, flags=re.MULTILINE)
        comment = re.sub(r"[^\w\s]", "", comment)
        comment = re.sub(r"\d+", "", comment)
       
        tokens = nltk.word_tokenize(comment.lower())
        tokens = [word for word in tokens if word not in stop_words]
        cleaned_comments.append(" ".join(tokens))
    return cleaned_comments


def analyze_sentiment(comments):
    sentiment_analyzer = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
    results = sentiment_analyzer(comments)
    return results


if __name__ == "__main__":
    print("Obtendo comentários do Instagram...")
    comments = get_instagram_comments(ACCESS_TOKEN, INSTAGRAM_MEDIA_ID)
    
    if comments:
        print(f"Comentários obtidos: {len(comments)}")
        print("Pré-processando os comentários...")
        cleaned_comments = preprocess_comments(comments)
        
        print("Analisando sentimentos...")
        sentiment_results = analyze_sentiment(cleaned_comments)
        
       
        df = pd.DataFrame({
            "Original Comment": comments,
            "Cleaned Comment": cleaned_comments,
            "Sentiment": [result['label'] for result in sentiment_results],
            "Score": [result['score'] for result in sentiment_results]
        })
        
        print(df)
       
        df.to_csv("sentiment_analysis_results.csv", index=False)
        print("Resultados salvos em 'sentiment_analysis_results.csv'.")
    else:
        print("Nenhum comentário encontrado.")
