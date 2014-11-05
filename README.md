# Rich learning Python the hard way

This repository contains the code I wrote to complete the [52 exercises](http://learnpythonthehardway.org/book/) of [Learn Python the Hard Way](http://learnpythonthehardway.org/) by [Zed Shaw](http://zedshaw.com/about/).

To ensure completion I have entered into a blood pact with a friend doing likewise.

I attempt to write about this probably horrific experience with [GitHub Pages](https://pages.github.com/) and [Pelican](http://blog.getpelican.com/) at [richlearnspythonthehardway.org](http://richlearnspythonthehardway.org/).

## Install

You can create a similar diary of trauma by [forking this repository](https://help.github.com/articles/fork-a-repo/). Replace Rich-specific bits as necessary.

```
mkvirtualenv lpthw
git clone git@github.com:richardcornish/lpthw.git
pip install -r requirements.txt
```

## Write

[Add and edit](http://docs.getpelican.com/en/latest/content.html) [Markdown](https://help.github.com/articles/markdown-basics/) files in `pelican/content/`. Then generate them:

```
pelican pelican/content -o pelican/output -s pelican/pelicanconf.py
cd pelican/output/
python -m SimpleHTTPServer
```

Visit [http://0.0.0.0:8000/](http://0.0.0.0:8000/).

## Publish

Now publish to the live Interwebs:

```
cd ../../ # Back to the top
ghp-import pelican/output
git push origin gh-pages
```

Visit [http://richardcornish.github.io/lpthw/](http://richardcornish.github.io/lpthw/).

## Domains

1. Replace the text in `pelican/content/extra/CNAME` with your own domain, and save, commit, push.
2. [Copy the IPs](https://help.github.com/articles/tips-for-configuring-an-a-record-with-your-dns-provider/) for A records from GitHub
3. Enter the records in your domain registrar's control panel, e.g. in [Google Domains](https://support.google.com/domains/answer/3290350?authuser=1&hl=en).
