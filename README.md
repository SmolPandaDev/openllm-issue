# OpenLLM cant connect to local server issue

## Getting Started
We use a virtual environment to do all our development in, this ensures that we don't import modules that accidentally conflict with other project work.

`python3 -m venv venv` - this will create your virtual environment inside a venv folder
`source venv/bin/activate` - this will activate your virtual env
`python3 -m pip install --upgrade pip`
`python3 -m pip install -r requirements.txt`


## Start OpenLLM locally

E.g. 

```shell
openllm serve phi3:3.8b-ggml-q4
```

Note: any model for your pc will do.


## Run the program

```shell
python3 main.py
```

Observe the error:

```shell
Traceback (most recent call last):
  File "/Users/work/learning/openllm-issue/main.py", line 3, in <module>
    llm = OpenLLM(server_url='http://localhost:3000')
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/langchain_community/llms/openllm.py", line 149, in __init__
    openllm.client.HTTPClient
    ^^^^^^^^^^^^^^
AttributeError: module 'openllm' has no attribute 'client'
```