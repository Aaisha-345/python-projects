import requests

def fetch_news(category=None, query=None):
    """
    Fetches live news articles using the NewsAPI service.
    Handles filters for categories or keyword searches.
    """
    # Replace with your actual NewsAPI key from https://newsapi.org/
    API_KEY = "YOUR_API_KEY_HERE"
    
    # Core URL configuration based on user choice
    if query:
        url = f"https://newsapi.org{query}&language=en&apiKey={API_KEY}"
    elif category:
        url = f"https://newsapi.org{category}&country=us&apiKey={API_KEY}"
    else:
        url = f"https://newsapi.org{API_KEY}"

    try:
        # 01. MVP Requirement: Get API payload
        res = requests.get(url)
        
        # Gracefully handle API errors (e.g., invalid key, network issue)
        if res.status_code != 200:
            print(f"\n[Error] Unable to fetch news. Server responded with status code: {res.status_code}")
            return []
            
        data = res.json()
        articles = data.get('articles', [])
        return articles

    except requests.exceptions.RequestException as e:
        print(f"\n[Network Error] Connection failed: {e}")
        return []

def display_articles(articles):
    """
    Loops through articles to extract and display title, source, and link.
    """
    # 01. MVP Requirement: Gracefully handle empty results
    if not articles:
        print("\n No articles found matching your criteria.")
        return

    print(f"\nShowing {len(articles[:5])} top results:")
    print("=" * 60)

    # 01. MVP Requirement: Extract & display title + source
    # 02. Challenge Level: Include clickable/copyable article links
    for index, article in enumerate(articles[:5], start=1):
        title = article.get('title', 'No Title Available')
        source_name = article.get('source', {}).get('name', 'Unknown Source')
        url = article.get('url', 'No Link Available')

        print(f"{index}. {title}")
        print(f"   Source: {source_name}")
        print(f"   Link: {url}")
        print("-" * 60)

def main():
    print("=== Welcome to the Simple News App ===")
    
    while True:
        print("\nSelect an option:")
        print("1. View Top General Headlines (MVP Level)")
        print("2. Filter Headlines by Category (Improve Level)")
        print("3. Search Articles by Keyword (Challenge Level)")
        print("4. Exit")
        
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == '1':
            print("\nFetching top headlines...")
            news = fetch_news()
            display_articles(news)
            
        elif choice == '2':
            # 02. Improve Level: Interactive category selection
            categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
            print("\nAvailable Categories:", ", ".join(categories))
            selected_cat = input("Enter category name: ").strip().lower()
            
            if selected_cat in categories:
                news = fetch_news(category=selected_cat)
                display_articles(news)
            else:
                print("\n[Invalid Category] Returning to main menu.")
                
        elif choice == '3':
            # 02. Challenge Level: Keyword search
            keyword = input("\nEnter search keyword: ").strip()
            if keyword:
                news = fetch_news(query=keyword)
                display_articles(news)
            else:
                print("\n[Error] Search keyword cannot be blank.")
                
        elif choice == '4':
            print("\nThank you for using the News App. Goodbye!")
            break
        else:
            print("\n[Invalid Selection] Please choose a number between 1 and 4.")

if __name__ == "__main__":
    main()