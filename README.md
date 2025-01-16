# Blog generator

This script is ~90% written by ChatGPT to generate my blog page.

------

First, create a virtual environment and activate it.

```
py -m venv <name>
source ./<name>/bin/activate
```

Install the dependencies.

```
pip install -r requirements.txt
```

------

Now,

Run `python3 _build/buildall.py` in the root of the project.

And, optionally, start a server with `python3 -m http.server` and go to `0.0.0.0:8000`.

To recompile the blog anytime a file changes, paste this command to a terminal window:

```bash
while inotifywait -e modify,create,delete -r .; do py _build/buildall.py; done
```

Have a web server running in another terminal window to see the changes to the blog quickly.

Use `python3 _build/newpost.py` to create a skeleton for a post.



------------------------------------------


I quickly added a feature to the blog.

Creating a footnote

```
<sup href="#fn1">1</sup>.

<footnote id="fn1" href="https://en.wikipedia.org/wiki/System_F">https://en.wikipedia.org/wiki/System\_F</footnote>
```

The id `fn<number>` is required.

Here is the script for the functionality (_build/SCRIPTS.py):

```js
document.querySelectorAll('sup')
    .forEach((supTag) => {
        supTag.addEventListener('click', (event) => {
            event.preventDefault();
            const targetId = supTag.getAttribute('href').substring(1);
            const target = document.getElementById(targetId);
            window.location.hash = targetId;
        });

    supTag.textContent = `֎ ${supTag.textContent}`;
});

document.querySelectorAll('footnote')
    .forEach((footnote, idx) => {
        const link = footnote.getAttribute("href");

        footnote.addEventListener('click', (event) => {
            event.preventDefault();
            if (link !== null) {
                window.open(link, "_blank");
            }
        });

    const id = footnote.getAttribute("id");
    const num = id.match(/\d+/)[0];
    const styleTag = document.getElementById("style-post");

    styleTag.sheet.insertRule(`#${id}::before {
    content: '֎${num}'; // give appropriate footnote number
    display: inline-block; /* this disables 'text-decoration: underline;' for the symbol */
    color: var(--green);
}`)
    
    if (link !== null) {
        footnote.setAttribute("title", link);
    }
});
```

It is not perfect. I will probably build my own DSL to create blog posts in the future.

