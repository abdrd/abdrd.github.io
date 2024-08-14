latex="""
<script defer src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"></script>
"""

fonts="""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Azeret+Mono:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Mono:ital,wght@0,400;0,700;1,400;1,700&display=swap" rel="stylesheet">
"""

bootstrap="""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
"""

css="""
:root {
    --title-bg: rgba(15, 140, 1, 0.3);
    --green: #0f8c01;
    --brighter-green: #5d9e03;
}

body {
    font-family: "Azeret Mono", serif;
    font-weight: 400;
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
    font-size: 3rem;
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

"""

index_css = """
:root {
    --link-hover-bg: rgba(5, 46, 252, 0.1);
    --post-link-border-color: rgba(5, 46, 252, 0.5);
}

body {
    font-family: "Azeret Mono", serif;
    font-weight: 400;
    line-height: 1.75;
    color: #333;
    background-color: #f7f7f7;
    padding: 2rem;
}

#title {
    margin-top: 2rem;
    margin-bottom: 2rem;
    color: #2c3e50;
    font-size: 3rem;
    font-weight: 700;
    text-align: center;
}

#accounts-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 2rem;
    margin-bottom: 3rem;
}

.account-link {
    position: relative;
    color: #2980b9;
    text-decoration: none;
    font-size: 1.1rem;
    transition: color 0.3s ease;
    padding: 0.2rem 04.rem;
}

.account-link::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    width: 0;
    height: 100%;
    background-color: var(--link-hover-bg);
    z-index: -1;
    transition: width 0.35s ease;
}

.account-link:hover::before {
    width: 100%;
}

.account-link:hover {
    color: #1a5276;
}

@media (max-width: 600px) {
    #accounts-container {
        gap: 0.5rem;
    }

    .account-link {
        font-size: 0.9rem;
        padding: 0.5rem;
    }
}

#posts-title-container {
    margin-top: 2rem;
    margin-bottom: 2rem;
    text-align: center;
    font-size: 2rem;
    font-weight: 600;
    color: #34495e;
}

#posts-container {
    margin-bottom: 2rem;
}

* {
    font-optical-sizing: auto;
    font-weight: 300;
    font-style: normal;
}

.post {
    position: relative;
    padding: 0.8rem;
    text-decoration: none;
    transition: color 0.3s ease;
    border: 1px, solid;
    border-color: var(--post-link-border-color);
}

.date {
    margin-top: 0.5rem;
}

.post::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    width: 0;
    height: 100%;
    background-color: var(--link-hover-bg);
    z-index: -1;
    transition: width 0.35s ease;
}

.post:hover::before {
    width: 100%;
}

"""
