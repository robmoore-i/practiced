#!/usr/local/bin/python3

import random

month_lengths = {
    "January" : 31,
    "February" : 28,
    "March" : 31,
    "April" : 30,
    "May" : 31,
    "June" : 30,
    "July" : 31,
    "August" : 31,
    "September" : 30,
    "October" : 31,
    "November" : 30,
    "December" : 31
}

def random_month():
    return random.choice(list(month_lengths.keys()))

def prompt(prompt, answer):
    return {
            "prompt": prompt,
            "answer": answer
        }

def february_prompt():
    leap_year = random.choice([True , False])
    if leap_year:
        return prompt("How many days are in February in a leap year?", "29")
    else:
        return prompt("How many days are in February in most years?", "28")

def random_prompt():
    month = random_month()
    if month == "February":
        return february_prompt()
    else:
        return prompt("How many days are in "+ month + "?", str(month_lengths[month]))

def prompt_text(prompt):
    return str(prompt).replace("\"", "\\\"").replace("'", "\"")

print(prompt_text(random_prompt()))

exit(0)