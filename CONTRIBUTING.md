Below are the different branches of the project:
- The Master Branch: The main branch of the deliverable that will be immediately deployed for ongoing production. Each update to the master branch implies that there is a new version of the application to deploy to production.
- The development branch: All development of the application is done in this branch until the next stable version of the software is obtained and merged with the master branch.
- Each developer creates his own development branch from the development branch. All developers merge their work on the development branch.
- Patch branch: branch for bug fixing. After correction, the work is merged with the master branch and a new version is automatically released.
We will use unittest for python tests and Jest for javascript tests.


do
```
git clone https://github.com/HamaBarhamou/Melonie-Electronix
git fetch origin // retrieve all project branches
git branch - a // list all branches
git checkout -b development origin/development  // Create a copy of the development branch in local
git checkout development
git checkout -b your_name  // Create your development branch from the development branch
// make your contribution and then
git add .   
git commit -m 'message commit'  
git push    
git chechout development
git merge your_name
git push
```

**NB: do not push on the branch master**  