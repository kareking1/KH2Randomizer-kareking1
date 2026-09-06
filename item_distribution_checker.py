from Class import settingkey
from Class.exceptions import RandomizerExceptions
from Class.itemClass import KH2Item
from Class.newLocationClass import KH2Location
from Class.randomUtils import random_seed_name
from Class.seedSettings import SeedSettings
from List.configDict import itemDifficulty, itemRarity, itemType, locationCategory, locationDepth
from Module.newRandomize import RandomizerSettings,Randomizer
from Module.seedEvaluation import LocationInformedSeedValidator

def make_rando_seed(seed_name):
    seed_settings = SeedSettings()
    seed_settings.set(settingkey.SUPERBOSSES_WITH_REWARDS,["AS","Sephi","DataOrg"])#,
    seed_settings.set(settingkey.PROOF_DEPTH,locationDepth.NoFirstVisit.name)
    seed_settings.set(settingkey.MISC_LOCATIONS_WITH_REWARDS,[])
    settings = RandomizerSettings(seed_name,True,"version",seed_settings, "")
    newSeedValidation = LocationInformedSeedValidator()
    randomizer = None
    while True:
        try:
            randomizer = Randomizer(settings)
            result = newSeedValidation.validate_seed(settings, randomizer)
            break
        except RandomizerExceptions as e:
            settings.random_seed = random_seed_name()
            settings.create_full_seed_string()
            last_error = e
            continue

    proof_worlds = set()


    for assignment in randomizer.assignments:
        loc: KH2Location = assignment.location
        item : KH2Item = assignment.item
        item2 : KH2Item = assignment.item2

        if loc.LocationCategory is locationCategory.WEAPONSLOT:
            continue

        if item:
            if item.ItemType in [itemType.PROOF_OF_CONNECTION,itemType.PROOF_OF_PEACE,itemType.PROOF_OF_NONEXISTENCE]:
                proof_worlds.add(loc.LocationTypes[0])
        if item2:
            if item2.ItemType in [itemType.PROOF_OF_CONNECTION,itemType.PROOF_OF_PEACE,itemType.PROOF_OF_NONEXISTENCE]:
                proof_worlds.add(loc.LocationTypes[0])
    
    return proof_worlds
        
        
if __name__ == '__main__':
    counts = {}

    num_attempts = 5000
    for attempt in range(num_attempts):
        if attempt%500==0:
            print(f"\t\t\t\t\t\t\t{attempt}")
        item_results = make_rando_seed(str(attempt))
        for proof_world in item_results:
            counts.setdefault(proof_world,0)
            counts[proof_world]+=1

    for world in counts.keys():
        world_count = counts[world]
        line_string = world.name+"\t"+str(world_count)
        print(line_string)

        
