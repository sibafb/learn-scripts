#!/bin/bash

Xaxis=$(xrandr --current | grep '*' | uniq | awk '{print $1}' | cut -d 'x' -f1)
Yaxis=$(xrandr --current | grep '*' | uniq | awk '{print $1}' | cut -d 'x' -f2)

echo "Xaxis" $Xaxis
echo "Yaxis" $Yaxis

gnome-terminal --geometry=80x20+0+0
gnome-terminal --geometry=80x20+0+500 -- bash -c "echo 'Hello Bash!'; top" 

