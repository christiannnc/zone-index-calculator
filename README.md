# What is this project?

For my Economics research seminar we had to complete a microeconomics exercise. My partner and I chose to do our project on rent in several different U.S. cities. We suspected that zoning regulations (what can and cannot be built on areas of land) play the biggest role in determining rent, and decided to create a "zone index" for each city to capture these effects.

The problem was each city does zoning a little differently, and each city also has thousands (sometimes even tens of thousands!) of zones. This project is a simple script that I set up to programatically calculate the zoning index for each city, which we were then able to add to our dataset.

## Getting started

If you are interested in running this project on your local, it is very easy to get set up. Simply clone this repo, then run `calculator.py`.

This repo has some datasets included already for cities like Los Angeles, Raleigh, and Denver. These datasets are **not** up-to-date, and are unchanged as of 02/06/2025.

### Adding more cities

To add more cities, there are a couple of manual steps that must be taken. This process if rather tedious because every city has its own unique zoning codes and regulations. However, this was the best solution given the time constraint and other requirements for the research project.

First, you must find a zoning CSV file for the city of interest. Most cities make this information easily accessible to the public, and you can typically find it by Googling something like "[city] zoning dataset csv". Once you have this dataset, rename it to '[city]\_zoning.csv' and add it to the `data` directory.

You must then update the `initialize()` function in `cities.py`. Add a new key to the dictionary, which will be the name of the city (this should match the prefix of the filename, for example if your filename is atlanta_zoning.csv, the key should be 'atlanta').

Next you must categorize the city's residential zone codes into low, medium, or high density. Additionally, some cities have mixed-use downtown zones (such as Raleigh's DX-20 and DX-40 zones) that are a combination of commercial, residential, or both types of buildings. These are categorized as alternative high density, or `ALT_HIGH`.

The following properties must be updated for the new city:

- **population** - the population of the city
- **area_key** - the key the dataset uses to identify each zone's area
- **zone_code_key** - the key the dataset uses to identify each zone's code
- **requires_area_conversion** - some datasets use feet instead of acres, in which case this property should be `True`, otherwise `False`
- **index** - the zone index; should be `0` to start and will be calculated by the program
- **area** - the total area of the city; should be `0` to start and will be calculated by the program
- **drop** - indicates a key that should trigger a row to be dropped if it is n/a

Again, this process is somewhat lengthy because there is no one-size-fits-all approach to zoning codes and/or regulations. However, when adding a new city the most important part is ensuring that the new city matches the same format as the existing cities in the `initialize()` function.

## A bit more about the zone index

Note: This section is more economics-based, but I felt I would include it for those who are interested.

I think the best way to describe the zoning index in more detail is to provide an excerpt from our research paper. Here is how we described it in that paper:

> A zoning index variable was also created to capture the effects that zoning regulations have on the supply of housing and how rent is impacted. Zoning regulations govern what can be built on “zones” of land in the United States. It is estimated that 70% of residential zones are zoned for low density housing. That is, on 70% of residential land in the U.S. it is illegal to build anything other than low density housing (typically single-family, detached homes). This can put significant pressure on the supply of housing, and we estimate that the result is a positive relationship with rent.
>
> Our zoning index attempts to represent the pressure placed on zoning to accommodate the population. It is calculated by dividing a municipality’s population by a weighted sum of the distributions of low, medium, and high density housing. The weights punish lower density housing, and reward higher density housing. As a result, a higher zoning index indicates that a city has more low density housing compared to a city with a lower zoning index.
>
> The value of the weights, which were determined with theory, are 0.1, 0.3, and 0.9 for low, medium, and high density zones, respectively. The reason the low density housing weight is 0.1 as opposed to 0 is because we did not want to completely eliminate its effects—it is less desirable than medium or high density housing, but it is still housing. Similarly, the reason for the high density housing weight of 0.9 as opposed to 1 is because land being zoned for high density housing says nothing about whether buildings on that land meet the maximum size allowances for that zone. For example, downtown Raleigh has a DX-40 zone code, with the 40 representing the maximum number of floors a building can have. However, anyone who has been to downtown Raleigh knows that very few buildings (especially residential buildings) have anywhere close to 40 floors.
