#!/usr/bin/python3

from generate_prompt import PromptGenerator

# Fun fact: In Georgian the forms for the accusative and dative
# cases are exactly the same, and it has become typical to always
# refer to them as one.

prompt_generator = PromptGenerator("prompt-generators/georgian")

print(prompt_generator.get_printed_output())
exit(0)
