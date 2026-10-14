# HTML Report Guide

主文件：[04_final_report.html](04_final_report.html)。保持 **HK Technology** 主题、默认 **Report / 报告** 阅读模式。图片、正文、证据、样式和脚本全部内嵌，可单独发送和离线打开；从 GitHub 下载原文件后使用浏览器阅读。

## 当前版本

正文和 24 项证据取自最新 U3 更正后的 [正式报告](04_final_report.md) 与 [证据矩阵](02_evidence_matrix.md)。本次归档没有改写两份源文件。

- 合同录入场景后：HT-2026-0007 的业务台账截图。
- 群简报场景后：DingTalk 保留的 10 月 10 日简报节选。
- 口语登记与通知场景后：待拍板与纠偏跟踪两项待办。

三张图补采于 2026-10-15。公开版本使用原像素矩形节选 PNG；完整 JPEG 仅本地留存，不再内嵌到 HTML。来源、原图指纹、节选指纹和证据边界见 [截图说明](07_operational_screenshot_evidence.md) 与 [图片清单](html_src/operational_image_manifest.json)。

## 阅读与打印

点击 E01–E24 查阅证据，再点击“返回引用处”返回正文。可切换 Slides / 演示，两个模式使用同一内容模型。网页内编辑后需“保存 HTML”；Markdown 不会被自动改写。

点击“打印 / PDF”按 A4 纵向打印，打印样式展开证据并隐藏控件。图片保持比例，与图注一起排版；可关闭浏览器自带页眉页脚。已有 PDF、Word 是此前未加入三张操作图的版本，留在本地 `.local-only/prior-exports/`，不随公开归档。

## 检查范围

[当前归档检查](qa/archive_checks.json) 绑定本版 HTML 指纹：核对 69 个正文内容块、24 项证据、三个图片位置及嵌入内容、PNG 尺寸、脚本语法、CSP 哈希与归档链接。未引入外部资源依赖。

本轮未重新进行浏览器视觉、交互和 PDF 打印验收；旧版多尺寸阅读、编辑保存和 18 页打印记录不视为本版已通过的证据。静态检查通过不保证所有终端的字体与打印分页一致。

## 构建与维护

`html_src/build_report.py` 从 Markdown、证据矩阵和操作图清单生成统一模型，调用 `corporate-web-slides` 1.3.0 构建器。`report.css` 与 `report.js` 是任务内适配；共享 Skill 未修改或复制入仓库。[构建依赖指纹](html_src/build_dependencies.json) 记录本次使用的 Skill 文件版本。

阅读 HTML 不需要安装任何依赖。重新构建需要 Python 3 及可用的 `corporate-web-slides` 1.3.0；该内部 Skill 未随公开仓库分发，因此本仓库不是完全自包含的构建环境。Node.js 仅用于脚本语法核对。已有 Skill 的环境可从本项目目录执行：

```sh
export CORPORATE_WEB_SLIDES_SKILL="/path/to/corporate-web-slides"
python3 report/html_src/build_report.py
python3 report/qa/verify_archive.py
```

未设置环境变量时，构建器使用 `~/.codex/skills/corporate-web-slides`。`content_map.json` 记录正文、证据和图片映射；生成的 `deck.json` 含重复图片数据，已忽略。公开入口及范围见 [项目 README](../README.md)。

## 提交检查说明

HK Technology 的同一张 PNG 标识在 HTML 配置和内容模型中各嵌入一次；其 Base64 恰好命中本机 ECC 的 AWS key 正则。公开仓库根目录 `.ecc-allowlist` 仅匹配该图片的完整、精确 `contentLogo` 数据行，不跳过其他字段或整个文件。静态检查另验证命中数和解码后的 PNG 指纹。未关闭或改写全局 Git 钩子。
