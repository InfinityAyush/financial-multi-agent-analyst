import yfinance as yf


def news_agent(company_name: str):

    try:
        search = yf.Search(company_name, news_count=5)

        news_items = []

        for article in search.news[:5]:

            news_items.append(
                {
                    "title": article.get("title"),
                    "publisher": article.get("publisher"),
                    "link": article.get("link")
                }
            )

        return {
            "company": company_name,
            "news": news_items
        }

    except Exception as e:
        return {
            "error": str(e)
        }