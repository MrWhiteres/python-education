#!/usr/bin/env bash
my_flag=false
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  if [[ "$USER" == "root" ]]; then
    cd /
    cd home
    mkdir -p Cron
    cd Cron
    echo "Folder created by path $PWD"
    my_flag=true
  else
    cd /
    cd home/$USER
    mkdir -p Cron
    cd Cron
    echo "Folder created by path $PWD"
    my_flag=true
  fi
elif [[ "$OSTYPE" == "msys" ]]; then
  name_windows_user=$(whoami)
  cd C:\\
  cd Users
  cd "$name_windows_user"
  cd Documents
  mkdir -p Cron
  cd Cron
  echo "Folder created by path $PWD"
  my_flag=true
else
  echo "an error occurred while creating a new folder"
fi

if [[ "$my_flag" == "true" ]]; then
  touch cron_jobs.txt
  touch weather.txt
  echo "$(date +%D) - $(date +%T)" >>cron_jobs.txt
  my_path_to_file_for_hour=$(realpath cron_jobs.txt)
  my_path_to_file_for_weather=$(realpath weather.txt)
  if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    export EDITOR=/bin/nano
    export VISUAL=nano
    crontab -e
    #0 * * * * add_new_hour.sh && curl -fsS --retry 3 https://cronhub.io/ping/af588f00-8ce3-11ec-8cc6-a98d47d712e3 >> $my_path_to_file_for_hour
    #0 7 * * * weather.sh && curl -fsS --retry 3 https://cronhub.io/ping/cc978be0-8cde-11ec-80b1-277e1edb0a88 >> $my_path_to_file_for_weather
  else
    curl wttr.in/Kharkiv
  fi

else
  echo "an error occurred while creating a new folder"
fi
