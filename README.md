## Build a Chatbot that can talk to users about your website

Powered by Pinecone and OpenAI

# How to use

- Clone this repo
- Create a pinecone/.env file with the following variables:

```
OPENAIKEY = '...'
PINECONEKEY = '...'
```

- run ```pip install -r requirements.txt```
- add your source urls to scraper/scraperV2.py
- create a folder named `text`
- run scraper/scraperV2.py
- run scraper/cleanup.py
- run pinecone/embedings.ipynb
- host pinecone/index.py on your website
