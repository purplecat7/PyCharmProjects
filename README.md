# PyCharmProjects


To add an independent repository:
- go to repo "cadets"
- move everything (incl .gitignore) to a sub-directory "cadets/LibSys2017_cadets"
- commit (Prepare cadets LibSys for merge into PyCharmProjects)
- in repo "PyCharmProjects"
- git remote add cadets ../cadets
- git fetch cadets
- git merge cadets/master --allow-unrelated-histories
- commit (Merge remote-tracking branch 'cadets/master' (L2 2017))
- check for various __init__.py files creeping in
- move the newly created folder to the right place (and rename if necessary)
- commit & push
