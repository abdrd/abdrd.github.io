latex="""
<script defer src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"></script>
"""

fonts="""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Mono:ital,wght@0,400;0,700;1,400;1,700&display=swap" rel="stylesheet">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poly:ital@0;1&display=swap" rel="stylesheet">

"""

bootstrap="""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
"""

css="""
:root {
    --title-bg: rgba(15, 140, 1, 0.3);
    --green: #0f8c01;
    --brighter-green: #5d7c31;
}

body {
    font-family: "Poly", serif;
    font-weight: 400;
    font-size: 1.2rem;
    text-align: justify;
    line-height: 1.75;
    color: #101110;
    background-color: #f7f7f7;
    padding: 2rem;
}

code {
    font-family: 'Space Mono';
    font-size: 1.1rem;
    color: var(--brighter-green);
}


pre {
    border: 2px solid transparent;
    padding: 1rem;
    font-size: 1.1rem;
    border-image: linear-gradient(to right, #000, var(--green)) 1;
}

h1, h2, h3, h4, h5, h6 {
    font-family: "Poly", serif;
    padding: 1.4rem, 1.4rem, 1.4rem, 0rem;
    margin-bottom: 1.2rem;
    margin-top: 1rem;
    background: linear-gradient(to right, var(--green), #084401);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent
    background-clip: text;
    color: transparent;
    border-bottom: 2px solid transparent;
}

h1 code, h2 code, h3 code, h4 code, h5 code, h6 code {
    font-size: 100%;
}

.gist a {
    font-size: 0.8rem;
}

a {
    text-decoration: none;
    color: var(--brighter-green);
    font-size: 1.2rem;
    font-style: italic;
    font-weight: 550;
    border: 1px solid var(--green);
    padding-left: 0.2rem;
    padding-right: 0.2rem;
}

a:hover {
    background: var(--green);
    color: #fff;
}

strong {
    font-weight: 500;
    color: #1c3000;
}

#home-link {
    font-size: 1.5rem;
}

#comment-link {
    font-size: 1.5rem;
    margin-left: 4rem;
}

#top-of-the-post-link {
    font-size: 1.5rem;
}

sup {
    cursor: pointer;
    user-select: none;
    color: var(--brighter-green);
    font-size: 1.2rem;
    font-style: italic;
    margin-left: 2px;
}

footnote {
    font-style: italic;
    color: #000;
    cursor: pointer;
}

footnote::before {
    margin-right: 8px;
}

"""

index_css = """
body {
    font-family: "Poly", serif;
    font-weight: 400;
    font-size: 1.2rem;
    text-align: justify;
    line-height: 1.75;
    color: #101110;
    background-color: #f7f7f7;
    padding: 4rem;
    margin-top: 1rem;
}

body::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-image: url('/docs/assets/bg.jpg');
    background-size: cover;
    background-position: center;
    opacity: 0.6;
    z-index: -1;
}

a {
    color: #0e2bed;
}

.account-link {
    display: block;
    margin: 1rem;
}

.post {
    margin: 1rem;
    font-size: 1.45rem;
}

#title {
    font-size: 2.8rem;
    background-color: #fffdcc;
    padding: 0.4rem;
}

.title-container h2 {
    font-size: 2.4rem;
    margin-top: 2rem;
}

"""
