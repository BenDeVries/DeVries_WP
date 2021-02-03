Pandoc latex template to build to a CSCRS LaTeX styled file.

Installation
============

Easy
----

Just copy `cscrs.latex` and `cscrs.sty` (in the `latex` dir) to the same
directory as your document file.

Advanced
--------

Only do this if you know what you are doing.

Copy `cscrs.latex` to your `.pandoc/templates/` directory.

Usage
=====

Markdown
--------

For a markdown file to be converted to latex with pandoc, put at the top of
your markdown file:

    ---
    title: Title of document
    author: Author Name
    ---

    Content ...

Compile with:

    pandoc input_file.md --template cscrs -o outputfile.tex (or outputfile.pdf)

R-markdown
----------

For an R markdown file to be converted with the `render()` function, put in the
top of your R markdown file:

    ---
    title: Title of document
    author: Author Name
    output:
        pdf_document:
            template: cscrs
    ---

Additional options discussed in `latex/README.md` can be added with YAML
options (see below).  Compile with:

    > library(rmarkdown)
    > render("filename.Rmd")

Options
-------

See the LaTeX readme for details.  The following options in the YAML (between
the `---` can be supplied.

`titlepage: true` -- produce a title page (true or false)

`twosided: true` -- produce a two-sided style document (true or false)

`msucolors: true` -- Color headers, footers, etc in MSU themed colors (true or
false)

`client: Client Name` -- the client name

`director: Director Name` -- the director

`secondary: Worker Bee 1 and Worker Bee 2` -- Names of secondary authors

`date: \today` -- optional, sets date displayed on titlepage
