import subprocess
import time
import json
import sys

config_filename = sys.argv[1]

config = {}

with open(config_filename) as config_file:
    config = json.load(config_file)

if len(config.values()) == 0:
    print("Config not found. Tried \"" + config_filename + "\".")
    exit(1)

interval_time_seconds    = int(config["time-seconds-between-harassments"])
harassment_script_name   = str(config["harassment-script"])
notification_script_name = str(config["notification-script"])
popup_title              = str(config["popup-title"])
content_generator_script = str(config["prompt-generator"])

def generate_prompt():
    return subprocess.getoutput("./" + content_generator_script)

def parse_prompt(generated_prompt_string):
    return json.loads(generated_prompt_string.replace("\\\"", "'"))

def harass():
    prompt = parse_prompt(generate_prompt())
    text_input_prompt = prompt["prompt"]
    answer = prompt["answer"]

    subprocess.check_call(
        "./" + harassment_script_name + " \"" + popup_title + "\" \"" + text_input_prompt + "\"",
        shell=True
    )
    
    subprocess.check_call(
        "./" + notification_script_name + " \"" + answer + "\"",
        shell=True
    )

while(True):
    harass()
    time.sleep(interval_time_seconds)