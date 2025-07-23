import streamlit as st

st.set_page_config(page_title="Agentic Trader Dashboard", page_icon="📈", layout="wide")


def main():
    st.title("Agentic Trader Dashboard")

    # Sidebar for configuration
    st.sidebar.header("Configuration")
    st.sidebar.selectbox(
        "Select Strategy", ["Moving Average Crossover", "RSI", "ML-Based"]
    )

    # Main content area
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Market Overview")
        # Placeholder for market data visualization
        st.info("Market data visualization will be implemented here")

    with col2:
        st.subheader("Strategy Performance")
        # Placeholder for strategy metrics
        st.info("Strategy performance metrics will be shown here")

    # Bottom section for trades
    st.subheader("Recent Trades")
    st.info("Recent trades table will be displayed here")


if __name__ == "__main__":
    main()
