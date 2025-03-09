import pandas as pd
import json
from cities import LOW, MED, HIGH, ALT_HIGH, initalize
from typing import Dict

# number of feet in an acre
ACRE_MULTIPLE = 43560
# percentage of mixed-use zones with residential buildings
MIXED_RESIDENTIAL_RATIO = 0.152

# punishes low-density housing and rewards high density housing
WEIGHTS = {
    LOW: 0.1,
    MED: 0.3,
    HIGH: 0.9
}


# parses the dataset to collect key values used for calculating the zone index
def process_zones(data: pd.DataFrame, categories: Dict, requires_area_conversion: bool, area_key: str, code_key: str) -> float:
    total_residential_area = 0

    for _, row in data.iterrows():
        area = 0
        if requires_area_conversion:
            area = row[area_key] / ACRE_MULTIPLE
        else:
            area = row[area_key]
        code = row[code_key]
        
        # calculates the total area for each zone category (low, med, high)
        if code in categories[LOW]['codes']:
            categories[LOW]['area'] += area
            total_residential_area += area
        elif code in categories[MED]['codes']:
            categories[MED]['area'] += area
            total_residential_area += area
        elif code in categories[HIGH]['codes'] or code.startswith(categories[ALT_HIGH]):
            transformed_area = area
            if code.startswith(categories[ALT_HIGH]):
                transformed_area *= MIXED_RESIDENTIAL_RATIO
            categories[HIGH]['area'] += transformed_area
            total_residential_area += transformed_area

    return total_residential_area

# calculates each zone category's distribution with respect to the total area
def calculate_distributions(densities: Dict, total_area: float):
    for density_label, density in densities.items():
        if density_label == ALT_HIGH:
            continue
        density['dist'] = density['area'] / total_area

def calculate_zone_index(population: float, categories: Dict, weights: Dict) -> float:
    # 1e5 is a random multiplier used to shrink the size of the index
    # since population will be very large
    weighted_sum = sum(
        weights[key] * categories[key]['dist'] 
        for key in categories if key != ALT_HIGH
    ) * 1e5
    return population / weighted_sum

# formats the distributions for a nicer-looking output in metrics.json
def format_density_distribution(city):
    distributions = { LOW: {}, MED: {}, HIGH: {} }

    for key in city['densities']:
        if key == ALT_HIGH:
            continue

        distributions[key] = {
            'area': round(city['densities'][key]['area'], 2),
            'share': round(city['densities'][key]['dist'], 4)
        }

    return distributions

def main():
    print('calculating...')
    initialized_cities = initalize()

    for key in initialized_cities:
        data = pd.read_csv(f"../data/{key}_zoning.csv")
        drop_key = initialized_cities[key]['drop']

        if drop_key != None:
            data = data.dropna(subset=[drop_key])
        
        densities = initialized_cities[key]['densities']
        initialized_cities[key]['area'] = process_zones(
            data, densities,
            initialized_cities[key]['requires_area_conversion'],
            initialized_cities[key]['area_key'],
            initialized_cities[key]['zone_code_key']
        )
        calculate_distributions(densities, initialized_cities[key]['area'])
        initialized_cities[key]['index'] = round(calculate_zone_index(initialized_cities[key]['population'], densities, WEIGHTS), 2)
    
    city_metrics = {}
    for key in initialized_cities:
        city_metrics[key] = {
            'zone_index': initialized_cities[key]['index'],
            'density_distributions': format_density_distribution(initialized_cities[key])
        }

    with open('../metrics.json', 'w') as file:
        json.dump(city_metrics, file)
    
    print('done!')

main()
