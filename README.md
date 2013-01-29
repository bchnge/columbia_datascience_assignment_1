homework\_1p5
=============

**Due:** Wednesday Feb 6, 6pm.  No commits after this time will be counted.

To receive full credit, you must commit and push code that passes all unit tests.

---

Description
-----------

For this homework you will write a very simple module that will
read in a file and calculate some basic stats from two columns of data.
You will have your first experience with collaborative work via git and
the issues potentially encountered therein is part of the challenge. It
will be up to you to split up the work, but we suggest a natural
structure of writing one function from the ones below per team member.


To see how things *should* work, look at `src/main.py` and `tests/testscripts.py`.  Since these modules import modules from directories that are not in `cwd` or `PATH`, you must modify the variable `PYTHONPATH`.  Do this by adding (to your *.bashrc* or *.bash_profile*)

    export PYTHONPATH=path-to-directory-above-homework_1p5:$PYTHONPATH

Then source it, i.e. once you have added the above line to your .bashrc
or .bash_profile file you will need to type "source ~/.bashrc" or
"source ~/.bash_profile" in the terminal shell.  You can also just close that
terminal and open a new one.

---

src/
---

**main.py**

Top level function, runs everything.  To run:

    $ cd src
    $ python main.py

**averager.py**

Function takes a file path, reads in the data, and returns the average of
the data points.

**maximum.py**

Function takes a file path, reads in the data, and returns the maximum of
the data points.

**minimum.py**

Function takes a file path, reads in the data, and returns the minimum of
the data points.


**summer.py**

Function takes a file path, reads in the data, and returns the sum of
the data points.

**data_length.py**

Function takes a file path, reads in the data, and returns the number of
the data points.


---

tests/
------

You will be graded on passing these tests.  You should also run these
tests as soon as you have completed writing the code.  To run them, you
must first edit the second line in `tests/testscripts.py`.  It currently
reads

    from homework_1p5.src import averager, maximum,\

The `homework_1p5` should be changed to the name of your repo, which is
something like `homework_1p5_team_XX`.  After doing that,

    $ cd tests
    $ python -m unittest -v testscripts

You should see output telling you that 5 tests were run and all failed.

---



IMPORTANT!
----------


Make sure that each member of the team commits and pushes the changes to
github. If at the end you run the tests locally and all is fine but you
have failed to push the latest changes to the repo we will not see
them... 


