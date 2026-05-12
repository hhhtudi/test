import streamlit as st

# 页面配置
st.set_page_config(page_title="在线点餐系统", page_icon="🍔", layout="wide")

# 初始化购物车
if "cart" not in st.session_state:
    st.session_state.cart = {}

# 菜品数据
foods = {
    "主食": [
        {"name": "香辣鸡腿堡", "price": 18},
        {"name": "牛肉汉堡", "price": 22},
        {"name": "鸡肉卷", "price": 15}
    ],
    "小吃": [
        {"name": "薯条", "price": 10},
        {"name": "鸡米花", "price": 12},
        {"name": "鸡翅", "price": 16}
    ],
    "饮品": [
        {"name": "可乐", "price": 6},
        {"name": "雪碧", "price": 6},
        {"name": "奶茶", "price": 12}
    ]
}

# 顶部标题
st.title("🍽️ 在线点餐软件")
st.divider()

# 左右布局
left, right = st.columns([2, 1])

# 左边：点餐区域
with left:
    for category, item_list in foods.items():
        st.subheader(f"📂 {category}")
        for food in item_list:
            name = food["name"]
            price = food["price"]
            col1, col2, col3 = st.columns([3,1,1])
            col1.write(f"{name}")
            col2.write(f"¥{price}")
            if col3.button("加入", key=name):
                if name in st.session_state.cart:
                    st.session_state.cart[name]["num"] += 1
                else:
                    st.session_state.cart[name] = {"price": price, "num": 1}
        st.divider()

# 右边：购物车
with right:
    st.subheader("🛒 我的购物车")
    total = 0
    if st.session_state.cart:
        for name, info in st.session_state.cart.items():
            num = info["num"]
            price = info["price"]
            subtotal = num * price
            total += subtotal
            # 增减数量
            c1, c2, c3, c4 = st.columns([2,1,1,1])
            c1.write(name)
            c2.write(f"x{num}")
            c3.write(f"¥{subtotal}")
            if c4.button("-", key=f"del_{name}"):
                st.session_state.cart[name]["num"] -= 1
                if st.session_state.cart[name]["num"] <= 0:
                    del st.session_state.cart[name]
                st.rerun()

        st.markdown("---")
        st.success(f"💰 合计总价：¥{total}")
        if st.button("提交订单", type="primary"):
            st.info("✅ 订单提交成功！等待商家接单～")
            st.session_state.cart.clear()
            st.rerun()
    else:
        st.info("购物车空空如也，快去点餐吧～")