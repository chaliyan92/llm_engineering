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


Own idea to collate all the latest tech news by LLM refering to best tech sites
infoq, twitter, dev.io etc ...