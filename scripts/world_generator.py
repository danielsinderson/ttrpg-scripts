"""
scripts to generate content for the Rust & Ruins TTRPG
- based off of its random tables and procedures

TODO: add name generation for region and cities
TODO: improve the readability of the output
"""

import random


suits = ["Gold", "Incense", "Wine", "Steel", "Sulfur", "Bone"]
num_samples = {
    "geographical features": 10,
    #"places of interest": 5,
    #"things of interest": 5,
    "social organizations": 1,
    "cultural adornments": 3,
    "cultural body modifications": 1,
    "primary foods": 4,
    "festivals": 3,
    "attitude towards magic": 1,
    "layout": 1,
    "building materials": 2,
    "building decorations": 2,
    "governments": 1,
    "recent historical events": 3,
    "current economy": 1,
    "local issues": 1,
    "current threats": 1
}

world_tables = {
    "region": {
        "geographical features": [
            "Ancient Megaplex",
            "Ashen Lands",
            "Blasted Lands",
            "Bog",
            "Canyons",
            "Cave System",
            "Coral Reef ",
            "Dense Forest ",
            "Desert",
            "Estuary",
            "Feywyrd",
            "Glacier",
            "Great Lake",
            "Great River",
            "Hot Springs",
            "Islands",
            "Jagged Mountain",
            "Jungle",
            "Mixed Forest",
            "Pit",
            "Prairie",
            "Primordium",
            "Rift",
            "Rocky Hills",
            "Rolling Hills",
            "Salt Lakes",
	    	"Savannah",
            "Tar Pits",
            "Tidal Swamp",
            "Time Lock",
            "Titanic Husk",
            "Tundra",
            "Volcano",
            "Weird Niche",
            "Whirlpool",
            "World Tree"
        ],
    },
    "city": {
        "layout": [
            "Concentric Circles",
            "Districts",
            "Fortress",
            "Grid",
            "Organic",
            "Spoke-and-wheel"
        ],
        "building materials": [
            "Brick or Mud",
            "Chitin",
            "Concrete",
            "Fabrics",
            "Stone",
            "Wood"
        ],
        "building decorations": [
            "Bones",
            "Flowers",
            "Feathers",
            "Gourds",
            "Glass",
            "Metals",
            "Hides",
            "Furs",
            "Resins",
            "Gems",
            "Shells",
            "Plants"
        ],
        "governments": [
            "Anarchy: Chaotic or Orderly or Organized",
            "Aristarchy: by Birth or by Contest or by Wealth",
            "Cryptarchy: Foreign Rule or Powerful Being or Secret Society",
            "Democracy: Direct or Hybrid or Representative",
            "Monarchy: Absolute or Petty or Zonal",
            "Oligarchy: Military or Religious or Political"
        ],
        "social organizations": [
            "Hereditary Castes",
            "Occupational Castes",
            "Astrological Castes",
            "Ritual Clans",
            "Military Clans",
            "Economic Clans",
            "Extended Kin Groups",
            "Moieties",
            "Nuclear Families",
            "Guilds",
            "Gangs",
            "Secret Societies",
            "Neighborhoods",
            "Districts",
            "Religious Sects",
            "Philosophies",
            "Magical Schools"
        ],
        "cultural adornments": [
            "Precious stones",
            "Metals",
            "Makeup",
            "Elaborate hair styles",
            "Flowers", 
            "feathers",
            "shell",
            "Small, trained animals",
            "Bones",
            "teeth",
            "claws"
        ],
        "cultural body modifications": [
            "Scarification",
            "Intricate hair removal",
            "Tattoos",
            "Piercings or subdermal implants",
            "Shaping of a body part",
            "Dyeing of skin, teeth, hair, or eyes"
        ],
        "primary foods": [
            "Berries",
            "Eggs",
            "Fermentations",
            "Fish",
            "Fruits",
            "Game",
            "Grains",
            "Insects",
            "Isopods",
            "Legumes",
            "Livestock",
            "Mushrooms",
            "Nuts",
            "Oils",
            "Resins",
            "Roots",
            "Seeds",
            "Shellfish",
            "Squash",
            "Vegetation"
        ],
        "festivals": [
            "Equinox (Autumnal)",
            "Equinox (Vernal)",
            "Harvest",
            "Historical",
            "Hunting",
            "Magical",
            "On births",
            "On deaths",
            "On full moon (12 day)",
            "On full moon (28 day)",
            "On both moons full (84 days)",
            "Planetary conjunction",
            "Political",
            "Religious",
            "Seasonal games",
            "Solar year begins",
            "Solstice (Summer)",
            "Solstice (Winter)",
            "Strange migration",
            "Working changes cycle"
        ],
        "attitude towards magic": [
            "Persecution",
            "Prohibition",
            "Prejudice",
            "Fear",
            "Regulation",
            "Ritual circumscription",
            "Cautio",
            "Unease",
            "Ambivalence",
            "Indifference",
            "Acceptance",
            "Curiosity",
            "Hopefulness",
            "Delight",
            "Awe",
            "Wonder",
            "Enthusiasm",
            "Study",
            "Manipulation",
            "Hunger"
        ],
        "recent historical events": [
            "Beneficial magic",
            "Economic boom",
            "Golden Age",
            "Massive public works",
            "Resource discovered",
            "Terraforming",
            "Cultural collapse",
            "Curse",
            "Disaster",
            "Plague",
            "Resource collapse",
            "War",
            "Cultural change",
            "Massive immigration",
            "Religious change",
            "Revolt",
            "Awakened machine",
            "Strange magic"
        ],
        "current economy": [
            "Booming",
            "Strong",
            "Reviving",
            "Weak",
            "Depressed",
            "Collapsing"
        ],
        "local issues": [
            "Addiction",
            "Ancient Discovery",
            "Corrupion",
            "Monsters",
            "Disease",
            "Strange Innovation"
        ],
        "current threats": [
            "Gangs",
            "Foreign Raiders",
            "War",
            "Monsters / Undead",
            "Wild Magic",
            "Powerful Foe"
        ]
    }
}


def generate_features(thing: str) -> str:
    feature_list = list(world_tables[thing].keys())
    features = [f"{feature}: {random.sample(world_tables[thing][feature], num_samples[feature])}" for feature in feature_list]
    features = [f"{thing.upper()}\nSuit: {random.choice(suits)}"] + features
    return "\n".join(features)


def generate_game_world() -> str:
    geography: str = generate_features("region")
    cities: str = [generate_features("city") for i in range(random.randint(2, 8))]
    return geography + "\n\n" + "\n\n".join(cities)


def main():
    world = generate_game_world()
    print(world)


if __name__ == "__main__":
    main()