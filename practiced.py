import subprocess
import time

interval_time_seconds = 10
harassment_script_name = "linux-harass.sh"
popup_title = "Practice Time!"
text_input_prompt = "Type stuff"

def harass():
    subprocess.check_call(
        "./" + harassment_script_name + " \"" + popup_title + "\" \"" + text_input_prompt + "\"",
        shell=True
    )

while(True):
    harass()
    time.sleep(interval_time_seconds)