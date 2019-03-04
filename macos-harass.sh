#!/bin/bash
if [[ $# -ne 2 ]]
then
  echo "USAGE: $0 <popup title> <text input prompt>"
  exit 1
fi

osascript -e "display dialog \"$2\" with title \"$1\" default answer \"\""
