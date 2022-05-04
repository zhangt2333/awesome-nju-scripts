# Awesome-NJU-Scripts

Some scripts about the life at NJU. 与 NJU 日常相关的一些脚本，如校园网登录脚本、自动健康填报、选课助手等，欢迎研究、使用、贡献 :smile:


# 目录

* [Latest](#latest)
   * [校园网登录脚本 nju-network-login-script](#校园网登录脚本-nju-network-login-script)
   * [研究生选课脚本 graduate-student-course-selector](#研究生选课脚本-graduate-student-course-selector)
* [Archived](#archived)
  * [自动健康填报 actions-NjuHealthReport](#自动健康填报-actions-njuhealthreport)
* [Contribution](#contribution)
* [License](#license)

# Latest

## 校园网登录脚本 `nju-network-login-script`

* 原理 —— 使用 curl 发送 HTTP 请求进行校园网认证：
  ```
  # 登录
  curl http://p.nju.edu.cn/portal_io/login -X POST -d "username=学号&password=密码"
  # 登出
  curl http://p.nju.edu.cn/portal_io/logout -X GET
  ```

* [该校园网登录 shell 脚本](nju-network-login-script/njunet.sh)，适用于 Linux/macOS 系统，主要提供对输入密码时的隐藏回显（如果不需要则上面 2 行命令可以满足你的上网需求），样例如下：
  
  ```bash
  $ bash njunet.sh
  Enter NJU ID:                        
  12345678                # 输入的学号会回显
  Enter password:         # 在这里输入密码不会回显或被记到命令行历史记录
  {"reply_code":1,"reply_msg":"登陆成功!","request_uri":"/portal_io/login","request_time":1651673862}
  ```
  
* 具体使用方式：
  ```
  # 下载
  curl https://raw.githubusercontent.com/zhangt2333/awesome-nju-scripts/main/nju-network-login-script/njunet.sh -o njunet.sh
  
  # 登录校园网，以下三种方式任选其一
  bash njunet.sh
  bash njunet.sh -u 学号
  bash njunet.sh -u 学号 -p 密码
  
  # 登出校园网
  bash njunet.sh logout
  ```

## 研究生选课脚本 `graduate-student-course-selector`

* NJU 研究生选课脚本


# Archived

## 自动健康填报 `actions-NjuHealthReport`
<details>
<summary>由于作者已润，该脚本 archived!，点击查看旧描述</summary>

* 自动进行每日健康填报
* 不需要自己购买服务器，也不需要自己配置服务器，真的 Serverless !!

</details>


# Contribution

本仓库旨在收集使得 NJU 生活更美好的一些脚本，如果有意被收录到本仓库，请提交 Issue 或 PR 参与贡献！

Looking forward to your contribution!

# License

MIT License: 
> 被授权人有权利在软件和软件的所有副本中包含版权声明和许可声明的前提下，使用、复制、修改、合并、出版发行、散布、再授权及贩售软件及软件的副本。授权人不为被授权人行为承担任何责任，且无义务对著作进行更新。
