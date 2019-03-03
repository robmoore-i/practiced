if [[ $# -ne 2 ]]
then
  echo "USAGE: $0 <popup title> <text input prompt>"
  exit 1
fi

zenity --entry --title="$1" --text="$2"
