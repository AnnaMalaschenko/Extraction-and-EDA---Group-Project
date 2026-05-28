########################################
#Palo's Color Cleaner
#possibly bunk attempt at creating a color cleaning module
#will probably edit this down the line to fully clean colorDetails


import re
import pandas as pd

def clean_color_details(series):

    # Step 1 - Normalize case
    series = series.str.lower().str.title().str.strip()

    # Step 2 - Standardize separators
    series = (series
        .str.replace(' And ', ' & ', regex=False)
        .str.replace(' W/', ' & ', regex=False)
        .str.replace(' With ', ' & ', regex=False)
        .str.replace(' / ', ' & ', regex=False)
        .str.replace(' Grey ', ' Gray ', regex=False)
    )

    # Step 3 - Tortie map
    tortie_map = {
        'Tortie': 'Tortoiseshell',
        'Torbie': 'Tortoiseshell',
        'Tortie & Orange/White': 'Tortoiseshell',
        'Tortie (Female) & Orange (Male)': 'Tortoiseshell',
        'Tortie - Black & Orange': 'Tortoiseshell',
        'Tortie/Calico': 'Tortoiseshell',
        'Torti': 'Tortoiseshell'
    }
    series = series.replace(tortie_map)

    # Step 4 - Siamese map
    siamese_map = {
        'Siamese Blue': 'Siamese',
        'Siamese Lilac Point': 'Siamese',
        'Siamese Looks': 'Siamese',
        'Siamese Ing': 'Siamese',
        'Siamese  - Lynx Pt.': 'Siamese',
        'Seal Point': 'Siamese',
        'Seal Point Siamese': 'Siamese',
        'Blue Point Siamese': 'Siamese',
        'Blue Point': 'Siamese',
        'Flame Point Siamese': 'Siamese',
        'Flame Point': 'Siamese',
        'White & Siamese': 'Siamese'
    }
    series = series.replace(siamese_map)

    # Step 5 - Black & White map
    black_white_map = {
        'Black & White': 'Black & White',
        'Black & A  White': 'Black & White',
        'Black & A White Bib': 'Black & White',
        'Black & White Bikini': 'Black & White',
        'Black & White Clerical': 'Black & White',
        'Black & White, Grey': 'Black & White',
        'Black & White Star': 'Black & White',
        'Black, Gray & White': 'Black & White',
        'Blac/White Bicolor': 'Black & White',
        'White & Black': 'Black & White',
        'With Black': 'Black & White',
        'With White': 'Black & White',
    }
    series = series.replace(black_white_map)

    # Step 6 - Brown Tabby map
    brown_tabby_map = {
        'Brown Tabby': 'Brown Tabby',
        'Brown & White Tabby': 'Brown Tabby',
        'Brown Tabby & A  White': 'Brown Tabby',
        'Brown Tabby & Orange': 'Brown Tabby',
        'Buff Tabby': 'Brown Tabby',
        'Brown/Tan Tabby': 'Brown Tabby',
        'Brown/Black/White Tabby': 'Brown Tabby',
    }
    series = series.replace(brown_tabby_map)

    # Step 7 - Gray Tabby map
    gray_tabby_map = {
        'Gray Tabby': 'Gray Tabby',
        'Gray Tabby & White': 'Gray Tabby'
    }
    series = series.replace(gray_tabby_map)

    # Step 8 - Gray & White map
    gray_white_map = {
        'Gray & White': 'Gray & White',
        'White & Gray': 'Gray & White',
    }
    series = series.replace(gray_white_map)

    # Step 9 - Tabby map
    tabby_map = {
        'Tabby': 'Tabby',
        'Tabby & White': 'Tabby',
        'Tabby W Calico': 'Tabby',
        'Tiger Stripe': 'Tabby',
    }
    series = series.replace(tabby_map)

    # Step 10 - Silver map
    silver_map = {
        'Silver': 'Silver',
        'Silver Tabby': 'Silver',
        'Silver Tabby & White': 'Silver',
    }
    series = series.replace(silver_map)

    # Step 11 - Orange Tabby map
    orange_tabby_map = {
        'Orange Tabby': 'Orange Tabby',
        'Orange Tabby & White': 'Orange Tabby',
        'Orange & White Tabby': 'Orange Tabby'
    }
    series = series.replace(orange_tabby_map)

    # Step 12 - Remove noise words
    words_to_remove = ['Light', 'Dilute', 'Dark', 'Classic', 'Solid', 'Bob', 'On', 
                       'And', 'Little', 'Her', 'Mix', 'Markings', 'Shading', 'Nose', 
                       'Paws', 'Eyes', 'Some', 'Chest', 'Mostly', 'Belly', 'Tips', 
                       'Tail', 'Legs', 'Feet', 'Face', 'Ears', 'Coat', 'Pattern', 
                       'Spots', 'Patches', 'Blk', 'Head', 'Color', 'Coloring', 'Colored']
    pattern = '|'.join(r'\b' + re.escape(word) + r'\b' for word in words_to_remove)
    series = series.str.replace(pattern, '', regex=True).str.strip()

    # Step 13 - Clean up extra spaces
    series = series.str.replace(r'\s+', ' ', regex=True).str.strip()

    return series