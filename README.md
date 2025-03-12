# Warrior-of-LAIght

AI-powered chatbot that recommends FF XIV Jobs based on conversation, made with LangChain, FAISS, and web scraping.

An example conversation can be "I want to fight on the front line" _Response_ "Which one of these is simplest to play?" _Response_

The project name is funny.

# Installations

You may need to install several components. The most common are:

pip install tiktoken

pip install langchain langchain-community langchain-openai faiss-cpu

Then you will need an OpenAI key. The one given on line 7 of Lang_Script.py is an example. Go to https://auth.openai.com/create-account to sign up/log in. Go to "API Keys" and get yours.

We then need to install it into the environment via two means

1.) Enter Windows Powershell and use $env:"_API key_"

2.) A much simpler approach, use this code already in the script (but commented out)

import os

os.environ["OPENAI_API_KEY"] = "_API key_"

Be warned there is a limit to how often you can access a key, so be ready to pay or create more accounts.

# Running it

In Command Prompt go to the directory the two files are in

Type in "python Lang_Script.py"

If no text or an error appears feel free to send a bug report to hkeating27@gmail.com
