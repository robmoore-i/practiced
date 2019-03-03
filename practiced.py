import subprocess
import time
import json

config_filename = 'practiced-config.json'
config = {}

with open(config_filename) as config_file:
    config = json.load(config_file)

if len(config.values()) == 0:
    print("Config not found. Tried \"" + config_filename + "\".")
    exit(1)

interval_time_seconds    = config["time-seconds-between-harassments"]
harassment_script_name   = config["harassment-script"]
popup_title              = config["popup-title"]
content_generator_script = config["prompt-generator"]

def generate_prompt():
    return subprocess.getoutput("./" + content_generator_script)

def harass():
    text_input_prompt = generate_prompt().replace("\"", "'")
    subprocess.check_call(
        "./" + harassment_script_name + " \"" + popup_title + "\" \"" + text_input_prompt + "\"",
        shell=True
    )

while(True):
    harass()
    time.sleep(interval_time_seconds)