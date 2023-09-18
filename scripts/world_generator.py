"""
scripts to generate content for the Rust & Ruins TTRPG
- based off of its random tables and procedures
"""

import random


suits = ["Gold", "Incense", "Wine", "Steel", "Sulfur", "Bone"]

world_tables = {
    "world features": {
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
        "places of interest": [
            "Dead magic zone",
            "Wild magic zone",
            "Haunted battlefield",
            "Petrified forest",
            "Crystal field",
            "Wizard's Tower",
            "Wrecked village",
            "Small temple",
            "Labor camp",
            "Abandoned mine",
            "Thriving village",
            "Spectacular garden",
            "Recent battlefield",
            "Massive or strange bridge",
            "Fort or castle",
            "Cave or pit",
            "Ruined city",
            "Inn",
            "Circus",
            "Lake",
            "Spire",
            "Monster lair / nest",
            "Catacombs",
            "Hoard / vault",
            "Bazaar",
            "Geysers and mud pits",
            "Magical spring",
            "Lava fields",
            "Prairie",
            "Recluse's hut",
            "Campsite",
            "Mythic underground",
            "Dangerous crossing",
            "Specialty school",
            "Observatory",
            "Floating or drowned city"
        ],
        "things of interest": [
            "Sealed burial mound",
            "Plundered burial mound",
            "Statue or tree with trapped spirit",
            "Giant statue",
            "Obelisk",
            "Wrecked ship",
            "Portal to another place",
            "Gruesome altar",
            "Henge or arch",
            "Defunct magical working",
            "Operating magical working",
            "Trapped weapon",
            "Hunting snare(s)",
            "Monster(s)",
            "Odd fungi / plants",
            "Odd creatures",
            "Toll",
            "Local spirit",
            "Corpses",
            "Treasure",
            "Giant crystal jutting from ground",
            "Massive tree",
            "Unattended feast",
            "Rusted automaton",
            "Warning sign",
            "Obscured path",
            "Husk of massive creature",
            "Herd animals",
            "Swarm of vermin",
            "Forgotten cache",
            "Dangerous but lucrative harvest",
            "Puzzle or riddle barrier",
            "Natural obstruction",
            "Magical obstruction",
            "Trap",
            "Holy site / offering"
        ]
    },
    "cultural features": {
        "social organization": [
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
            "Precious stones and/or metals",
            "Special or extensive makeup",
            "Elaborate hair styles",
            "Flowers, feathers, and/or shell &",
            "Small, trained animals",
            "Bones, teeth, and/or claws"
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
        ]
    },
    "city features": {
        "layout": [
            "Concentric Circles",
            "Districts",
            "Fortress",
            "Grid",
            "Organic",
            "Spoke-and-wheel"
        ],
        "primary building materials": [
            "Brick or Mud",
            "Chitin",
            "Concrete",
            "Fabrics",
            "Stone",
            "Wood"
        ],
        "decoration": [
            "Bones / flowers",
            "Feathers / gourds",
            "Glass / metals",
            "Hides / furs",
            "Resins / gems",
            "Shells / plants"
        ],
        "governments": [
            "Anarchy: Chaotic or Orderly or Organized",
            "Aristarchy: by Birth or by Contest or by Wealth",
            "Cryptarchy: Foreign Rule or Powerful Being or Secret Society",
            "Democracy: Direct or Hybrid or Representative",
            "Monarchy: Absolute or Petty or Zonal",
            "Oligarchy: Military or Religious or Political"
        ],
        "good historical events": [
            "Beneficial magic",
            "Economic boom",
            "Golden Age",
            "Massive public works",
            "Resource discovered",
            "Terraforming"
        ],
        "bad historical events": [
            "Cultural collapse",
            "Curse",
            "Disaster",
            "Plague",
            "Resource collapse",
            "War"
        ],
        "neutral historical events": [
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

dungeon_tables = {
    "features": {
        "lighting": [],
        "history": []
    },
    "plants": {},
    "animals": {},
    "fungus": {},
    "oozes": {},
    "hazards": {
        "tricks": [],
        "traps": [],
        "curses": []
    },
    "instabilities": {}
}



def generate_geography() -> str:
    n = random.randint(3, 5)
    feature_list = world_tables["world features"]["geographical features"]
    features = [random.choice(feature_list) for i in range(n)]
    return "Your worlds primary geographical features are the following:\n    - " + "\n    - ".join(features)


def generate_culture() -> str:
    return ""


def generate_city() -> str:
    return ""


def generate_world() -> str:
    geography: str = generate_geography()
    return geography


def main():
    world = generate_world()
    print(world)


if __name__ == "__main__":
    main()