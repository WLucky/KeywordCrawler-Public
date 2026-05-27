# Cookie 配置指南

## 快速开始

### 1. 复制模板文件

首先，将对应平台的 cookie 模板文件复制为真实的 cookie 文件：

```bash
# Windows (PowerShell)
copy config\cookies\bili_cookie.txt.example config\cookies\bili_cookie.txt
copy config\cookies\dy_cookie.txt.example config\cookies\dy_cookie.txt
copy config\cookies\ks_cookie.txt.example config\cookies\ks_cookie.txt
copy config\cookies\tieba_cookie.txt.example config\cookies\tieba_cookie.txt
copy config\cookies\wb_cookie.txt.example config\cookies\wb_cookie.txt
copy config\cookies\xhs_cookie.txt.example config\cookies\xhs_cookie.txt
copy config\cookies\zhihu_cookie.txt.example config\cookies\zhihu_cookie.txt
```

### 2. 编辑 Cookie 文件（重要！）

⚠️ **关键步骤：必须删除所有注释！**

1. 打开复制后的 `*_cookie.txt` 文件
2. **删除文件中的所有内容**（包括所有注释行）
3. **只粘贴你的 Cookie 字符串**，不要留任何注释
4. 保存文件

**正确的文件内容示例：**
```
buvid3=xxx; b_nut=xxx; SESSDATA=xxx; bili_jct=xxx; ...
```

**错误示例（不要这样）：**
```
# 这是注释
buvid3=xxx; b_nut=xxx; ...
```

### 3. 获取 Cookie

按照各模板文件中的说明，获取对应平台的 Cookie：
1. 打开浏览器，访问对应平台网站
2. 登录你的账号
3. 按 F12 打开开发者工具
4. 切换到 Network (网络) 标签
5. 刷新页面，任意选择一个请求
6. 在 Request Headers 中找到 Cookie，复制完整内容

### 4. 运行程序

现在你可以正常运行爬虫程序了！

---

## Git 仓库配置（双仓库方案）

### 仓库结构

- **公共仓库 (Public Repo)**：用于开源分享，不包含敏感信息
  - 包含：`*_cookie.txt.example` 模板文件
  - 不包含：`*_cookie.txt` 真实 cookie 文件

- **私有仓库 (Private Repo)**：用于个人开发，包含完整信息
  - 包含：所有文件（包括真实的 cookie 文件）

### 设置 Git Remote

```bash
# 1. 查看当前 remote
git remote -v

# 2. 添加公共仓库（如果还没有）
git remote add public https://github.com/你的用户名/你的公共仓库.git

# 3. 添加私有仓库
git remote add private https://github.com/你的用户名/你的私有仓库.git

# 4. 查看配置结果
git remote -v
```

### 日常开发工作流

```bash
# 在私有仓库开发
git checkout main
git add .
git commit -m "你的提交信息"
git push private main

# 同步到公共仓库（移除敏感信息后）
# 确保 cookie 文件已被 .gitignore 忽略
git push public main
```

### 从公共仓库拉取更新

```bash
# 拉取公共仓库的更新
git fetch public
git merge public/main

# 或者使用 rebase
git rebase public/main
```

---

## 安全说明

⚠️ **重要提示**：

1. **永远不要**将包含真实 Cookie 的文件提交到公共仓库
2. Cookie 包含你的登录凭证，泄露可能导致账号被盗
3. 定期更换 Cookie 以确保安全
4. 如果不小心泄露了 Cookie，请立即修改平台密码

---

## 故障排除

### Cookie 文件未生效？

- 确认文件命名正确：`{platform}_cookie.txt`
- 确认文件位于 `config/cookies/` 目录下
- 确认 Cookie 内容格式正确（完整的 Cookie 字符串）

### Git 仍然追踪 Cookie 文件？

- 确认 `.gitignore` 规则正确
- 如果文件已被追踪，使用以下命令移除：
  ```bash
  git rm --cached config/cookies/*_cookie.txt
  git commit -m "Remove sensitive cookie files from tracking"
  ```

