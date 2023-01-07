# Lambda

## About
In political campaigns data is becoming an ever important resource. When planning door knocking campaigns to talk with residents a database is untilized to store address and home owner information. This allows the orginizers to tier homes and ensure time is not wasted bothering residents who do not want to support the campaign. However when this residents move this information is not updated and them can remain "tiered out". The goal for this project is to demonstrate a potential solution for this problem. Rental (and housing sale) information is gathered from websites on homes in specific areas. This information can then be used to update stistical models to reflect the world more accuratly. For now we will be pulling simply rental listings from rentfaster, but this is expected to expand into the future to also include home sales.

Scraping methodology for Rent Faster originally adopted from [this](https://rpubs.com/calebbraun/rentfaster) R project.

## Roadmap

**Version 0**
Version 0 will scape data from RentFaster to be export addresses in a targeted search area to a CSV file using a python script

**Version 1**
Version 1 will integrate more functionality including the ability to specific more peramters and be offered in a command line tool package

**Version 2**
Version 2 will expand on version 1 to include the ability to search through multiple sites

**Version 3**
Version 3 will introduce a Web Interface for the scraper to make it more accessable and easy to use

**Version 4**
Version 4 will introduce the option to be offered as a SaaS to search listings and offer other benifical campaign planning solutions and integrations

For more information read the whitepaper here!

## Disclaimer
Only webscrape with premission from the website owner. Running this script and/or program may violate terms and conditions of websites, code is provided for educational purposes only. The uses takes al responsibility over ensuring their use of this tool complies with website terms and all applicable laws and regulations.
