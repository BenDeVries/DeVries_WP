# MS Statistics Writing Project Template

This repository contains both an RMD and a Latex template for formatting a writing project required
for completion of a Masters of Science in Statistics at Montana State University.
Files include:

- abstract.tex - Your abstract.
- WPROJ.sty - Style file contains packages, formatting, new commands, and
your cover sheet information (your name, your advisor's name, your title,
date of completion, and name of current writing project coordinator).
Add any other needed packages or new commands to this file.
- coversheet.tex - Creates cover sheet for writing project document. You
will not need to edit this file.
- main_LATEX.tex - Latex file to combine individual sections to create your document.
Compile this file to produce a pdf of your entire document. Names of sections
should match names of .tex files in "body" folder
- main_RMD.tex - RMD file that contains the ability to combine individual latex sections or write code / text directly in RMD.
Compile this file to produce a pdf of your entire document. When using latex sections, names of sections should match names of .tex files in "body" folder
- references.bib - BibTeX file of your references. 
- body folder - .tex files of each section
- figures folder - all figures included in your document


## Recommendations and Resources

### Version Control
Create a GitHub repository for your writing project
and share this with your Advisor. You will need to install
[Git](https://git-scm.com/downloads) on your computer, and create a [GitHub](https://github.com/) account.
Though I recommend learning to use Git via the command line,
[Sourcetree](https://www.sourcetreeapp.com/) or [GitHub Desktop](https://desktop.github.com/)
are tools that facilitate communication between Git and GitHub.

- [How to set up Git on your computer](https://help.github.com/en/github/getting-started-with-github/set-up-git#setting-up-git)
- [General GitHub documentation](https://help.github.com/en/github)
- [Udacity's Version Control with Git free online course](https://www.udacity.com/course/version-control-with-git--ud123)

### Reference Manager
I recommend using
[Zotero](https://www.zotero.org/) to manage your references. Zotero allows you to create a group,
which means you can share your references with your Advisor and Committee.
Zotero has an addin for Chrome and other web browsers to scrape any citation
information from a website, and you can export all of your references
from Zotero into a BibTex file.

### LaTeX and BibTeX References
- [The Not So Short Introduction to LaTeX](http://mirrors.rit.edu/CTAN/info/lshort/english/lshort.pdf)
- [natbib Reference Sheet](https://gking.harvard.edu/files/natnotes2.pdf)
- [More details on using the natbib package](https://gking.harvard.edu/files/natbib2.pdf)
