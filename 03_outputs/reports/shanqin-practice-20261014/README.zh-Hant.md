# Shanqin Collaboration Practice

[English](README.md) · [简体中文](README.zh-Hans.md) · **繁體中文**

千問辦公與釘釘協同實踐的報告、證據及必要素材歸檔。實踐日期為 2026-10-10，報告日期為 2026-10-14，實際界面截圖補採於 2026-10-15。

**建議先讀 [正式報告](report/04_final_report.md) / [英文譯本](report/04_final_report_EN.md)，或下載 [離線 HTML 報告](report/04_final_report.html) 後在瀏覽器打開。** HTML 使用 HK Technology 主題，默認英文與 Report 連續閱讀模式；頂部 Language 可切換簡體中文／繁體中文。圖片、樣式和腳本全部內嵌，支持瀏覽器打印。GitHub 文件頁顯示源碼，需下載原文件閱讀。

這是個人實踐分析及管理討論材料，採用模擬業務數據；不代表所在機構的官方評估、部署決定或產品背書。HK Technology 是本次選用的視覺主題。

## 閱讀入口

本倉庫 14 份中文 Markdown 均提供英文譯本；英文是各級 README 的默認入口，頂部鏈接可切換簡體和繁體。譯本不作為新增獨立證據。

| 文件 | 用途 |
| --- | --- |
| [主管場景簡報](report/08_management_brief.html) | corporate-web-slides 原生 Report：三方協同場景、待驗證業務價值、科技部門候選用途和下一步建議；默認英文，支持簡體／繁體中文、Slides 與網頁編輯；五張原始截圖內嵌，實踐人員 Leo Zhang |
| [英文 PPTX](report/08_management_brief_EN.pptx) / [簡體 PPTX](report/08_management_brief_SC.pptx) / [繁體 PPTX](report/08_management_brief_TC.pptx) / [英文模板 POTX](report/08_management_brief_EN.potx) | 主管簡報的原生可編輯導出，17 頁及對應講稿；已核對結構、圖片及母版繼承，PowerPoint 實機顯示未驗證 |
| [正式報告 Markdown](report/04_final_report.md) / [英文譯本](report/04_final_report_EN.md) / [HTML](report/04_final_report.html) | 最新更正後的管理判斷與場景分析；HTML 默認英文、支持簡體／繁體；HTML 與中文 Markdown 同步包含六張真實界面配圖 |
| [正式報告英文 PPTX](report/04_final_report_EN.pptx) / [簡體 PPTX](report/04_final_report_SC.pptx) / [繁體 PPTX](report/04_final_report_TC.pptx) / [英文 POTX](report/04_final_report_EN.potx) | 完整報告的三語可編輯演示與英文模板；74 頁，原生文字、表格、獨立圖片及講稿；PowerPoint 實機顯示未驗證 |
| [素材清單](report/01_material_inventory.md) / [英文譯本](report/01_material_inventory_EN.md) | 實際檢查範圍、來源等級和未取得材料 |
| [證據矩陣](report/02_evidence_matrix.md) / [英文譯本](report/02_evidence_matrix_EN.md) | E01–E24，區分事實、觀察、推論與待驗證假設 |
| [獨立管理分析](report/03_management_analysis.md) / [英文譯本](report/03_management_analysis_EN.md) | 流程變化、增量價值與評估方法 |
| [待確認事項](report/05_open_questions.md) / [英文譯本](report/05_open_questions_EN.md) | 尚需補證和人工判斷的事項 |
| [HTML 使用與維護](report/06_html_readme.md) / [英文譯本](report/06_html_readme_EN.md) | 離線閱讀、打印、構建依賴與驗收邊界 |
| [操作截圖說明](report/07_operational_screenshot_evidence.md) / [英文譯本](report/07_operational_screenshot_evidence_EN.md) | 合同台帳、群簡報、待辦的來源、時間、裁剪及證明邊界 |
| [記錄索引](report/evidence/record_index.md) / [英文譯本](report/evidence/record_index_EN.md) / [事實摘錄](report/evidence/selected_factual_extracts.json) | 歷史會話的定位及必要業務返回字段 |
| [逐文件目錄](report/evidence/file_catalog.md) / [英文譯本](report/evidence/file_catalog_EN.md) / [來源指紋](report/evidence/source_manifest.json) | 原審閱的 98 個文件對象及其公開可用性；不是 98 份獨立證據 |
| [歸檔檢查](report/qa/archive_checks.json) | 當前 HTML 指紋、內容覆蓋、圖片、鏈接和腳本檢查 |

## 版本與事實口徑

最新分析以 `report/04_final_report.md` 和 `report/02_evidence_matrix.md` 為準。U3 更正保持不變：本人全程觀察千問辦公，由 AI 完成合同錄入，未點擊補充協議；已核讀日誌仍缺少具體寫入調用和確認上下文。單人演示不等於多人協作閉環，工具動作成功不等於效率收益或持續可靠性已驗證。

本目錄原有的三份千問整理稿保留原文，屬於**待核驗的歷史底稿**，其中“完整閉環”“邊界問題修復”“確認門已驗證”等強表述已在正式報告中降級或糾正：

- [原報告初稿](千问办公与钉钉协同实践-基于陕秦项目的场景观察与应用建议-初稿-2026-10-14.md) / [英文譯本](original_report_draft_EN.md)
- [原實踐素材與事實清單](实践素材与事实清单-2026-10-14.md) / [英文譯本](practice_materials_and_facts_EN.md)
- [原核心發現與管理啟示](核心发现与管理启示-2026-10-14.md) / [英文譯本](original_key_findings_EN.md)
- [必要源材料說明](source_materials/README.zh-Hant.md)：當日 AI 復盤及模擬補充協議。

舊 PDF、Word 尚未加入六張操作截圖，現移至本地 `report/.local-only/prior-exports/`，不隨公開倉庫發佈。舊瀏覽器及打印驗收也只適用於當時版本。當前正式報告已完成三語、兩種視圖和五種視口檢查，測試副本已驗證編輯後序列化保存重開，原生導出內容與截圖也已核對。實際瀏覽器下載落盤、PowerPoint 實機顯示和打印分頁仍未驗證。

## 歸檔範圍

```text
shanqin-practice-20261014/
├── README.md / README.zh-Hans.md / README.zh-Hant.md
├── .gitignore / publication_files.json
├── 三份原始千問整理稿及對應英文譯本
├── source_materials/             # M4 當日復盤、M5 模擬協議
└── report/
    ├── 01…08 文檔、正式報告與主管場景簡報
    ├── assets/published/         # 6 張真實界面截圖與節選
    ├── evidence/                 # 來源指紋、索引、事實摘錄
    ├── html_src/                 # 任務內構建代碼及內容映射
    └── qa/                      # 當前靜態檢查腳本及記錄
```

`publication_files.json` 是公開文件清單。原始 JSONL、含演示賬號和個人標識的技能包、完整窗口截圖、準備材料截圖、字體副本、重複預覽與舊導出不隨公開歸檔。完整原圖留在本地；公開 PNG 保留報告所需矩形，新補採的 JPEG 為業務網頁區域或完整業務頁；HTML 只嵌入公開配圖。截圖仍含與場景有關的顯示名和演示業務數據，不聲稱完全匿名化。

原始文件的哈希和歷史記錄行號保留。未公開來源在清單中標為本地留存，公眾無法僅憑這些定位獨立重現全部審閱。公開的事實摘錄也不是服務端審計日誌。

相關公眾號文章與分享演示仍放在個人知識庫原有 `03_outputs/articles/` 和 `03_outputs/presentations/` 分類中；它們是衍生產物，未複製到本倉庫作為新增證據。本地舊入口 `report_output/` 已遷至本目錄的 `report/`，歷史日誌中的舊路徑按此對應。

## 維護

三個 README 語言版本應同步維護。英文文檔對應的中文來源和指紋記錄在 `report/html_src/markdown_translations.json`；來源變更後需複核譯文，再更新指紋。完整英文報告沿用三語 HTML 的英文譯文，通過 `python3 report/html_src/build_english_report.py` 生成，只需 Python 3，不重建 HTML。

先更新 Markdown / 證據 / 圖片來源清單，再按 [構建說明](report/06_html_readme.md) / [英文譯本](report/06_html_readme_EN.md) 生成 HTML。原始底稿不回寫；新證據應注明採集時間、來源和適用範圍。變更公開文件範圍時同步更新 `publication_files.json`，並執行：

```sh
python3 report/qa/verify_archive.py
```

主管場景簡報是正式報告的衍生閱讀入口，不作為新增獨立證據。唯一內容源為 `report/html_src/management_brief_model.json`，三語正文、圖注和講稿共用版式與截圖。`build_management_brief.py` 調用 corporate-web-slides 1.3.0 原生 Report 構建器，共享 Skill 與網頁運行組件未修改。閱讀時無需依賴；重建需要 Python 3、Node.js 與已安裝的該 Skill：

```sh
python3 report/html_src/build_management_brief.py
python3 report/qa/verify_management_brief.py
python3 report/qa/verify_archive.py
```

修改模型後先重建 HTML，再使用網頁的 Export PPTX / Export POTX 導出各語言文件；隨後運行驗證腳本。Office 核對腳本檢查現有文件，不負責生成。重建會重置瀏覽器與 Office 驗證記錄，不能直接沿用舊版通過結論。具體操作與本次驗證邊界見 [HTML 使用與維護](report/06_html_readme.md) / [英文譯本](report/06_html_readme_EN.md)，記錄見 [主管簡報檢查](report/qa/management_brief_checks.json)。

該命令只做靜態核對，不訪問業務系統或釘釘；需要 Python 3 和 Node.js。公開倉庫為 [wwa-lab/qwen-office-collaboration-practice](https://github.com/wwa-lab/qwen-office-collaboration-practice)。
