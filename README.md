# Rich learns Python the hard way

This repository contains the code I wrote to complete the [52 exercises](https://learnpythonthehardway.org/book/) of [Learn Python the Hard Way](https://learnpythonthehardway.org/) by [Zed Shaw](https://zedshaw.com/about/).

I attempt to write about this probably horrific experience with [GitHub Pages](https://pages.github.com/) and [Pelican](http://blog.getpelican.com/) at [richlearnspythonthehardway.org](http://richlearnspythonthehardway.org/).

## Install

You can create a similar diary of trauma by [forking this repository](https://help.github.com/articles/fork-a-repo/). Replace Rich-specific bits as necessary. I typically install projects to `~/Sites`, but is by no means required.

```
mkvirtualenv -p python3 rich-learns-python-the-hard-way
git clone git@github.com:richardcornish/rich-learns-python-the-hard-way.git
cd rich-learns-python-the-hard-way/
pip install -r requirements.txt
```

## Write

[Add](http://docs.getpelican.com/en/latest/content.html) and edit [Markdown](https://help.github.com/articles/markdown-basics/) files in `pelican/content/`. Then generate them:

```
pelican pelican/content -o pelican/output -s pelican/pelicanconf.py -t pelican/themes/rich
cd pelican/output/ && python -m SimpleHTTPServer  # Python 2
cd pelican/output/ && python -m http.server  # Python 3
```

Add `-t` to `pelican` for plain text. :)

Visit [http://0.0.0.0:8000/](http://0.0.0.0:8000/).

## Publish

Now publish to the live Interwebs.

```
cd ../../ # Back to the top
git add .
git commit -m "..."
git push origin master
ghp-import -p pelican/output
```

Visit [http://richardcornish.github.io/lpthw/](http://richardcornish.github.io/lpthw/) (or [http://richlearnspythonthehardway.org/](http://richlearnspythonthehardway.org/)).

## Domains

1. Replace the text in `pelican/content/extra/CNAME` with your own domain (and follow publish steps).
2. [Copy the IP addresses](https://help.github.com/articles/tips-for-configuring-an-a-record-with-your-dns-provider/) for A records from GitHub
3. Enter the IP addresses for the A record of your domain into your domain registrar's control panel, e.g. in [Google Domains](https://support.google.com/domains/answer/3290350?authuser=1&hl=en).
