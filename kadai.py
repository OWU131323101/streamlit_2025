import streamlit as st
from datetime import datetime, date
import random

if 'history' not in st.session_state:
    st.session_state.history = []

def get_zodiac(birthday):
    month = birthday.month
    day = birthday.day

    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "水瓶座"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "魚座"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "牡羊座"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "牡牛座"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "双子座"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "蟹座"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "獅子座"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "乙女座"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "天秤座"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "蠍座"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "射手座"
    else:
        return "山羊座"

# ラッキーカラーの辞書
lucky_colors = {
    "楽しい": {"name": "黄色", "hex": "#FFD700", "image": "yellow.jpg"},
    "普通": {"name": "青色", "hex": "#1E90FF", "image": "blue.jpg"},
    "悲しい": {"name": "灰色", "hex": "#808080", "image": "gray.jpg"},
    "イライラ": {"name": "赤色", "hex": "#DC143C", "image": "red.jpg"},
    "疲れた": {"name": "緑色", "hex": "#3CB371", "image": "green.jpg"},
    "ワクワク": {"name": "オレンジ色", "hex": "#FFA500", "image": "orange.jpg"},
    "落ち着いている": {"name": "紫色", "hex": "#9370DB", "image": "purple.jpg"},
}

# 星座ごとの占い結果
horoscope = {
    "水瓶座": ["今日は新しい挑戦が吉！", "友達との時間を大切にしましょう。", "リラックスする時間を作りましょう。"],
    "魚座": ["直感を信じて行動すると良い結果が！", "感謝の気持ちを忘れずに。", "新しい趣味を始めるのに最適な日です。"],
    "牡羊座": ["積極的な行動が成功を呼びます！", "健康に気をつけてください。", "周囲の人に優しく接しましょう。"],
    "牡牛座": ["計画を立てると良い結果が得られます。", "自然の中で過ごすとリフレッシュできます。", "新しい出会いがあるかも。"],
    "双子座": ["コミュニケーションが鍵となる日です。", "好奇心を大切にしましょう。", "新しいアイデアが浮かびそうです。"],
    "蟹座": ["家族との時間を大切にしましょう。", "感情を整理する時間を作りましょう。", "自分を信じて行動してください。"],
    "獅子座": ["リーダーシップを発揮するチャンス！", "自信を持って進みましょう。", "楽しい出来事が待っています。"],
    "乙女座": ["細かい作業に集中すると良い結果が。", "整理整頓をすると気分が良くなります。", "新しいスキルを学ぶのに良い日です。"],
    "天秤座": ["バランスを大切にしましょう。", "人間関係が良好になる日です。", "美しいものに触れると幸せを感じます。"],
    "蠍座": ["深い洞察力が役立つ日です。", "秘密を守ることが重要です。", "新しい挑戦が待っています。"],
    "射手座": ["冒険心を大切にしましょう。", "旅行の計画を立てると良いかも。", "楽観的な気持ちで過ごしましょう。"],
    "山羊座": ["目標に向かって努力すると成功します。", "責任感を持って行動しましょう。", "自分のペースで進むことが大切です。"]
}

st.title("占いサイト")
# 時間によってあいさつを変更
now = datetime.now()
hour = now.hour
if 5 <= hour < 12:
    greeting = "おはようございます！"
elif 12 <= hour < 18:
    greeting = "こんにちは！"
elif 18 <= hour < 22:
    greeting = "こんばんは！"
else:
    greeting = "遅くまでお疲れ様です！"

# キャプション
st.caption(f"{greeting}今日の運勢を占ってみましょう！")

# 基本事項の入力
with st.form("user_inform"):
    with st.expander("入力フォーム"):
        #名前
        name = st.text_input("名前")

        #誕生日
        birthday = st.date_input(
            label="誕生日を選択してください",
            value=date(2004, 1, 1), # デフォルト値
            min_value=date(1960, 1, 1), # 誕生日の最小値
            max_value=date.today(), # 誕生日の最大値は今日の日付
            help="カレンダーから日付を選択してください"
        )

        #気分
        mood = st.selectbox("今の気分を選択してください", options=lucky_colors.keys())
    
        #ボタン表示
        submitted = st.form_submit_button("占う")

# 出力用
if  submitted:
    # 名前が入力されていない場合のエラーメッセージ
    if not name:
        st.error("名前を入力してください")
        st.stop()

    st.success(f"{name}さん、診断結果が表示されました！")
    st.balloons()

    zodiac = get_zodiac(birthday)
    fortune = random.choice(horoscope[zodiac])
    lucky_color_info = lucky_colors[mood]
    color_name = lucky_color_info["name"]
    color_hex = lucky_color_info["hex"]

    result_data = {
        "name": name,
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M'),
        "birthday": birthday.strftime('%Y年%m月%d日'),
        "zodiac": zodiac,
        "fortune": fortune,
        "mood": mood,
        "color_name": color_name,
        "color_hex": color_hex
        }
    st.session_state.history.insert(0, result_data)
        
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        # ランダムに占い結果を選択
        st.subheader("今日の運勢")
        st.write(f"**{zodiac}のあなた**")
        st.write(f" {fortune}")

    with col2:
        # 選択された気分に基づいてラッキーカラーを取得
        st.subheader("今日のラッキーカラー")
        lucky_color = lucky_color_info.get("color", "")
        lucky_image = lucky_color_info.get("image", "")

        st.markdown(
            f'<div style="background-color:{color_hex}; color:white; padding: 20px; border-radius: 10px; text-align: center; font-size: 24px; font-weight: bold;">{color_name}</div>',
            unsafe_allow_html=True
        )
        if lucky_image:
            st.image(lucky_image, width=300, caption=f"{color_name}のモノを探してみましょう！")
               
    st.write("良い一日になりますように！")
    st.markdown("---")
     
    with st.expander("占い結果の履歴を見る", expanded=False):
        if not st.session_state.history:
            st.write("まだ履歴はありません。")
        else:
            if st.button("履歴をクリア"):
                st.session_state.history = []
                st.rerun()

            for idx, entry in enumerate(st.session_state.history):
                st.markdown(f"**{len(st.session_state.history) - idx}. {entry['timestamp']}の占い結果 ({entry['name']}さん)**")
                st.markdown(f"""
                - **運勢:** {entry['fortune']} 
                - **気分:** {entry['mood']}
                - **ラッキーカラー:** <span style='color:{entry['color_hex']}; font-weight:bold;'>{entry['color_name']}</span>
                """, unsafe_allow_html=True)
                st.markdown("---")