#!/bin/bash
if [[ $# -ne 1 ]]
then
  echo "USAGE: $0 <notification text>"
  exit 1
fi

osascript -e "display notification with title \"$1\""