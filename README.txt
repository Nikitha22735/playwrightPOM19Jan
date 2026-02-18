

git commands:
1. git branch creation
2. git stash
3. git pull
4. git stash pop



fixture:


before and after Testcases





Reports:

1. HTML
2. ALLURE



total steps in CICD:

1. grabbing a lptop
2. python installation
3. git clone
4. download dependency (reqiuierments.txt)
5.playwright test execution
6. ALLURE Reports




//// explain your Project structure:
1.pages folder
2. Testcases Folder
3. we are using POM with pytest
4. each an every testcase we ahve to write in the form of "test_" even the testfil should strt with "test_"
5.we are using the testdata folder to stiore the testDta (json, csv, .env)
6.we he a conftest.py to store the fixtures
7.reequirements.txt to specify the plugins and versions
8. report using Allure
9. we are hosting CICD in GITHUB Atcions and to facilitate thatn we are using .yml file