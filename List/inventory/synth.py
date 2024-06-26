from dataclasses import dataclass, field

from List.configDict import itemType
from List.inventory.item import InventoryItem


@dataclass(frozen=True)
class SynthItem(InventoryItem):
    id: int
    name: str
    type: itemType = field(init=False, default=itemType.SYNTH)


DarkShard = SynthItem(280, "Dark Shard")
DarkStone = SynthItem(281, "Dark Stone")
DarkGem = SynthItem(282, "Dark Gem")
DarkCrystal = SynthItem(283, "Dark Crystal")
BlazingShard = SynthItem(317, "Blazing Shard")
BlazingStone = SynthItem(318, "Blazing Stone")
BlazingGem = SynthItem(319, "Blazing Gem")
BlazingCrystal = SynthItem(320, "Blazing Crystal")
LightningShard = SynthItem(325, "Lightning Shard")
LightningStone = SynthItem(326, "Lightning Stone")
LightningGem = SynthItem(327, "Lightning Gem")
LightningCrystal = SynthItem(328, "Lightning Crystal")
PowerShard = SynthItem(329, "Power Shard")
PowerStone = SynthItem(330, "Power Stone")
PowerGem = SynthItem(331, "Power Gem")
PowerCrystal = SynthItem(332, "Power Crystal")
LucidShard = SynthItem(333, "Lucid Shard")
LucidStone = SynthItem(334, "Lucid Stone")
LucidGem = SynthItem(335, "Lucid Gem")
LucidCrystal = SynthItem(336, "Lucid Crystal")
DenseShard = SynthItem(337, "Dense Shard")
DenseStone = SynthItem(338, "Dense Stone")
DenseGem = SynthItem(339, "Dense Gem")
DenseCrystal = SynthItem(340, "Dense Crystal")
TwilightShard = SynthItem(341, "Twilight Shard")
TwilightStone = SynthItem(342, "Twilight Stone")
TwilightGem = SynthItem(343, "Twilight Gem")
TwilightCrystal = SynthItem(344, "Twilight Crystal")
MythrilShard = SynthItem(345, "Mythril Shard")
MythrilStone = SynthItem(346, "Mythril Stone")
MythrilGem = SynthItem(347, "Mythril Gem")
MythrilCrystal = SynthItem(348, "Mythril Crystal")
BrightShard = SynthItem(349, "Bright Shard")
BrightStone = SynthItem(350, "Bright Stone")
BrightGem = SynthItem(351, "Bright Gem")
BrightCrystal = SynthItem(352, "Bright Crystal")
EnergyShard = SynthItem(353, "Energy Shard")
EnergyStone = SynthItem(354, "Energy Stone")
EnergyGem = SynthItem(355, "Energy Gem")
EnergyCrystal = SynthItem(356, "Energy Crystal")
SerenityShard = SynthItem(357, "Serenity Shard")
SerenityStone = SynthItem(358, "Serenity Stone")
SerenityGem = SynthItem(359, "Serenity Gem")
SerenityCrystal = SynthItem(360, "Serenity Crystal")
OrichalcumPlus = SynthItem(361, "Orichalcum+")
Orichalcum = SynthItem(377, "Orichalcum")
FrostShard = SynthItem(378, "Frost Shard")
FrostStone = SynthItem(379, "Frost Stone")
FrostGem = SynthItem(380, "Frost Gem")
FrostCrystal = SynthItem(381, "Frost Crystal")
RemembranceShard = SynthItem(576, "Remembrance Shard")
RemembranceStone = SynthItem(577, "Remembrance Stone")
RemembranceGem = SynthItem(578, "Remembrance Gem")
RemembranceCrystal = SynthItem(579, "Remembrance Crystal")
TranquilityShard = SynthItem(580, "Tranquility Shard")
TranquilityStone = SynthItem(581, "Tranquility Stone")
TranquilityGem = SynthItem(582, "Tranquility Gem")
TranquilityCrystal = SynthItem(583, "Tranquility Crystal")
LostIllusion = SynthItem(584, "Lost Illusion")
ManifestIllusion = SynthItem(585, "Manifest Illusion")
