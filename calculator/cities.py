LOW = 'low'
MED = 'med'
HIGH = 'high'
ALT_HIGH = 'alt_high'

# hard-coded data about each city that is used for calculating
# that city's zoning index
def initalize():
    return {
        'phoenix': {
            'densities': {
                LOW: {'codes': {'S-1', 'R1-10', 'RE-43', 'RE-24', 'R1-14', 'RE-35', 'R1-18', 'R1-10', 'R1-8'}, 'area': 0, 'dist': 0},
                MED: {'codes': {'R1-6', 'R-2', 'R-3', 'R-3A', 'R-4', 'R-5', 'R-4A'}, 'area': 0, 'dist': 0},
                HIGH: {'codes': {'UR'}, 'area': 0, 'dist': 0},
                ALT_HIGH: ('HR', 'DTC')
            },
            'population':  1.65e6,
            'area_key': 'ACRES',
            'zone_code_key': 'ZONING',
            'requires_area_conversion': False,
            'index': 0,
            'area': 0,
            'drop': 'ACRES',
        },
        'raleigh': {
            'densities': {
                LOW: {'codes': {'R-1', 'R-2', 'R-3', 'R-4'}, 'area': 0, 'dist': 0},
                MED: {'codes': {'R-5', 'R-6', 'RX-3', 'RX-4'}, 'area': 0, 'dist': 0},
                HIGH: {'codes': {'R-10', 'RX-5', 'RX-7', 'RX-12'}, 'area': 0, 'dist': 0},
                ALT_HIGH: ('DX')
            },
            'population':  4.82e5,
            'area_key': 'SHAPEAREA',
            'zone_code_key': 'ZONING',
            'requires_area_conversion': True,
            'index': 0,
            'area': 0,
            'drop': None
        },
        'dallas': {
            'densities': {
                LOW: {'codes': {'R-7.5(A)', 'R-7.5(A)', 'R-13(A)', 'R-16(A)' 'R-1/2ac(A)', 'R-1ac(A)', 'MH'}, 'area': 0, 'dist': 0},
                MED: {'codes': {'D(A)', 'TH-1(A)', 'TH-2(A)', 'TH-3(A)', 'CH'}, 'area': 0, 'dist': 0},
                HIGH: {'codes': {'MF-1(A)', 'MF-2(A)', 'MF-3(A)', 'MF-4(A)'}, 'area': 0, 'dist': 0},
                ALT_HIGH: ()
            },
            'population': 1.303e6,
            'area_key': 'Shape__Area',
            'zone_code_key': 'ZONE_DIST',
            'requires_area_conversion': True,
            'index': 0,
            'area': 0,
            'drop': None
        },
        'los_angeles': {
            'densities': {
                LOW: {'codes': {'RA', 'A1', 'RE40', 'RE20', 'RE15', 'RE11', 'RE9', 'RMP'}, 'area': 0, 'dist': 0},
                MED: {'codes': {'RS', 'R1', 'R1V', 'R1F', 'R1R', 'R1H', 'R2', 'RD3', 'RD4', 'RD5', 'RD6'}, 'area': 0, 'dist': 0},
                HIGH: {'codes': {'RD1.5', 'RD2', 'RW2', 'R3', 'RAS3', 'R4', 'RAS4', 'R5'}, 'area': 0, 'dist': 0},
                ALT_HIGH: ()
            },
            'population': 3.821e6,
            'area_key': 'Shape__Area',
            'zone_code_key': 'ZONE_CLASS',
            'requires_area_conversion': True,
            'index': 0,
            'area': 0,
            'drop': None
        },
        'cincinnati': {
            'densities': {
                LOW: {'codes': {'SF-20', 'SF-10'}, 'area': 0, 'dist': 0},
                MED: {'codes': {'SF-6', 'SF-4'}, 'area': 0, 'dist': 0},
                HIGH: {'codes': {'SF-2'}, 'area': 0, 'dist': 0},
                ALT_HIGH: ()
            },
            'population': 3.11e5,
            'area_key': 'ACRES',
            'zone_code_key': 'ZONING',
            'requires_area_conversion': False,
            'index': 0,
            'area': 0,
            'drop': None
        }
    }