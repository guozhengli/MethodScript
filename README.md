## 说明
### 方法脚本，存放一些个人日常用到的或者用不到的一些方法。不限制语言。
## 格式
### 引用标签
* 作用： 在根下填写label文件，里面存入各方法及功能目录(类似于书籍的目录)
* 存储格式(按阶写入) 比如command命令
* # Python
* #   -- command 系统调用内置函数
### 第一层包 为语言包 比如 python、Golang、Django、VUE等
### 第二层包 为方法包 方法包可分为
#### 1、项目方法 --- 如果是整体项目 则 需要写入项目的名称、路径 以及作用和使用方法 例：
* # 项目：MethodScript
* # 项目路径： /Users/ligz01/share/MethodScript
* # 作用：此项目只作为 方法笔记存储 可看可跑可运行 即是它的目的
* # 使用方法：
  # 测试脚本 引用标签 python print
  python /Users/ligz01/share/MethodScript/Python/test.py
#### 2、内部调用方法 ---- 将建立包目录为其根目录
* # 功能：测试
* # 根目录：项目起始目录 Python/Test  说明：Python是第一层语言包 Test为该功能的根目录
* # 使用方法：
  # 运行： cd /Users/ligz01/share/MethodScript/Python/Test;python main.py
#### 3、类或个别实现方法 ---- 建立相关的语言后缀文件
* # 功能：command的使用
* # 使用方法：
  # cd /Users/ligz01/share/MethodScript/Python/; python command_script.py
### 第三层即文件内部填写说明(说明应写在文件的开头或者项目的README.md中) 格式如下
* # python 3.6
* # 编辑日期：2019/02/25
* # 功能：测试print
* # 依赖包：python
* # 执行方法： python script.py
## 分支说明
### master分支为所有语言包的整体分支，只一大节写完后才可以合并到master分支上(一大节指有各小项目的必须项目说明功能等都完善了不在变更了)
### 其他分支为各语言名称以及测试分支(什么都可以写就是测试用的临时分支)
