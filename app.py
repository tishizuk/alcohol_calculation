import streamlit as st

def calculate_alcohol_volume(alcohol_percentage, target_alcohol_grams):
    """
    アルコール摂取量を計算する関数
    
    Args:
        alcohol_percentage (float): アルコール度数（%）
        target_alcohol_grams (float): 目標アルコール量（g）
    
    Returns:
        float: 摂取できるアルコール量（mL）
    """
    # アルコールの密度（g/mL）
    alcohol_density = 0.789
    
    # 摂取できるアルコール量(mL) = 目標アルコール量(g) × 100 / アルコール度数(%) / アルコールの密度(g/mL)
    alcohol_volume = (target_alcohol_grams * 100) / (alcohol_percentage * alcohol_density)
    
    return alcohol_volume

def main():
    # ページタイトル
    st.title("🍺 アルコール摂取量計算機")
    st.write("目標とするアルコール量と飲み物のアルコール度数から、摂取すべき量を計算します。")
    
    # サイドバーに計算式を表示
    st.sidebar.markdown("### 📐 計算式")
    st.sidebar.latex(r"""
    摂取できるアルコール量(mL) = \frac{目標アルコール量(g) \times 100}{アルコール度数(\%) \times アルコールの密度(g/mL)}
    """)
    st.sidebar.write("アルコールの密度: 0.789 g/mL")
    
    # 入力フォーム
    st.header("📊 計算パラメータ")
    
    col1, col2 = st.columns(2)
    
    with col1:
        alcohol_percentage = st.number_input(
            "アルコール度数 (%)",
            min_value=0.1,
            max_value=100.0,
            value=5.0,
            step=0.1,
            help="お酒のラベルに記載されているアルコールのパーセンテージを入力してください"
        )
    
    with col2:
        target_alcohol_grams = st.number_input(
            "目標アルコール量 (g)",
            min_value=0.1,
            max_value=200.0,
            value=20.0,
            step=0.1,
            help="摂取したい純アルコールの量を入力してください"
        )
    
    # 計算ボタン
    if st.button("計算実行", type="primary"):
        try:
            # 計算実行
            result = calculate_alcohol_volume(alcohol_percentage, target_alcohol_grams)
            
            # 結果表示
            st.header("🎯 計算結果")
            
            # メトリクス表示
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(
                    label="摂取すべき量",
                    value=f"{result:.1f} mL",
                    help="この量を飲むことで目標のアルコール量を摂取できます"
                )
            
            with col2:
                st.metric(
                    label="アルコール度数",
                    value=f"{alcohol_percentage}%"
                )
            
            with col3:
                st.metric(
                    label="目標アルコール量",
                    value=f"{target_alcohol_grams} g"
                )
            
            # 詳細情報
            st.info(f"""
            **計算詳細:**
            - アルコール度数: {alcohol_percentage}%
            - 目標アルコール量: {target_alcohol_grams} g
            - アルコール密度: 0.789 g/mL
            - **摂取すべき量: {result:.1f} mL**
            """)
            
            # 参考情報
            st.header("📋 参考情報")
            
            # 一般的なお酒のアルコール度数
            st.subheader("一般的なお酒のアルコール度数")
            reference_data = {
                "ビール": "4-6%",
                "ワイン": "11-15%",
                "日本酒": "15-16%",
                "焼酎": "20-25%",
                "ウイスキー": "40-43%",
                "ウォッカ": "40-50%"
            }
            
            for drink, percentage in reference_data.items():
                st.write(f"- **{drink}**: {percentage}")
            
            # 適量の目安
            st.subheader("適量の目安")
            st.warning("""
            **厚生労働省の指針:**
            - 男性: 1日平均20g程度
            - 女性: 男性の1/2-2/3程度
            
            **注意:** 個人差があります。体調や薬の服用状況によって適量は変わります。
            """)
            
        except Exception as e:
            st.error(f"計算エラーが発生しました: {str(e)}")
    
    # フッター
    st.markdown("---")
    st.markdown("### ⚠️ 注意事項")
    st.write("""
    - この計算結果は参考値です
    - 個人の体質や健康状態を考慮してください
    - 適度な飲酒を心がけましょう
    - 20歳未満の飲酒は法律で禁じられています
    """)

if __name__ == "__main__":
    main()
