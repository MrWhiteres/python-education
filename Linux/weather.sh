#!/usr/bin/env bash
curl "https://api.openweathermap.org/data/2.5/weather?q=Kharkov,ua&appid=$(env[WEATHER])" >> weather.txt
