# AI_Detectors_Project
This project is on the topic of AI Detectors in Education. The main goal is assessing the efficacy of AI detectors in identifying AI-Generated code in the education system.
This tool is to help educators have an idea of whether their students are participating in programming related classes or if they are just feeding prompts into the various AI engines and replicating that as their solution.
We are going to be focusing on 5 Large Language Models (LLMs) to generate code based on a common prompt. We will then write human-generated code to match these prompts and run both sets of code through AI code detectors to see if these detectors can efficiently categorize code as human-generated or AI-generated.

LLMs Used: ChatGPT, Gemini, Grok, Claude and Perplexity AI
AI Generated Code Detectors: GPTZero, Sapling, GPT-2 Detector, DetectGPT and Giant Language Model Test Room, ZeroGPT.

Sources: https://www.kaggle.com/code/amss10/detecting-llm-generated-code/input

User Manual For Running Software (running_model.py)

1. Ensure that the following libraries are installed on the host machine :
- Pandas - ```pip install pandas```
- Seaborn -  ```pip install seaborn```
- TensorFlow - ```pip install tensorflow```
- scikit-learn - ```pip install sklearn```
- Matplotlib -  ```pip install matplotlib```
- Numpy - ```pip install numpy```
- Natural Language Toolkit (NTLK) - ```pip install ntlk```

2. Once these packages are installed, import the modules and necessary packages into your IDE and ensure they are compatible with your Python version (tested on Python3.11).
- ```python3 sample_run.py```

3. Before reading the data file, update the path of the file on line 33 to the absolute path on your local computer.

4. After editing the path of the file, run the code and wait for a result.

5. After you have received the confusion matrix as a result, save the image to your computer, and close out of the window.
