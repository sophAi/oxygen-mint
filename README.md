# Oxygen-Mint Theme (Mint-Y-Aqua Backbone)

[![GTK](https://img.shields.io/badge/GTK-3.0%20%7C%204.0%20%7C%202.0-blue.svg)](https://www.gtk.org/)
[![Desktop](https://img.shields.io/badge/Desktop-MATE%20%7C%20Cinnamon%20%7C%20XFCE-brightgreen.svg)](https://linuxmint.com/)
[![License](https://img.shields.io/badge/License-GPL--3.0-orange.svg)](LICENSE)

**Oxygen-Mint** 是一款為現代 Linux Mint 設計的高質感桌面主題。本專案以 Linux Mint 22.3 原廠官方的 **`Mint-Y-Aqua`** 為現代架構骨幹，並深度融合經典 **KDE 4 Oxygen** 的標誌性設計語彙（立體光澤、金屬質感、水晶色澤與經典湛藍天色）。

本主題兼具現代系統相容性（原生支援 GTK 3.24+、GTK 4.14+、Libadwaita、MATE Marco 與 Cinnamon）以及經典 KDE Oxygen 精緻、沉穩、立體的視覺享受。

---

## ✨ 核心特色與設計重點

### 1. 現代架構骨幹 (Mint-Y-Aqua Backbone)
- **跨版本與跨框架相容**：原生支援 **GTK 3.24.41** 與 **GTK 4.14**，完整適配 **Libadwaita 1.5 / 1.7** 與 **Cinnamon** 桌面。
- **高整合度色盤**：繼承 Mint-Y-Aqua 的湖水青藍（`@define-color accent_color #1f9ede;`），與 Oxygen 標誌性湛藍自然交融。

### 2. Oxygen 經典語彙深度融合
- **經典沉穩底色 (`#D8D8D8`) 與頂部平滑過渡**：
  視窗底色全面套用經典 Oxygen 灰底 `#D8D8D8`，搭配平滑漸層（`linear-gradient(to bottom, #e2e2e2 0%, #d8d8d8 120px, #d2d2d2 100%)`），營造沉穩高雅的層次感。
- **選單列與工具列色調一致性**：
  全面將選單列（Menubar）與工具列（Toolbar）底色統一為 `#D8D8D8`，消除突兀跳色。
- **桌面背景獨立隔離保護 (Desktop Wallpaper Isolation)**：
  特別加入隔離過濾規則，徹底保護 Caja、Nemo、Nautilus 與 XFCE 桌面管理器視窗透明度，絕不干擾或覆蓋使用者自訂桌布。
- **立體水晶按鈕 (3D Glossy Buttons)**：
  細緻雕琢按鈕高光漸層（`#ffffff` → `#ebebeb` → `#dadada`）、1px 細緻外框與內反光立體倒角，滑鼠懸停時綻放湛藍色柔和光暈。
- **原汁原味膠囊圓弧捲軸與方向按鈕 (Pill Capsule Scrollbars & Steppers)**：
  整合更新版高解析度素材（`scroll-thumb-vert.png`、`scroll-thumb-horiz.png`），捲軸等比縮放至舒適精簡的 14px（0.8x），保留半圓形膠囊端點（`border-radius: 9999px`）與微下陷底軌；前後端點完整支援經典 Oxygen 步進按鈕（垂直捲軸頂部向上 `▲`、底部向下 `▼`；水平捲軸向左 `◀`、向右 `▶`，並具備 RTL 鏡像適配）。
- **進度指示條 (Progress Bars)**：
  以 Oxygen 標誌性的天空藍 **`#A6BBCD`** 為基底，呈現多重金屬高光過渡漸層，並搭配深色凹槽底軌。
- **控制滑桿 (Scale & Slider Bars)**：
  音量、亮度等調節滑桿全面換裝 `#A6BBCD` 高光圓形滑塊與高亮填充指示軌。
- **Linux Mint / MATE 音量 OSD 彈出視窗專屬優化 (Volume & Media OSD HUD)**：
  專門為 `mate-settings-daemon`（`MsdMediaKeysWindow`）量身打造樣式：
  - 具備 12px 圓角與立體陰影的高對比 HUD 視窗框架。
  - 下陷半透明底槽（`rgba(0, 0, 0, 0.16)`）。
  - 以 **`#A6BBCD`** 為核心的亮藍立體進度條，徹底解決先前在灰底環境下音量條反白、難以辨識的對比問題。
- **視窗外框與標題列按鈕 (Marco / Metacity Window Borders)**：
  導入 Oxygen 經典圓形紅、綠、藍寶石視窗控制鈕（關閉、最大化、最小化），完美支援 MATE 的 Marco 視窗管理員。

---

## 📂 目錄結構

```
oxygen-mint/
├── .gitignore              # Git 版本控制忽略設定
├── install.sh              # 一鍵建置與安裝腳本
├── README.md               # 專案說明文件
├── src/                    # 原始碼與構建核心
│   ├── base-mint-y-aqua/   # 結合 Oxygen 質感的 Mint-Y-Aqua 核心樣式
│   │   ├── gtk-2.0/        # GTK 2 主題 (kde42-oxygen pixmap 引擎)
│   │   ├── gtk-3.0/        # GTK 3 主題 (包含 Oxygen 漸層/捲軸/OSD/桌布隔離)
│   │   ├── gtk-4.0/        # GTK 4 主題 (相容現代 GTK4 / Libadwaita 軟體)
│   │   ├── libadwaita-1.5/ # Libadwaita 1.5 樣式支援
│   │   ├── libadwaita-1.7/ # Libadwaita 1.7 樣式支援
│   │   ├── metacity-1/     # Marco / Metacity 視窗按鈕與裝飾
│   │   ├── cinnamon/       # Cinnamon 桌面樣式
│   │   ├── xfwm4/          # Xfce 視窗裝飾
│   │   ├── openbox-3/      # Openbox 樣式
│   │   └── index.theme     # 主題定義檔 (Name=Oxygen-Mint)
│   └── build-themes.py     # 主題編譯、打包與同步安裝腳本
└── usr/
    └── share/
        └── themes/
            └── Oxygen-Mint/ # 編譯產出的完整發行主題包
```

---

## 🚀 安裝方式

### 方式一：一鍵快速安裝 (推薦)

克隆專案後，直接於專案根目錄執行安裝腳本：

```bash
git clone https://github.com/sophAi/oxygen-mint.git
cd oxygen-mint
./install.sh
```

該腳本會自動呼叫建置程式，將主題安裝至使用者主題目錄 `~/.themes/Oxygen-Mint`。

### 方式二：手動重新建置

如需修改樣式檔案（CSS/RC）並重新編譯：

```bash
cd oxygen-mint/src
python3 build-themes.py
```

`build-themes.py` 會自動：
1. 將樣式組裝並輸出至 `usr/share/themes/Oxygen-Mint/`。
2. 同步安裝/覆蓋至目前使用者的個人目錄 `~/.themes/Oxygen-Mint/`。
3. 自動設定相應檔案讀取權限（`chmod -R a+rX`）。

---

## 🎨 如何套用主題

### Linux Mint (MATE 桌面環境)
1. 開啟 **控制中心 (Control Center)** → **外觀 (Appearance)**。
2. 在「主題」分頁中選取 **`Oxygen-Mint`** 即可立即套用！
3. 若需微調視窗標題列按鈕，可在「自訂 (Customize)」中確認「視窗邊框」已選取 `Oxygen-Mint`。

### Linux Mint (Cinnamon 桌面環境)
1. 開啟 **系統設定 (System Settings)** → **主題 (Themes)**。
2. 將「應用程式 (Applications)」、「視窗邊框 (Window borders)」及「桌面 (Desktop)」選取為 **`Oxygen-Mint`**。

### XFCE 桌面環境
1. 開啟 **設定 (Settings)** → **外觀 (Appearance)**，選取 `Oxygen-Mint`。
2. 開啟 **視窗管理員 (Window Manager)**，將樣式設為 `Oxygen-Mint`。

---

## 🛠️ 系統需求

- **作業系統**：Linux Mint 22.3+（亦相容 Ubuntu 24.04 LTS、Debian 12+ 等系統）
- **環境依賴**：
  - `python3`（用於執行安裝與打包腳本）
  - `gtk2-engines-pixbuf`（若需執行傳統 GTK 2 應用程式）

---

## 📜 授權協議 (License)

本專案衍生自 Linux Mint 官方主題 `Mint-Y-Aqua` 與經典 `KDE Oxygen`：
- 主題骨架與樣式依循 **GPL-3.0** 授權條款。
- 部分圖標與 Oxygen 原始素材遵循 **LGPL-2.1+** 授權條款。
