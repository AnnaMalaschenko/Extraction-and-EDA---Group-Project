import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

RG_API_KEY = os.getenv("RG_API_KEY")

headers = {
    "Authorization": RG_API_KEY
}

all_rows = []

page = 1

while True:
    print(f"Pulling page {page}...")

    url = f"https://api.rescuegroups.org/v5/public/animals/search/cats?page={page}"

    response = requests.get(url, headers=headers)
    raw_data = response.json()

    animals = raw_data.get("data", [])

    if len(animals) == 0:
        break

    for animal in animals:
        attributes = animal.get("attributes", {})

        all_rows.append({
            "id": animal.get("id"),
            "name": attributes.get("name"),
            "species_id": animal.get("relationships", {})
                              .get("species", {})
                              .get("data", [{}])[0]
                              .get("id"),
            "breed_primary": attributes.get("breedPrimary"),
            "breed_secondary": attributes.get("breedSecondary"),
            "breed_string": attributes.get("breedString"),
            "sex": attributes.get("sex"),
            "age_group": attributes.get("ageGroup"),
            "age_string": attributes.get("ageString"),
            "size_current": attributes.get("sizeCurrent"),
            "size_uom": attributes.get("sizeUOM"),
            "adoption_pending": attributes.get("isAdoptionPending"),
            "needs_foster": attributes.get("isNeedingFoster"),
            "picture_count": attributes.get("pictureCount"),
            "thumbnail_url": attributes.get("pictureThumbnailUrl"),
            "created_date": attributes.get("createdDate"),
            "updated_date": attributes.get("updatedDate"),
            "description": attributes.get("descriptionText")
        })

    page += 1

df = pd.DataFrame(all_rows)

df.to_csv(
    "data/raw/rescue_groups_cats.csv",
    index=False
)

print(df.shape)
print("Cat dataset saved.")