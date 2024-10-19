import STYLES
import os
import datetime
import string

TITLE = "BLOG - abdrd"

def make_post_list():
    posts = []
    directories = [f.name for f in os.scandir(".") if f.is_dir()]
    for d in directories:
        if d in string.punctuation or d.startswith("_"):
            continue
        meta_file = os.path.join(d, "me.ta")
        if not os.path.exists(meta_file):
            continue
        with open(meta_file, 'r') as f:
            contents = f.read()
            dictionary = {}
            for line in contents.splitlines():
                splitted = line.split("=")
                k, v = splitted[0], splitted[1]
                dictionary[k] = v
            dictionary["url"] = d
            posts.append(dictionary)
    posts.sort(key=lambda x: datetime.datetime.strptime(x["date"], '%d-%m-%Y'), reverse=True)
    html = ""
    for p in posts:
        human_date = datetime.datetime.strptime(p["date"], '%d-%m-%Y').strftime('%B %d, %Y')
        html += f'<a class="post" href={p["url"]+"/"}>{p["title"]}</a><p class="date">{human_date}</p>'
    return (html, "No posts" if len(posts) == 0 else "Posts")

(posts_html, posts_title) = make_post_list()

index = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
        {STYLES.bootstrap}
        {STYLES.fonts}
    <style>

/*




         
                                                                                        _.oo.
                                                                 _.u[[/;:,.         .odMMMMMM'
                                                              .o888UU[[[/;:-.  .o@P^    MMM^
                                                             oN88888UU[[[/;::-.        dP^
                                                            dNMMNN888UU[[[/;:--.   .o@P^
                                                           ,MMMMMMN888UU[[/;::-. o@^
                                                           NNMMMNN888UU[[[/~.o@P^
                                                           888888888UU[[[/o@^-..
                                                          oI8888UU[[[/o@P^:--..
                                                       .@^  YUU[[[/o@^;::---..
                                                     oMP     ^/o@P^;:::---..
                                                  .dMMM    .o@^ ^;::---...
                                                 dMMMMMMM@^`       `^^^^
                                                YMMMUP^
                                                 ^^





*/
    
        {STYLES.index_css}
    </style>

    <title>{TITLE}</title>
</head>

<body class="container">
    <h2 id="title">Abidin Durdu</h2>
    <div class="title-container">
        <h2>Contact</h2>
    </div>
    <div id="accounts-container">
        <a class="account-link" target="_blank" href="https://github.com/abdrd/">GitHub (abdrd)</a>
        <a class="account-link" target="_blank" href="https://twitter.com/abidindrd_">Twitter (abidindrd_)</a>
        <a class="account-link" href="mailto:abidindrd@gmail.com">Email (abidindrd@gmail.com)</a>
    </div>
    <div class="title-container">
        <h2>{posts_title}</h2>
    </div>
    <div id="posts-container">
        {posts_html}
    </div>
</body>
</html>
"""

def make_index():
    with open("index.html", 'w') as f:
        f.write(index)
    print("Built index.html")
