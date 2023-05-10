# Githubs Pages入门

# 关于 GitHub Pages

## 本文内容

- 关于 GitHub Pages
- GitHub Pages 站点的类型
- GitHub Pages 站点的发布来源
- 静态站点生成器
- GitHub Pages 使用限制
- GitHub Pages 上的 MIME 类型
- 数据收集
- 延伸阅读

你可以使用 GitHub Pages 直接从 GitHub.com 上的仓库托管关于自己、你的组织或你的项目的站点。

GitHub Pages 适用于具有 GitHub Free 和组织的 GitHub Free 的公共仓库，以及具有 GitHub Pro、GitHub Team、GitHub Enterprise Cloud 和 GitHub Enterprise Server 的公共和私有仓库。 有关详细信息，请参阅“[GitHub 的产品](https://docs.github.com/zh/get-started/learning-about-github/githubs-products)”。

## [关于 GitHub Pages](https://docs.github.com/zh/pages/getting-started-with-github-pages/about-github-pages#关于-github-pages)

GitHub Pages 是一项静态站点托管服务，它直接从 GitHub 上的仓库获取 HTML、CSS 和 JavaScript 文件，（可选）通过构建过程运行文件，然后发布网站。 可以在 [GitHub Pages 示例集合](https://github.com/collections/github-pages-examples)中看到 GitHub Pages 站点的示例。

你可以在 GitHub 的 `github.io` 域或自己的自定义域上托管站点。 有关详细信息，请参阅“[配置 GitHub Pages 站点的自定义域](https://docs.github.com/zh/pages/configuring-a-custom-domain-for-your-github-pages-site)”。

你可以创建在 Internet 上公开可用的 GitHub Pages 站点。 使用 GitHub Enterprise Cloud 的组织还可以通过管理对站点的访问控制来私下发布站点。 有关详细信息，请参阅 GitHub Enterprise Cloud 文档中的“[更改 GitHub Pages 站点的可见性](https://docs.github.com/zh/enterprise-cloud@latest/pages/getting-started-with-github-pages/changing-the-visibility-of-your-github-pages-site)”。

若要开始操作，请参阅“[创建 GitHub Pages 站点](https://docs.github.com/zh/pages/getting-started-with-github-pages/creating-a-github-pages-site)”。

组织所有者可禁止从组织的存储库发布 GitHub Pages 站点。 有关详细信息，请参阅“[管理组织的 GitHub Pages 站点发布](https://docs.github.com/zh/organizations/managing-organization-settings/managing-the-publication-of-github-pages-sites-for-your-organization)”。

## [GitHub Pages 站点的类型](https://docs.github.com/zh/pages/getting-started-with-github-pages/about-github-pages#github-pages-站点的类型)

有三种类型的 GitHub Pages 站点：项目、用户和组织。 项目站点连接到 GitHub 上托管的特定项目，例如 JavaScript 库或配方集合。 用户和组织站点连接到 GitHub.com 上的特定帐户。

若要发布用户站点，必须创建名为 `<username>.github.io` 的个人帐户拥有的存储库。 若要发布组织站点，必须创建名为 `<organization>.github.io` 的组织帐户拥有的存储库。 除非使用的是自定义域，否则用户和组织站点在 `http(s)://<username>.github.io` 或 `http(s)://<organization>.github.io` 中可用。

项目站点的源文件与其项目存储在同一个仓库中。 除非使用的是自定义域，否则项目站点在 `http(s)://<username>.github.io/<repository>` 或 `http(s)://<organization>.github.io/<repository>` 中可用。

有关自定义域如何影响站点的 URL 的详细信息，请参阅“[关于自定义域名和 GitHub 页面](https://docs.github.com/zh/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages)”。

您只能为 GitHub 上的每个帐户创建一个用户或组织站点。 项目站点（无论是组织还是个人帐户拥有）没有限制。

## [GitHub Pages 站点的发布来源](https://docs.github.com/zh/pages/getting-started-with-github-pages/about-github-pages#github-pages-站点的发布来源)

警告：GitHub Pages 站点可以在 Internet 上公开，即使该站点的存储库是私有的。 如果站点的存储库中有敏感数据，你可能想要在发布前删除数据。 有关详细信息，请参阅“[关于仓库](https://docs.github.com/zh/repositories/creating-and-managing-repositories/about-repositories#about-repository-visibility)”。

可以在将更改推送到特定分支时发布站点，也可以编写 GitHub Actions 工作流来发布站点。

如果不需要对站点的生成过程进行任何控制，则建议在将更改推送到特定分支时发布站点。 可以指定要用作发布源的分支和文件夹。 源分支可以是存储库中的任何分支，源文件夹可以是源分支上的存储库根目录 (`/`)，也可以是源分支上的 `/docs` 文件夹。 将更改推送到源分支时，源文件夹中的更改将发布到 GitHub Pages 站点。

如果想使用 Jekyll 以外的生成过程，或者不想使用专用分支来保存已编译的静态文件，则建议编写 GitHub Actions 工作流来发布站点。 GitHub 为常见的发布方案提供入门工作流，以帮助编写工作流。

有关详细信息，请参阅“[配置 GitHub Pages 站点的发布源](https://docs.github.com/zh/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)”。

## [静态站点生成器](https://docs.github.com/zh/pages/getting-started-with-github-pages/about-github-pages#static-site-generators)

GitHub Pages 会发布您推送到仓库的任何静态文件。 您可以创建自己的静态文件或使用静态站点生成器为您构建站点。 您还可以在本地或其他服务器上自定义自己的构建过程。

如果使用自定义生成过程或 Jekyll 以外的静态站点生成器，可以编写 GitHub Actions 来生成和发布站点。 GitHub 为多个静态站点生成器提供入门工作流。 有关详细信息，请参阅“[配置 GitHub Pages 站点的发布源](https://docs.github.com/zh/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)”。

如果从源分支发布站点，GitHub Pages 将默认使用 Jekyll 生成站点。 如果想使用 Jekyll 以外的静态站点生成器，则建议编写 GitHub Actions 来生成和发布站点。 否则，通过在发布源的根目录中创建一个名为 `.nojekyll` 的空文件来禁用 Jekyll 生成过程，然后按照静态站点生成器的说明在本地生成站点。

GitHub Pages 不支持服务器端语言，例如 PHP、Ruby 或 Python。

## [GitHub Pages 使用限制](https://docs.github.com/zh/pages/getting-started-with-github-pages/about-github-pages#github-pages-使用限制)

2016 年 6 月 15 日后创建并使用 `github.io` 域的 GitHub Pages 站点通过 HTTPS 提供服务。 如果您在 2016 年 6 月 15 日之前创建站点，您可以为站点的流量启用 HTTPS 支持。 有关详细信息，请参阅“[使用 HTTPS 保护 GitHub Pages 站点](https://docs.github.com/zh/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https)”。

### [禁止使用](https://docs.github.com/zh/pages/getting-started-with-github-pages/about-github-pages#prohibited-uses)

GitHub Pages 并非旨在用于或允许用作免费的 Web 托管服务来运行你的在线业务、电子商务站点或主要针对促进商业交易或提供商业软件即服务 (SaaS) 的任何其他网站。 GitHub Pages 站点不应该用于敏感事务，例如发送密码或信用卡号码。

此外，你对 GitHub Pages 的使用受 [GitHub 服务条款](https://docs.github.com/zh/site-policy/github-terms/github-terms-of-service)的约束，包括对快速致富计划、淫秽内容以及暴力或威胁性内容或活动的限制。

### [使用限制](https://docs.github.com/zh/pages/getting-started-with-github-pages/about-github-pages#usage-limits)

GitHub Pages 站点受到以下使用限制的约束：

- GitHub Pages 源存储库的建议限制为 1 GB。 有关详细信息，请参阅“[关于 GitHub 上的大文件](https://docs.github.com/zh/repositories/working-with-files/managing-large-files/about-large-files-on-github#file-and-repository-size-limitations)”
- 发布的 GitHub Pages 站点不得超过 1 GB。
- GitHub Pages 站点的软带宽限制为每月 100 GB。
- GitHub Pages 站点的软限制为每小时 10 次生成。 如果使用自定义 GitHub Actions 工作流生成和发布站点，则此限制不适用
- 为了为所有 GitHub Pages 站点提供一致的服务质量，可能会实施速率限制。 这些速率限制无意干扰 GitHub Pages 的合法使用。 如果你的请求触发了速率限制，你将收到相应响应，其中包含 HTTP 状态代码 `429` 以及信息性 HTML 正文。

如果您的站点超出这些使用配额，我们可能无法为您的站点提供服务；或者您可能收到来自 [GitHub 支持](https://support.github.com/contact?tags=docs-generic) 的礼貌电子邮件，建议降低站点对服务器影响的策略，包括将第三方内容分发网络 (CDN) 置于您的站点前，利用其他 GitHub 功能（如发行版）或转用可能更符合您需求的其他托管服务。

## [GitHub Pages 上的 MIME 类型](https://docs.github.com/zh/pages/getting-started-with-github-pages/about-github-pages#github-pages-上的-mime-类型)

MIME 类型是服务器发送到浏览器的标头，提供有关浏览器所请求文件性质和格式的信息。 GitHub Pages 支持数千种文件扩展名中 750 多种 MIME 类型。 支持的 MIME 类型列表是从 [mime-db 项目](https://github.com/jshttp/mime-db)生成的。

虽然无法基于每个文件或每个仓库指定自定义 MIME 类型，但您可以添加或修改 MIME 类型以在 GitHub Pages 上使用。 有关详细信息，请参阅 [mime-db 贡献指南](https://github.com/jshttp/mime-db#adding-custom-media-types)。

## [数据收集](https://docs.github.com/zh/pages/getting-started-with-github-pages/about-github-pages#data-collection)

访问 GitHub Pages 站点时，出于安全目的，无论访问者是否已登录 GitHub ，都会记录并存储访问者的 IP 地址。 有关 GitHub 的安全做法的详细信息，请参阅 [GitHub 隐私声明](https://docs.github.com/zh/site-policy/privacy-policies/github-privacy-statement)。

## [延伸阅读](https://docs.github.com/zh/pages/getting-started-with-github-pages/about-github-pages#further-reading)

- GitHub Skills 上的 [GitHub Pages](https://github.com/skills/github-pages)
- "[存储库](https://docs.github.com/zh/rest/repos#pages)"



# 创建 GitHub Pages 站点

## 本文内容

- 为站点创建仓库
- 创建站点
- 后续步骤
- 延伸阅读

您可以在新仓库或现有仓库中创建 GitHub Pages 站点。

GitHub Pages 适用于具有 GitHub Free 和组织的 GitHub Free 的公共仓库，以及具有 GitHub Pro、GitHub Team、GitHub Enterprise Cloud 和 GitHub Enterprise Server 的公共和私有仓库。 有关详细信息，请参阅“[GitHub 的产品](https://docs.github.com/zh/get-started/learning-about-github/githubs-products)”。

**注意：** 组织所有者可以限制从组织拥有的存储库发布 GitHub Pages 站点。 有关详细信息，请参阅“[管理组织的 GitHub Pages 站点发布](https://docs.github.com/zh/organizations/managing-organization-settings/managing-the-publication-of-github-pages-sites-for-your-organization)”。

## [为站点创建仓库](https://docs.github.com/zh/pages/getting-started-with-github-pages/creating-a-github-pages-site#creating-a-repository-for-your-site)

可以为站点创建存储库或选择现有存储库。

如果存储库中并非所有文件都与站点相关，且要为存储库创建 GitHub Pages 站点，则能够为站点配置发布源。 例如，可以使用专用分支和文件夹保存站点源文件，也可以使用自定义 GitHub Actions 工作流来生成和部署站点源文件。

如果拥有存储库的帐户使用组织的 GitHub Free 或 GitHub Free，存储库必须是公共的。

如果要在现有存储库中创建站点，请跳至“[创建站点](https://docs.github.com/zh/pages/getting-started-with-github-pages/creating-a-github-pages-site#creating-your-site)”一节。

1. 在任何页面的右上角，使用 下拉菜单选择“新建存储库”。![包含创建新存储库选项的下拉菜单](https://docs.github.com/assets/cb-31554/images/help/repository/repo-create.png)1. 使用“所有者”下拉菜单选择你想要拥有存储库的帐户。![“所有者”下拉菜单](https://docs.github.com/assets/cb-26658/images/help/repository/create-repository-owner.png)1. 输入仓库的名称和说明（可选）。 如果要创建用户或组织站点，则存储库必须命名为 `<user>.github.io` 或 `<organization>.github.io`。 如果您的用户或组织名称包含大写字母，您必须小写字母。 有关详细信息，请参阅“[关于 GitHub Pages](https://docs.github.com/zh/pages/getting-started-with-github-pages/about-github-pages#types-of-github-pages-sites)”。![创建存储库字段](https://docs.github.com/assets/cb-48482/images/help/pages/create-repository-name-pages.png)1. 选择仓库可见性。 有关详细信息，请参阅“[关于仓库](https://docs.github.com/zh/repositories/creating-and-managing-repositories/about-repositories#about-repository-visibility)”。![用于选择存储库可见性的单选按钮](https://docs.github.com/assets/cb-20877/images/help/repository/create-repository-public-private.png)1. 选择“使用 README 初始化此存储库”。 1. 单击“创建存储库”。

## [创建站点](https://docs.github.com/zh/pages/getting-started-with-github-pages/creating-a-github-pages-site#creating-your-site)

必须先在 GitHub 上有站点的仓库，然后才可创建站点。 如果未在现有存储库中创建站点，请参阅“[为站点创建存储库](https://docs.github.com/zh/pages/getting-started-with-github-pages/creating-a-github-pages-site#creating-a-repository-for-your-site)”。

警告：GitHub Pages 站点可以在 Internet 上公开，即使该站点的存储库是私有的。 如果站点的存储库中有敏感数据，你可能想要在发布前删除数据。 有关详细信息，请参阅“[关于仓库](https://docs.github.com/zh/repositories/creating-and-managing-repositories/about-repositories#about-repository-visibility)”。

1. 在 GitHub 上，导航到站点的仓库。 1. 确定要使用的发布源。 有关详细信息，请参阅“[配置 GitHub Pages 站点的发布源](https://docs.github.com/zh/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)”。

2. 为站点创建入口文件。 GitHub Pages 将查找 `index.html`、`index.md` 或 `README.md` 文件，作为站点的入口文件。

   如果发布源是分支和文件夹，则入口文件必须位于源分支上源文件夹的顶层。 例如，如果发布源是 `main` 分支上的 `/docs` 文件夹，则入口文件必须位于名为 `main` 的分支上的 `/docs` 文件夹。

   如果发布源是 GitHub Actions 工作流，则部署的项目必须在项目的顶层包含入口文件。 可以选择使用 GitHub Actions 工作流在工作流运行时生成入口文件，而不是将入口文件添加到存储库。 1. 配置发布源。 有关详细信息，请参阅“[配置 GitHub Pages 站点的发布源](https://docs.github.com/zh/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)”。 1. 在存储库名称下，单击 “设置”。 如果看不到“设置”选项卡，请选择 下拉菜单，然后单击“设置” 。

   ![存储库标头的屏幕截图，其中显示了选项卡。 “设置”选项卡以深橙色边框突出显示。](https://docs.github.com/assets/cb-28266/images/help/repository/repo-actions-settings.png)

3. 在边栏的“代码和自动化”部分，单击“ 页面”。

4. 若要查看已发布的网站，请在“GitHub Pages”下单击“ 访问网站”。![GitHub Pages 确认消息的屏幕截图，其中列出了站点的 URL。 在 URL 右侧，标有“访问网站”的按钮用深橙色框出。](https://docs.github.com/assets/cb-81121/images/help/pages/click-pages-url-to-preview.png)

   **注意：** 对站点的更改在推送到 GitHub 后，最长可能需要 10 分钟才会发布。 如果一小时后仍然在浏览器中看不到 GitHub Pages 站点更改，请参阅“[关于 GitHub Pages 站点的 Jekyll 构建错误](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/about-jekyll-build-errors-for-github-pages-sites)”。

5. GitHub Pages 站点是使用 GitHub Actions 工作流生成和部署的。 有关详细信息，请参阅“[查看工作流程运行历史记录](https://docs.github.com/zh/actions/monitoring-and-troubleshooting-workflows/viewing-workflow-run-history)”。

   注意：公共存储库免费使用 GitHub Actions。 如果专用存储库和内部存储库超出每月分配的免费分钟数，则会收取使用费。 有关详细信息，请参阅“[使用限制、计费和管理](https://docs.github.com/zh/actions/learn-github-actions/usage-limits-billing-and-administration)”。

**注意**：如果从分支进行发布且站点尚未自动发布，请确保具有管理员权限和经验证的电子邮件地址的人员已将站点推送到发布源。

## [后续步骤](https://docs.github.com/zh/pages/getting-started-with-github-pages/creating-a-github-pages-site#next-steps)

您可以通过创建更多新文件向网站添加更多页面。 每个文件都将在网站上与发布源相同的目录结构中。 例如，如果项目网站的发布源是 `gh-pages` 分支，并且你在 `gh-pages` 分支上创建了名为 `/about/contact-us.md` 的新文件，该文件将在 `https://<user>.github.io/<repository>/about/contact-us.html` 下。

您还可以添加主题以自定义网站的外观。 有关详细信息，请参阅“[使用 Jekyll 向 GitHub Pages 站点添加主题](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/adding-a-theme-to-your-github-pages-site-using-jekyll)”。

要更多地自定义您的站点，您可以使用 Jekyl - 内置 GitHub Pages 支持的静态站点生成器。 有关详细信息，请参阅“[关于 GitHub 页面和 Jekyll](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll)”。

## [延伸阅读](https://docs.github.com/zh/pages/getting-started-with-github-pages/creating-a-github-pages-site#further-reading)

- "[排查构建错误](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/troubleshooting-jekyll-build-errors-for-github-pages-sites)"
- “[创建和删除仓库中的分支](https://docs.github.com/zh/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository)”
- “[创建新文件](https://docs.github.com/zh/repositories/working-with-files/managing-files/creating-new-files)”





# 配置 GitHub Pages 站点的发布源

## 本文内容

- 关于发布源
- 从分支进行发布
- 使用自定义 GitHub Actions 工作流进行发布

可以将 GitHub Pages 站点配置为在将更改推送到特定分支时进行发布，也可以编写 GitHub Actions 工作流来发布站点。

谁可以使用此功能

People with admin or maintainer permissions for a repository can configure a publishing source for a GitHub Pages site.

GitHub Pages 适用于具有 GitHub Free 和组织的 GitHub Free 的公共仓库，以及具有 GitHub Pro、GitHub Team、GitHub Enterprise Cloud 和 GitHub Enterprise Server 的公共和私有仓库。 有关详细信息，请参阅“[GitHub 的产品](https://docs.github.com/zh/get-started/learning-about-github/githubs-products)”。

## [关于发布源](https://docs.github.com/zh/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#about-publishing-sources)

可以在将更改推送到特定分支时发布站点，也可以编写 GitHub Actions 工作流来发布站点。

如果不需要对站点的生成过程进行任何控制，则建议在将更改推送到特定分支时发布站点。 可以指定要用作发布源的分支和文件夹。 源分支可以是存储库中的任何分支，源文件夹可以是源分支上的存储库根目录 (`/`)，也可以是源分支上的 `/docs` 文件夹。 将更改推送到源分支时，源文件夹中的更改将发布到 GitHub Pages 站点。

如果想使用 Jekyll 以外的生成过程，或者不想使用专用分支来保存已编译的静态文件，则建议编写 GitHub Actions 工作流来发布站点。 GitHub 为常见的发布方案提供入门工作流，以帮助编写工作流。

警告：GitHub Pages 站点可以在 Internet 上公开，即使该站点的存储库是私有的。 如果站点的存储库中有敏感数据，你可能想要在发布前删除数据。 有关详细信息，请参阅“[关于仓库](https://docs.github.com/zh/repositories/creating-and-managing-repositories/about-repositories#about-repository-visibility)”。

## [从分支进行发布](https://docs.github.com/zh/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#publishing-from-a-branch)

1. 确保你要用作发布源的分支已经存在于你的存储库中。

2. 在 GitHub 上，导航到站点的仓库。 1. 在存储库名称下，单击 “设置”。 如果看不到“设置”选项卡，请选择 下拉菜单，然后单击“设置” 。

   ![存储库标头的屏幕截图，其中显示了选项卡。 “设置”选项卡以深橙色边框突出显示。](https://docs.github.com/assets/cb-28266/images/help/repository/repo-actions-settings.png)

3. 在边栏的“代码和自动化”部分，单击“ 页面”。

4. 在“生成和部署”的“源”下，选择“从分支进行部署”。

5. 在“生成和部署”的“分支”下，使用“无”或“分支”下拉菜单并选择发布源 。

   ![用于选择发布源的下拉菜单的屏幕截图](https://docs.github.com/assets/cb-47267/images/help/pages/publishing-source-drop-down.png)

6. （可选）使用下拉菜单选择发布源的文件夹。

   ![用于选择发布源的文件夹的下拉菜单的屏幕截图](https://docs.github.com/assets/cb-24510/images/help/pages/publishing-source-folder-drop-down.png)

7. 单击“保存” 。

   ![用于保存对发布源设置的更改的按钮的屏幕截图](https://docs.github.com/assets/cb-59268/images/help/pages/publishing-source-save.png)

### [从分支进行发布疑难解答](https://docs.github.com/zh/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#troubleshooting-publishing-from-a-branch)

**Note:** If your repository contains symbolic links, you will need to publish your site using a GitHub Actions workflow. For more information about GitHub Actions, see "[GitHub Actions文档](https://docs.github.com/zh/actions)."

**注意**：如果从分支进行发布且站点尚未自动发布，请确保具有管理员权限和经验证的电子邮件地址的人员已将站点推送到发布源。

如果选择任意分支上的 `docs` 文件夹作为发布源，稍后从存储库中的该分支中删除 `/docs` 文件夹，则站点不会生成，并且你将收到缺失 `/docs` 文件夹的页面生成错误消息。 有关详细信息，请参阅“[排查构建错误](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/troubleshooting-jekyll-build-errors-for-github-pages-sites#missing-docs-folder)”。

GitHub Pages 站点将始终使用 GitHub Actions 工作流程运行进行部署，即使您已将 GitHub Pages 站点配置为使用其他 CI 工具构建也是如此。 大多数外部 CI 工作流通过将生成输出提交到存储库的 `gh-pages` 分支来“部署”到 GitHub Pages，且通常包含 `.nojekyll` 文件。 发生这种情况时， GitHub Actions 工作流程将检测分支不需要构建步骤的状态，并且仅执行将站点部署到 GitHub Pages 服务器所需的步骤。

若要查找构建或部署的潜在错误，可以通过查看仓库的工作流程运行来检查 GitHub Pages 站点的工作流程运行情况。 有关详细信息，请参阅“[查看工作流程运行历史记录](https://docs.github.com/zh/actions/monitoring-and-troubleshooting-workflows/viewing-workflow-run-history)”。 有关如何在出现错误时重新运行工作流的详细信息，请参阅“[重新运行工作流程和作业](https://docs.github.com/zh/actions/managing-workflow-runs/re-running-workflows-and-jobs)”。

## [使用自定义 GitHub Actions 工作流进行发布](https://docs.github.com/zh/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#使用自定义-github-actions-工作流进行发布)

注意：使用自定义 GitHub Actions 工作流发布 GitHub Pages 站点的功能处于测试阶段，可能会发生变化。

若要将站点配置为使用 GitHub Actions 进行发布，请执行以下操作：

1. 在 GitHub 上，导航到站点的仓库。 1. 在存储库名称下，单击 “设置”。 如果看不到“设置”选项卡，请选择 下拉菜单，然后单击“设置” 。

   ![存储库标头的屏幕截图，其中显示了选项卡。 “设置”选项卡以深橙色边框突出显示。](https://docs.github.com/assets/cb-28266/images/help/repository/repo-actions-settings.png)

2. 在边栏的“代码和自动化”部分，单击“ 页面”。

3. 在“生成和部署”的“源”下，选择“GitHub Actions”。

4. GitHub 将推荐多个入门工作流。 如果已有用于发布站点的工作流，可跳过此步骤。 否则，请选择其中一个选项来创建 GitHub Actions 工作流。 有关创建自定义工作流的详细信息，请参阅“[创建自定义 GitHub Actions 工作流以发布站点](https://docs.github.com/zh/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#creating-a-custom-github-actions-workflow-to-publish-your-site)”。

   GitHub Pages 不会将特定工作流与 GitHub Pages 设置相关联。 但 GitHub Pages 设置将链接到最近部署你的站点的工作流运行。

### [创建自定义 GitHub Actions 工作流以发布站点](https://docs.github.com/zh/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#创建自定义-github-actions-工作流以发布站点)

有关 GitHub Actions 的详细信息，请参阅“[GitHub Actions文档](https://docs.github.com/zh/actions)”。

将站点配置为使用 GitHub Actions 进行发布时，GitHub 将针对常见发布方案推荐入门工作流。 工作流的一般流程如下：

1. 每当推送到存储库的默认分支，或者每当从“操作”选项卡手动运行工作流时，就会触发工作流。
2. 使用 [`actions/checkout`](https://github.com/actions/checkout) 操作签出存储库内容。
3. 如果站点需要，请生成任何静态站点文件。
4. 使用 [`actions/upload-pages-artifact`](https://github.com/actions/upload-pages-artifact) 操作将静态文件作为项目上传。
5. 如果推送到默认分支触发了工作流，请使用 [`actions/deploy-pages`](https://github.com/actions/deploy-pages) 操作来部署项目。 如果拉取请求触发了工作流，则跳过此步骤。

入门工作流使用名为 `github-pages` 的部署环境。 如果存储库尚未包含名为 `github-pages` 的环境，则自动创建该环境。 建议添加环境保护规则，确保仅默认分支可部署到该环境。 有关详细信息，请参阅“[使用环境进行部署](https://docs.github.com/zh/actions/deployment/targeting-different-environments/using-environments-for-deployment)”。

**注意**：存储库文件中的 `CNAME` 文件不会自动添加或删除自定义域。 必须通过存储库设置或 API 配置自定义域。 有关详细信息，请参阅“[管理 GitHub Pages 站点的自定义域](https://docs.github.com/zh/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site#configuring-a-subdomain)”和 [Pages API 参考文档](https://docs.github.com/zh/rest/pages#update-information-about-a-github-pages-site)。

### [使用自定义 GitHub Actions 工作流进行发布故障排除](https://docs.github.com/zh/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#使用自定义-github-actions-工作流进行发布故障排除)

有关如何对 GitHub Actions 工作流进行故障排除的信息，请参阅“[关于监控和疑难解答](https://docs.github.com/zh/actions/monitoring-and-troubleshooting-workflows/about-monitoring-and-troubleshooting)”。

# 为 GitHub 页面站点创建自定义 404 页面

您可以自定义在人们尝试访问您站点上不存在的页面时显示的 404 错误页面。

GitHub Pages 适用于具有 GitHub Free 和组织的 GitHub Free 的公共仓库，以及具有 GitHub Pro、GitHub Team、GitHub Enterprise Cloud 和 GitHub Enterprise Server 的公共和私有仓库。 有关详细信息，请参阅“[GitHub 的产品](https://docs.github.com/zh/get-started/learning-about-github/githubs-products)”。

1. 在 GitHub 上，导航到站点的仓库。 1. 导航到站点的发布来源。 有关详细信息，请参阅“[配置 GitHub Pages 站点的发布源](https://docs.github.com/zh/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)”。 1. 在文件列表上方，使用“添加文件”下拉列表，在其中单击“创建新文件” 。 “![添加文件”下拉列表中的“创建新文件”](https://docs.github.com/assets/cb-26718/images/help/repository/create_new_file.png)

2. 在“文件名”字段中，键入 `404.html` 或 `404.md`。

3. 如果将文件命名为

    

   ```
   404.md
   ```

   ，请将以下 YAML 前页添加到文件的开头：

   ```yaml
   ---
   permalink: /404.html
   ---
   ```

4. 在 YAML 前页（如果存在）下方添加要在 404 页面上显示的内容。

5. 单击“提交更改...”

6. 在“提交消息”字段中，输入简短、有意义的提交消息，以描述对文件的更改。 您可以在提交消息中将提交归于多个作者。 有关详细信息，请参阅“[创建有多个作者的提交](https://docs.github.com/zh/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/creating-a-commit-with-multiple-authors)”。

7. 如果在 GitHub.com 上有多个电子邮件地址与你的帐户关联，请单击电子邮件地址下拉菜单，然后选择要用作 Git 作者电子邮件地址的电子邮件地址。 只有经过验证的电子邮件地址才会出现在此下拉菜单中。 如果启用了电子邮件地址隐私，则 `<username>@users.noreply.github.com` 是默认提交作者的电子邮件地址。 有关详细信息，请参阅“[设置提交电子邮件地址](https://docs.github.com/zh/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address)”。![选择提交电子邮件地址](https://docs.github.com/assets/cb-114333/images/help/repository/choose-commit-email-address.png)1. 在提交消息字段下面，确定是要将提交添加到当前分支还是新分支。 如果当前分支是默认分支，则应选择为提交创建新分支，然后创建拉取请求。 有关详细信息，请参阅“[创建拉取请求](https://docs.github.com/zh/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)”。![提交分支选项](https://docs.github.com/assets/cb-27122/images/help/repository/choose-commit-branch.png)1. 单击“提交更改”或“建议更改” 。

## [延伸阅读](https://docs.github.com/zh/pages/getting-started-with-github-pages/creating-a-custom-404-page-for-your-github-pages-site#further-reading)

- Jekyll 文档中的[前页](http://jekyllrb.com/docs/frontmatter)



# 使用 HTTPS 保护 GitHub Pages 站点

## 本文内容

- 关于 HTTPS 和 GitHub Pages
- 对您的 GitHub Pages 站点强制实施 HTTPS
- 证书预配疑难解答（“证书尚未创建”错误）
- 解决具有混合内容的问题

HTTPS 增加一层加密，用于防止其他人窥探或篡改您的站点的流量。 您可对 GitHub Pages 站点强制实施 HTTPS，从而将所有 HTTP 请求透明地重定向到 HTTPS。

GitHub Pages 适用于具有 GitHub Free 和组织的 GitHub Free 的公共仓库，以及具有 GitHub Pro、GitHub Team、GitHub Enterprise Cloud 和 GitHub Enterprise Server 的公共和私有仓库。 有关详细信息，请参阅“[GitHub 的产品](https://docs.github.com/zh/get-started/learning-about-github/githubs-products)”。

拥有仓库管理员权限的人可对 GitHub Pages 站点实施 HTTPS。

## [关于 HTTPS 和 GitHub Pages](https://docs.github.com/zh/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https#关于-https-和-github-pages)

所有 GitHub Pages 站点（包括使用自定义域正确配置的站点）均支持 HTTPS 和 HTTPS 强制实施。 有关自定义域的详细信息，请参阅“[关于自定义域名和 GitHub 页面](https://docs.github.com/zh/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages)”和“[自定义域和 GitHub Pages 疑难解答](https://docs.github.com/zh/pages/configuring-a-custom-domain-for-your-github-pages-site/troubleshooting-custom-domains-and-github-pages#https-errors)”。

GitHub Pages 站点不应该用于敏感事务，例如发送密码或信用卡号码。

警告：GitHub Pages 站点可以在 Internet 上公开，即使该站点的存储库是私有的。 如果站点的存储库中有敏感数据，你可能想要在发布前删除数据。 有关详细信息，请参阅“[关于仓库](https://docs.github.com/zh/repositories/creating-and-managing-repositories/about-repositories#about-repository-visibility)”。

**注意：** RFC3280 表示通用名称的最大长度应为 64 个字符。 因此，GitHub Pages 网站的整个域名必须小于 64 个字符，才能成功创建证书。

## [对您的 GitHub Pages 站点强制实施 HTTPS](https://docs.github.com/zh/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https#对您的-github-pages-站点强制实施-https)

1. 在 GitHub 上，导航到站点的仓库。 1. 在存储库名称下，单击 “设置”。 如果看不到“设置”选项卡，请选择 下拉菜单，然后单击“设置” 。

   ![存储库标头的屏幕截图，其中显示了选项卡。 “设置”选项卡以深橙色边框突出显示。](https://docs.github.com/assets/cb-28266/images/help/repository/repo-actions-settings.png)

2. 在边栏的“代码和自动化”部分，单击“ 页面”。

3. 在 GitHub Pages 下，选择“强制实施 HTTPS”。

## [证书预配疑难解答（“证书尚未创建”错误）](https://docs.github.com/zh/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https#troubleshooting-certificate-provisioning-certificate-not-yet-created-error)

当您在 Pages 设置中设置或更改自定义域名时，系统会开始自动进行 DNS 检查。 此检查确定您的 DNS 设置是否配置为允许 GitHub 自动获取证书。 如果检查成功，GitHub 会将作业排队以从 [Let's Encrypt](https://letsencrypt.org/) 请求 TLS 证书。 收到有效证书后，GitHub 会自动将其上传到处理 Pages 的 TLS 终止的服务器。 成功完成此过程后，您的自定义域名旁边将显示一个复选标记。

该过程可能需要一些时间。 如果在单击“保存”后几分钟未完成此过程，请尝试单击自定义域名旁边的“删除” 。 重新键入域名，然后单击“保存”。 这将取消并重新启动预配过程。

## [解决具有混合内容的问题](https://docs.github.com/zh/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https#resolving-problems-with-mixed-content)

如果对 GitHub Pages 站点启用了 HTTPS，但站点的 HTML 仍通过 HTTP 引用图像、CSS 或 JavaScript，则站点将提供“混合内容”。 提供混合内容可能会降低站点的安全性，并导致在加载资产时出现问题。

要删除站点的混合内容，请在站点的 HTML 中将 `http://` 更改为 `https://`，确保所有资产都通过 HTTPS 提供。

资产通常位于以下位置：

- 如果站点使用 Jekyll，则 HTML 文件可能位于“_layouts”文件夹中。
- CSS 通常位于 HTML 文件的 `<head>` 部分。
- JavaScript 通常位于 `<head>` 部分或结束 `</body>` 标记之前。
- 图像通常位于 `<body>` 部分。

**提示：** 如果在站点的源文件中找不到你的资产，请尝试在文本编辑器或 GitHub 上搜索站点源文件中的 `http`。

### [HTML 文件中引用的资产示例](https://docs.github.com/zh/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https#examples-of-assets-referenced-in-an-html-file)

| 资产类型   | HTTP                                                         | HTTPS                                                        |
| :--------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| CSS        | `<link rel="stylesheet" href="http://example.com/css/main.css">` | `<link rel="stylesheet" href="https://example.com/css/main.css">` |
| Javascript | `<script type="text/javascript" src="http://example.com/js/main.js"></script>` | `<script type="text/javascript" src="https://example.com/js/main.js"></script>` |
| 映像       | `<a href="http://www.somesite.com"><img src="http://www.example.com/logo.jpg" alt="Logo"></a>` | `<a href="https://www.somesite.com"><img src="https://www.example.com/logo.jpg" alt="Logo"></a>` |



# 将子模块用于 GitHub Pages

您可以将子模块用于 GitHub Pages 以在站点代码中包含其他项目。

GitHub Pages 适用于具有 GitHub Free 和组织的 GitHub Free 的公共仓库，以及具有 GitHub Pro、GitHub Team、GitHub Enterprise Cloud 和 GitHub Enterprise Server 的公共和私有仓库。 有关详细信息，请参阅“[GitHub 的产品](https://docs.github.com/zh/get-started/learning-about-github/githubs-products)”。

如果 GitHub Pages 站点的仓库包含子模块，则在构建站点时会自动拉取其内容。

只能使用指向公共仓库的子模块，因为 GitHub Pages 服务器无法访问私有仓库。

对子模块（包括嵌套子模块）使用 `https://` 只读 URL。 你可以在 .gitmodules 文件中进行此更改。

## [延伸阅读](https://docs.github.com/zh/pages/getting-started-with-github-pages/using-submodules-with-github-pages#further-reading)

- *Pro Git* 书中的“[Git 工具 - 子模块](https://git-scm.com/book/en/Git-Tools-Submodules)”
- "[排查构建错误](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/troubleshooting-jekyll-build-errors-for-github-pages-sites)"



# 取消发布 GitHub Pages 站点

您可以取消发布 GitHub Pages 站点，使该站点不再可用。

谁可以使用此功能

People with admin or maintainer permissions for a repository can unpublish a GitHub Pages site.

GitHub Pages 适用于具有 GitHub Free 和组织的 GitHub Free 的公共仓库，以及具有 GitHub Pro、GitHub Team、GitHub Enterprise Cloud 和 GitHub Enterprise Server 的公共和私有仓库。 有关详细信息，请参阅“[GitHub 的产品](https://docs.github.com/zh/get-started/learning-about-github/githubs-products)”。

取消发布站点时，该站点将不再可用。 所有现有存储库设置或内容都不受影响。

1. 在 GitHub.com 上，导航到存储库的主页。
2. 在 GitHub Pages 下的“站点所在位置”消息旁，单击 。
3. 在显示的菜单中，选择“取消发布站点”。![GitHub Pages 设置的屏幕截图，其中显示了实时 Pages 站点的 URL。 在右侧的水平烤肉串图标下，“取消发布站点”下拉列表选项用深橙色框出。](https://docs.github.com/assets/cb-77368/images/help/pages/unpublish-site.png)





























































































































