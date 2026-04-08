import streamlit as st
from deep_translator import GoogleTranslator
from PIL import Image
import requests
import os
import io

# ── 頁面設定（必須是第一個 Streamlit 指令）─────────────
st.set_page_config(
    page_title="AI 書籤產生器",
    page_icon="🎨",
    layout="centered"
)

# ── 標題 ──────────────────────────────────────────────
st.title("🎨 AI 書籤產生器")
st.caption("輸入描述，AI 幫你生成獨一無二的書籤！")
st.divider()

# ── 側欄：API 金鑰設定 ─────────────────────────────────
with st.sidebar:
    st.header("⚙️ 設定")
    api_key = st.text_input(
        "Stability AI 金鑰",
        type="password",          # 輸入時隱藏文字，像密碼框
        placeholder="sk-..."
    )
    st.caption("金鑰不會被儲存，只在這次使用")
    st.divider()
    st.markdown("**藝術風格**")
    風格 = st.selectbox(
        "選擇風格",
        ["水彩插畫", "油畫風格", "日系動漫", "寫實攝影", "像素藝術"],
        label_visibility="collapsed"
    )

# ── 風格對照表 ─────────────────────────────────────────
風格對照 = {
    "水彩插畫": "watercolor illustration style",
    "油畫風格":  "oil painting style",
    "日系動漫":  "anime style, Studio Ghibli",
    "寫實攝影":  "photorealistic, high detail",
    "像素藝術":  "pixel art style",
}

# ── 主要輸入區 ─────────────────────────────────────────
描述 = st.text_input(
    "請描述你想要的書籤背景",
    placeholder="例如：星空下的螢火蟲森林，夢幻氛圍..."
)

產生按鈕 = st.button("✨ 產生書籤", use_container_width=True, type="primary")

# ── 按下按鈕後的邏輯 ───────────────────────────────────
if 產生按鈕:
    if not api_key:
        st.error("⚠️ 請在左側欄輸入 Stability AI 金鑰")
        st.stop()                  # 停止往下執行

    if not 描述.strip():
        st.error("⚠️ 請先輸入書籤描述")
        st.stop()

    # 翻譯中文 → 英文
    with st.spinner("🌐 正在翻譯描述..."):
        try:
            英文描述 = GoogleTranslator(source="zh-TW", target="en").translate(描述)
        except Exception:
            英文描述 = 描述        # 翻譯失敗就用原文

    完整prompt = (
        f"{英文描述}, {風格對照[風格]}, "
        "vertical composition, bookmark design, beautiful, detailed"
    )
    st.caption(f"📝 送出的英文描述：`{完整prompt}`")

    # 呼叫 Stability AI
    with st.spinner("🎨 AI 正在繪圖，請稍候..."):
        response = requests.post(
            "https://api.stability.ai/v2beta/stable-image/generate/core",
            headers={
                "authorization": f"Bearer {api_key}",
                "accept": "image/*",
            },
            files={"none": ""},
            data={
                "prompt": 完整prompt,
                "aspect_ratio": "9:21",
                "output_format": "png",
            },
            timeout=60
        )

    if response.status_code != 200:
        st.error(f"❌ API 錯誤 {response.status_code}：{response.text[:200]}")
        st.stop()

    # 顯示圖片
    img = Image.open(io.BytesIO(response.content))  # 把回傳資料變成圖片
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes.seek(0)                               # 把讀取位置移回開頭

    st.success("✅ 書籤生成成功！")

    # 用欄位排版：左邊放書籤圖，右邊放說明
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(img, caption="你的書籤", use_container_width=True)
    with col2:
        st.markdown("### 📥 下載書籤")
        st.download_button(
            label="下載 PNG 檔案",
            data=img_bytes,
            file_name="my_bookmark.png",
            mime="image/png",
            use_container_width=True
        )
        st.markdown("---")
        st.markdown(f"**風格：** {風格}")
        st.markdown(f"**比例：** 9:21（書籤直向）")
