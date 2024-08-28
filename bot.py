import praw

reddit = praw.Reddit(#Creds go here)

wordl = ["tayyip", "erdoğan", "teyyip", "turkey", "rte", "r.t.e",
         "r.t.e.", "uzun adam", "turgay", "nigga", "karaboga", "karaboğa", "türkiye", "turk", "türk", "cockroach",
         "erdogan", "arab", "armenian genocide", "atatürk", "ataturk", "atagay", "erdogay", "turkish", "turks"]


text = "The brand new Dutchfucker-3000 (developed proudly in Republic of Turkiye) is here to inform you about: \n\n https://discord.gg/5vDpxDrb9f - For even more brainrot.\n\n https://balkansirl.net \n\n Stay tuned."
text_k="The brand new Dutchfucker-3000 (developed proudly in Republic of Turkiye) is here to inform you about: \n\n https://discord.gg/5vDpxDrb9f - For even more brainrot.\n\n https://balkansirl.net \n\n Stay tuned. \n\n Also, \n\n\n\n K"
for submission in reddit.subreddit("balkans_irl").stream.submissions(skip_existing=True):
     try:
        is_k=False
        post_title_words = submission.title.lower().split()  # Split the title into words
        for word in post_title_words:
            if word in wordl:
                is_k=True
                break
            else:
                is_k=False
        if is_k:
            submission.reply(text_k)
        else:
            submission.reply(text)
     except:
