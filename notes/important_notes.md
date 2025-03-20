# LLM Engineering

## Week 1 - Day 2

### Frontier models
1. Closed-Source:
    - GPT-4 (OpenAI)
    - Claude (Anthropic)
    - Gemini (Google DeepMind)
    - PaLM (Google)


2. Open-Source:
    - LLaMA (Meta)
    - Mistral (Mistral AI)
    - Qwen (Alibaba Cloud)
    - Phi (Microsoft)

### Three ways to use models

1. Using Chat interfaces
    - Ex: ChatGPT
2. Cloud APIs
    - Ex: LLM API, Frameworks like langchain
    - Manages Ai cloud services
        - Amazon bedrock
        - Google vertext 
        - Azure ML
3. Direct inference
    - With HugginFace transformer library
    - With Ollama to run locally

## Week 1 - Day 4

### Rule of thumb for tokens
- 1 token ~= 4 characters
- 1 character ~= 0.75 tokens
- 1000 tokens ~= 750 characters

### Context Window

The context window (or “context length”) of a large language model (LLM) is the amount of text, in tokens, that the model can consider or “remember” at any one time. A larger context window enables an AI model to process longer inputs and incorporate a greater amount of information into each output.
Ref - [link](https://www.ibm.com/think/topics/context-window)

## Week 1 - Day 5

- One shot prompting - You give an example with the question in the prompt
- Zero shot prompting - You don't give an example, LLM figure all the things on its own


Own idea to collate all the latest tech news by LLM referring to best tech sites
infoq, twitter, dev.io etc ...

## Week 2 - Day 3

- System Prompt - Establish ground rules like "If you don't know the answer, just say so". Provide critical background context
- Context - More relevant background information pertaining to the topic
- Multi Shot Prompting - Providing examples for the context

## Week 3 - Day 1

Hugging Face
 - It's a platform providing tools, datasets. libraries to develop LLM application. Provides hosting and sharing too
 - It has 3 main features
    - Models - Over 800,000 open source models
    - Datasets - About 200,000 datasets
    - Space - Apps made with Gradio, Leaderboard to compare the models, Deploy the application on Hugging Face cloud
- Hugging Face Libraries
    - Hugging Face Hub - To login to Hugging Face and interact, The Hugging Face Hub is a platform with over 900k models, 200k datasets, and 300k demos in which people can easily collaborate in their ML workflows
        - The Hugging Face Hub hosts Git-based repositories, which are version-controlled buckets that can contain all your files
        - Models: hosting the latest state-of-the-art models for NLP, vision, and audio tasks
        - Datasets: featuring a wide variety of data for different domains and modalities
        - Spaces: interactive apps for demonstrating ML models directly in your browser, Spaces is a simple way to host ML demo apps on the Hub. They allow you to build your ML portfolio, showcase your projects at conferences or to stakeholders, and work collaboratively with other people in the ML ecosystem
    - Dataset - Access to the datasets
    - Transformers -  A wrapper for LLM transformers (Tensorflow code PyTorch and JAXk), Transformers provides APIs and tools to easily download and train state-of-the-art pretrained models. Using pretrained models can reduce your compute costs, carbon footprint, and save you the time and resources required to train a model from scratch. These models support common tasks
    - PEFT - ( Parameter-Efficient Fine-Tuning) To train LLM
    - TRL - Transformer Reinforcement Learning
    - Accelerate - Distributed configuration management
