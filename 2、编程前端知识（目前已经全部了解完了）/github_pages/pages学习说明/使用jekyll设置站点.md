# 关于 GitHub 页面和 Jekyll

Jekyll 是一个静态站点生成器，内置 GitHub Pages 支持。

## 关于 Jekyll 

**Jekyll 是一个静态站点生成器**，内置 GitHub Pages 支持和简化的构建过程。 Jekyll 使用 Markdown 和 HTML 文件，并根据您选择的布局创建完整静态网站。 Jekyll 支持 Markdown 和 Lick，这是一种可在网站上加载动态内容的模板语言。 有关详细信息，请参阅 [Jekyll](https://jekyllrb.com/)。

Windows 并未正式支持 Jekyll。 有关详细信息，请参阅 Jekyll 文档中的“[Windows 上的 Jekyll](http://jekyllrb.com/docs/windows/#installation)”。

我们建议将 Jekyll 用于 GitHub Pages。 如果您喜欢，可以使用其他静态站点生成器或者在本地或其他服务器上自定义构建过程。 有关详细信息，请参阅“[关于 GitHub Pages](https://docs.github.com/zh/pages/getting-started-with-github-pages/about-github-pages#static-site-generators)”。

## 在 GitHub Pages 网站中配置 Jekyll 

可以通过编辑 **_config.yml 文件来配置大多数 Jekyll 设置，例如站点的主题和插件**。 有关详细信息，请参阅 Jekyll 文档中的“[配置](https://jekyllrb.com/docs/configuration/)”。

对于 GitHub Pages 站点，有些配置设置不能更改。

```yaml
lsi: false
safe: true
source: [your repo's top level directory]
incremental: false
highlighter: rouge
gist:
  noscript: false
kramdown:
  math_engine: mathjax
  syntax_highlighter: rouge
```

默认情况下，Jekyll 不会构建以下文件或文件夹：

- 位于名为 `/node_modules` 或 `/vendor` 的文件夹中
- 以 `_`、`.` 或 `#` 开头
- 以 `~` 结尾
- 被配置文件中的 `exclude` 设置排除

如果**想要 Jekyll 处理其中任何文件，可以使用配置文件中的 `include` 设置。**

## 前页附属资料 

要为网站上的页面或帖子设置变量和元数据，例如标题和布局， 您可以将 YAML 前页添加到任意 Markdown 或 HTML 文件的顶部。 有关详细信息，请参阅 Jekyll 文档中的“[前页](https://jekyllrb.com/docs/front-matter/)”。

可以添加 `site.github` 到帖子或页面，以将任何存储库引用元数据添加到站点。 有关详细信息，请参阅 Jekyll 元数据文档中的“[使用 `site.github`](https://jekyll.github.io/github-metadata/site.github/)”。

## 主题 

您可以将 Jekyll 主题添加到 GitHub Pages 站点，以自定义站点的外观。 有关详细信息，请参阅 Jekyll 文档中的“[主题](https://jekyllrb.com/docs/themes/)”。

可以在 GitHub 上添加支持的主题到站点。 有关详细信息，请参阅 GitHub Pages 站点中的“[支持的主题](https://pages.github.com/themes/)”，以及“[使用 Jekyll 向 GitHub Pages 站点添加主题](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/adding-a-theme-to-your-github-pages-site-using-jekyll)”。

要使用 GitHub 上托管的任何其他开放源代码 Jekyll 主题，可以手动添加主题。有关详细信息，请参阅 [GitHub 上托管的主题](https://github.com/topics/jekyll-theme)，“[使用 Jekyll 向 GitHub Pages 站点添加主题](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/adding-a-theme-to-your-github-pages-site-using-jekyll)”。

您可以通过编辑主题文件来覆盖任何主题的默认值。 有关详细信息，请参阅主题文档和 Jekyll 文档中的“[替代主题的默认值](https://jekyllrb.com/docs/themes/#overriding-theme-defaults)”。

## 插件 

您可以下载或创建 Jekyll 插件，以便为您的网站扩展 Jekyll 的功能。 例如，通过 [jemoji](https://github.com/jekyll/jemoji) 插件，可在站点的任何页面上使用 GitHub 风格的表情符号，就像在 GitHub 上使用一样。 有关详细信息，请参阅 Jekyll 文档中的“[插件](https://jekyllrb.com/docs/plugins/)”。

GitHub Pages 使用默认启用且不能禁用的插件：

- [`jekyll-coffeescript`](https://github.com/jekyll/jekyll-coffeescript)
- [`jekyll-default-layout`](https://github.com/benbalter/jekyll-default-layout)
- [`jekyll-gist`](https://github.com/jekyll/jekyll-gist)
- [`jekyll-github-metadata`](https://github.com/jekyll/github-metadata)
- [`jekyll-optional-front-matter`](https://github.com/benbalter/jekyll-optional-front-matter)
- [`jekyll-paginate`](https://github.com/jekyll/jekyll-paginate)
- [`jekyll-readme-index`](https://github.com/benbalter/jekyll-readme-index)
- [`jekyll-titles-from-headings`](https://github.com/benbalter/jekyll-titles-from-headings)
- [`jekyll-relative-links`](https://github.com/benbalter/jekyll-relative-links)

可以通过将插件的 gem 添加到 _config.yml 文件中的 `plugins` 设置来启用其他插件。 有关详细信息，请参阅 Jekyll 文档中的“[配置](https://jekyllrb.com/docs/configuration/)”。

有关受支持的插件列表，请参阅 GitHub Pages 站点上的“[依赖项版本](https://pages.github.com/versions/)”。 有关特定插件的使用信息，请参阅插件的文档。

提示：可以保持更新 GitHub Pages gem，确保使用所有插件的最新版本。 有关详细信息，请参阅 GitHub Pages 站点上的“[使用 Jekyll 在本地测试 GitHub Pages 站点](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll#updating-the-github-pages-gem)”和“[依赖项版本](https://pages.github.com/versions/)”。

GitHub Pages 无法使用不支持的插件构建网站。 如果想使用不支持的插件，请在本地生成网站，然后将网站的静态文件推送到 GitHub。

## 语法突出显示

为了使网站更容易读取，代码片段在 GitHub Pages 上突显，就像在 GitHub 上突显一样。 有关如何在 GitHub 上高亮显示语法的详细信息，请参阅“[创建和突显代码块](https://docs.github.com/zh/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks)”。

默认情况下，网站上的代码块将被 Jekyll 突出显示。 Jekyll 使用与 [Pygments](https://github.com/jneen/rouge) 兼容的 [Rouge](http://pygments.org/) 突显工具。 Pygments 已被弃用，在 Jekyll 4 中不受支持。 如果在 _config.yml 文件中指定 Pygments，则 Rouge 将用作后备。 Jekyll 不能使用任何其他语法突显工具，如果你在 _config.yml 文件中指定其他语法突显工具，你将收到页面生成警告。 有关详细信息，请参阅“[关于 GitHub Pages 站点的 Jekyll 构建错误](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/about-jekyll-build-errors-for-github-pages-sites)”。

如果想使用其他突显工具，如 `highlight.js`，则必须更新项目的 _config.yml 文件来禁用 Jekyll 的语法突出显示。

```yaml
kramdown:
  syntax_highlighter_opts:
    disable : true
```

如果主题不含用于语法突出显示的 CSS，可以生成 GitHub 的语法突出显示 CSS 并将其添加到项目的 `style.css` 文件。

```shell
$ rougify style github > style.css
```

## 本地构建网站

如果从分支进行发布，则将更改合并到站点的发布源时，会自动发布对站点的更改。 如果从自定义 GitHub Actions 工作流进行发布，则触发工作流（通常通过推送到默认分支）时会发布更改。 如果想先预览你的更改，可以在本地而不是 GitHub 上进行更改。 然后在本地测试站点。 有关详细信息，请参阅“[使用 Jekyll 在本地测试 GitHub Pages 站点](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll)”。







# 使用 Jekyll 创建 GitHub Pages 站点

## 本文内容

- 先决条件
- 为站点创建仓库
- 创建站点
- 后续步骤

您可以使用 Jekyll 在新仓库或现有仓库中创建 GitHub Pages 站点。

谁可以使用此功能

People with admin permissions for a repository can create a GitHub Pages site with Jekyll.

[Mac](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll?platform=mac)[Windows](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll?platform=windows)[Linux](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll?platform=linux)

GitHub Pages 适用于具有 GitHub Free 和组织的 GitHub Free 的公共仓库，以及具有 GitHub Pro、GitHub Team、GitHub Enterprise Cloud 和 GitHub Enterprise Server 的公共和私有仓库。 有关详细信息，请参阅“[GitHub 的产品](https://docs.github.com/zh/get-started/learning-about-github/githubs-products)”。

**注意：** 组织所有者可以限制从组织拥有的存储库发布 GitHub Pages 站点。 有关详细信息，请参阅“[管理组织的 GitHub Pages 站点发布](https://docs.github.com/zh/organizations/managing-organization-settings/managing-the-publication-of-github-pages-sites-for-your-organization)”。

## [先决条件](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll#prerequisites)

必须安装 Jekyll 和 Git 后才可使用 Jekyll 创建 GitHub Pages 站点。 有关详细信息，请参阅 Jekyll 文档中的[安装](https://jekyllrb.com/docs/installation/)和“[设置 Git](https://docs.github.com/zh/get-started/quickstart/set-up-git)”。

建议使用 [Bundler](http://bundler.io/) 安装和运行 Jekyll。 Bundler 可管理 Ruby gem 依赖项，减少 Jekyll 构建错误和阻止环境相关的漏洞。 要安装 Bundler：

1. 安装 Ruby。 有关详细信息，请参阅 Ruby 文档中的“[安装 Ruby](https://www.ruby-lang.org/en/documentation/installation/)”。
2. 安装 Bundler。 有关详细信息，请参阅“[Bundler](https://bundler.io/)”。

## [为站点创建仓库](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll#creating-a-repository-for-your-site)

可以为站点创建存储库或选择现有存储库。

如果存储库中并非所有文件都与站点相关，且要为存储库创建 GitHub Pages 站点，则能够为站点配置发布源。 例如，可以使用专用分支和文件夹保存站点源文件，也可以使用自定义 GitHub Actions 工作流来生成和部署站点源文件。

如果拥有存储库的帐户使用组织的 GitHub Free 或 GitHub Free，存储库必须是公共的。

如果要在现有存储库中创建站点，请跳至“[创建站点](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll#creating-your-site)”一节。

1. 在任何页面的右上角，使用 下拉菜单选择“新建存储库”。![包含创建新存储库选项的下拉菜单](%E4%BD%BF%E7%94%A8jekyll%E8%AE%BE%E7%BD%AE%E7%AB%99%E7%82%B9.assets/repo-create.png)1. 使用“所有者”下拉菜单选择你想要拥有存储库的帐户。![“所有者”下拉菜单](%E4%BD%BF%E7%94%A8jekyll%E8%AE%BE%E7%BD%AE%E7%AB%99%E7%82%B9.assets/create-repository-owner.png)1. 输入仓库的名称和说明（可选）。 如果要创建用户或组织站点，则存储库必须命名为 `<user>.github.io` 或 `<organization>.github.io`。 如果您的用户或组织名称包含大写字母，您必须小写字母。 有关详细信息，请参阅“[关于 GitHub Pages](https://docs.github.com/zh/pages/getting-started-with-github-pages/about-github-pages#types-of-github-pages-sites)”。![创建存储库字段](%E4%BD%BF%E7%94%A8jekyll%E8%AE%BE%E7%BD%AE%E7%AB%99%E7%82%B9.assets/create-repository-name-pages.png)1. 选择仓库可见性。 有关详细信息，请参阅“[关于仓库](https://docs.github.com/zh/repositories/creating-and-managing-repositories/about-repositories#about-repository-visibility)”。![用于选择存储库可见性的单选按钮](%E4%BD%BF%E7%94%A8jekyll%E8%AE%BE%E7%BD%AE%E7%AB%99%E7%82%B9.assets/create-repository-public-private.png)

## [创建站点](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll#creating-your-site)

必须先在 GitHub 上有站点的仓库，然后才可创建站点。 如果未在现有存储库中创建站点，请参阅“[为站点创建存储库](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll#creating-a-repository-for-your-site)”。

警告：GitHub Pages 站点可以在 Internet 上公开，即使该站点的存储库是私有的。 如果站点的存储库中有敏感数据，你可能想要在发布前删除数据。 有关详细信息，请参阅“[关于仓库](https://docs.github.com/zh/repositories/creating-and-managing-repositories/about-repositories#about-repository-visibility)”。

1. 打开Git Bash。

2. 如果还没有本地版存储，请导航到想要存储站点源文件的位置，将 PARENT-FOLDER 替换为要包含存储库文件夹的文件夹。

   ```shell
   $ cd PARENT-FOLDER
   ```

3. 如果尚未初始化本地 Git 存储库，请将 REPOSITORY-NAME 替换为存储库名称。

   ```shell
   $ git init REPOSITORY-NAME
   > Initialized empty Git repository in /Users/octocat/my-site/.git/
   # Creates a new folder on your computer, initialized as a Git repository
   ```

4. 将目录更改为仓库。

   ```shell
   $ cd REPOSITORY-NAME
   # Changes the working directory
   ```

5. 确定要使用的发布源。 有关详细信息，请参阅“[配置 GitHub Pages 站点的发布源](https://docs.github.com/zh/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)”。 1. 导航到站点的发布来源。 有关详细信息，请参阅“[配置 GitHub Pages 站点的发布源](https://docs.github.com/zh/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)”。 例如，如果选择从默认分支上的 `docs` 文件夹发布站点，请创建目录并将目录更改为 `docs` 文件夹。

   ```shell
   $ mkdir docs
   # Creates a new folder called docs
   $ cd docs
   ```

   如果选择从 `gh-pages` 分支发布站点，请创建并签出 `gh-pages` 分支。

   ```shell
   $ git checkout --orphan gh-pages
   # Creates a new branch, with no history or contents, called gh-pages, and switches to the gh-pages branch
   $ git rm -rf .
   # Removes the contents from your default branch from the working directory
   ```

6. 若要创建新 Jekyll 站点，请使用 `jekyll new` 命令：

   ```shell
   $ jekyll new --skip-bundle .
   # Creates a Jekyll site in the current directory
   ```

7. 打开 Jekyll 创建的 Gemfile 文件。

8. 将“#”添加到以 `gem "jekyll"` 开头的行首，以注释禁止此行。

9. 编辑以 `# gem "github-pages"` 开头的行，以添加 `github-pages` gem。 将此行更改为：

   ```shell
   gem "github-pages", "~> GITHUB-PAGES-VERSION", group: :jekyll_plugins
   ```

   将 GITHUB-PAGES-VERSION 替换为 `github-pages` gem 的最新支持版本。 可以在以下位置找到这个版本：“[依赖项版本](https://pages.github.com/versions/)”。

   正确版本的 Jekyll 将安装为 `github-pages` gem 的依赖项。

10. 保存并关闭 Gemfile。

11. 从命令行中，运行 `bundle install`。

12. （可选）对 `_config.yml` 文件进行任何必要的编辑。 当仓库托管在子目录时相对路径需要此设置。 有关详细信息，请参阅“[将子文件夹拆分成新仓库](https://docs.github.com/zh/get-started/using-git/splitting-a-subfolder-out-into-a-new-repository)”。

    ```yml
    domain: my-site.github.io       # if you want to force HTTPS, specify the domain without the http at the start, e.g. example.com
    url: https://my-site.github.io  # the base hostname and protocol for your site, e.g. http://example.com
    baseurl: /REPOSITORY-NAME/      # place folder name if the site is served in a subfolder
    ```

13. （可选）在本地测试您的站点。 有关详细信息，请参阅“[使用 Jekyll 在本地测试 GitHub Pages 站点](https://docs.github.com/zh/articles/testing-your-github-pages-site-locally-with-jekyll)”。

14. 添加并提交您的工作。

    ```shell
    git add .
    git commit -m 'Initial GitHub pages site with Jekyll'
    ```

15. 将 GitHub.com 上的存储库添加为远程存储库，将 将 USER 替换为拥有该存储库的帐户并将 REPOSITORY 替换为存储库名称 。

    ```shell
    $ git remote add origin https://github.com/USER/REPOSITORY.git
    ```

16. 将存储库推送到 GitHub，将 BRANCH 替换为所操作的分支的名称。

    ```shell
    $ git push -u origin BRANCH
    ```

17. 配置发布源。 有关详细信息，请参阅“[配置 GitHub Pages 站点的发布源](https://docs.github.com/zh/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)”。 1. 在 GitHub 上，导航到站点的仓库。 1. 在存储库名称下，单击 “设置”。 如果看不到“设置”选项卡，请选择 下拉菜单，然后单击“设置” 。

    ![存储库标头的屏幕截图，其中显示了选项卡。 “设置”选项卡以深橙色边框突出显示。](%E4%BD%BF%E7%94%A8jekyll%E8%AE%BE%E7%BD%AE%E7%AB%99%E7%82%B9.assets/repo-actions-settings.png)

18. 在边栏的“代码和自动化”部分，单击“ 页面”。

19. 若要查看已发布的网站，请在“GitHub Pages”下单击“ 访问网站”。![GitHub Pages 确认消息的屏幕截图，其中列出了站点的 URL。 在 URL 右侧，标有“访问网站”的按钮用深橙色框出。](%E4%BD%BF%E7%94%A8jekyll%E8%AE%BE%E7%BD%AE%E7%AB%99%E7%82%B9.assets/click-pages-url-to-preview.png)

    **注意：** 对站点的更改在推送到 GitHub 后，最长可能需要 10 分钟才会发布。 如果一小时后仍然在浏览器中看不到 GitHub Pages 站点更改，请参阅“[关于 GitHub Pages 站点的 Jekyll 构建错误](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/about-jekyll-build-errors-for-github-pages-sites)”。

20. GitHub Pages 站点是使用 GitHub Actions 工作流生成和部署的。 有关详细信息，请参阅“[查看工作流程运行历史记录](https://docs.github.com/zh/actions/monitoring-and-troubleshooting-workflows/viewing-workflow-run-history)”。

    注意：公共存储库免费使用 GitHub Actions。 如果专用存储库和内部存储库超出每月分配的免费分钟数，则会收取使用费。 有关详细信息，请参阅“[使用限制、计费和管理](https://docs.github.com/zh/actions/learn-github-actions/usage-limits-billing-and-administration)”。

**注意**：如果从分支进行发布且站点尚未自动发布，请确保具有管理员权限和经验证的电子邮件地址的人员已将站点推送到发布源。

## [后续步骤](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll#next-steps)

若要向网站添加新页面或帖子，请参阅“[使用 Jekyll 向 GitHub Pages 站点添加内容](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/adding-content-to-your-github-pages-site-using-jekyll)”。

您可以将 Jekyll 主题添加到 GitHub Pages 站点，以自定义站点的外观。有关详细信息，请参阅“[使用 Jekyll 向 GitHub Pages 站点添加主题](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/adding-a-theme-to-your-github-pages-site-using-jekyll)”。



# 使用 Jekyll 在本地测试 GitHub Pages 站点

## 本文内容

- 先决条件
- 本地构建网站
- 更新 GitHub Pages gem
- 延伸阅读

您可以在本地构建 GitHub Pages 站点，以预览和测试对站点的更改。

[Mac](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll?platform=mac)[Windows](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll?platform=windows)[Linux](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll?platform=linux)

GitHub Pages 适用于具有 GitHub Free 和组织的 GitHub Free 的公共仓库，以及具有 GitHub Pro、GitHub Team、GitHub Enterprise Cloud 和 GitHub Enterprise Server 的公共和私有仓库。 有关详细信息，请参阅“[GitHub 的产品](https://docs.github.com/zh/get-started/learning-about-github/githubs-products)”。

任何拥有仓库读取权限的人都可以在本地测试 GitHub Pages 站点。

## [先决条件](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll#prerequisites)

在使用 Jekyll 测试站点之前，您必须：

- 安装 [Jekyll](https://jekyllrb.com/docs/installation/)
- 创建一个 Jekyll 站点。 有关详细信息，请参阅“[使用 Jekyll 创建 GitHub Pages 站点](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll)”。

建议使用 [Bundler](http://bundler.io/) 安装和运行 Jekyll。 Bundler 可管理 Ruby gem 依赖项，减少 Jekyll 构建错误和阻止环境相关的漏洞。 要安装 Bundler：

1. 安装 Ruby。 有关详细信息，请参阅 Ruby 文档中的“[安装 Ruby](https://www.ruby-lang.org/en/documentation/installation/)”。
2. 安装 Bundler。 有关详细信息，请参阅“[Bundler](https://bundler.io/)”。

## [本地构建网站](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll#building-your-site-locally)

1. 打开Git Bash。 1. 导航到站点的发布来源。 有关详细信息，请参阅“[配置 GitHub Pages 站点的发布源](https://docs.github.com/zh/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)”。

2. 运行 `bundle install`。

3. 在本地运行您的 Jekyll 站点。

   ```shell
   $ bundle exec jekyll serve
   > Configuration file: /Users/octocat/my-site/_config.yml
   >            Source: /Users/octocat/my-site
   >       Destination: /Users/octocat/my-site/_site
   > Incremental build: disabled. Enable with --incremental
   >      Generating...
   >                    done in 0.309 seconds.
   > Auto-regeneration: enabled for '/Users/octocat/my-site'
   > Configuration file: /Users/octocat/my-site/_config.yml
   >    Server address: http://127.0.0.1:4000/
   >  Server running... press ctrl-c to stop.
   ```

   注意：如果已安装 Ruby 3.0 或更高版本（如果通过 Homebrew 安装了默认版本，则表示可能已经安装），你可能会在此步骤中遇到错误。 这是因为这些版本的 Ruby 不再附带安装 `webrick`。

   要修复错误，请尝试运行 `bundle add webrick`，然后重新运行 `bundle exec jekyll serve`。

4. 若要预览网站，请在 Web 浏览器中导航到 `http://localhost:4000`。

## [更新 GitHub Pages gem](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll#更新-github-pages-gem)

Jekyll 是一个活跃的开源项目，经常更新。 如果计算机上的 `github-pages` gem 与 GitHub Pages 服务器上的 `github-pages` gem 已过期，则站点外观在本地构建时可能与在 GitHub 上发布时不同。 为避免这种情况，请定期更新计算机上的 `github-pages` gem。

1. 打开Git Bash。

2. 更新

    

   ```
   github-pages
   ```

    

   gem。

   - 如果已安装 Bundler，请运行 `bundle update github-pages`。
   - 如果尚未安装 Bundler，请运行 `gem update github-pages`。

## [延伸阅读](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll#further-reading)

- Jekyll 文档中的 [GitHub Pages](http://jekyllrb.com/docs/github-pages/)







# 使用 Jekyll 向 GitHub Pages 站点添加内容

## 本文内容

- 关于 Jekyll 站点中的内容
- 向站点添加新页面
- 向站点添加新帖子
- 后续步骤

您可以在 GitHub Pages 上向 Jekyll 站点添加新页面或帖子。

GitHub Pages 适用于具有 GitHub Free 和组织的 GitHub Free 的公共仓库，以及具有 GitHub Pro、GitHub Team、GitHub Enterprise Cloud 和 GitHub Enterprise Server 的公共和私有仓库。 有关详细信息，请参阅“[GitHub 的产品](https://docs.github.com/zh/get-started/learning-about-github/githubs-products)”。

拥有仓库写入权限的人员可以使用 Jekyll 向 GitHub Pages 站点添加内容。

## [关于 Jekyll 站点中的内容](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/adding-content-to-your-github-pages-site-using-jekyll#about-content-in-jekyll-sites)

必须先创建一个 Jekyll 站点，然后才可将内容添加到 GitHub Pages 上的 Jekyll 站点。 有关详细信息，请参阅“[使用 Jekyll 创建 GitHub Pages 站点](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll)”。

Jekyll 站点中内容的主要类型是页面和帖子。 页面是指与某个特定日期没有关联的独立内容，例如“关于”页面。 默认的 Jekyll 站点包含一个名为 `about.md` 的文件，该文件在 `YOUR-SITE-URL/about` 呈现为站点上的一个页面。 您可以编辑该文件的内容以个性化“关于”页面，也可以使用“关于”页作为模板创建新页面。 有关详细信息，请参阅 Jekyll 文档中的“[页面](https://jekyllrb.com/docs/pages/)”。

帖子是博客文章。 默认 Jekyll 站点包含名为 `_posts` 的目录，其中包含默认帖子文件。 您可以编辑该帖子的内容，也可以将默认帖子用作模板来创建新帖子。 有关详细信息，请参阅 Jekyll 文档中的“[帖子](https://jekyllrb.com/docs/posts/)”。

主题包括默认布局、包含和样式表，它们将自动应用到站点上的新页面和帖子，但您可以覆盖其中任何默认值。 有关详细信息，请参阅“[关于 GitHub 页面和 Jekyll](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll#themes)”。

要为网站上的页面或帖子设置变量和元数据，例如标题和布局， 您可以将 YAML 前页添加到任意 Markdown 或 HTML 文件的顶部。 有关详细信息，请参阅 Jekyll 文档中的“[前页](https://jekyllrb.com/docs/front-matter/)”。

如果从分支进行发布，则将更改合并到站点的发布源时，会自动发布对站点的更改。 如果从自定义 GitHub Actions 工作流进行发布，则触发工作流（通常通过推送到默认分支）时会发布更改。 如果想先预览你的更改，可以在本地而不是 GitHub 上进行更改。 然后在本地测试站点。 有关详细信息，请参阅“[使用 Jekyll 在本地测试 GitHub Pages 站点](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll)”。

## [向站点添加新页面](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/adding-content-to-your-github-pages-site-using-jekyll#adding-a-new-page-to-your-site)

1. 在 GitHub 上，导航到站点的仓库。 1. 导航到站点的发布来源。 有关详细信息，请参阅“[配置 GitHub Pages 站点的发布源](https://docs.github.com/zh/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)”。

2. 在发布源的根目录中，为名为 `PAGE-NAME.md` 的页面创建新文件，将 PAGE-NAME 替换为对该页面有意义的文件名。

3. 在文件顶部添加以下 YAML 前页，将 PAGE-TITLE 替换为页面的标题，将 URL-PATH 替换为想要的页面 URL 的路径。 例如，如果站点的基 URL 为

    

   ```
   https://octocat.github.io
   ```

   ，并且 URL-PATH 为

    

   ```
   /about/contact/
   ```

   ，则页面将位于

    

   ```
   https://octocat.github.io/about/contact
   ```

   。

   ```shell
   layout: page
   title: "PAGE-TITLE"
   permalink: /URL-PATH
   ```

4. 在前页下方，为页面添加内容。

5. 单击“提交更改...”

6. 在“提交消息”字段中，输入简短、有意义的提交消息，以描述对文件的更改。 您可以在提交消息中将提交归于多个作者。 有关详细信息，请参阅“[创建有多个作者的提交](https://docs.github.com/zh/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/creating-a-commit-with-multiple-authors)”。

7. 如果在 GitHub.com 上有多个电子邮件地址与你的帐户关联，请单击电子邮件地址下拉菜单，然后选择要用作 Git 作者电子邮件地址的电子邮件地址。 只有经过验证的电子邮件地址才会出现在此下拉菜单中。 如果启用了电子邮件地址隐私，则 `<username>@users.noreply.github.com` 是默认提交作者的电子邮件地址。 有关详细信息，请参阅“[设置提交电子邮件地址](https://docs.github.com/zh/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address)”。![选择提交电子邮件地址](%E4%BD%BF%E7%94%A8jekyll%E8%AE%BE%E7%BD%AE%E7%AB%99%E7%82%B9.assets/choose-commit-email-address.png)1. 在提交消息字段下面，确定是要将提交添加到当前分支还是新分支。 如果当前分支是默认分支，则应选择为提交创建新分支，然后创建拉取请求。 有关详细信息，请参阅“[创建拉取请求](https://docs.github.com/zh/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)”。![提交分支选项](%E4%BD%BF%E7%94%A8jekyll%E8%AE%BE%E7%BD%AE%E7%AB%99%E7%82%B9.assets/choose-commit-branch.png)1. 单击“提交更改”或“建议更改” 。 1. 为您提议的更改创建拉取请求。

8. 在“Pull Requests（拉取请求）”列表中，单击要合并的拉取请求。 1. 单击“合并拉取请求”。 有关详细信息，请参阅“[合并拉取请求](https://docs.github.com/zh/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request)”。 1. 如有提示，输入提交消息，或接受默认消息。 1. 单击“确认合并”。 1. （可选）删除分支。 有关详细信息，请参阅“[创建和删除仓库中的分支](https://docs.github.com/zh/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository)”。

## [向站点添加新帖子](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/adding-content-to-your-github-pages-site-using-jekyll#adding-a-new-post-to-your-site)

1. 在 GitHub 上，导航到站点的仓库。 1. 导航到站点的发布来源。 有关详细信息，请参阅“[配置 GitHub Pages 站点的发布源](https://docs.github.com/zh/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)”。

2. 导航到 `_posts` 目录。

3. 创建名为 `YYYY-MM-DD-NAME-OF-POST.md` 的新文件，将 YYYY-MM-DD 替换为帖子的日期，将 NAME-OF-POST 替换为帖子的名称。

4. 在文件顶部添加以下 YAML 前页，包括用引号括起来的帖子标题、帖子的日期和时间（格式为 YYYY-MM-DD hh:mm:ss -0000），以及任意数量的帖子类别。

   ```shell
   layout: post
   title: "POST-TITLE"
   date: YYYY-MM-DD hh:mm:ss -0000
   categories: CATEGORY-1 CATEGORY-2
   ```

5. 在前页下方，为帖子添加内容。

6. 单击“提交更改...”

7. 在“提交消息”字段中，输入简短、有意义的提交消息，以描述对文件的更改。 您可以在提交消息中将提交归于多个作者。 有关详细信息，请参阅“[创建有多个作者的提交](https://docs.github.com/zh/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/creating-a-commit-with-multiple-authors)”。

8. 如果在 GitHub.com 上有多个电子邮件地址与你的帐户关联，请单击电子邮件地址下拉菜单，然后选择要用作 Git 作者电子邮件地址的电子邮件地址。 只有经过验证的电子邮件地址才会出现在此下拉菜单中。 如果启用了电子邮件地址隐私，则 `<username>@users.noreply.github.com` 是默认提交作者的电子邮件地址。 有关详细信息，请参阅“[设置提交电子邮件地址](https://docs.github.com/zh/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address)”。![选择提交电子邮件地址](%E4%BD%BF%E7%94%A8jekyll%E8%AE%BE%E7%BD%AE%E7%AB%99%E7%82%B9.assets/choose-commit-email-address.png)1. 在提交消息字段下面，确定是要将提交添加到当前分支还是新分支。 如果当前分支是默认分支，则应选择为提交创建新分支，然后创建拉取请求。 有关详细信息，请参阅“[创建拉取请求](https://docs.github.com/zh/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)”。![提交分支选项](%E4%BD%BF%E7%94%A8jekyll%E8%AE%BE%E7%BD%AE%E7%AB%99%E7%82%B9.assets/choose-commit-branch.png)1. 单击“提交更改”或“建议更改” 。 1. 为您提议的更改创建拉取请求。

9. 在“Pull Requests（拉取请求）”列表中，单击要合并的拉取请求。 1. 单击“合并拉取请求”。 有关详细信息，请参阅“[合并拉取请求](https://docs.github.com/zh/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request)”。 1. 如有提示，输入提交消息，或接受默认消息。 1. 单击“确认合并”。 1. （可选）删除分支。 有关详细信息，请参阅“[创建和删除仓库中的分支](https://docs.github.com/zh/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository)”。

您的帖子现在应该显示在您的站点上！ 如果站点的基 URL 为 `https://octocat.github.io`，则新帖子将位于 `https://octocat.github.io/YYYY/MM/DD/TITLE.html`。

## [后续步骤](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/adding-content-to-your-github-pages-site-using-jekyll#next-steps)

您可以将 Jekyll 主题添加到 GitHub Pages 站点，以自定义站点的外观。有关详细信息，请参阅“[使用 Jekyll 向 GitHub Pages 站点添加主题](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/adding-a-theme-to-your-github-pages-site-using-jekyll)”。





# 使用 Jekyll 为 GitHub Pages 站点设置 Markdown 处理器

您可以选择一个 Markdown 处理器来确定 Markdown 在 GitHub Pages 站点上的呈现方式。

GitHub Pages 适用于具有 GitHub Free 和组织的 GitHub Free 的公共仓库，以及具有 GitHub Pro、GitHub Team、GitHub Enterprise Cloud 和 GitHub Enterprise Server 的公共和私有仓库。 有关详细信息，请参阅“[GitHub 的产品](https://docs.github.com/zh/get-started/learning-about-github/githubs-products)”。

拥有仓库写入权限的人可为 GitHub Pages 站点设置 Markdown 处理器。

GitHub Pages 支持两种 Markdown 处理器：[kramdown](http://kramdown.gettalong.org/) 和 GitHub 自己的 Markdown 处理器，后者用于在整个 GitHub 中呈现 [GitHub 风格的 Markdown (GFM)](https://github.github.com/gfm/)。 有关详细信息，请参阅“[关于在 GitHub 上编写和设置格式](https://docs.github.com/zh/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/about-writing-and-formatting-on-github)”。

您可以在任一处理器上使用 GitHub 风格的 Markdown，但只有我们的 GFM 处理器始终与您在 GitHub 上看到的结果相匹配。

1. 在 GitHub 上，导航到站点的仓库。

2. 在存储库中，浏览到 _config.yml 文件。

3. 在文件视图的右上角，单击 以打开文件编辑器。

   ![文件的屏幕截图。 在标头中，标有铅笔图标的按钮以深橙色标出。](%E4%BD%BF%E7%94%A8jekyll%E8%AE%BE%E7%BD%AE%E7%AB%99%E7%82%B9.assets/edit-file-edit-button.png)

   注意：除了使用默认文件编辑器编辑和提交文件，还可以选择使用 [github.dev 代码编辑器](https://docs.github.com/zh/codespaces/the-githubdev-web-based-editor)，方法是选择 下拉菜单并单击“在 github.dev 中打开” 。

   ![文件的屏幕截图。 在标头中，一个朝下三角形图标用深橙色框出。](%E4%BD%BF%E7%94%A8jekyll%E8%AE%BE%E7%BD%AE%E7%AB%99%E7%82%B9.assets/edit-file-edit-dropdown.png)

4. 找到以 `markdown:` 开头的行，然后将值更改为 `kramdown` 或 `GFM`。 整行应显示为 `markdown: kramdown` 或 `markdown: GFM`。

5. 单击“提交更改...”

6. 在“提交消息”字段中，输入简短、有意义的提交消息，以描述对文件的更改。 您可以在提交消息中将提交归于多个作者。 有关详细信息，请参阅“[创建有多个作者的提交](https://docs.github.com/zh/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/creating-a-commit-with-multiple-authors)”。

7. 如果在 GitHub.com 上有多个电子邮件地址与你的帐户关联，请单击电子邮件地址下拉菜单，然后选择要用作 Git 作者电子邮件地址的电子邮件地址。 只有经过验证的电子邮件地址才会出现在此下拉菜单中。 如果启用了电子邮件地址隐私，则 `<username>@users.noreply.github.com` 是默认提交作者的电子邮件地址。 有关详细信息，请参阅“[设置提交电子邮件地址](https://docs.github.com/zh/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address)”。![选择提交电子邮件地址](%E4%BD%BF%E7%94%A8jekyll%E8%AE%BE%E7%BD%AE%E7%AB%99%E7%82%B9.assets/choose-commit-email-address-168369808407511.png)1. 在提交消息字段下面，确定是要将提交添加到当前分支还是新分支。 如果当前分支是默认分支，则应选择为提交创建新分支，然后创建拉取请求。 有关详细信息，请参阅“[创建拉取请求](https://docs.github.com/zh/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)”。![提交分支选项](%E4%BD%BF%E7%94%A8jekyll%E8%AE%BE%E7%BD%AE%E7%AB%99%E7%82%B9.assets/choose-commit-branch-168369808407513.png)1. 单击“提交更改”或“建议更改” 。

## [延伸阅读](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/setting-a-markdown-processor-for-your-github-pages-site-using-jekyll#further-reading)

- [kramdown 文档](https://kramdown.gettalong.org/documentation.html)
- [GitHub 风格的 Markdown 规范](https://github.github.com/gfm/)

# 使用 Jekyll 向 GitHub Pages 站点添加主题

## 本文内容

- 添加主题
- 自定义主题的 CSS
- 自定义主题的 HTML 布局
- 延伸阅读

您可以通过添加和自定义主题来个性化 Jekyll 站点。

GitHub Pages 适用于具有 GitHub Free 和组织的 GitHub Free 的公共仓库，以及具有 GitHub Pro、GitHub Team、GitHub Enterprise Cloud 和 GitHub Enterprise Server 的公共和私有仓库。 有关详细信息，请参阅“[GitHub 的产品](https://docs.github.com/zh/get-started/learning-about-github/githubs-products)”。

拥有仓库写入权限的人员可以使用 Jekyll 将主题添加到 GitHub Pages 网站。

如果从分支进行发布，则将更改合并到站点的发布源时，会自动发布对站点的更改。 如果从自定义 GitHub Actions 工作流进行发布，则触发工作流（通常通过推送到默认分支）时会发布更改。 如果想先预览你的更改，可以在本地而不是 GitHub 上进行更改。 然后在本地测试站点。 有关详细信息，请参阅“[使用 Jekyll 在本地测试 GitHub Pages 站点](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll)”。

## [添加主题](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/adding-a-theme-to-your-github-pages-site-using-jekyll#adding-a-theme)

1. 在 GitHub 上，导航到站点的仓库。 1. 导航到站点的发布来源。 有关详细信息，请参阅“[配置 GitHub Pages 站点的发布源](https://docs.github.com/zh/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)”。

2. 导航到“_config.yml”。

3. 在文件视图的右上角，单击 以打开文件编辑器。

   ![文件的屏幕截图。 在标头中，标有铅笔图标的按钮以深橙色标出。](%E4%BD%BF%E7%94%A8jekyll%E8%AE%BE%E7%BD%AE%E7%AB%99%E7%82%B9.assets/edit-file-edit-button-168369811558515.png)

   注意：除了使用默认文件编辑器编辑和提交文件，还可以选择使用 [github.dev 代码编辑器](https://docs.github.com/zh/codespaces/the-githubdev-web-based-editor)，方法是选择 下拉菜单并单击“在 github.dev 中打开” 。

   ![文件的屏幕截图。 在标头中，一个朝下三角形图标用深橙色框出。](%E4%BD%BF%E7%94%A8jekyll%E8%AE%BE%E7%BD%AE%E7%AB%99%E7%82%B9.assets/edit-file-edit-dropdown-168369811558617.png)

4. 为主题名称添加新行。

   - 若要使用支持的主题，请键入 `theme: THEME-NAME`，将 THEME-NAME 替换为主题存储库的 README 中显示的主题名称。 有关支持主题的列表，请参阅 GitHub Pages 站点上的“[支持主题](https://pages.github.com/themes/)”。![配置文件中支持的主题](%E4%BD%BF%E7%94%A8jekyll%E8%AE%BE%E7%BD%AE%E7%AB%99%E7%82%B9.assets/add-theme-to-config-file.png)
   - 若要使用在 GitHub 上托管的任何其他 Jekyll 主题，请键入 `remote_theme: THEME-NAME`，将 THEME-NAME 替换为主题存储库的 README 中显示的主题名称。![配置文件中不支持的主题](%E4%BD%BF%E7%94%A8jekyll%E8%AE%BE%E7%BD%AE%E7%AB%99%E7%82%B9.assets/add-remote-theme-to-config-file.png)1. 单击“提交更改...”

5. 在“提交消息”字段中，输入简短、有意义的提交消息，以描述对文件的更改。 您可以在提交消息中将提交归于多个作者。 有关详细信息，请参阅“[创建有多个作者的提交](https://docs.github.com/zh/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/creating-a-commit-with-multiple-authors)”。

6. 如果在 GitHub.com 上有多个电子邮件地址与你的帐户关联，请单击电子邮件地址下拉菜单，然后选择要用作 Git 作者电子邮件地址的电子邮件地址。 只有经过验证的电子邮件地址才会出现在此下拉菜单中。 如果启用了电子邮件地址隐私，则 `<username>@users.noreply.github.com` 是默认提交作者的电子邮件地址。 有关详细信息，请参阅“[设置提交电子邮件地址](https://docs.github.com/zh/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address)”。![选择提交电子邮件地址](%E4%BD%BF%E7%94%A8jekyll%E8%AE%BE%E7%BD%AE%E7%AB%99%E7%82%B9.assets/choose-commit-email-address-168369811558721.png)1. 在提交消息字段下面，确定是要将提交添加到当前分支还是新分支。 如果当前分支是默认分支，则应选择为提交创建新分支，然后创建拉取请求。 有关详细信息，请参阅“[创建拉取请求](https://docs.github.com/zh/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)”。![提交分支选项](%E4%BD%BF%E7%94%A8jekyll%E8%AE%BE%E7%BD%AE%E7%AB%99%E7%82%B9.assets/choose-commit-branch-168369811558723.png)1. 单击“提交更改”或“建议更改” 。

## [自定义主题的 CSS](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/adding-a-theme-to-your-github-pages-site-using-jekyll#customizing-your-themes-css)

这些说明非常适用于 GitHub Pages 官方支持的主题。 有关支持主题的完整列表，请参阅 GitHub Pages 站点上的“[支持主题](https://pages.github.com/themes/)”。

主题的源仓库也可能对自定义主题有所帮助。 例如，请参阅 [Minima 的自述文件](https://github.com/jekyll/minima#customizing-templates)。

1. 在 GitHub 上，导航到站点的仓库。 1. 导航到站点的发布来源。 有关详细信息，请参阅“[配置 GitHub Pages 站点的发布源](https://docs.github.com/zh/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)”。

2. 新建一个名为 /assets/css/style.scss 的文件。

3. 在文件顶部添加以下内容：

   ```scss
   ---
   ---
   
   @import "{{ site.theme }}";
   ```

4. 在 `@import` 行的后面直接添加所需的任何自定义 CSS 或 Sass（包括导入）。

## [自定义主题的 HTML 布局](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/adding-a-theme-to-your-github-pages-site-using-jekyll#customizing-your-themes-html-layout)

这些说明非常适用于 GitHub Pages 官方支持的主题。 有关支持主题的完整列表，请参阅 GitHub Pages 站点上的“[支持主题](https://pages.github.com/themes/)”。

主题的源仓库也可能对自定义主题有所帮助。 例如，请参阅 [Minima 的自述文件](https://github.com/jekyll/minima#customizing-templates)。

1. 在 GitHub 上，导航到主题的源仓库。 例如，Minima 的源存储库为 https://github.com/jekyll/minima 。
2. 在 _layouts 文件夹中，导航到主题的 default.html 文件。
3. 复制该文件的内容。
4. 在 GitHub 上，导航到站点的仓库。 1. 导航到站点的发布来源。 有关详细信息，请参阅“[配置 GitHub Pages 站点的发布源](https://docs.github.com/zh/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)”。
5. 创建一个名为 _layouts/default.html 的文件。
6. 粘贴之前复制的默认布局内容。
7. 根据需要自定义布局。

## [延伸阅读](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/adding-a-theme-to-your-github-pages-site-using-jekyll#further-reading)

- "[创建新文件](https://docs.github.com/zh/repositories/working-with-files/managing-files/creating-new-files)"

# 关于 GitHub Pages 站点的 Jekyll 构建错误

## 本文内容

- 关于 Jekyll 构建错误
- 查看 GitHub Actions 的 Jekyll 构建错误消息
- 在本地查看 Jekyll 构建错误消息
- 在拉取请求中查看 Jekyll 构建错误消息
- 通过电子邮件查看 Jekyll 构建错误
- 使用第三方 CI 服务查看拉取请求中的 Jekyll 构建错误消息

如果在本地或 GitHub 上构建 GitHub Pages 站点发生 Jekyll 错误，您将收到一条错误消息，其中包含相关详细信息。

GitHub Pages 适用于具有 GitHub Free 和组织的 GitHub Free 的公共仓库，以及具有 GitHub Pro、GitHub Team、GitHub Enterprise Cloud 和 GitHub Enterprise Server 的公共和私有仓库。 有关详细信息，请参阅“[GitHub 的产品](https://docs.github.com/zh/get-started/learning-about-github/githubs-products)”。

## [关于 Jekyll 构建错误](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/about-jekyll-build-errors-for-github-pages-sites#about-jekyll-build-errors)

如果从分支发布，则将更改推送到站点的发布源后，有时， GitHub Pages 不会尝试生成站点。

- 推送更改的人尚未验证他们的电子邮件地址。 有关详细信息，请参阅“[验证电子邮件地址](https://docs.github.com/zh/get-started/signing-up-for-github/verifying-your-email-address)”。
- 您使用部署密钥推送。 如果要自动推送到站点的仓库，您可以改为设置计算机用户。 有关详细信息，请参阅“[管理部署密钥](https://docs.github.com/zh/authentication/connecting-to-github-with-ssh/managing-deploy-keys#machine-users)”。
- 您使用的是未配置为构建发布源的 CI 服务。 例如，Travis CI 不会生成 `gh-pages` 分支，除非将分支添加到安全列表。 有关详细信息，请参阅 Travis CI 上的“[自定义生成](https://docs.travis-ci.com/user/customizing-the-build/#safelisting-or-blocklisting-branches)”或 CI 服务的文档。

**注意：** 对站点的更改在推送到 GitHub 后，最长可能需要 10 分钟才会发布。

如果 Jekyll 尝试构建站点但遇到错误，你将收到一条构建错误消息。

有关排查生成错误的详细信息，请参阅“[排查构建错误](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/troubleshooting-jekyll-build-errors-for-github-pages-sites)”。

## [查看 GitHub Actions 的 Jekyll 构建错误消息](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/about-jekyll-build-errors-for-github-pages-sites#查看-github-actions-的-jekyll-构建错误消息)

默认情况下，除非已将 GitHub Pages 网站配置为使用其他 CI 工具，否则 GitHub Pages 网站使用 GitHub Actions 工作流程运行构建和部署。 要查找潜在的构建错误，您可以通过查看仓库的工作流程运行来检查 GitHub Pages 站点的工作流程运行情况。 有关详细信息，请参阅“[查看工作流程运行历史记录](https://docs.github.com/zh/actions/monitoring-and-troubleshooting-workflows/viewing-workflow-run-history)”。 有关如何在出现错误时重新运行工作流的详细信息，请参阅“[重新运行工作流程和作业](https://docs.github.com/zh/actions/managing-workflow-runs/re-running-workflows-and-jobs)”。

## [在本地查看 Jekyll 构建错误消息](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/about-jekyll-build-errors-for-github-pages-sites#viewing-jekyll-build-error-messages-locally)

我们建议在本地测试您的站点，这样您可以在命令行上看到构建错误消息，并在更改推送到 GitHub 之前解决任何构建失败。 有关详细信息，请参阅“[使用 Jekyll 在本地测试 GitHub Pages 站点](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll)”。

## [在拉取请求中查看 Jekyll 构建错误消息](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/about-jekyll-build-errors-for-github-pages-sites#viewing-jekyll-build-error-messages-in-your-pull-request)

如果从分支发布，当创建拉取请求来更新 GitHub 上的发布源时，拉取请求的“检查”选项卡上会显示生成错误消息。 有关详细信息，请参阅“[关于状态检查](https://docs.github.com/zh/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks)”。

如果使用自定义 GitHub Actions 工作流进行发布，以在拉取请求中查看生成错误消息，则必须将工作流配置为在 `pull_request` 触发器上运行。 执行此操作时，如果工作流已由 `pull_request` 事件触发，则建议跳过所有部署步骤。 这样，无需将拉取请求中的更改部署到站点即可查看所有生成错误。 有关详细信息，请参阅“[触发工作流的事件](https://docs.github.com/zh/actions/using-workflows/events-that-trigger-workflows#pull_request)”和“[表达式](https://docs.github.com/zh/actions/learn-github-actions/expressions)”。

## [通过电子邮件查看 Jekyll 构建错误](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/about-jekyll-build-errors-for-github-pages-sites#viewing-jekyll-build-errors-by-email)

如果从分支发布，当将更改推送到 GitHub 上的发布源时，GitHub Pages 将尝试生成站点。 如果构建失败，您将在您的主要电子邮件地址收到一封电子邮件。

如果使用自定义 GitHub Actions 工作流进行发布，以在拉取请求中接收有关生成错误的电子邮件，则必须将工作流配置为在 `pull_request` 触发器上运行。 执行此操作时，如果工作流已由 `pull_request` 事件触发，则建议跳过所有部署步骤。 这样，无需将拉取请求中的更改部署到站点即可查看所有生成错误。 有关详细信息，请参阅“[触发工作流的事件](https://docs.github.com/zh/actions/using-workflows/events-that-trigger-workflows#pull_request)”和“[表达式](https://docs.github.com/zh/actions/learn-github-actions/expressions)”。

## [使用第三方 CI 服务查看拉取请求中的 Jekyll 构建错误消息](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/about-jekyll-build-errors-for-github-pages-sites#viewing-jekyll-build-error-messages-in-your-pull-request-with-a-third-party-ci-service)

可以将第三方服务（如 [Travis CI](https://travis-ci.com/)）配置为在每次提交后显示错误消息。

1. 如果尚未在发布源的根目录中添加名为 Gemfile 的文件并包含以下内容：

   ```ruby
   source `https://rubygems.org`
   gem `github-pages`
   ```

2. 为您选择的测试服务配置站点仓库。 例如，使用 [Travis CI](https://travis-ci.com/) 在发布源的根目录中添加名为 *.travis.yml* 的文件并包含以下内容：

   ```yaml
   language: ruby
   rvm:
     - 2.3
   script: "bundle exec jekyll build"
   ```

3. 您可能需要使用第三方测试服务激活仓库。 更多信息请参阅测试服务的文档。



# 排查构建错误

## 本文内容

- 如果您收到一般错误消息，请检查常见问题。
- \- 使用空格代替制表符。
- 确保传递给与日期相关的 Liquid 筛选器的任何变量在所有情况下都具有值，并且永远不会传递 nil 或 ""。
- 高亮插件语言无效
- 有关详细信息，请参阅“关于 GitHub 页面和 Jekyll”。
- 若要指定与 UTC 偏移的时区，请使用格式 YYYY-MM-DD HH:MM:SS +/-TTTT，例如 2014-04-18 11:30:00 +0800。
- 为防止以后出错，请在您的常用文本编辑器中安装 Sass 或 SCSS 语法检查插件。
- 如果要使用子模块，请确保在引用子模块时使用 https://（而不是 http://），并且子模块位于公共存储库中。
- \- 使用空格代替制表符。
- 有关详细信息，请参阅“使用 Jekyll 为 GitHub Pages 站点设置 Markdown 处理器”。
- 如果 docs 文件夹被意外删除，你可以执行以下任一操作：
- 如果要使用子模块，请初始化子模块。
- 绝对永久链接以站点的根目录开头，而相对永久链接以包含引用页面的文件夹开头。
- 有关 for 循环的正确语法的详细信息，请参阅 Liquid 文档中的“迭代标记”。
- 要排除故障，请确保错误消息所指文件中的所有逻辑标记都正确关闭。
- 若要排除故障，请确保错误消息所指文件中的所有输出标记都以 }} 终止。
- 有关默认变量的列表，请参阅 Jekyll 文档中的“变量”。

如果在本地或 GitHub 上构建 GitHub Pages 站点时发生 Jekyll 错误，您可以使用错误消息排查故障。

GitHub Pages 适用于具有 GitHub Free 和组织的 GitHub Free 的公共仓库，以及具有 GitHub Pro、GitHub Team、GitHub Enterprise Cloud 和 GitHub Enterprise Server 的公共和私有仓库。 有关详细信息，请参阅“[GitHub 的产品](https://docs.github.com/zh/get-started/learning-about-github/githubs-products)”。

## [如果您收到一般错误消息，请检查常见问题。](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/troubleshooting-jekyll-build-errors-for-github-pages-sites#troubleshooting-build-errors)

您使用的插件不受支持。 有关详细信息，请参阅“[关于 GitHub 页面和 Jekyll](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll#plugins)”。

您的仓库已超过我们的仓库大小限制。

- 有关详细信息，请参阅“[关于 GitHub 上的大文件](https://docs.github.com/zh/repositories/working-with-files/managing-large-files/about-large-files-on-github)” 你更改了 _config.yml 文件中的 `source` 设置。
- 如果从分支发布站点，GitHub Pages 在生成过程中会覆盖此设置。 已发布文件中的文件名包含不支持的冒号 (`:`)。
- 如果您收到特定的错误消息，请查看下面的错误消息疑难解答信息。 修复任何错误后，通过将更改推送到站点的源分支（如果从分支发布）或通过触发自定义 GitHub Actions 工作流（如果使用 GitHub Actions 发布）来触发另一个生成。
- Config 文件错误

此错误意味着站点构建失败，因为 _config.yml 文件包含语法错误。

若要排除故障，请确保 _config.yml 文件遵循以下规则：

## [- 使用空格代替制表符。](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/troubleshooting-jekyll-build-errors-for-github-pages-sites#--使用空格代替制表符)

- 在“`:`”后面为每个键/值对添加空格，例如 `timezone: Africa/Nairobi`。
- 仅使用 UTF-8 字符。
- 引用任何特殊字符（如 `:`），例如 `title: "my awesome site: an adventure in parse errors"`。
- 对于多行值，用于 `|` 创建新行和 `>` 来忽略换行符。

若要识别任何错误，可以将 YAML 文件的内容复制并粘贴到 YAML Linter，例如 [YAML 验证程序](http://codebeautify.org/yaml-validator)。

**Note:** If your repository contains symbolic links, you will need to publish your site using a GitHub Actions workflow. For more information about GitHub Actions, see "[GitHub Actions文档](https://docs.github.com/zh/actions)."

日期不是有效的日期时间

此错误意味着站点上的某个页面包含无效的日期时间。

要排除故障，请搜索错误消息中的文件和文件布局，以调用任何与日期相关的 Liquid 过滤器。

## [确保传递给与日期相关的 Liquid 筛选器的任何变量在所有情况下都具有值，并且永远不会传递 `nil` 或 `""`。](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/troubleshooting-jekyll-build-errors-for-github-pages-sites#确保传递给与日期相关的-liquid-筛选器的任何变量在所有情况下都具有值并且永远不会传递-nil-或-)

有关详细信息，请参阅 Liquid 文档中的“[Liquid 筛选器](https://help.shopify.com/en/themes/liquid/filters)”。

文件在包含目录中不存在 此错误意味着代码引用了 _includes 目录中不存在的文件。 若要进行故障排除，请在 `include` 的错误消息中搜索文件，以查看你在哪些地方引用了其他文件，例如 `{% include example_header.html %}`。 如果你引用的任何文件不在 _includes 目录中，请将这些文件复制或移动到 _includes 目录 。

## 

文件未采用正确的 UTF-8 编码

此错误意味着你使用了非拉丁字符（例如 `日本語`）但没有告诉计算机预期这些符号。 若要排除故障，请通过在 _config.yml 文件中添加以下行来强制使用 UTF-8 编码：

## [高亮插件语言无效](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/troubleshooting-jekyll-build-errors-for-github-pages-sites#file-is-not-properly-utf-8-encoded)

此错误意味着你在配置文件中指定了除 [Rouge](https://github.com/jneen/rouge) 或 [Pygments](http://pygments.org/) 之外的任何语法高亮插件。

若要排除故障，请更新 _config.yml 文件以指定 [Rouge](https://github.com/jneen/rouge) 或 [Pygments](http://pygments.org/)。

```yaml
encoding: UTF-8
```

## [有关详细信息，请参阅“](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/troubleshooting-jekyll-build-errors-for-github-pages-sites#markdown-errors)[关于 GitHub 页面和 Jekyll](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll#syntax-highlighting)”。

帖子日期无效

此错误意味着站点上的帖子在文件名或 YAML 前页中包含无效的日期。 要排除故障，请确保所有日期的 UTC 格式均为 YYYY-MM-DD HH:MM:SS， 并且都是实际日历日期。

## [若要指定与 UTC 偏移的时区，请使用格式 YYYY-MM-DD HH:MM:SS +/-TTTT，例如 `2014-04-18 11:30:00 +0800`。](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/troubleshooting-jekyll-build-errors-for-github-pages-sites#invalid-post-date)

如果你在 _config.yml 文件中指定日期格式，请确保格式正确。

Sass 或 SCSS 无效 此错误意味着您的仓库包含内容无效的 Sass 或 SCSS 文件。

要排除故障，请查看指示 Sass 或 SCSS 无效的错误消息中包含的行号。

## [为防止以后出错，请在您的常用文本编辑器中安装 Sass 或 SCSS 语法检查插件。](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/troubleshooting-jekyll-build-errors-for-github-pages-sites#invalid-sass-or-scss)

子模块无效

此错误意味着您的仓库包含尚未正确初始化的子模块。 要排除故障，请先决定您是否真的想要使用子模块，它是 Git 项目内的 Git 项目； 子模块有时是意外创建的。

如果不想使用子模块，请删除子模块，将 PATH-TO-SUBMODULE 替换为子模块的路径：

```shell
$ git submodule deinit PATH-TO-SUBMODULE
$ git rm PATH-TO-SUBMODULE
$ git commit -m "Remove submodule"
$ rm -rf .git/modules/PATH-TO-SUBMODULE
```

## [如果要使用子模块，请确保在引用子模块时使用 `https://`（而不是 `http://`），并且子模块位于公共存储库中。](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/troubleshooting-jekyll-build-errors-for-github-pages-sites#invalid-submodule)

数据文件中的 YAML 无效

此错误意味着 _data 文件夹中的多个文件之一包含无效的 YAML。

若要排除故障，请确保 _data 文件夹中的 YAML 文件遵循以下规则：

## [- 使用空格代替制表符。](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/troubleshooting-jekyll-build-errors-for-github-pages-sites#--使用空格代替制表符-1)

- 在“`:`”后面为每个键/值对添加空格，例如 `timezone: Africa/Nairobi`。
- 仅使用 UTF-8 字符。
- 引用任何特殊字符（如 `:`），例如 `title: "my awesome site: an adventure in parse errors"`。
- 对于多行值，用于 `|` 创建新行和 `>` 来忽略换行符。

若要识别任何错误，可以将 YAML 文件的内容复制并粘贴到 YAML Linter，例如 [YAML 验证程序](http://codebeautify.org/yaml-validator)。

有关 Jekyll 数据文件的详细信息，请参阅 Jekyll 文档中的“[数据文件](https://jekyllrb.com/docs/datafiles/)”。

Markdown 错误

此错误意味着您的仓库包含 Markdown 错误。

要排除故障，请确保使用受支持的 Markdown 处理器。

## [有关详细信息，请参阅“](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/troubleshooting-jekyll-build-errors-for-github-pages-sites#markdown-errors)[使用 Jekyll 为 GitHub Pages 站点设置 Markdown 处理器](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/setting-a-markdown-processor-for-your-github-pages-site-using-jekyll)”。

然后，确认错误消息中的文件使用有效的 Markdown 语法。

有关详细信息，请参阅 Daring Fireball 上的“[Markdown：语法](https://daringfireball.net/projects/markdown/syntax)”。 缺少 docs 文件夹

此错误意味着你已选择分支上的 `docs` 文件夹作为发布源，但该分支上存储库的根目录中没有 `docs` 文件夹。 若要排除故障，如果 `docs` 文件夹被意外移动，请尝试将 `docs` 文件夹移回你为发布源选择的分支上的存储库根目录。

## [如果 `docs` 文件夹被意外删除，你可以执行以下任一操作：](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/troubleshooting-jekyll-build-errors-for-github-pages-sites#missing-docs-folder)

使用 Git 还原或撤消删除。

有关详细信息，请参阅 Git 文档中的“[git-revert](https://git-scm.com/docs/git-revert.html)”。 在为发布源选择的分支上的存储库根目录中创建一个新的 `docs` 文件夹，并将站点的源文件添加到该文件夹中。

- 有关详细信息，请参阅“[创建新文件](https://docs.github.com/zh/repositories/working-with-files/managing-files/creating-new-files)”。 更改发布源。
- 有关详细信息，请参阅“[配置 GitHub Pages 站点的发布源](https://docs.github.com/zh/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)”。 缺少子模块
- 此错误意味着您的仓库包含不存在或尚未正确初始化的子模块。 要排除故障，请先决定您是否真的想要使用子模块，它是 Git 项目内的 Git 项目； 子模块有时是意外创建的。

如果不想使用子模块，请删除子模块，将 PATH-TO-SUBMODULE 替换为子模块的路径：

```shell
$ git submodule deinit PATH-TO-SUBMODULE
$ git rm PATH-TO-SUBMODULE
$ git commit -m "Remove submodule"
$ rm -rf .git/modules/PATH-TO-SUBMODULE
```

## [如果要使用子模块，请初始化子模块。](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/troubleshooting-jekyll-build-errors-for-github-pages-sites#missing-submodule)

有关详细信息，请参阅 *Pro Git* 书中的“[Git 工具 - 子模块](https://git-scm.com/book/en/v2/Git-Tools-Submodules)”。

配置了相对永久链接

此错误意味着 _config.yml 文件中存在 GitHub Pages 不支持的相对永久链接。 永久链接是引用站点上特定页面的永久 URL。

## [绝对永久链接以站点的根目录开头，而相对永久链接以包含引用页面的文件夹开头。](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/troubleshooting-jekyll-build-errors-for-github-pages-sites#relative-permalinks-configured)

GitHub Pages 和 Jekyll 不再支持相对永久链接。

有关永久链接的详细信息，请参阅 Jekyll 文档中的“[永久链接](https://jekyllrb.com/docs/permalinks/)”。 若要排除故障，请从 _config.yml 文件中删除 `relative_permalinks` 行，并将站点中的任何相对永久链接重新格式化为绝对永久链接。 有关详细信息，请参阅“[编辑文件](https://docs.github.com/zh/repositories/working-with-files/managing-files/editing-files)”。 'for' 循环中的语法错误 此错误意味着代码在 Liquid `for` 循环声明中包含无效语法。 若要排除故障，请确保错误消息所指文件中的所有 `for` 循环都具有正确的语法。

## [有关 `for` 循环的正确语法的详细信息，请参阅 Liquid 文档中的“](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/troubleshooting-jekyll-build-errors-for-github-pages-sites#syntax-error-in-for-loop)[迭代标记](https://help.shopify.com/en/themes/liquid/tags/iteration-tags#for)”。

标记未正确关闭

此错误消息意味着您的代码包含未正确关闭的逻辑标记。 例如，`{% capture example_variable %}` 必须由 `{% endcapture %}` 关闭。

## [要排除故障，请确保错误消息所指文件中的所有逻辑标记都正确关闭。](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/troubleshooting-jekyll-build-errors-for-github-pages-sites#tag-not-properly-closed)

有关详细信息，请参阅 Liquid 文档中的“[Liquid 标记](https://help.shopify.com/en/themes/liquid/tags)”。 标记未正确终止

此错误意味着您的代码包含未正确终止的输出标记。 例如，是 `{{ page.title }` 而不是 `{{ page.title }}`。

## [若要排除故障，请确保错误消息所指文件中的所有输出标记都以 `}}` 终止。](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/troubleshooting-jekyll-build-errors-for-github-pages-sites#tag-not-properly-terminated)

有关详细信息，请参阅 Liquid 文档中的“[Liquid 对象](https://help.shopify.com/en/themes/liquid/objects)”。 未知标记错误

此错误意味着您的代码包含无法识别的 Liquid 标记。 要排除故障，请确保错误消息所指文件中的所有 Liquid 标记都与 Jekyll 的默认变量相匹配，并且标记名称没有拼写错误。

## [有关默认变量的列表，请参阅 Jekyll 文档中的“](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/troubleshooting-jekyll-build-errors-for-github-pages-sites#unknown-tag-error)[变量](https://jekyllrb.com/docs/variables/)”。

不受支持的插件是无法识别标记的常见来源。

如果您通过在本地生成站点并将静态文件推送到 GitHub 的方法在站点中使用不受支持的插件，请确保该插件未引入 Jekyll 默认变量中没有的标记。 有关支持的插件的列表，请参阅“[关于 GitHub 页面和 Jekyll](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll#plugins)”。

Unsupported plugins are a common source of unrecognized tags. If you use an unsupported plugin in your site by generating your site locally and pushing your static files to GitHub, make sure the plugin is not introducing tags that are not in Jekyll's default variables. For a list of supported plugins, see "[关于 GitHub 页面和 Jekyll](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll#plugins)."

























