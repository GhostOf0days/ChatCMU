## Build a Chatbot that can talk to users about your website

Powered by Pinecone and OpenAI

## Example:

https://ChatCMU.com/

# How to use

- Clone this repo
- Create a pinecone/.env file with the following variables:

```
OPENAIKEY =
PINECONEKEY =
```

- run ```pip install -r requirements.txt```
- add your source urls to scraper/main.py
- create a folder named `text`
- run scraper/main.py
- run pinecone/embedings.ipynb
- host pinecone/index.html on your website
