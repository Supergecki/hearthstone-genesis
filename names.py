name_prefaces = list(set([
    #initial prefixes
    'Holy', 'Dark', 'Merchant', 'Lively', 'Blood', 'Furious', 'Death', 'Critical', 'High',
    'Fel', 'Time', 'Goblin', 'Elven', 'Shady', 'Deaf', 'Deadly', 'Arcane', 'Experienced',
    'Black', 'White', 'Gold', 'Silver', 'Green', 'Blue', 'Orange', 'Red', 'Grey', 'Shadow',
    'Demonic', 'Wild', 'Power', 'Rowdy', 'Shattered', 'Sun', 'Moon',
    'Steamweedle', 'Parasitic', 'Lonely', 'Tauren', 'Murloc', 'Diabolic', 'Kvaldir',
    'Stealthy', 'Kabal', 'Babbling', 'Bubbling', 'Dragon', 'Armored', 'Jade', 'Diamond', 'Onyx',
    'Smoking', 'Coughing', 'Worthless', 'Awful', 'Bad', 'Wise', 'Tortured', 'Light',
    'Solemn', 'Divine', 'Zephyr', 'Electric', 'Amateur', 'Greedy', 'Humble', 'Skeletal',
    'Ancient', "Death's", 'Inspiring', 'Shadow of',

    #unordered prefixes
    'Unholy', 'Knight', 'Undead', 'Water', 'Air',
    'Fire', 'Earth', 'Frenzy', 'Calm', 'Life', 'Undeath', 'Dying', 'Dangerous', 'Demonic', 'Chronical',
    'Gnome', 'Kobold', 'Treant', 'Troll', 'Enlightened', 'Harmless', 'Harmful', 'Poisonous', 'Young',
    'Elder', 'Elderly', 'Bronze', 'Copper', 'Cobalt', 'Iron', 'Silverhand', 'Tamed', 'Unleashed', 'Might',
    'Force', 'Destructive', 'Destruction', 'Broken', 'Star', 'Friendly', 'Group', 'Mass', 'Devilish', 'Devil',
    'Grimestreet', 'Speaking', 'Screaming', 'Crying', 'Elemental', 'Beast', 'Totem', 'Ruby', 'Emerald', 'Burning',
    'Horrible', 'Horror', 'Terrible', 'Intelligent', 'Allmighty', 'Taunting', 'Lightning', 'Thunder', 'Dumb', 'Idiot',
    'Zombie', 'Fresh', 'New', "Light's", "Life's", 'Mirror of', 'Mark of', 'Lunar', 'Flesh', 'Rune', 'Commanding',
    'Awakened', 'Running', 'Toxic', 'Flying', 'Sealed', 'Natural', 'Shielded',

    #The Witchwood
    'Forest', 'Woods', 'Whispering', 'Bewitched', 'Hunting', 'Dire', 'Terror', 'Hidden', 'Cathedral', 'Ghostly', 'Ghost',
    'Imaginary', 'Scale', 'Blink', 'Spectral', 'Cursed', 'Blazing', 'Earthen', 'Dusk', 'Twilight', 'Militia', 'Swamp', 'Lost',
    'Hench-Clan', 'Nightmare', 'Phantom', 'Raven', 'Voodoo', 'Mad', 'Night', 'Day', 'Crazy', 'Witchwood', 'Darkmire', 'Furious',
    'Worgen', 'Gilnean',

    #Kobolds and Catacombs
    'Greedy', 'Astral', 'Branching', 'Ironwood', 'Oaken', 'Grizzled', 'Wandering', 'Cave', 'Crushing', 'Shifting', 'Raven',
    'Explosive', 'Leyline', "Dragon's", 'Benevolent', 'Crystal', 'Psyonic', 'Gilded', "Twilight's", 'Psychic', 'Cavern', 'Sudden',
    "Fal'dorei", 'Unstable', 'Murmuring', 'Primal', 'Windshear', 'Sapphire', 'Amethyst', 'Possessed', 'Void', 'Feral', 'Wax', 'Plated',
    'Boisterous', 'Fungal', 'Lone', 'Rummaging', 'Sewer', 'Shrieking', 'Stoneskin', 'Toothy', 'Ebon', 'Hoarding', 'Shimmering',
    'Mushroom', 'Shroom', 'Sneaky', 'Carnivorous', 'Corrosive', 'Furbolg', 'Guild', 'Trogg', 'Hungry', 'Corridor', 'Spiteful',
    'Violet', 'Sleepy',

    #Rise of Shadows
    'Dream', 'Lucent', "The Forest's", 'Rapid', 'Shimmer', 'Marked', 'Magic', 'Mana', 'Messenger', "Conjurer's", 'Kirin Tor', 'Desperate',
    'Lightforged', 'Mysterious', 'EVIL', 'Shadowy', 'Hench-Clan', 'Unsleeping', 'Convincing', 'Daring', 'Underbelly', 'Sludge',
    'Soul of', 'Scar', 'Walking', 'Eager', 'Aranasi', 'Darkest', 'Jumbo', 'Sweeping', 'Vicious', 'Omega', 'Dimensional', 'Potion', 'Dalaran',
    'Faceless', 'Proud', 'Traveling', 'Azerite', 'Recurring', 'Eccentric', 'Mad', 'Unseen', 'Exotic', 'Tunnel', 'Heroic', 'Whirlwind', 'Burly',
    'Big',

    #Curse of Naxxramas
    'Poison', 'Web', "Anub'ar", "Death's", 'Echoing', 'Haunted', 'Mad', "Nerub'ar", 'Nerubian', 'Dancing', 'Wailing',

    #The Grand Tournament
    'Living', 'Darnassus', 'Mulch', 'Savage', 'Brave', 'Bear', "King's", 'Dread', 'Stable', 'Ram', 'Acid', 'Fallen', 'Coldarra', 'Competitive',
    'Argent', 'War', 'Tuskarr', 'Pure', 'Confused', 'Confusing', 'Wyrmrest', 'Spawn of', 'Undercity', 'Poisoned', 'Shado-Pan', 'Ancestral',
    'Charged', 'Draenei', 'Thunder Bluff', 'Tiny', 'Wrath', 'Fearsome', "Alexstrasza's", 'Orgrimmar', 'Magnataur', 'Sea', 'Injured', 'Lowly',
    'Tournament', 'Boneguard', 'Garrison', 'Lance', 'Coliseum', 'Dragonhawk', 'Fencing', 'Ice', "Light's", 'Silent', 'Evil', 'Frigid', 'Pit',
    'Grand', 'Captured', 'Chill', 'North Sea', 'Frost',

    #Hall of Fame
    'Gloom', 'Mind', 'Glitter', 'Murkspark', "Captain's", 'Coldlight', 'Old', 'Azure', 'Elite', 'Molten',

    #Descent of Dragons
    'Dwarven', 'Phase', 'Diving', 'Primordial', 'Rolling', 'Righteous', 'Sand', 'Sanctuary', 'Sky', 'Timeless', 'Amber', "Galakrond's",
    "Lazul's", 'Mind', 'Fate', 'Grave', 'Chrono', 'Time', 'Infinite', 'Bloodsail', "Dragon's", 'Seal', 'Necrium', 'Umbral', 'Candle', "Storm's", 'Surging',
    'Squall', 'Corrupt', 'Dark', 'Dragonblight', 'Fiendish', 'Veiled', 'Crazed', 'Abyssal', 'Sky', 'Ramming', 'Depth', 'Hot', 'Evasive', 'Parachute',
    'Tasty', 'Bad', 'Blowtorch', 'Goboglide', 'Devoted', 'Dragonmaw', 'Hoard', 'Wing', "Zul'Drak", 'Big', 'Old', 'Chromatic', 'Plate', 'Tentacled',
    'Camouflaged', 'Utgarde', 'Twin',

    #Ashes of Outland
    'Crimson', 'Sigil', 'Immolation', 'Ashtongue', 'Imprisoned', 'Skull', 'Coilfang', 'Pit', 'Ironbark', 'Glowfly', 'Marsh', 'Hell', 'Pack',
    "Scavenger's", 'Augmented', "Mok'nathal", 'Scrap', 'Nagrand', 'Apexis', "Incanter's", 'Netherwind', 'Deep', 'Aldor', 'Hand', 'Underlight',
    'Reliquary', 'Sethekk', 'Psyche', 'Soul', 'Blackjack', 'Ambush', 'Dirty', 'Greyheart', 'Bogstrok', 'Serpentshrine', 'Totemic', 'Vivid',
    'Boggspine', 'Torrent', 'Dark', 'Nightshade', 'The Dark', 'Hand of', 'Enhanced', 'Sword', 'Bonechewer', 'Warmaul', 'Bloodboil', 'Ethereal',
    'Infectious', 'Rocket', 'Soulbound', "Mo'arg", 'Rustsworn', 'Blistering', 'Overconfident', 'Terrorguard', 'Burrowing', 'Disguised',
    'Ruststeed', 'Waste', 'Scavenging', 'Supreme', 'Scrapyard',
]))

#print(sorted(name_prefaces))

names = list(set([
    #initial names
    'Knight', 'Soldier', 'Adventurer', 'Commander', 'Seeker', 'Priestess', 'Striker', 'Bomber',
    'Underground', 'Shade', 'Ghost', 'Apprentice', 'Wizard', 'Archer', 'Skullsplitter',
    'Medic', 'Destroyer', 'Reaver', 'Recruiter', 'Recruit', 'Demon', 'Conjurer', 'Monster',
    'Spellcaster', 'Keeper', 'Snake', 'Civilian', 'Sniper', 'Murloc', 'Mindbender',
    'Lifebender', 'Soulbender', 'Gatekeeper', 'Giant', 'Gargoyle', 'Vampire', 'Breadmaker',
    'Breeder', 'Grinder', 'Bloodsucker', 'Trapper', 'First Mate', 'Second Mate', 'Captain',
    'Master', 'Ogre', 'Alchemist', 'Kabalist', 'Gypsy', 'Merchant', 'Ambusher', 'Ninja',
    'Guardian', 'Squashbuckler', 'Brother', 'Whisperer', 'Initiate', 'Garbageman', 'Garbage',
    'Old Thing', 'Old One', 'Sergeant', 'Seer', 'Oracle', 'Beefcake', 'Bartender', 'Rager',
    'Bruiser', 'King', 'Queen', 'Bishop', 'Assassin', 'Barbarian', 'Sorcerer', 'Amazon',
    'Paladin', 'Predator', 'Banshee', 'Scourge', 'Marine', 'Scientist', 'Experiment', 'Mage',
    'Abomination', 'Wall',

    #unordered names
    'Princess', 'Ritualist', 'Ruiner', 'Trader', 'Thrower',

    #Mean Streets of Gadgetzan
    'Dreamer', 'Sensei', 'Pack', 'Lackey', 'Marshal', 'Sheriff', 'Enforcer',
    'Protector', 'Mage', 'Priest', 'Warlock', 'Druid', 'Rogue', 'Shaman', 'Paladin', 'Warrior', 'Hunter',
    'Operative', 'Rager', 'Illusionist', 'Chieftain', 'Apothecary', 'Defender', 'Gadgeteer', 'Blacksmith',
    'Pirate', 'Tunneler', 'Sniper', 'Baron', 'Courier', 'Trickster', 'Smuggler', 'Sergeant', 'Healer',
    'Chemist', 'Corsair', 'Master', 'Agents', 'Investigator', 'Detective',

    #Journey to Un'Goro
    'Forager', 'Hatchling', 'Stalker', 'Warden', 'Tempest', 'Surger', 'Champion', 'Caller', 'Slayer', 'Harbinger',
    'Sentinel', 'Lurker', 'Sentry', 'Lord', 'Shard', 'Crawler', 'Runt', 'Egg', 'Ooze', 'Lookout', 'Creeper', 'Lizard',
    'Fledgling', 'Scout', 'Phoenix', 'Hydra', 'Servant', 'Crusher', 'Watcher', 'Drake', 'Primalist',

    #Knights of the Frozen Throne
    'Scavenger', 'Tracker', 'Bat', 'Widow', 'Bowman', 'Walker', 'Wraith', 'Crusader', 'Guard', 'Ascendant', 'Acolyte',
    'Bishop', 'Statue', 'Haunter', 'Pillager', 'Breaker', 'Hexxer', 'Reveler', 'Fiend', 'Berserker', 'Soulclaimer',
    'Revenant', 'Veteran', 'Tiller', 'Cleric', 'Prince', 'Zealot', 'Fisherman', 'Speaker', 'Enchanter', 'Ghoul',
    'Rider', 'Gravedigger', 'Punisher', 'Shambler', 'Necromancer', 'Howler', 'Freebooter', 'Rascal', 'Abomination',
    'Skeleton', 'Worm', 'Scalebane', 'Raiser', "Val'kyr", 'Colossus', 'Ghost', 'Unraveler', 'Weaver',

    #Blackrock Mountain
    'Lumberer', 'Waker', 'Consort', 'Whelp', 'Skulker', 'Boss', 'Flinger', 'Technician', 'Corruptor', 'Patron',
    'Emperor',

    #Descent of Dragons
    'Spellwing', 'Claw', 'Explorer', 'Storm', 'Gryphon', 'Bane', 'Sharpshooter', 'Caster', 'Dragonrider', 'Disciple',
    'Envoy', 'Elementalist', 'Summoner', 'Netherwing', 'Worshipper', 'Cultist', 'Raider', 'Barge', 'Quartermaster',
    'Scion', 'Chimaera', 'Flyfish', 'Hawk', 'Tech', 'Dragonbreath', 'Hippogryph', 'Skyfin', 'Gyrocopter', 'Battlemage',
    'Brigand', 'Batrider', 'Scalerider', 'Wyrm', 'Feywing', 'Saboteur', 'Poacher', 'Menace', 'Albatross', 'Transmogrifier',
    'Balloon', 'Dirigible', 'Maniac', 'Drakonid', 'Tyrant', 'Grapplesniper', 'Purifier',

    #Goblins vs Gnomes
    'Cub', 'Tender', 'Cat', 'Leaper', 'Chugger', 'Spewer', 'Blastmage', 'Spellstopper', 'Leviathan', 'Minibot', 'Boxer',
    'Bot', 'Barber', 'Cheat', 'Cogmaster', 'Zap-o-matic', 'Spiritwalker', 'Cannon', 'Golem', 'Clunker', 'Engine', 'Juggernaut',
    'Maiden', 'Dummy', 'Sheep', 'Warper', 'Machine', 'Stomper', 'Recombobulator', 'Infantry', 'Experimenter', 'Sapper',
    'Hobgoblin', 'Illuminator', 'Exorcist', 'Brute', 'Tank', 'Mystic', 'Tallstrider', 'Yeti', 'Shredder', 'Healbot',
    'Lobber', 'Dog', 'Sky Golem',

    #Ashes of Outland
    'Sigil Runner', 'Felfin', 'Netherwalker', 'Battlelord', 'Antaen', 'Warlord', 'Satyr', 'Boar', 'Felmaw', 'Porcupine', 'Lion',
    'Scryer', 'Observer', 'Sungill', 'Attendant', 'Truthseeker', 'Homunculus', 'Veilweaver', 'Overseer', 'Stunner', 'Sage', 'Vagrant',
    'Clacker', 'Rumbler', 'Scrap Imp', 'Imp', 'Glare', 'Matron', 'Dreadlord', "Gan'arg", 'Challenger', 'Augmerchant', 'Sporeling',
    'Brawler', 'Vilefiend', 'Artificer', 'Rot', 'Orc', 'Escapee', 'Scorpid', 'Wanderer', 'Navigator', 'Sky Stalker', 'Shivarra',
    'Vanguard',
]))

actions = list(set([
    #initial actions
    'Fusion', 'Summoning', 'Summon', 'Sacrifice', 'Pact', 'Light', 'Well', 'Knife', 'Partnership',
    'Fell', 'Fall', 'Star', 'Doom', 'Control', 'Horror', 'Blessings', 'Corruption', 'Hex', 'Bind',
    'Counter', 'Fit', 'Check', 'Sight', 'Call', 'Calling', "of C'thun", 'Calls', 'Hands', 'Gate',
    'Nether', 'World', 'Region', 'Defense', 'Defenses', 'Offense', 'Weapon', 'Sun', 'Moon', 'Moonlight',
    'Roar', 'Growl', 'Twist', 'Bolt', 'Shot', 'Trap', 'Cast', 'Spell', 'Book', 'Scroll', 'Portal',

    #unordered actions
    'Raid', 'Raiding', 'Unleash', 'Reinforcement', 'Rituals', 'Awakening',

    #Whispers of the Old Gods
    'Rage', 'Infest', 'Flame', 'Destruction', 'Tome', 'Healing', 'Strength', 'Strike',

    #The Boomsday Project
    'Plan', 'Toss', 'Prank', 'Rift', 'Matrix', 'Ray', 'Device', 'Replication', 'Haze', 'Blade', 'Espionage',
    'Vial', 'Burst', 'Reaction', 'Infusion', 'Bomb', 'Assembly', 'Boots',

    #Rastakhan's Rumble
    'Pounce', 'Instincts', 'Roar', 'Hatchet', 'Revenge', 'Arrow', 'Call', 'Evocation', 'Image', 'Scorch',
    'Wave', 'Claw', 'Flash', 'Battleaxe', 'Regeneration', 'Seance', 'Madness', 'Hysteria', 'Tooth', 'Steel',
    'Barrage', 'Smash', 'Visions', 'Rain', 'Rally', 'Shriek', 'Bolt', 'Contract', 'Devastation', 'Roar', 'Whip',

    #One Night in Karazhan
    'Trick', 'Purify', 'Claws', 'Protection', 'Bane',

    #Saviours of Uldum
    'Potential', 'Expedition', 'Overflow', 'Unseal', 'Spear', 'Swarm', 'Mysteries', 'Ward', 'Blessing', 'Activation',
    'Ritual', 'Ripple', 'Penance', 'Plague', 'Burglary', 'Disguise', 'Scimitar', 'Surge', 'Quake', 'Deal', 'Archaeology',

    #League of Explorers
    'Idol', 'Hat', 'Torch', 'Trial',

    #Descent of Dragons
    'Embiggen', 'Secure', 'Breath', 'Clear', 'Reinforcements', 'Hammer', 'Allies', 'Fireball', 'Cause', 'Rune', 'Rip', 'Pack',
    'Rain', 'Skies', 'Rites', 'Chopper',

    #Ashes of Outland
    'Aura', 'Metamorphosis', 'Warglaives', 'Fortunes', 'Beam', 'Germination', 'Growth', 'Tactics', 'Ingenuity', 'Slam', 'Evocation',
    'Flow', 'Blast', 'Wisdom', 'Justice', 'Hope', 'Split', 'Bamboozle', 'Tricks', 'Reflection', 'Spores', 'Knuckles', 'Council', 'Felbolt',
    'Cache', 'Bladestorm', 'Bulwark', 
]))
