import praw
from time import sleep
wordl = ["tayyip", "erdoğan", "teyyip", "turkey", "rte", "r.t.e",
         "r.t.e.", "uzun adam", "turgay", "nigga", "karaboga", "karaboğa", "türkiye", "turk", "türk", "cockroach",
         "erdogan", "arab", "armenian genocide", "atatürk", "ataturk", "atagay", "erdogay", "turkish", "t"]

reddit = praw.Reddit(
    #stuff go here
)

subl = ["balkans_irl"]  # Subs that bot will reply on
d = 0

# Move the set initialization outside the loop
titlel = []
wait=3
is_k=False
while True:
    sub = reddit.subreddit(subl[d])
    print(subl[d])

    for post in sub.new(limit=1):
        skip=False
        for f in titlel:
            if post.id==f:
                skip=True
        if skip:
            continue
        post_title_words = post.title.lower().split()  # Split the title into words
        for word in post_title_words:
            if word in wordl and post.id not in titlel:
                print(f"Found a relevant word in post: {post.title.lower()}")
                is_k=True
                break  # Exit the inner loop if a relevant word is found
        try:
            if is_k:
                rep_temp="hi favorite (i hope so) balkan bot here, here's some links for some reason \n\n [imageboard](http://balkansirl.net) [discord](https://discord.gg/balkansirl) \n\n also you can click [here](https://www.reddit.com/message/compose/?to=/r/balkans_irl) to contact the mods. \n\n Also, \n\n\n\n K"
            else:
                rep_temp="hi favorite (i hope so) balkan bot here, here's some links for some reason \n\n [imageboard](http://balkansirl.net) [discord](https://discord.gg/balkansirl) \n\n also you can click [here](https://www.reddit.com/message/compose/?to=/r/balkans_irl) to contact the mods."
            post.reply(rep_temp)
            print("Replied to a post.(" + subl[d] + ")")
        except Exception as e:
            print("Couldn't reply. ({})".format(e))
        titlel.append(post.id)  # Add the post ID to the set
        is_k=False

    if d == len(subl) - 1:
        d = 0
    else:
        d += 1
    if len(titlel) > 100:
        del titlel[:50]
    sleep(wait)
    # Switch to another sub
