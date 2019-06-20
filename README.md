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

An _executable script_ (including correct shebang line) which _prints to stdout_ a _string of json_ with two fields: `prompt` and `answer` _when run from the top
level directory_. For example:

```
Rob-Computer:practiced rob$ ./prompt-generators/georgian/src/print_prompt.py
{"prompt": "What is the english for \"აშენებ\"?", "answer": "build"}
Rob-Computer:practiced rob$
```

## Writing a prompt generator

With the specification above in mind, I have a couple of python examples. One for Georgian language, another for the lengths of the different months of the year. These live in `prompt-generators/`. To create a simple given->answer mapping, basically just copy the one for month-lengths and add everything you want into the dictionary.

## Wish list

- I want to generify my existing prompt-generator for Georgian into one for all languages. Expected difficulty: easy.

- I want to adjust the entry point of the program to be more user friendly. Config files piss me off. Expected difficulty: pips.

- I want to be able to interleave multiple prompt generators, so that I can learn Georgian and the lengths of the months at the same time. Expected difficulty: tricky.

- I want to have an implementation of the VocabPrompter interface which can combine multiple json files from the vocab lists. Expected difficulty: easy.

- I want to be able to specify the vocab lists I want to use from the entry point of the program, rather than fucking with code before running it. Expected difficulty: fine.