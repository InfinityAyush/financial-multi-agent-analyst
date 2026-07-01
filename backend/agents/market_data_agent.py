import yfinance as yf


def market_data_agent(company_name: str):
    """
    Fetches financial data for a company using Yahoo Finance.
    """

    try:
        # Search for the company ticker
        ticker_search = yf.Search(company_name, max_results=1)

        if not ticker_search.quotes:
            return {
                "error": f"Could not find stock symbol for {company_name}"
            }

        # Example: NVIDIA -> NVDA
        symbol = ticker_search.quotes[0]["symbol"]

        # Create ticker object
        stock = yf.Ticker(symbol)

        # Get company information
        info = stock.info

        market_data = {
            "company": info.get("longName", company_name),
            "symbol": symbol,
            "current_price": info.get("currentPrice", "N/A"),
            "market_cap": info.get("marketCap", "N/A"),
            "pe_ratio": info.get("trailingPE", "N/A"),
            "fifty_two_week_high": info.get("fiftyTwoWeekHigh", "N/A"),
            "fifty_two_week_low": info.get("fiftyTwoWeekLow", "N/A"),
            "sector": info.get("sector", "N/A"),
            "industry": info.get("industry", "N/A")
        }

        return market_data

    except Exception as e:
        return {
            "error": str(e)
        }