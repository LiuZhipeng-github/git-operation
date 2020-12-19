# Git 操作

### 原子命令

$ git merge [branch]    将所选分支合并到当前分支（将有文件更新的分支更新到当前分支）

$ git push 提交主分支更新

$ git push --all 提交所有更新

$ git push --set-upstream origin test 提交分支更新

$git push origin :master     ==   git push origin --delete master 表示删除origin主机的master分支。

$ git tag version1.0.0 创建新版本号

$ git tag -d version1.0.0 删除版本号

$ git checkout [tagname] 切换到版本

$ git branch [branchname] 创建新本地分支

$ git branch -d [branchname] 删除本地分支

$ git checkout [branch] 切换到所选分支

### 组合命令

$ git checkout -b test3;git merge new;git push --all 

将有新内容的分支更新到新建分支并合并，最后上传

$ git add .;git commit -m 'up';git push --set-upstream origin new

提交本地分支的所有更新

$ git merge test3;git push --all;git checkout master;git push origin --delete test1 

将test3的新内容合并到当前分支，然后提交所有，然后切换到主分支并删除test1分支（注意：必须要先切换到主分支才可以删除远端分支，而且切换到主分支前必须commit所有修改）

$ git add .;git commit -m 'up';git tag version1.0.2;git push --all;git push origin --tag

