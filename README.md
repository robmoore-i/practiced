# Practiced

Configure this tool to periodically harass you with the aim of practicing stuff.

## Problem

I want a program that will poke me to do practice periodically while I am on my computer.

## Solution

I want to configure the thing with a static list of phrases to poke me with. If I do this, I want to control
the ordering, or choose it to be random.

I might want to configure the thing with a function to generate phrases to poke me with.

## Desired usage

I want to run

```
./practiced.sh practiced-config.json
```

And that should start the process and begin harassing me. The first harassment should be immediate because I
want instant feedback that the thing did the thing right.

I foresee that I'd also like to be able to shut the thing up at any time, but that I would like that button's
presence to be configurable.

## Desired configuration options

I want to control

- The content of the harassments
- The time between harassments
- Optionally, a time after which the thing just shuts up
- A flag to indicate if I want the option to shut the thing up when it harasses me
