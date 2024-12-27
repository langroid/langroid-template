# Template for a Langroid-based project

Example project using the [Langroid](https://github.com/langroid/langroid) Multi-Agent
Programming framework to build LLM applications.

## How to use this template

On GitHub, click on the green "Use this template" button to create a new repo
based on this template.

## Set up various keys in the `.env` file or as environment variables

Typically your `.env` file should look something like this:

```bash
GEMINI_API_KEY=your_key
OPENAI_API_KEY=your_key
```

## Use `uv` to manage Python dependencies and virtual env

Install `uv`, see [here](https://docs.astral.sh/uv/getting-started/installation/)

## Change the project name

If your specific project name is `myproject`, then:

- Change `example` to your specific project name in the `pyproject.toml` file.
- rename the `example` folder to `myproject`


## Create virtual env and install dependencies

Then create a virtual env, activate it and install the dependencies:
```bash
uv venv --python 3.11
. ./.venv/bin/activate 
uv sync
```



