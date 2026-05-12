import streamlit as st

st.set_page_config(page_title="房贷计算器", page_icon="🏠", layout="centered")
st.title("🏠 房贷计算器 APP")
st.divider()

# 输入区域
loan_money = st.number_input("贷款金额（元）", min_value=10000, value=1000000, step=10000)
year = st.slider("贷款年限（年）", min_value=1, max_value=30, value=20)
rate = st.number_input("年利率（%）", min_value=1.0, max_value=8.0, value=3.8, step=0.01)
mode = st.radio("还款方式", ["等额本息", "等额本金"])

# 计算
month = year * 12
month_rate = rate / 100 / 12

if st.button("开始计算", type="primary"):
    st.divider()
    st.subheader("📊 计算结果")

    if mode == "等额本息":
        # 等额本息公式
        month_pay = loan_money * month_rate * (1 + month_rate) ** month / ((1 + month_rate) ** month - 1)
        total_pay = month_pay * month
        total_interest = total_pay - loan_money

        st.info(f"每月固定月供：{month_pay:,.2f} 元")
        st.info(f"还款总额：{total_pay:,.2f} 元")
        st.info(f"总利息：{total_interest:,.2f} 元")

    else:
        # 等额本金公式
        first_month = loan_money / month + loan_money * month_rate
        min_month = loan_money / month + (loan_money - loan_money / month * (month - 1)) * month_rate
        total_interest = (month + 1) * loan_money * month_rate / 2
        total_pay = loan_money + total_interest

        st.info(f"首月月供：{first_month:,.2f} 元")
        st.info(f"每月递减：{(loan_money/month * month_rate):,.2f} 元")
        st.info(f"末月月供：{min_month:,.2f} 元")
        st.info(f"还款总额：{total_pay:,.2f} 元")
        st.info(f"总利息：{total_interest:,.2f} 元")

st.divider()
st.caption("© 房贷计算器 | AI开发自制APP")