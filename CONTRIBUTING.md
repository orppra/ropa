# Contributing
Thanks for taking the time. To contribute, first fork this repository and clone it.

## Environment
You will need PyQt4 to run the program.
```
sudo apt install python-qt4
```

To install the rest of the dependencies, do
```
sudo pip install -r requirements.txt -r requirements-devel.txt
```

## Pull Request
### Make changes
Create a branch to make your changes.
```
git checkout -b branch-name
```

When you are done making changes, add the files to tracking.
```
git add .
```

### Commit
To write a commit.
```
git commit
```

The title of the commit should be in the following format:
```
<module affected>: <changes>
```

For example,
```
SearchService: Fix printing error
```

Then in the commit contents, elaborate on the change. In the end, the commit should look like the following:
```
SearchService: Fix printing error

Fix the error that is causing the printing to not work as intended.
```

The commit messages should be as descriptive as possible and each commit should not contain multiple unrelated changes.

### Pull Request
When you are done committing all changes, push them to github.
```
git push --set-upstream origin branch-name
```

On Github, in your forked repository, there will be a button to "Compare and Pull Request". 

In your pull request, adapt the format as mentioned for the commits, with a clear description what the pull request is doing. When satisfied, send the pull request.

## Testing
Before sending a pull request, make sure your code passes all the test cases. Run them by doing
```
./runtests.sh static
./runtests.sh unit
```
