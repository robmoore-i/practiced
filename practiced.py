import subprocess
import time
import json

config_filename = 'practiced-config.json'
config = {}

with open(config_filename) as config_file:
    config = json.load(config_file)

if len(config.values()) == 0:
    print("Valid config not found. Tried \"" + config_filename + "\".")
    exit(1)

interval_time_minutes = config["time-minutes-between-harassments"]
interval_time_seconds = min(60 * interval_time_minutes, 5)
harassment_script_name = config["harassment-script"]
popup_title = config["popup-title"]

text_input_prompt = "Type stuff"

def harass():
    subprocess.check_call(
        "./" + harassment_script_name + " \"" + popup_title + "\" \"" + text_input_prompt + "\"",
        shell=True
    )

while(True):
    harass()
    time.sleep(interval_time_seconds)