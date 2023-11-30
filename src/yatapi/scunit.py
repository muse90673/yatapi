"""Wrapper for a Starcraft Unit reference.

"""


class SCUnit:
    def __init__(self, value: str):
        self.value = value

    def __repr__(self):
        return self.value


# meta units
MEN: SCUnit = SCUnit('"Men"')
ANY_UNIT: SCUnit = SCUnit('"Any unit"')
BUILDINGS: SCUnit = SCUnit('"Buildings"')
FACTORIES: SCUnit = SCUnit('"Factories"')
# real units
ALAN_SCHEZAR_GOLIATH: SCUnit = SCUnit('"Alan Schezar (Goliath)"')
ALAN_TURRET: SCUnit = SCUnit('"Alan Turret"')
ALDARIS_TEMPLAR: SCUnit = SCUnit('"Aldaris (Templar)"')
ALEXEI_STUKOV_GHOST: SCUnit = SCUnit('"Alexei Stukov (Ghost)"')
ARCTURUS_MENGSK_BATTLECRUISER: SCUnit = SCUnit('"Arcturus Mengsk (Battlecruiser)"')
ARTANIS_SCOUT: SCUnit = SCUnit('"Artanis (Scout)"')
BENGALAAS_JUNGLE: SCUnit = SCUnit('"Bengalaas (Jungle)"')
CANTINA: SCUnit = SCUnit('"Cantina"')
CAVE: SCUnit = SCUnit('"Cave"')
CAVEIN: SCUnit = SCUnit('"Cave-in"')
COCOON: SCUnit = SCUnit('"Cocoon"')
DANIMOTH_ARBITER: SCUnit = SCUnit('"Danimoth (Arbiter)"')
DARK_SWARM: SCUnit = SCUnit('"Dark Swarm"')
DARK_TEMPLAR_HERO: SCUnit = SCUnit('"Dark Templar (Hero)"')
DATA_DISC: SCUnit = SCUnit('"Data Disc"')
DEVOURING_ONE_ZERGLING: SCUnit = SCUnit('"Devouring One (Zergling)"')
DISRUPTION_FIELD: SCUnit = SCUnit('"Disruption Field"')
DUKE_TURRET_TYPE_1: SCUnit = SCUnit('"Duke Turret type 1"')
DUKE_TURRET_TYPE_2: SCUnit = SCUnit('"Duke Turret type 2"')
EDMUND_DUKE_SIEGE_MODE: SCUnit = SCUnit('"Edmund Duke (Siege Mode)"')
EDMUND_DUKE_SIEGE_TANK: SCUnit = SCUnit('"Edmund Duke (Siege Tank)"')
FENIX_DRAGOON: SCUnit = SCUnit('"Fenix (Dragoon)"')
FENIX_ZEALOT: SCUnit = SCUnit('"Fenix (Zealot)"')
FLAG: SCUnit = SCUnit('"Flag"')
FLOOR_GUN_TRAP: SCUnit = SCUnit('"Floor Gun Trap"')
FLOOR_HATCH_UNUSED: SCUnit = SCUnit('"Floor Hatch (UNUSED)"')
FLOOR_MISSILE_TRAP: SCUnit = SCUnit('"Floor Missile Trap"')
GANTRITHOR_CARRIER: SCUnit = SCUnit('"Gantrithor (Carrier)"')
GERARD_DUGALLE_GHOST: SCUnit = SCUnit('"Gerard DuGalle (Ghost)"')
GOLIATH_TURRET: SCUnit = SCUnit('"Goliath Turret"')
GUI_MONTAG_FIREBAT: SCUnit = SCUnit('"Gui Montag (Firebat)"')
HUNTER_KILLER_HYDRALISK: SCUnit = SCUnit('"Hunter Killer (Hydralisk)"')
HYPERION_BATTLECRUISER: SCUnit = SCUnit('"Hyperion (Battlecruiser)"')
INDEPENDENT_COMMAND_CENTER: SCUnit = SCUnit('"Independent Command Center"')
INDEPENDENT_STARPORT: SCUnit = SCUnit('"Independent Starport"')
INFESTED_COMMAND_CENTER: SCUnit = SCUnit('"Infested Command Center"')
INFESTED_DURAN: SCUnit = SCUnit('"Infested Duran"')
INFESTED_KERRIGAN_INFESTED_TERRAN: SCUnit = SCUnit('"Infested Kerrigan (Infested Terran)"')
INFESTED_TERRAN: SCUnit = SCUnit('"Infested Terran"')
ION_CANNON: SCUnit = SCUnit('"Ion Cannon"')
JIM_RAYNOR_MARINE: SCUnit = SCUnit('"Jim Raynor (Marine)"')
JIM_RAYNOR_VULTURE: SCUnit = SCUnit('"Jim Raynor (Vulture)"')
JUMP_GATE: SCUnit = SCUnit('"Jump Gate"')
KAKARU_TWILIGHT: SCUnit = SCUnit('"Kakaru (Twilight)"')
KHALIS_CRYSTAL: SCUnit = SCUnit('"Khalis Crystal"')
KHAYDARIN_CRYSTAL: SCUnit = SCUnit('"Khaydarin Crystal"')
KHAYDARIN_CRYSTAL_FORMATION: SCUnit = SCUnit('"Khaydarin Crystal Formation"')
KUKULZA_GUARDIAN: SCUnit = SCUnit('"Kukulza (Guardian)"')
KUKULZA_MUTALISK: SCUnit = SCUnit('"Kukulza (Mutalisk)"')
KYADARIN_CRYSTAL_FORMATION: SCUnit = SCUnit('"Kyadarin Crystal Formation"')
LEFT_PIT_DOOR: SCUnit = SCUnit('"Left Pit Door"')
LEFT_UPPER_LEVEL_DOOR: SCUnit = SCUnit('"Left Upper Level Door"')
LEFT_WALL_FLAME_TRAP: SCUnit = SCUnit('"Left Wall Flame Trap"')
LEFT_WALL_MISSILE_TRAP: SCUnit = SCUnit('"Left Wall Missile Trap"')
MAGELLAN_SCIENCE_VESSEL: SCUnit = SCUnit('"Magellan (Science Vessel)"')
MAP_REVEALER: SCUnit = SCUnit('"Map Revealer"')
MATRIARCH_QUEEN: SCUnit = SCUnit('"Matriarch (Queen)"')
MATURE_CRYSALIS: SCUnit = SCUnit('"Mature Crysalis"')
MINERAL_CHUNK_TYPE_1: SCUnit = SCUnit('"Mineral Chunk (Type 1)"')
MINERAL_CHUNK_TYPE_2: SCUnit = SCUnit('"Mineral Chunk (Type 2)"')
MINERAL_FIELD_TYPE_1: SCUnit = SCUnit('"Mineral Field (Type 1)"')
MINERAL_FIELD_TYPE_2: SCUnit = SCUnit('"Mineral Field (Type 2)"')
MINERAL_FIELD_TYPE_3: SCUnit = SCUnit('"Mineral Field (Type 3)"')
MINING_PLATFORM: SCUnit = SCUnit('"Mining Platform"')
MOJO_SCOUT: SCUnit = SCUnit('"Mojo (Scout)"')
NORAD_II_BATTLECRUISER: SCUnit = SCUnit('"Norad II (Battlecruiser)"')
NORAD_II_CRASHED_BATTLECRUISER: SCUnit = SCUnit('"Norad II (Crashed Battlecruiser)"')
NUCLEAR_MISSILE: SCUnit = SCUnit('"Nuclear Missile"')
OVERMIND_COCOON: SCUnit = SCUnit('"Overmind Cocoon"')
POWER_GENERATOR: SCUnit = SCUnit('"Power Generator"')
PROTOSS_ARBITER: SCUnit = SCUnit('"Protoss Arbiter"')
PROTOSS_ARBITER_TRIBUNAL: SCUnit = SCUnit('"Protoss Arbiter Tribunal"')
PROTOSS_ARCHON: SCUnit = SCUnit('"Protoss Archon"')
PROTOSS_ASSIMILATOR: SCUnit = SCUnit('"Protoss Assimilator"')
PROTOSS_BEACON: SCUnit = SCUnit('"Protoss Beacon"')
PROTOSS_CARRIER: SCUnit = SCUnit('"Protoss Carrier"')
PROTOSS_CITADEL_OF_ADUN: SCUnit = SCUnit('"Protoss Citadel of Adun"')
PROTOSS_CORSAIR: SCUnit = SCUnit('"Protoss Corsair"')
PROTOSS_CYBERNETICS_CORE: SCUnit = SCUnit('"Protoss Cybernetics Core"')
PROTOSS_DARK_ARCHON: SCUnit = SCUnit('"Protoss Dark Archon"')
PROTOSS_DARK_TEMPLAR: SCUnit = SCUnit('"Protoss Dark Templar"')
PROTOSS_DRAGOON: SCUnit = SCUnit('"Protoss Dragoon"')
PROTOSS_FLAG_BEACON: SCUnit = SCUnit('"Protoss Flag Beacon"')
PROTOSS_FLEET_BEACON: SCUnit = SCUnit('"Protoss Fleet Beacon"')
PROTOSS_FORGE: SCUnit = SCUnit('"Protoss Forge"')
PROTOSS_GATEWAY: SCUnit = SCUnit('"Protoss Gateway"')
PROTOSS_HIGH_TEMPLAR: SCUnit = SCUnit('"Protoss High Templar"')
PROTOSS_INTERCEPTOR: SCUnit = SCUnit('"Protoss Interceptor"')
PROTOSS_MARKER: SCUnit = SCUnit('"Protoss Marker"')
PROTOSS_NEXUS: SCUnit = SCUnit('"Protoss Nexus"')
PROTOSS_OBSERVATORY: SCUnit = SCUnit('"Protoss Observatory"')
PROTOSS_OBSERVER: SCUnit = SCUnit('"Protoss Observer"')
PROTOSS_PHOTON_CANNON: SCUnit = SCUnit('"Protoss Photon Cannon"')
PROTOSS_PROBE: SCUnit = SCUnit('"Protoss Probe"')
PROTOSS_PYLON: SCUnit = SCUnit('"Protoss Pylon"')
PROTOSS_REAVER: SCUnit = SCUnit('"Protoss Reaver"')
PROTOSS_ROBOTICS_FACILITY: SCUnit = SCUnit('"Protoss Robotics Facility"')
PROTOSS_ROBOTICS_SUPPORT_BAY: SCUnit = SCUnit('"Protoss Robotics Support Bay"')
PROTOSS_SCARAB: SCUnit = SCUnit('"Protoss Scarab"')
PROTOSS_SCOUT: SCUnit = SCUnit('"Protoss Scout"')
PROTOSS_SHIELD_BATTERY: SCUnit = SCUnit('"Protoss Shield Battery"')
PROTOSS_SHUTTLE: SCUnit = SCUnit('"Protoss Shuttle"')
PROTOSS_STARGATE: SCUnit = SCUnit('"Protoss Stargate"')
PROTOSS_TEMPLAR_ARCHIVES: SCUnit = SCUnit('"Protoss Templar Archives"')
PROTOSS_TEMPLE: SCUnit = SCUnit('"Protoss Temple"')
PROTOSS_UNUSED_TYPE_1: SCUnit = SCUnit('"Protoss Unused type 1"')
PROTOSS_UNUSED_TYPE_2: SCUnit = SCUnit('"Protoss Unused type 2"')
PROTOSS_ZEALOT: SCUnit = SCUnit('"Protoss Zealot"')
PSI_DISRUPTER: SCUnit = SCUnit('"Psi Disrupter"')
PSI_EMITTER: SCUnit = SCUnit('"Psi Emitter"')
RAGNASAUR_ASH_WORLD: SCUnit = SCUnit('"Ragnasaur (Ash World)"')
RASZAGAL_DARK_TEMPLAR: SCUnit = SCUnit('"Raszagal (Dark Templar)"')
RHYNADON_BADLANDS: SCUnit = SCUnit('"Rhynadon (Badlands)"')
RIGHT_PIT_DOOR: SCUnit = SCUnit('"Right Pit Door"')
RIGHT_UPPER_LEVEL_DOOR: SCUnit = SCUnit('"Right Upper Level Door"')
RIGHT_WALL_FLAME_TRAP: SCUnit = SCUnit('"Right Wall Flame Trap"')
RIGHT_WALL_MISSILE_TRAP: SCUnit = SCUnit('"Right Wall Missile Trap"')
RUINS: SCUnit = SCUnit('"Ruins"')
SAMIR_DURAN_GHOST: SCUnit = SCUnit('"Samir Duran (Ghost)"')
SARAH_KERRIGAN_GHOST: SCUnit = SCUnit('"Sarah Kerrigan (Ghost)"')
SCANNER_SWEEP: SCUnit = SCUnit('"Scanner Sweep"')
SCANTID_DESERT: SCUnit = SCUnit('"Scantid (Desert)"')
START_LOCATION: SCUnit = SCUnit('"Start Location"')
STASIS_CELLPRISON: SCUnit = SCUnit('"Stasis Cell/Prison"')
TANK_TURRET_TYPE_1: SCUnit = SCUnit('"Tank Turret type 1"')
TANK_TURRET_TYPE_2: SCUnit = SCUnit('"Tank Turret type 2"')
TASSADAR_TEMPLAR: SCUnit = SCUnit('"Tassadar (Templar)"')
TASSADARZERATUL_ARCHON: SCUnit = SCUnit('"Tassadar/Zeratul (Archon)"')
TERRAN_ACADEMY: SCUnit = SCUnit('"Terran Academy"')
TERRAN_ARMORY: SCUnit = SCUnit('"Terran Armory"')
TERRAN_BARRACKS: SCUnit = SCUnit('"Terran Barracks"')
TERRAN_BATTLECRUISER: SCUnit = SCUnit('"Terran Battlecruiser"')
TERRAN_BEACON: SCUnit = SCUnit('"Terran Beacon"')
TERRAN_BUNKER: SCUnit = SCUnit('"Terran Bunker"')
TERRAN_CIVILIAN: SCUnit = SCUnit('"Terran Civilian"')
TERRAN_COMMAND_CENTER: SCUnit = SCUnit('"Terran Command Center"')
TERRAN_COMSAT_STATION: SCUnit = SCUnit('"Terran Comsat Station"')
TERRAN_CONTROL_TOWER: SCUnit = SCUnit('"Terran Control Tower"')
TERRAN_COVERT_OPS: SCUnit = SCUnit('"Terran Covert Ops"')
TERRAN_DROPSHIP: SCUnit = SCUnit('"Terran Dropship"')
TERRAN_ENGINEERING_BAY: SCUnit = SCUnit('"Terran Engineering Bay"')
TERRAN_FACTORY: SCUnit = SCUnit('"Terran Factory"')
TERRAN_FIREBAT: SCUnit = SCUnit('"Terran Firebat"')
TERRAN_FLAG_BEACON: SCUnit = SCUnit('"Terran Flag Beacon"')
TERRAN_GHOST: SCUnit = SCUnit('"Terran Ghost"')
TERRAN_GOLIATH: SCUnit = SCUnit('"Terran Goliath"')
TERRAN_MACHINE_SHOP: SCUnit = SCUnit('"Terran Machine Shop"')
TERRAN_MARINE: SCUnit = SCUnit('"Terran Marine"')
TERRAN_MARKER: SCUnit = SCUnit('"Terran Marker"')
TERRAN_MEDIC: SCUnit = SCUnit('"Terran Medic"')
TERRAN_MISSILE_TURRET: SCUnit = SCUnit('"Terran Missile Turret"')
TERRAN_NUCLEAR_SILO: SCUnit = SCUnit('"Terran Nuclear Silo"')
TERRAN_PHYSICS_LAB: SCUnit = SCUnit('"Terran Physics Lab"')
TERRAN_REFINERY: SCUnit = SCUnit('"Terran Refinery"')
TERRAN_SCV: SCUnit = SCUnit('"Terran SCV"')
TERRAN_SCIENCE_FACILITY: SCUnit = SCUnit('"Terran Science Facility"')
TERRAN_SCIENCE_VESSEL: SCUnit = SCUnit('"Terran Science Vessel"')
TERRAN_SIEGE_TANK_SIEGE_MODE: SCUnit = SCUnit('"Terran Siege Tank (Siege Mode)"')
TERRAN_SIEGE_TANK_TANK_MODE: SCUnit = SCUnit('"Terran Siege Tank (Tank Mode)"')
TERRAN_STARPORT: SCUnit = SCUnit('"Terran Starport"')
TERRAN_SUPPLY_DEPOT: SCUnit = SCUnit('"Terran Supply Depot"')
TERRAN_VALKYRIE: SCUnit = SCUnit('"Terran Valkyrie"')
TERRAN_VULTURE: SCUnit = SCUnit('"Terran Vulture"')
TERRAN_WRAITH: SCUnit = SCUnit('"Terran Wraith"')
TOM_KAZANSKY_WRAITH: SCUnit = SCUnit('"Tom Kazansky (Wraith)"')
TORRASQUE_ULTRALISK: SCUnit = SCUnit('"Torrasque (Ultralisk)"')
UNCLEAN_ONE_DEFILER: SCUnit = SCUnit('"Unclean One (Defiler)"')
UNUSED_TERRAN_BLDG_TYPE_1: SCUnit = SCUnit('"Unused Terran Bldg type 1"')
UNUSED_TERRAN_BLDG_TYPE_2: SCUnit = SCUnit('"Unused Terran Bldg type 2"')
UNUSED_ZERG_BLDG: SCUnit = SCUnit('"Unused Zerg Bldg"')
UNUSED_ZERG_BLDG_5: SCUnit = SCUnit('"Unused Zerg Bldg 5"')
UNUSED_TYPE_1: SCUnit = SCUnit('"Unused type 1"')
UNUSED_TYPE_2: SCUnit = SCUnit('"Unused type 2"')
UNUSED_UNIT_228: SCUnit = SCUnit('"Unused unit 228"')
URAJ_CRYSTAL: SCUnit = SCUnit('"Uraj Crystal"')
URSADON_ICE_WORLD: SCUnit = SCUnit('"Ursadon (Ice World)"')
VESPENE_GEYSER: SCUnit = SCUnit('"Vespene Geyser"')
VESPENE_ORB_PROTOSS_TYPE_1: SCUnit = SCUnit('"Vespene Orb (Protoss Type 1)"')
VESPENE_ORB_PROTOSS_TYPE_2: SCUnit = SCUnit('"Vespene Orb (Protoss Type 2)"')
VESPENE_SAC_ZERG_TYPE_1: SCUnit = SCUnit('"Vespene Sac (Zerg Type 1)"')
VESPENE_SAC_ZERG_TYPE_2: SCUnit = SCUnit('"Vespene Sac (Zerg Type 2)"')
VESPENE_TANK_TERRAN_TYPE_1: SCUnit = SCUnit('"Vespene Tank (Terran Type 1)"')
VESPENE_TANK_TERRAN_TYPE_2: SCUnit = SCUnit('"Vespene Tank (Terran Type 2)"')
VULTURE_SPIDER_MINE: SCUnit = SCUnit('"Vulture Spider Mine"')
WARBRINGER_REAVER: SCUnit = SCUnit('"Warbringer (Reaver)"')
WARP_GATE: SCUnit = SCUnit('"Warp Gate"')
XELNAGA_TEMPLE: SCUnit = SCUnit('"Xel\'Naga Temple"')
YGGDRASILL_OVERLORD: SCUnit = SCUnit('"Yggdrasill (Overlord)"')
YOUNG_CHRYSALIS: SCUnit = SCUnit('"Young Chrysalis"')
ZERATUL_DARK_TEMPLAR: SCUnit = SCUnit('"Zeratul (Dark Templar)"')
ZERG_BEACON: SCUnit = SCUnit('"Zerg Beacon"')
ZERG_BROODLING: SCUnit = SCUnit('"Zerg Broodling"')
ZERG_CEREBRATE: SCUnit = SCUnit('"Zerg Cerebrate"')
ZERG_CEREBRATE_DAGGOTH: SCUnit = SCUnit('"Zerg Cerebrate Daggoth"')
ZERG_CREEP_COLONY: SCUnit = SCUnit('"Zerg Creep Colony"')
ZERG_DEFILER: SCUnit = SCUnit('"Zerg Defiler"')
ZERG_DEFILER_MOUND: SCUnit = SCUnit('"Zerg Defiler Mound"')
ZERG_DEVOURER: SCUnit = SCUnit('"Zerg Devourer"')
ZERG_DRONE: SCUnit = SCUnit('"Zerg Drone"')
ZERG_EGG: SCUnit = SCUnit('"Zerg Egg"')
ZERG_EVOLUTION_CHAMBER: SCUnit = SCUnit('"Zerg Evolution Chamber"')
ZERG_EXTRACTOR: SCUnit = SCUnit('"Zerg Extractor"')
ZERG_FLAG_BEACON: SCUnit = SCUnit('"Zerg Flag Beacon"')
ZERG_GREATER_SPIRE: SCUnit = SCUnit('"Zerg Greater Spire"')
ZERG_GUARDIAN: SCUnit = SCUnit('"Zerg Guardian"')
ZERG_HATCHERY: SCUnit = SCUnit('"Zerg Hatchery"')
ZERG_HIVE: SCUnit = SCUnit('"Zerg Hive"')
ZERG_HYDRALISK: SCUnit = SCUnit('"Zerg Hydralisk"')
ZERG_HYDRALISK_DEN: SCUnit = SCUnit('"Zerg Hydralisk Den"')
ZERG_LAIR: SCUnit = SCUnit('"Zerg Lair"')
ZERG_LARVA: SCUnit = SCUnit('"Zerg Larva"')
ZERG_LURKER: SCUnit = SCUnit('"Zerg Lurker"')
ZERG_LURKER_EGG: SCUnit = SCUnit('"Zerg Lurker Egg"')
ZERG_MARKER: SCUnit = SCUnit('"Zerg Marker"')
ZERG_MUTALISK: SCUnit = SCUnit('"Zerg Mutalisk"')
ZERG_NYDUS_CANAL: SCUnit = SCUnit('"Zerg Nydus Canal"')
ZERG_OVERLORD: SCUnit = SCUnit('"Zerg Overlord"')
ZERG_OVERMIND: SCUnit = SCUnit('"Zerg Overmind"')
ZERG_OVERMIND_WITH_SHELL: SCUnit = SCUnit('"Zerg Overmind (With Shell)"')
ZERG_QUEEN: SCUnit = SCUnit('"Zerg Queen"')
ZERG_QUEENS_NEST: SCUnit = SCUnit('"Zerg Queen\'s Nest"')
ZERG_SCOURGE: SCUnit = SCUnit('"Zerg Scourge"')
ZERG_SPAWNING_POOL: SCUnit = SCUnit('"Zerg Spawning Pool"')
ZERG_SPIRE: SCUnit = SCUnit('"Zerg Spire"')
ZERG_SPORE_COLONY: SCUnit = SCUnit('"Zerg Spore Colony"')
ZERG_SUNKEN_COLONY: SCUnit = SCUnit('"Zerg Sunken Colony"')
ZERG_ULTRALISK: SCUnit = SCUnit('"Zerg Ultralisk"')
ZERG_ULTRALISK_CAVERN: SCUnit = SCUnit('"Zerg Ultralisk Cavern"')
ZERG_ZERGLING: SCUnit = SCUnit('"Zerg Zergling"')
