#!/bin/bash
if [[ $# -ne 1 ]]
then
  echo "USAGE: $0 <notification text>"
  exit 1
fi

notify-send "$1"
