### GitHub创建仓库及上传文件

#### 1、创建仓库

登录GitHub --->点击 +  --->New repository  ---> 命名，选择 public，勾选 readme   --->点击 Create repository   创建完成

#### 2、创建本地文件夹

点击创建的仓库  --->  Clone Or Download    ---> 保存连接

打开 git 命令行，输入 git clone [仓库链接]      本地仓库文件夹就创建好了

#### 3、推送

进入 本地仓库文件夹： cd [文件夹]   

将要上传的文件放到本地仓库文件夹

git status     可查看文件状态，红色为本地文件，绿色为暂存文件

git add [文件名]   将本地文件暂存       [git reset [文件名]]  取消暂存

git commit -m [信息]     提交文件，并添加一段备注信息

git push origin master    将文件推送到中央代码库

#### 4、拉取

git pull origin master    如果中央代码库的文件新于本地文件，使用此代码可更新本地代码库

