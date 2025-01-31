## Web Page Summarizer

This projects uses OpenAI to summarize the contenet of a given webpage

### Prerequisite

 - A python installation
 - Refer to VSCode configuration to support Python development https://code.visualstudio.com/docs/python/python-tutorial

### How to run

- Add .env file at the root of the project with OPENAI_API_KEY https://platform.openai.com/settings/organization/billing/overview
- Activate a python virtual environment
- Install dependencies in requirements.txt
    - For windows

        ```
        > Set-ExecutionPolicy Unrestricted -Scope Process
        > .\.venv\Scripts\activate
        > pip install -r requirements.txt
        ```
- Run main.py
