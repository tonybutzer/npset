# npset
Repo to do detailed analysis of National Park Service ET Code for the AWS cloud.


"""
October 2018
Gridded Cloud Water Balance Model Version 2: Incorporating Senay et al. NDVI method of calcula
ting AET and Jennings et al. 2018 T50 coefficients for estimating snow.
The previous model version used Daymet snow estimates rather than estimating snow.
"""

git reset HEAD~

git reset --hard


git status

After this, you should see something along the lines of

On branch master
Your branch is ahead of 'origin/master' by 2 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

The important part is the "2 commits"! From here, go ahead and type in:

git reset HEAD~<HOWEVER MANY COMMITS YOU WERE BEHIND>

So, for the example above, one would type:

git reset HEAD~2

After you typed that, your "git status" should say:

On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree

