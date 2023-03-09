#!/bin/bash

Xaxis=$(xrandr --current | grep '*' | uniq | awk '{print $1}' | cut -d 'x' -f1)
Yaxis=$(xrandr --current | grep '*' | uniq | awk '{print $1}' | cut -d 'x' -f2)

export_ip () {
    echo "hello"
    echo "world"
}
echo "Xaxis" $Xaxis
echo "Yaxis" $Yaxis

gnome-terminal --geometry=80x7+0+0      -- bash -c "echo 'Hello Bash!'; top"  --title A
gnome-terminal --geometry=80x7+0+300    -- bash -c "echo 'Hello Bash!'; top"  --title B
gnome-terminal --geometry=80x7+0+600    -- bash -c "echo 'Hello Bash!'; top"  --title C
gnome-terminal --geometry=80x7+1500+0   -- bash -c "echo 'Hello Bash!'; top"  --title D
gnome-terminal --geometry=80x7+1500+300 -- bash -c "echo 'Hello Bash!'; top"  --title E
gnome-terminal --geometry=80x7+1500+600 -- bash -c "echo 'Hello Bash!'; top"  --title F
