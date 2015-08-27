Reads YouTube gaming chat, interprets commands, executes then using xdgtool to inject input

to run, you need Linux (too lazy to make a Windows version), xdgtool (sudo apt-get install xdgtool) and Python3

run:

`python3 main.py videoID`
where Video ID is the bit after "v=" in the Youtube URL i.e. if the gaming URL is "https://gaming.youtube.com/watch?v=nV82kpdftDU" use nV82kpdftDU

Commands are defined in cmds.py

The comment loader is partially based on https://github.com/xedoc/Ubiquitous2/blob/master/Ubiquitous2/Model/Chats/YoutubeChat.cs - copied its use of the JSON API instead of the protobuf interface that YouTube Gaming itself uses

Licensed under Creative Commons CC0 license i.e. do whatever you want with this code, I don't care
