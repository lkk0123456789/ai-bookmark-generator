# 🎨 AI 書籤產生器

一個基於 AI 的書籤圖片生成工具，讓你只需輸入中文描述，就能獲得獨一無二的精美書籤圖案！

## ✨ 功能介紹

### 🖼️ AI 圖片生成
- 使用 [Stability AI](https://stability.ai/) 的 Stable Image Core API 來生成高品質圖片
- 書籤採用 **9:21 直向比例**，完美符合真實書籤的尺寸

### 🌐 自動中翻英
- 使用者只需輸入**中文描述**，系統會自動透過 Google Translate 翻譯成英文再送給 AI
- 不需要擔心英文 prompt 怎麼寫！

### 🎨 多種藝術風格
可從以下風格中選擇，讓書籤更有個人特色：

| 風格名稱 | 說明 |
|----------|------|
| 水彩插畫 | 柔和、透明感的水彩繪畫效果 |
| 油畫風格 | 厚重、細膩的古典油畫質感 |
| 日系動漫 | 宮崎駿吉卜力風格的日系動漫畫風 |
| 寫實攝影 | 高細節、接近真實照片的寫實風格 |
| 像素藝術 | 復古遊戲風格的像素藝術 |

### 📥 一鍵下載
- 生成完成後可直接**下載 PNG 格式**的書籤圖片，方便列印或分享

## 🚀 快速開始

### 環境需求

- Python 3.8+
- Stability AI API 金鑰（可至 [platform.stability.ai](https://platform.stability.ai/) 申請）

### 安裝步驟

1. **複製專案**
   ```bash
   git clone https://github.com/lkk0123456789/ai-bookmark-generator.git
   cd ai-bookmark-generator
   ```

2. **安裝依賴套件**
   ```bash
   pip install -r requirements.txt
   ```

3. **啟動應用程式**
   ```bash
   streamlit run bookmark_web.py
   ```

4. 開啟瀏覽器前往 `http://localhost:8501`

## 🧑‍💻 使用方式

1. 在左側欄輸入你的 **Stability AI 金鑰**
2. 選擇喜歡的**藝術風格**
3. 在主畫面輸入書籤的**中文描述**（例如：「星空下的螢火蟲森林，夢幻氛圍」）
4. 點擊 **✨ 產生書籤**，等待 AI 繪圖
5. 圖片生成後，點擊**下載 PNG 檔案**儲存書籤

## 🛠️ 技術架構

| 套件 | 用途 |
|------|------|
| [Streamlit](https://streamlit.io/) | 網頁介面框架 |
| [Stability AI API](https://stability.ai/) | AI 圖片生成 |
| [deep-translator](https://github.com/nidhaloff/deep-translator) | 中文翻譯成英文 |
| [Pillow](https://pillow.readthedocs.io/) | 圖片處理 |
| [Requests](https://docs.python-requests.org/) | HTTP API 請求 |

## 📋 注意事項

- API 金鑰**不會被儲存**，每次使用需重新輸入
- 圖片生成需要約 10～30 秒，請耐心等待
- 使用 Stability AI API 需要消耗額度，請留意帳戶餘額
