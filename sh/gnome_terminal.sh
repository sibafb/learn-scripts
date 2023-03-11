#!/bin/bash

# Ubuntu | ターミナル起動時の表示サイズ・表示位置の指定
# (https://tbpgr.hatenablog.com/entry/20130904/1378306039)
# --geometry=XSIZExYSIZE+XOFFSET+YOFFSET
gnome-terminal --geometry=80x20+0+0

# 新しい「GNOME端末」を開いてコマンドを実行する方法
# https://linuxfan.info/gnome-terminal-with-command
# -- command
gnome-terminal -- top

# gnome-terminal -- bash -c "実行したいコマンド; bash"
gnome-terminal -- bash -c "date; echo; cal; bash"

# Ubuntu：ルーチン化した日々のコマンドを実行するシェルスクリプト
# https://marbles.hatenablog.com/entry/2022/08/30/151236 

gnome-terminal --window --bash $(dirname ${0})/gnome_terminals_tabs.sh

