"""
A script to generate my blog.
"""

import os, sys, re, markdown2, yaml, shutil
from dataclasses import dataclass
from datetime import datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape

CONFIG = {
    "VERSION": "0.1.0",
    "POSTS_DIR": "posts",
    "LAYOUT_DIR": "site",
    "AUTHOR": {
        "NAME": "Abidin Durdu",
        "EMAIL": "abidindrd@gmail.com",
        "SOCIAL": [("GitHub", "https://github.com/abdrd"),
                    ("LinkedIn", "https://linkedin.com/in/abdrd")],
    }
}

def gece_error(msg):
    print(f"\033[31merror\033[0m: {msg}")
    sys.exit(1)
    
def main():
    if not os.path.isdir(CONFIG["POSTS_DIR"]):
        gece_error(f"'{CONFIG["POSTS_DIR"]}' directory must exist")
        
    posts = os.listdir(CONFIG["POSTS_DIR"])
    md_files = [f for f in posts if f.endswith((".md", ".mdown", ".markdown"))]  

    @dataclass
    class CompiledMarkdown:
        def __str__(self):
            return f"CompiledMarkdown{{name:{self.name}, frontmatter:{self.frontmatter}, html:{self.html}}}"
        
        name: str
        frontmatter: dict[str, str]
        html: str
    
    def compile_markdown(file_name) -> CompiledMarkdown:
        file_path = os.path.join(CONFIG["POSTS_DIR"], file_name)
        file = open(file_path, "r")
        raw_markdown = file.read()
        file.close()

        pattern = r"^---\s*\n(.*?)\n---\s*\n(.*)$"
        match = re.match(pattern, raw_markdown, re.DOTALL)
        if not match:
            gece_error(f"frontmatter not found in '{file_path}'")

        html = markdown2.markdown(match.group(2), extras=["fenced-code-blocks"])
        # add target="_blank" to all links
        html = re.sub(r'(<a\s+[^>]*)(>)', r'\1 target="_blank"\2', html)

        cm = CompiledMarkdown(name=file_name,
                    frontmatter=yaml.safe_load(match.group(1)),
                    html=html)

        if "title" not in cm.frontmatter and "date" not in cm.frontmatter:
            gece_error(f"'title' and 'date' fields are missing from the frontmatter in '{file_path}'")

        return cm
    
    compiled_mds = [compile_markdown(f) for f in md_files]

    if not os.path.isdir(CONFIG["LAYOUT_DIR"]):
        gece_error(f"'{CONFIG["LAYOUT_DIR"]}' directory must exist")

    global_ctx = {
        "index_title": "[BLOG] Abidin Durdu - abdrd",

            "posts":sorted(
                    [
                        {
                            "url_path": os.path.splitext(md.name)[0],
                            **md.frontmatter,
                        } for md in compiled_mds
                    ],
                    key=lambda x: datetime.strptime(x["date"], "%d-%m-%Y"),
                    reverse=True
                ),
            "author": {
            "name": CONFIG["AUTHOR"]["NAME"],
            "email": CONFIG["AUTHOR"]["EMAIL"],
            "social": CONFIG["AUTHOR"]["SOCIAL"],
        }
    }

    site = [f for f in os.listdir(CONFIG["LAYOUT_DIR"]) if f.endswith(".html")]

    jenv = Environment(
        loader=FileSystemLoader(os.path.join("site")),
        autoescape=False
    )

    @dataclass
    class RenderedPost:
        url_path: str
        html: str       
        
    def render_posts(global_ctx, posts: list[CompiledMarkdown]) -> list[RenderedPost]:
        template = jenv.get_template("post.html")
        return [RenderedPost(url_path=os.path.splitext(post.name)[0],
                             html=template.render(**global_ctx,
                                                    **post.frontmatter, content=post.html)) for post in posts]

    # TODO rewrite the generator to be more general-purpose.
   
    def render_index(global_ctx) -> str:
        return jenv.get_template("index.html").render(**global_ctx)
    
    def render_about(global_ctx) -> str:
        return jenv.get_template("about.html").render(**global_ctx)

    def render_contact(global_ctx) -> str:
        return jenv.get_template("contact.html").render(**global_ctx)

    @dataclass
    class Builder:
        index: str
        about: str
        contact: str
        posts: list[RenderedPost]

        def _copy_assets(self):
            site_assets_dir_path = os.path.join("site", "assets")
            if os.path.isdir(site_assets_dir_path):
                if os.path.isdir("assets"):
                    shutil.rmtree("assets")
                shutil.copytree(site_assets_dir_path, "assets")
            

        def write_to_disk(self):
            os.makedirs("about", exist_ok=True)
            os.makedirs("contact", exist_ok=True)

            with open(os.path.join("about", "index.html"), "w") as f:
                f.write(self.about)
                
            with open(os.path.join("contact", "index.html"), "w") as f:
                f.write(self.contact)
            
            with open("index.html", "w") as f:
                f.write(self.index)

            for post in self.posts:
                os.makedirs(post.url_path, exist_ok=True)
                with open(os.path.join(post.url_path, "index.html"), "w") as f:
                    f.write(post.html)

            self._copy_assets()
            

    builder = Builder(index=render_index(global_ctx),
                        about=render_about(global_ctx),
                        contact=render_contact(global_ctx),
                        posts=render_posts(global_ctx, compiled_mds))
    
    builder.write_to_disk()

    
if __name__ == "__main__":
    main()
