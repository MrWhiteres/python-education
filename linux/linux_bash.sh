#!/usr/bin/env bash
if [ -n "$1" ]; then
  if [ -d "$1" ]; then
    cd "$1" || exit
    ls | sort | uniq -u
  else
    echo "Directory $1 DOES NOT exists."
  fi
else
  ls | sort | uniq -u
fi
date
