# Shanqin Collaboration Practice

[English](README.md) · **简体中文** · [繁體中文](README.zh-Hant.md)

千问办公与钉钉协同实践的报告、证据及必要素材归档。实践日期为 2026-10-10，报告日期为 2026-10-14，实际界面截图补采于 2026-10-15。

**建议先读 [正式报告](report/04_final_report.md) / [英文译本](report/04_final_report_EN.md)，或下载 [离线 HTML 报告](report/04_final_report.html) 后在浏览器打开。** HTML 使用 HK Technology 主题，默认英文与 Report 连续阅读模式；顶部 Language 可切换简体中文／繁體中文。图片、样式和脚本全部内嵌，支持浏览器打印。GitHub 文件页显示源码，需下载原文件阅读。

这是个人实践分析及管理讨论材料，采用模拟业务数据；不代表所在机构的官方评估、部署决定或产品背书。HK Technology 是本次选用的视觉主题。

## 阅读入口

本仓库 14 份中文 Markdown 均提供英文译本；英文是各级 README 的默认入口，顶部链接可切换简体和繁体。译本不作为新增独立证据。

| 文件 | 用途 |
| --- | --- |
| [主管场景简报](report/08_management_brief.html) | corporate-web-slides 原生 Report：三方协同场景、待验证业务价值、科技部门候选用途和下一步建议；默认英文，支持简体／繁體中文、Slides 与网页编辑；五张原始截图内嵌，实践人员 Leo Zhang |
| [英文 PPTX](report/08_management_brief_EN.pptx) / [简体 PPTX](report/08_management_brief_SC.pptx) / [繁体 PPTX](report/08_management_brief_TC.pptx) / [英文模板 POTX](report/08_management_brief_EN.potx) | 主管简报的原生可编辑导出，17 页及对应讲稿；已核对结构、图片及母版继承，PowerPoint 实机显示未验证 |
| [正式报告 Markdown](report/04_final_report.md) / [英文译本](report/04_final_report_EN.md) / [HTML](report/04_final_report.html) | 最新更正后的管理判断与场景分析；HTML 默认英文、支持简体／繁体；HTML 与中文 Markdown 同步包含六张真实界面配图 |
| [正式报告英文 PPTX](report/04_final_report_EN.pptx) / [简体 PPTX](report/04_final_report_SC.pptx) / [繁体 PPTX](report/04_final_report_TC.pptx) / [英文 POTX](report/04_final_report_EN.potx) | 完整报告的三语可编辑演示与英文模板；74 页，原生文字、表格、独立图片及讲稿；PowerPoint 实机显示未验证 |
| [素材清单](report/01_material_inventory.md) / [英文译本](report/01_material_inventory_EN.md) | 实际检查范围、来源等级和未取得材料 |
| [证据矩阵](report/02_evidence_matrix.md) / [英文译本](report/02_evidence_matrix_EN.md) | E01–E24，区分事实、观察、推论与待验证假设 |
| [独立管理分析](report/03_management_analysis.md) / [英文译本](report/03_management_analysis_EN.md) | 流程变化、增量价值与评估方法 |
| [待确认事项](report/05_open_questions.md) / [英文译本](report/05_open_questions_EN.md) | 尚需补证和人工判断的事项 |
| [HTML 使用与维护](report/06_html_readme.md) / [英文译本](report/06_html_readme_EN.md) | 离线阅读、打印、构建依赖与验收边界 |
| [操作截图说明](report/07_operational_screenshot_evidence.md) / [英文译本](report/07_operational_screenshot_evidence_EN.md) | 合同台账、群简报、待办的来源、时间、裁剪及证明边界 |
| [记录索引](report/evidence/record_index.md) / [英文译本](report/evidence/record_index_EN.md) / [事实摘录](report/evidence/selected_factual_extracts.json) | 历史会话的定位及必要业务返回字段 |
| [逐文件目录](report/evidence/file_catalog.md) / [英文译本](report/evidence/file_catalog_EN.md) / [来源指纹](report/evidence/source_manifest.json) | 原审阅的 98 个文件对象及其公开可用性；不是 98 份独立证据 |
| [归档检查](report/qa/archive_checks.json) | 当前 HTML 指纹、内容覆盖、图片、链接和脚本检查 |

## 版本与事实口径

最新分析以 `report/04_final_report.md` 和 `report/02_evidence_matrix.md` 为准。U3 更正保持不变：本人全程观察千问办公，由 AI 完成合同录入，未点击补充协议；已核读日志仍缺少具体写入调用和确认上下文。单人演示不等于多人协作闭环，工具动作成功不等于效率收益或持续可靠性已验证。

本目录原有的三份千问整理稿保留原文，属于**待核验的历史底稿**，其中“完整闭环”“边界问题修复”“确认门已验证”等强表述已在正式报告中降级或纠正：

- [原报告初稿](千问办公与钉钉协同实践-基于陕秦项目的场景观察与应用建议-初稿-2026-10-14.md) / [英文译本](original_report_draft_EN.md)
- [原实践素材与事实清单](实践素材与事实清单-2026-10-14.md) / [英文译本](practice_materials_and_facts_EN.md)
- [原核心发现与管理启示](核心发现与管理启示-2026-10-14.md) / [英文译本](original_key_findings_EN.md)
- [必要源材料说明](source_materials/README.zh-Hans.md)：当日 AI 复盘及模拟补充协议。

旧 PDF、Word 尚未加入六张操作截图，现移至本地 `report/.local-only/prior-exports/`，不随公开仓库发布。旧浏览器及打印验收也只适用于当时版本。当前正式报告已完成三语、两种视图和五种视口检查，测试副本已验证编辑后序列化保存重开，原生导出内容与截图也已核对。实际浏览器下载落盘、PowerPoint 实机显示和打印分页仍未验证。

## 归档范围

```text
shanqin-practice-20261014/
├── README.md / README.zh-Hans.md / README.zh-Hant.md
├── .gitignore / publication_files.json
├── 三份原始千问整理稿及对应英文译本
├── source_materials/             # M4 当日复盘、M5 模拟协议
└── report/
    ├── 01…08 文档、正式报告与主管场景简报
    ├── assets/published/         # 6 张真实界面截图与节选
    ├── evidence/                 # 来源指纹、索引、事实摘录
    ├── html_src/                 # 任务内构建代码及内容映射
    └── qa/                      # 当前静态检查脚本及记录
```

`publication_files.json` 是公开文件清单。原始 JSONL、含演示账号和个人标识的技能包、完整窗口截图、准备材料截图、字体副本、重复预览与旧导出不随公开归档。完整原图留在本地；公开 PNG 保留报告所需矩形，新补采的 JPEG 为业务网页区域或完整业务页；HTML 只嵌入公开配图。截图仍含与场景有关的显示名和演示业务数据，不声称完全匿名化。

原始文件的哈希和历史记录行号保留。未公开来源在清单中标为本地留存，公众无法仅凭这些定位独立重现全部审阅。公开的事实摘录也不是服务端审计日志。

相关公众号文章与分享演示仍放在个人知识库原有 `03_outputs/articles/` 和 `03_outputs/presentations/` 分类中；它们是衍生产物，未复制到本仓库作为新增证据。本地旧入口 `report_output/` 已迁至本目录的 `report/`，历史日志中的旧路径按此对应。

## 维护

三个 README 语言版本应同步维护。英文文档对应的中文来源和指纹记录在 `report/html_src/markdown_translations.json`；来源变更后需复核译文，再更新指纹。完整英文报告沿用三语 HTML 的英文译文，通过 `python3 report/html_src/build_english_report.py` 生成，只需 Python 3，不重建 HTML。

先更新 Markdown / 证据 / 图片来源清单，再按 [构建说明](report/06_html_readme.md) / [英文译本](report/06_html_readme_EN.md) 生成 HTML。原始底稿不回写；新证据应注明采集时间、来源和适用范围。变更公开文件范围时同步更新 `publication_files.json`，并执行：

```sh
python3 report/qa/verify_archive.py
```

主管场景简报是正式报告的衍生阅读入口，不作为新增独立证据。唯一内容源为 `report/html_src/management_brief_model.json`，三语正文、图注和讲稿共用版式与截图。`build_management_brief.py` 调用 corporate-web-slides 1.3.0 原生 Report 构建器，共享 Skill 与网页运行组件未修改。阅读时无需依赖；重建需要 Python 3、Node.js 与已安装的该 Skill：

```sh
python3 report/html_src/build_management_brief.py
python3 report/qa/verify_management_brief.py
python3 report/qa/verify_archive.py
```

修改模型后先重建 HTML，再使用网页的 Export PPTX / Export POTX 导出各语言文件；随后运行验证脚本。Office 核对脚本检查现有文件，不负责生成。重建会重置浏览器与 Office 验证记录，不能直接沿用旧版通过结论。具体操作与本次验证边界见 [HTML 使用与维护](report/06_html_readme.md) / [英文译本](report/06_html_readme_EN.md)，记录见 [主管简报检查](report/qa/management_brief_checks.json)。

该命令只做静态核对，不访问业务系统或钉钉；需要 Python 3 和 Node.js。公开仓库为 [wwa-lab/qwen-office-collaboration-practice](https://github.com/wwa-lab/qwen-office-collaboration-practice)。
