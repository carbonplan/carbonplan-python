There are a variety of other projects related to carbonplan-python that are often co-released.  You may want to check their status while releasing.

Release per project:

*   Commit

        git commit -a -m "bump version to x.x.x"

*   Tag commit

        git tag -a x.x.x -m 'Version x.x.x'

*   Push to GitHub

        git push ${remote} main --tags

*   Upload to PyPI

        git clean -xfd
        python setup.py sdist bdist_wheel
        twine upload dist/*

*   Update JupyterHub / Docker images to pull new releases
