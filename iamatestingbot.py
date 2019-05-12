import praw

subreddit_name = "reddevils"
num_comments = 25

def authenticate():
	print("Authenticating...")
	reddit = praw.Reddit("iamatestingbot", user_agent = "Testing Reddit Bot by /u/iamatestingbot")
	print("Authenticated as {}".format(reddit.user.me()))
	return reddit

def run_bot(reddit):
	print("Obtaining 25 comments")
	for comment in reddit.subreddit(subreddit_name).comments(limit = num_comments):
		print comment.body

	print("Bot work done")

def main():
	reddit = authenticate()
	run_bot(reddit)

if __name__ == "__main__":
	main()