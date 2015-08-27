import subprocess
STANDARD_DELAY=1000
MOUSEDELTA=20

def xdotool(*argz):
	argzstr = ["xdotool"] + [str(a) for a in argz]
	subprocess.call(argzstr)

def keypress(key):
	xdotool("key", "--delay", STANDARD_DELAY, key)
def mousemove(x, y):
	xdotool("mousemove_relative", "--", x, y)
def click(btn):
	xdotool("click", "--delay", STANDARD_DELAY, btn)

cmds = {
	"j": lambda: keypress("space"),
	"up": lambda: mousemove(0, -MOUSEDELTA),
	"down": lambda: mousemove(0, MOUSEDELTA),
	"left": lambda: mousemove(-MOUSEDELTA, 0),
	"right": lambda: mousemove(MOUSEDELTA, 0),
	"l": lambda: click(0),
	"r": lambda: click(1)
}

keys = "wasdeq0123456789"
for k in keys:
	cmds[k] = lambda k=k: keypress(k)
def get_command(name):
	return cmds.get(name.strip().lower())
