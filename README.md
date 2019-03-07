# Practiced

Configure this tool to periodically harass you with the aim of practicing stuff.

## Usage

Run the below command:

```
python3 practiced.py <practiced config file>
```

No external libraries required - it uses OS-specific shell commands instead. I have tested on ubuntu and macos.

## Configuration

Two configurations are in the repository. They are the json files. For example:

```
{
  "harassment-script": "linux-scripts/linux-harass.sh",
  "notification-script": "linux-scripts/linux-notify.sh",
  "prompt-generator": "prompt-generators/month_lengths/execute_generate_prompt.py",
  "popup-title": "Practice Time!",
  "time-seconds-between-harassments": 300
}
```

Note that the script paths are from the location of wherever you run `practiced.py` from.

## Prompt Generator

An _executable script_ (including correct shebang line) which _prints to stdout_ a _string of json_ with two fields: `prompt` and `answer`. For example:

```
Rob-Computer:practiced rob$ ./prompt-generators/georgian/src/print_prompt.py
{"prompt": "What is the english for \"აშენებ\"?", "answer": "build"}
Rob-Computer:practiced rob$
```

## Writing a prompt generator

With the specification above in mind, I have a couple of python examples. One for Georgian language, another for the lengths of the different months of the year. These live in `prompt-generators/`. To create a simple given->answer mapping, basically just copy the one for month-lengths and add everything you want into the dictionary.