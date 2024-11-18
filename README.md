# Análise de Sentimento de Comentários do Instagram

Este projeto realiza a análise de sentimento de comentários de publicações do Instagram usando a API do Instagram e a biblioteca transformers da Hugging Face. O código extrai os comentários de uma mídia específica, os pré-processa (removendo stopwords, URLs, emojis e outros caracteres especiais) e, em seguida, utiliza um modelo pré-treinado para classificar os sentimentos desses comentários.

Descrição do Projeto
O objetivo deste projeto é coletar os comentários de uma publicação do Instagram e realizar a análise de sentimento para determinar se os comentários são positivos, negativos ou neutros. A análise de sentimento é feita utilizando o modelo BERT (Bidirectional Encoder Representations from Transformers), que foi treinado para lidar com múltiplos idiomas.

Como Funciona:


Autenticação e Acesso à API:

O projeto usa a API do Instagram Graph API para acessar os comentários de uma publicação específica.
Para acessar a API do Instagram, você precisa de um Access Token que pode ser obtido através do Facebook Developer Portal.
Extração de Comentários:

A função get_instagram_comments() realiza uma requisição à API para obter os comentários de uma mídia específica utilizando o ID da mídia e o Access Token.
Pré-processamento de Comentários:

Os comentários são processados para remover URLs, emojis e outros caracteres especiais.
As stopwords (palavras comuns e irrelevantes) são removidas para melhorar a qualidade da análise.
Análise de Sentimentos:

A biblioteca transformers é utilizada para fazer a análise de sentimentos dos comentários usando um modelo BERT multilingue.
O modelo classifica os comentários em categorias de sentimento e gera um escore de confiança para cada sentimento.
Resultado:

O script cria um DataFrame com os resultados e salva em um arquivo CSV (sentiment_analysis_results.csv), que contém:
O comentário original
O comentário pré-processado
O sentimento atribuído (ex: POSITIVE, NEGATIVE, NEUTRAL)
O score de confiança para a análise de sentimento


Como Utilizar:


Instalação das Bibliotecas:

Certifique-se de ter as bibliotecas necessárias instaladas. Execute o seguinte comando para instalar os pacotes requeridos:
"pip install requests pandas torch transformers nltk"

Obter o Access Token:

Acesse o Facebook Developer Portal e crie um App para obter o seu Access Token. Lembre-se de que o token de acesso pode expirar, então você pode precisar gerar um novo após algum tempo.
Configurar o Token de Acesso:

Substitua o Access Token no código pela chave gerada no passo anterior.
Obter o ID da Mídia:

Você pode obter o ID da mídia acessando a URL da postagem ou utilizando a API para buscar as mídias publicadas em sua conta.


Executar o Script:

Após fazer as configurações, execute o script. Ele buscará os comentários da mídia especificada e realizará a análise de sentimentos.

Ver os Resultados:

O script criará um arquivo CSV (sentiment_analysis_results.csv) com os resultados da análise de sentimentos.
Bibliotecas e Frameworks Utilizados
requests: Para fazer requisições HTTP à API do Instagram.
pandas: Para manipulação de dados e criação do arquivo CSV.
torch: Framework de deep learning utilizado pelo modelo de análise de sentimentos.
transformers: Biblioteca da Hugging Face para trabalhar com modelos pré-treinados de NLP, como o BERT.
nltk: Biblioteca de processamento de linguagem natural para pré-processamento de texto.
re: Para trabalhar com expressões regulares, removendo caracteres especiais e URLs.


Linguagem Utilizada:
Este projeto foi desenvolvido utilizando Python 3.

Requisitos
Python 3.6+
Instalar as dependências: requests, pandas, torch, transformers, nltk.


IMPORTANTE


Token de Acesso: Certifique-se de alterar o Access Token no código pelo SEU PRÓPRIO TOKEN, obtido no Facebook Developer Portal.
O projeto foi testado com uma conta Business/Creator do Instagram. Se você estiver utilizando uma conta pessoal, pode ser necessário converter para uma conta profissional para obter o acesso necessário via API.
