# Blog generator

This script is ~90% written by ChatGPT to generate my blog page.

Run `python3 _build/buildall.py` in the root of the project.

And, optionally, start a server with `python3 -m http.server` and go to `0.0.0.0:8000`.

To recompile the blog anytime a file changes, paste this command to a terminal window:

```bash
while inotifywait -e modify,create,delete -r .; do py _build/buildall.py; done
```

Have a web server running in another terminal window to see the changes to the blog quickly.

Use `python3 _build/newpost.py` to create a skeleton for a post.