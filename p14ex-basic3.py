import streamlit as st


st.header("今日の料理")
st.subheader("カレーライス")
st.image("food_curryrice_white.png")

md = """
## 材料

- 肉：　300ｇ
- ジャガイモ：中２個
- 人参：小1本

## 作り方
1. 材料を切ります
2. 肉を炒めます
3. 煮込んでルーを入れます
"""
st.markdown(md)

