# Command Line Generative AI 

A true computer geek never leaves the terminal and tries to achieve everything via the command line.

Since the AI movement, the usage of chatbots like ChatGPT has become part of the daily job in a developer's life.

However, navigating the browser interface for a chatbot is painful for people who don't like leaving the terminal.

Rejoice now that your generative AI chatbot, built using **Google's** Large Language Model(LLM) **Gemini Pro**, can be executed from your command line with this program.

## Setup:
### Requirements:
- Python 3.9+
### Installation:
-   Create a virtual environment (if you prefer to)
    ```
    python3 -m venv myenv
    ```
-  Activate virtual environment
    -   On Unix or MacOS:
        ```
        source myenv/bin/activate
        ```
    -   On Windows:
        ```
        myenv\Scripts\activate
        ```
- Install required packages:
    ```
    pip install -r requirements.txt
    ```
## Generate Gemini API Key:
This program is built using **Google's** Large Language Model(LLM) **Gemini Pro**. It requires API Key which you can generate for free [here](https://aistudio.google.com/app/apikey).

Copy your API Key and paste it into .env file.

## Start Chatting
- For most use case cases, running main.py without arguments is sufficient.
    ```
    python3 main.py
    ```
- If you're not satisfied with the response and like to see various responses, you can change the temperature by providing it as a command line argument.
    ```
    python3 main.py 0.5
    ```
    Temperature config ranges from 0.0 to 1.0, default is 0.9. You can read more about how temperature impacts your responses [here](https://ai.stackexchange.com/questions/32477/what-is-the-temperature-in-the-gpt-models).

> **Tip:** You can set bash or zsh alias 'ai' for executing the above commands so that its handy to start the bot.

Visit https://fazal.me for more info about me.