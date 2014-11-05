# Rich learning Python the hard way

This repository contains the code I wrote to complete the [52 exercises](http://learnpythonthehardway.org/book/) of [Learn Python the Hard Way](http://learnpythonthehardway.org/) by [Zed Shaw](http://zedshaw.com/about/).

To ensure completion I have entered into a blood pact with a friend doing likewise.

I attempt to write about this probably horrific experience with [GitHub Pages](https://pages.github.com/) and [Pelican](http://blog.getpelican.com/) at [http://richlearnspythonthehardway.org/](richlearnspythonthehardway.org).

## Installation

You can create a similar diary of trauma.

```
mkvirtualenv lpthw
git clone git@github.com:richardcornish/lpthw.git
pip install -r requirements.txt
```

Add and edit Markdown files in `pelican/content/`. Then generate them:

```
pelican pelican/content -o pelican/output -s pelican/pelicanconf.py
cd pelican/output/
python -m SimpleHTTPServer
```

Visit [http://0.0.0.0:8000/](http://0.0.0.0:8000/).

Now publish to the live Interwebs:

```
cd ../../
ghp-import pelican/output
git push origin gh-pages
```

Visit [http://richardcornish.github.io/lpthw/](http://richardcornish.github.io/lpthw/). Because Pelican uses absolute paths and GitHub Pages for projects uses relative paths, i.e. `lpthw/`, paths will break unless visiting the [pretty domain](http://richlearnspythonthehardway.org/).
