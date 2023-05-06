import streamlit as st




# st.latex(r'''
# a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
# \sum_{k=0}^{n-1} ar^k =
# a \left(\frac{1-r^{n}}{1-r}\right)
# ''')


def calculate_tp(risk_amount, entry, stoploss):
    result = int(risk_amount / ((entry - stoploss) * 100))
    try:
        tp1 = round(((risk_amount) + (result * (entry * 100))) / result / 100, 2)
        tp2 = round(((2 * risk_amount) + (result * (entry * 100))) / result / 100, 2)
        tp3 = round(((2.4 * risk_amount) + (result * (entry * 100))) / result / 100, 2)
        tp = f"{tp1} @1R | {tp2} @ 2Rs | {tp3} @ 2.4Rs"
    except ZeroDivisionError:
        tp = 0

    doc = f"""Risk: ${risk_amount}\n
    Entry: ${entry} / contract
    StopLoss: ${stoploss} / contract
    Qty: {result} contract(s)\n
    _____________________
    TP: ${tp}

    """
    return doc

def main():
    st.title('Risk Units Calculator')
    st.text("For Options Trading")

    col1, col2 = st.columns(2)

    with col1:
        risk_amount = st.number_input('Risk Amount', step=10,value=100)
        entry = round(st.number_input('Entry', step=0.01,value=0.5),2)
        sp_val = entry/2 if entry!=0 else 0
        sp = st.number_input('Stop Loss', step=0.01, value=sp_val)
        calculate = st.button('Calculate')

    with col2:
        if calculate:
            result = calculate_tp(risk_amount, entry, sp)
            st.text_area('Result', result, height=250)



    st.text("\n"*10)
    st.text(r'''Assumptions:
    - Risk 1% of Portfolio
    - Expected Return: 2.4R

    Formula:
    ''')
            
    st.latex(r'''Contracts = \frac{X * RiskAmount}{(Entry - StopLoss)*100}''')

    st.latex(r'''TakeProfit = 
    \frac{(2.4 * RiskAmount)+(Contracts * Entry * 100)}{Contracts/100}''')

    st.text("* Reference: RealLifeTrading - Jeremy's R units")

if __name__ == '__main__':
    main()