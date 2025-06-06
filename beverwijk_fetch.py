from funda_scraper.scrape import FundaScraper

if __name__ == "__main__":
    scraper = FundaScraper(
        area="beverwijk",
        want_to="buy",
        page_start=1,
        number_of_pages=1,
        find_sold=False,
    )
    df = scraper.run(raw_data=True)
    print(df.head())
