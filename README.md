# BG3 繁中修正版輔助工具

適用於 [柏德之門3繁中修正](https://paratranz.cn/projects/7918) 的小工具。

相關連結：[巴哈文章](https://forum.gamer.com.tw/C.php?bsn=2954&snA=5347&tnum=11)

~~需安裝 Python 並了解基本使用方式。~~

## 使用方式

使用前需先下載 ExportTool 此軟體。

可從 [Norbyte/lslib](https://github.com/Norbyte/lslib/releases) 點選下載最新 (latest) 版本的壓縮檔（如 ` ExportTool-v1.18.7.zip `） 並解壓縮。

並將 [柏德之門3繁中修正](https://paratranz.cn/projects/7918) 的所有 csv 檔案下載至 `[本資料夾]/translated` 路徑下。

### 1. 解開繁中翻譯檔案封裝

打開 ExportTool 資料夾中的 `ConverterApp.exe` 並點選到 `PAK/LSV Tools` 分頁的 `Extract Package`，按照以下設定後點選 `Extract Package` 按鈕後稍等一下即可。

**繁中翻譯**
```plain
Package path: [柏德之門 3 安裝資料夾]/Data/Localization/ChineseTraditional/ChineseTraditional.pak
Destination Path: [本資料夾]/pak/zh_tw
```

**英文原文**
```plain
Package path: [柏德之門 3 安裝資料夾]/Data/Localization/English.pak
Destination Path: [本資料夾]/pak/en
```

### 2. 將 loca 檔案轉為 xml 格式

將 ExportTool 切換到 `Localization` 分頁，分別按照以下設定，並點選 `Convert` 按鈕。

**繁中翻譯**

```plain
Input file path: [本資料夾]/pak/zh_tw/Localization/ChineseTraditional/chinesetraditional.loca
Output file path: [本資料夾]/source/chinesetraditional.xml
```

**英文原文**

```plain
Input file path: [本資料夾]/pak/en/Localization/English/english.loca
Output file path: [本資料夾]/source/english.xml
```

### 3-1. 更新 xml 翻譯檔案

執行 `python update_xml.py` 或直接執行 `update_xml.exe` 即可得到更新過的翻譯檔案 `translated/chinesetraditional.xml`。

### 3-2. 取得新增的未修正中文翻譯（非必要）

執行 `python find_new_translations.py` 或直接執行 `find_new_translations.exe` 即可取得未修正的新翻譯 `zh_tw_new_translations.csv`。

### 4. 將修正後翻譯轉回 loca 格式

回到 ExportTool `Localization` 分頁按照以下設定，並點選 `Convert` 按鈕。

```plain
Input file path: [本資料夾]/translated/chinesetraditional.xml
Output file path: [本資料夾]/pak/zh_tw/Localization/ChineseTraditional/chinesetraditional.loca
```

### 5. 封裝中文翻譯檔案

回到 ExportTool `PAK/LSV Tools` 分頁的 `Create Package` 按照以下設定並點選 `Create Package` 按鈕，即可得到封裝後檔案 `ChineseTraditional.pak`。

```plain
Source Path: [本資料夾]/pak/zh_tw
Package path: [本資料夾]/ChineseTraditional.pak
Version: V18(Baldur's Gate 3 Release)
Compression: LZ4 HC
```