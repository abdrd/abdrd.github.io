
## The first one makes clicking `sup` elements go to the appropriate footnote.
## The second one makes footnotes act like links.

footnote_script = """
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
"""
