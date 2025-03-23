
## Methodology
I built a Python scraper using Selenium that automatically browses eBay's tech deals page, scrolls down to load all listings, and collects details like titles, prices, original prices, shipping information, and product links, saving them into a CSV file for analysis. I then cleaned this data, making sure prices were consistent, handling any missing values, and calculating discounts accurately. Lastly, I explored the data visually to find patterns like peak deal hours, typical discounts, popular brands, and shipping trends, using tools such as histograms, scatter plots, and keyword analysis.

## Key Findings from EDA
- Peak Deal Times: Most deals appear around (9 AM) and (12 PM), suggesting these are optimal times for buyers to find deals.
- Pricing Trends: Most tech items were priced below $500, though a few premium products reached as high as $2,500.
- Typical Discounts: Common discounts ranged between 10% and 30%, but some standout deals offered savings of over 80%.
- Shipping Preferences: The majority of sellers provided "Free shipping," making it the preferred option among listings.
- Popular Brands: Products mentioning "Apple" and "iPhone" were especially common, highlighting their popularity among buyers.
- Best Deals: The biggest discounts were frequently on Samsung smartwatches, suggesting these items provide significant savings opportunities.

## Challenges Faced
- Handling missing data, particularly in original price fields.

## Potential Improvements
I could run the scraper longer, maybe for a week or more, to gather more detailed data and spot trends over different days.
Also, I could expand the scraper to include other eBay categories
