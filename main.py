from funda_scraper.scrape import FundaScraper
from funda_scraper.searchrequest import SearchRequest

if __name__ == "__main__":
    search_params = SearchRequest(
        area="Amsterdam",
        want_to="buy",
        find_sold=False,
        page_start=90,
        number_of_pages=150,
        # min_price=500,
        # max_price=2000
    )

    scraper = FundaScraper(search_params)
    df = scraper.run(clean_data=True)
    # df.head()

    # It's also possible to to extraction separately from fetching the html pages
    # data_extractor = DataExtractor()
    # data_extractor.extract_data(search_params, run_id = "196a5756-8643-11ef-840d-a0510ba6104e", clean_data = True)
