#!/usr/bin/env bash
curl "https://api.openweathermap.org/data/2.5/weather?q=Kharkov,UK&appid=$(env[WEATHER])" >> weather.txt
