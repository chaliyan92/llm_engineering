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

## Week 3 - Day 2

Running Hugging Face libraries using Google Colab

### Learning Hugging Face Transformers

Basically Hugging Face Transformer Library provides APIs to interact with open-source models for typical `inference` tasks using `pipelines`

Follow this Hugging Face API https://huggingface.co/docs/transformers/main_classes/pipelines#transformers.pipeline.task

Side note: 
1. Training

    Training is when you provide a model with data for it to adapt to get better at a task in the future. It does this by updating its internal settings - the parameters or weights of the model. If you're Training a model that's already had some training, the activity is called "fine-tuning".

2. Inference

    Inference is when you are working with a model that has already been trained. You are using that model to produce new outputs on new inputs, taking advantage of everything it learned while it was being trained. Inference is also sometimes referred to as "Execution" or "Running a model".

From this point onwards please follow the Google Colab links I provide here

Link- https://colab.research.google.com/drive/14fG6AElqZxDJs940PjgjJ9Etns_OmryB#scrollTo=olaJP0u0H5xW

Note - Understand the __call__ in HuggingFace refer [Python Notes](python_notes.md)\

## Week 3 - Day 4

## Quantization in Large Language Models (LLMs)

**What is Quantization?**

Quantization in the context of LLMs is a process of **reducing the precision** of the numerical representations used for the model's weights and activations. Instead of using high-precision floating-point numbers (like FP32 or FP16), quantization converts these values to lower-precision integer formats (like INT8 or INT4).

Think of it like compressing an image. You reduce the number of bits used to represent each pixel's color, which can decrease the file size but might also slightly reduce the image quality. Similarly, quantizing an LLM reduces the number of bits used to store its parameters and perform calculations.

**Why is Quantization Important?**

Quantization is a crucial technique for several reasons, particularly when it comes to deploying and scaling LLMs:

1.  **Reduced Model Size:** Lower precision data types require significantly less memory. For example, switching from FP32 (32 bits per parameter) to INT8 (8 bits per parameter) can reduce the model size by a factor of four. This makes it easier to:
    * **Store models:** Smaller models require less storage space on disk.
    * **Load models into memory:** This is especially important for devices with limited RAM, like mobile phones or edge devices.
    * **Transmit models:** Smaller files are faster to download and share.

2.  **Faster Inference Speed:** Integer arithmetic is generally much faster than floating-point arithmetic on most hardware. By using lower-precision integer operations, quantized LLMs can achieve significantly faster inference times (generating text or answering questions). This is critical for real-time applications.

3.  **Lower Energy Consumption:** Performing computations with lower-precision numbers requires less energy. This is a significant advantage for battery-powered devices and for reducing the overall environmental impact of running large AI models.

4.  **Increased Deployment Flexibility:** Smaller and faster models can be deployed on a wider range of hardware, including devices with limited computational resources. This democratizes access to LLMs and enables their use in more diverse applications.

5.  **Improved Scalability:** With reduced memory footprint and faster inference, it becomes feasible to run more instances of the LLM on the same hardware, improving the overall throughput and scalability of the system.

**In summary, quantization is a vital optimization technique that makes LLMs more practical for real-world deployment by reducing their size, increasing their speed, lowering their energy consumption, and expanding their compatibility with various hardware.** While there can be a slight trade-off in model accuracy, various quantization techniques aim to minimize this loss while achieving significant efficiency gains.

No, **when you reduce the size of a number from high-precision to low precision, the value of the number will generally **not** remain exactly the same.** This process inherently involves some level of **approximation** and **loss of information**.

Here's an explanation of why:

* **Limited Representation:** Lower-precision formats (like INT8 or INT4) have a significantly smaller range of representable values and a coarser granularity compared to higher-precision formats (like FP32 or FP16).
* **Rounding and Truncation:** When you convert a high-precision number to a lower-precision format, the value needs to be "fit" into the limited set of representable numbers in the lower-precision format. This typically involves either:
    * **Rounding:** The high-precision value is rounded to the nearest representable value in the lower-precision format.
    * **Truncation:** The extra bits of information that cannot be represented in the lower-precision format are simply discarded (truncated).

**Analogy:**

Imagine you have a very precise ruler with millimeter markings (high precision). You want to measure the length of a small object. Let's say the object is 10.37 mm long.

Now, imagine you only have a ruler with centimeter markings (low precision). When you try to measure the same object with the centimeter ruler:

* You might round it to the nearest centimeter, which would be 10 cm.
* You might truncate the decimal part and say it's 10 cm.

In both cases, you've lost the finer detail of the 0.37 mm. The value is no longer exactly the same.

**Impact on LLMs:**

In the context of LLMs, the weights and activations are initially stored in higher-precision formats that can represent a wide range of values with fine-grained detail. When these are quantized to lower precision:

* **Weight Values:** The precise values of the connections between neurons are approximated by the coarser values in the lower-precision format. This can lead to a slight change in how the model processes information.
* **Activation Values:** Similarly, the intermediate calculations within the model are performed with lower precision, which can introduce small errors in the computations.

**The Goal of Quantization:**

The goal of quantization in LLMs is to reduce the model size and improve efficiency *while minimizing the degradation in the model's performance (accuracy)*. Sophisticated quantization techniques are employed to achieve this balance. These techniques often involve:

* **Careful selection of the quantization scheme:** Different methods (e.g., post-training quantization, quantization-aware training) and different bit widths (e.g., INT8, INT4) have varying impacts on accuracy.
* **Calibration:** Techniques to determine the optimal mapping from high-precision to low-precision values to minimize information loss.
* **Quantization-aware training:** Training the model while simulating the effects of quantization to make it more robust to the lower precision.

**In conclusion, quantization inevitably introduces some level of approximation, and the numerical values of the model's parameters and activations will not remain exactly the same after the conversion to a lower-precision format. The key is to perform this quantization in a way that yields significant efficiency benefits with an acceptable trade-off in model accuracy.**