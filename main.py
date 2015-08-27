import sys
import cmds
import chatfetcher

def main():
	if len(sys.argv) != 2:
		print("usage: python3 main.py youtubeVideoID")
		return
	fetcher = chatfetcher.FetchTube(sys.argv[1])
	for comment in chatfetcher.get_comments(fetcher):
		print(comment)
		cmd = cmds.get_command(comment)
		if cmd:
			cmd()

if __name__ == "__main__":
	main()
