# HTML Report Guide

主文件：[04_final_report.html](04_final_report.html)。保持 **HK Technology** 主题、默认 **English** 和 **Report / 报告** 阅读模式。顶部 **Language / 语言** 可切换 English、简体中文、繁體中文；正文、图注、表格、讲稿、目录和证据说明同步切换，原始截图不改字。图片、正文、证据、样式和脚本全部内嵌，可单独发送和离线打开；从 GitHub 下载原文件后使用浏览器阅读。

## 当前版本

正文和 24 项证据取自最新 U3 更正后的 [正式报告](04_final_report.md) 与 [证据矩阵](02_evidence_matrix.md)。本轮将全部六张真实截图及图注同步加入正式 Markdown；证据矩阵的历史判断保持不变。

- 实践背景后：业务驾驶舱概览。
- 合同录入场景后：HT-2026-0007 的业务台账截图。
- 风险汇总场景后：业务项目台账及 DingTalk 保留的 10 月 10 日简报节选。
- 口语登记与通知场景后：待拍板与纠偏跟踪两项待办，以及当前风险跟踪空列表。

六张图均补采于 2026-10-15。前三张沿用原像素节选 PNG；新增三张使用浏览器直接返回的 JPEG 截图字节。钉钉完整窗口仍仅本地留存，不内嵌到 HTML。来源、原图指纹、节选指纹和证据边界见 [截图说明](07_operational_screenshot_evidence.md) 与 [图片清单](html_src/operational_image_manifest.json)。

## 阅读与打印

点击 E01–E24 查阅证据，再点击“返回引用处”返回正文。可切换 Slides / 演示，两个模式使用同一内容模型。网页内编辑后需“保存 HTML”；Markdown 不会被自动改写。

点击“打印 / PDF”按 A4 纵向打印，打印样式展开证据并隐藏控件。图片保持比例，与图注一起排版；可关闭浏览器自带页眉页脚。已有 PDF、Word 是此前未加入本版六张操作图的版本，留在本地 `.local-only/prior-exports/`，不随公开归档。

## 检查范围

[当前归档检查](qa/archive_checks.json) 绑定本版 HTML 指纹：核对 69 个正文内容块、24 项证据、六个图片位置及嵌入内容、PNG/JPEG 尺寸、脚本语法、CSP 哈希与归档链接。未引入外部资源依赖。

本版检查了三种语言 × 两种视图 × 五种视口的 30 种组合，语言控件均可见，六张截图正常加载，没有检测到文字或页面横向溢出；检查了英文证据跳转及返回引用处。测试副本使用原生保存序列化、通过本地字节捕获替代下载传输，重开后保留繁体选择和编辑内容，切换英文后仍可返回；这不代表实际浏览器下载落盘已验证。详情见 [浏览器检查](qa/browser_checks.json)。PowerPoint 实机显示、完整编辑器回归和 PDF 分页未验证，旧版打印记录不作为本版通过证据。

## 构建与维护

图片来源清单中的图注须与 Markdown 的 `screenshot:UI-xx` 标记块一致；构建器会校验二者，避免两个版本漏图或说明分叉。

`html_src/build_report.py` 从 Markdown、证据矩阵、操作图清单和 [report_locales.json](html_src/report_locales.json) 生成统一三语模型，调用 `corporate-web-slides` 1.3.0 构建器。翻译表以原文片段为键，缺失译文会阻止构建；改动原文后须同步更新并核对译文。三语共用截图、链接和几何，分页按三语所需空间计算，因此完整演示增至 74 页，Report 连续阅读仍保留原文层次。`report.css` 与 `report.js` 是任务内适配；共享 Skill 未修改或复制入仓库。[构建依赖指纹](html_src/build_dependencies.json) 记录本次使用的 Skill 文件版本。

阅读 HTML 不需要安装任何依赖。重新构建需要 Python 3 及可用的 `corporate-web-slides` 1.3.0；该内部 Skill 未随公开仓库分发，因此本仓库不是完全自包含的构建环境。Node.js 仅用于脚本语法核对。已有 Skill 的环境可从本项目目录执行：

```sh
export CORPORATE_WEB_SLIDES_SKILL="/path/to/corporate-web-slides"
python3 report/html_src/build_report.py
python3 report/qa/verify_archive.py
```

未设置环境变量时，构建器使用 `~/.codex/skills/corporate-web-slides`。`content_map.json` 记录正文、证据、图片映射及译文指纹；生成的 `deck.json` 含重复图片数据，已忽略。公开入口及范围见 [项目 README](../README.md)。

正式报告另附 [英文 PPTX](04_final_report_EN.pptx)、[简体 PPTX](04_final_report_SC.pptx)、[繁体 PPTX](04_final_report_TC.pptx) 及 [英文 POTX](04_final_report_EN.potx)。三语正文、表格、74 页讲稿和六张原始图片均经 [原生导出检查](qa/verify_report_exports.py) 核对，新增页继承内容版式已通过 OOXML 模拟检查；不是 PowerPoint 实机验收。网页阅读模式简化工具栏，在 **Edit / 编辑** 模式可见 Export PPTX / POTX。更新 HTML 后须重新导出，再运行 `python3 report/qa/verify_report_exports.py` 和归档检查；不能用旧导出替代新版结果。

## 三语主管简报

[08_management_brief.html](08_management_brief.html) 使用 **corporate-web-slides 1.3.0 原生 Report 模式**，与上面的正式报告分别维护。它把原有业务价值分析整理为 17 个阅读段落／演示页，保留五张真实截图、证据边界及科技部门借鉴；实践人员为 **Leo Zhang**。

默认英文。工具栏 **Language** 可切换简体中文、繁體中文，正文、图注、讲稿和编辑器语言同步切换，截图中的原文保持不变。**View** 可切换 Report / Slides。**Edit** 修改当前语言内容，**Save HTML** 保存可继续编辑的完整文件；切换语言后需留意其他译文的过期提示。**Export PPTX / Export POTX** 导出当前语言和最新编辑模型的演示布局，不是 Report 长网页的截图。

交付的 [英文 PPTX](08_management_brief_EN.pptx)、[简体 PPTX](08_management_brief_SC.pptx)、[繁体 PPTX](08_management_brief_TC.pptx) 和 [英文 POTX 模板](08_management_brief_EN.potx) 包含原生文字、流程形状、独立截图、17 页讲稿及通用内容母版。品牌与主题定义保留在内容模型中，便于继续维护。

唯一内容源为 [management_brief_model.json](html_src/management_brief_model.json)，通过 [build_management_brief.py](html_src/build_management_brief.py) 调用 Skill 的原生 Report 渲染器；没有另写一套报告 DOM 或翻译源。构建依赖同上，环境变量 `CORPORATE_WEB_SLIDES_SKILL` 同样适用。网页修改后保存的 HTML 包含自己的最新模型，不会自动改写仓库中的 JSON。

本版检查覆盖三种语言、Report / Slides、五种视口的 30 种组合，无检测到的文字溢出或页面横向溢出；五张截图均正常加载且与来源字节一致。已检查标题、正文、讲稿编辑，语言切换后的译文过期标记，以及复制、删除、撤销、重做。测试副本通过序列化并重新打开保留编辑；浏览器实际下载落盘未确认，不能据此视为下载链路已验证。

Office 文件使用未修改的 Skill 导出组件在本地生成；[核对脚本](qa/verify_management_brief.py) 检查了三语文字与讲稿、原图字节、包内关系、原生对象，以及新增页继承内容版式。PowerPoint 实机显示、`file://` 打开、PDF 分页及完整拖动／裁切编辑组合尚未验证。具体结果绑定当前 HTML 指纹，见 [主管简报检查记录](qa/management_brief_checks.json)。

## 提交检查说明

HK Technology 的同一张 PNG 标识在 HTML 配置和内容模型中各嵌入一次；其 Base64 恰好命中本机 ECC 的 AWS key 正则。公开仓库根目录 `.ecc-allowlist` 仅匹配该图片的完整、精确 `contentLogo` 数据行，不跳过其他字段或整个文件。静态检查另验证命中数和解码后的 PNG 指纹。未关闭或改写全局 Git 钩子。
