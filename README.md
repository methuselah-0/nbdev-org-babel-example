# An nbdev-org-babel example
> Literate Programming using nbdev, org-babel and emacs-jupyter


# An nbdev-org-babel example

> Literate Programming using nbdev, org-babel and emacs-jupyter

## Installation



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

create an index.org file in your nbs<sub>path</sub> directory.

create a directory inside the `nbs_path` directory with the same name as `lib_name` (as defined in settings.ini)

create your literate program in `~/src/nbs_path/lib_name/my_project.org`

Finally, run `nbdev_build_docs_from_org` which will create the needed
library and documentation for your project.


