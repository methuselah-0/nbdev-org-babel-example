# An nbdev-org-babel example
> Literate Programming using nbdev, org-babel and emacs-jupyter


# An nbdev-org-babel example

> Literate Programming using nbdev, org-babel and emacs-jupyter

## Installation



See [this link](https://methuselah-0.github.io/nbdev-org-babel-example//) for the jekyll website documentation generated using
`nbdev_build_docs_from_org`.

There are currently (as of 2020-05-29) many unmentioned dependencies
in nbdev-org-babel, such as ox-ipynb, xq, moreutils (sponge) and
various emacs libraries. Checkout the bash script in the source code
in nbdev-org-babel, to figure those out if you are missing some. I
hope nbdev-org-babel gets rewritten in python and merged to fastai's
nbdev master in some distant future.

Install procedure(assuming you have dependencies installed):

`git clone https://github.com/methuselah-0/nbdev-org-babel.git`

`cd to nbdev-org-babel`

`pip install -e .`

`cd ~/src`

`nbdev_new my_new_project`

`cd my_new_project`

Edit the settings.ini file as you normally would with any nbdev project.

However, make sure that the following two settings correspond to the github repo name isntead of the defaults:

`doc_baseurl = /nbdev-org-babel-example/`

`git_url = https://github.com/%(user)s/nbdev-org-babel-example/tree/%(branch)s/`

create an index.org file in your `nbs_path` directory.

create a directory inside the `nbs_path` directory with the same name as `lib_name` (as defined in settings.ini)

create your literate program in `/path/to/repo_name/nbs_path/lib_name/my_project.org`

create index.org in `/path/to/repo_name/nbs_path/`.

Run `nbdev_install_git_hooks`.

Finally, run `nbdev_build_docs_from_org` which will create the needed
library and documentation for your project.

Note that if you don't want to run the whole procedure from org-files,
to ipynb files to building the docs, you can do for example
`nbdev_build_docs --force_all '*'` to just rebuild the html docs from
current ipynb files.

To see the results of the `.github/workflows/main.yml` CI-definition;
`Click Actions -> Click some commit-message -> Click Build in the left
pane -> Click the 3 dots in the upper right corner -> view raw logs`

If you are using some dependency packages, make sure to add those in
`settings.ini` under requirements, e.g. `requirements = scipy>=1.4.1
numpy>=1.18.4 matplotlib>=3.2.1`.

Also, see [how to setup console scripts](https://nbdev.fast.ai/tutorial/#Set-up-console-scripts), and [how to upload your project
to pypi](https://nbdev.fast.ai/tutorial/#Upload-to-pypi). However, you might find 2 problems out-of-the-box when
running `make release`. In the Makefile from the nbdev template
project, you may need to change `python3 setup.py sdist bdist_wheel`
to `python3 set...`. Secondly, you may need to install the wheel
and twine packages: `pip install wheel`.



## Emacs Python Setup Suggestions



List of stuff that is useful for Python LP-programming in emacs:

-   repl: interactively exploring and testing code (emacs-jupyter)
-   version control (git)
-   automatic check for the code's adherence to best practices and
    syntax highlighting (flycheck-pycheckers)
-   debugging, debugger (real-gud)
-   code definition lookup (emacs-jupyter, ag)
-   docs-generation (org-babel, nbdev, pandoc)
-   code generation & completion (yasnippet, jedi)


