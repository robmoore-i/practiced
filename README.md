# Practiced

Configure this tool to periodically harass you with the aim of practicing stuff.

## Usage

First you need to configure the tool. With that in mind, here's how you use it once configured.

```
python3 practiced.py <practiced config file>
```

You don't need any libraries.

## Configuration

There are optional parameters and required ones. The format is json. An example configuration with all of the options is in the repository. It's called `practiced-config.json`.

### Required configuration parameters

For `practiced` to do its job, it really just needs two things:

- A way of harassing you
- Guidance on what to harass you with

To achieve this, you must put in the config two scripts.

```
{
    ...
    "harassment-script": "<executable script>",
    "prompt-generator": "<executable script>",
    ...
}
```

#### Harassment script

This script is periodically executed. It ought to pop something up on your screen. It must conform to the usage:

```
USAGE: ./harassment-script <popup title> <text input prompt>
```

#### Prompt Generator

This script must print a single line to stdout, which is the text input prompt for the harassments. What is the computer reminding you to practice? Type something! This script's job is to print the prompt to stdout.

### Defaulted configuration parameters

`practiced` can be configured in some ways:

- What is the title for the popups?
- How frequent should the harassments be?

For these, two configuration parameters can be used:

```
{
    "popup-title": "<title>",
    "time-seconds-between-harassments": <a number greater than 0>
}
```

#### Default values

`popup-title` defaults to "Practice Time!"

`time-seconds-between-harassments` defaults to 300
