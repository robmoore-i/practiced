# Practiced

Configure this tool to periodically harass you with the aim of practicing stuff.

## Usage

First you need to configure the tool. With that in mind, here's how you use it once configured.

```
python3 practiced.py <practiced config file>
```

You don't need any libraries.

## Configuration

Two configurations are in the repository. They are the json files. You'll want to change the `prompt-generator` entry.

## Prompt Generator

An _executable script_ (including correct shebang line) which _prints to stdout_ a _string of json_ with two fields: `prompt` and `answer`. For example:

```
Rob-Computer:practiced rob$ ./generate-prompt.py 
{"prompt": "What is the english for \"აშენებ\"?", "answer": "build"}
Rob-Computer:practiced rob$
```