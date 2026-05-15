import random

# Base Character Class
class Character:
    def __init__(self, name, health, max_health, attack_min, attack_max):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.attack_min = attack_min
        self.attack_max = attack_max
        self.is_evading = False
        self.is_shielded = False
        self.is_stealthed = False

    def attack(self, target):
        damage = random.randint(self.attack_min, self.attack_max)
        print(f"{self.name} attacks {target.name}!")
        target.take_damage(damage)

    def take_damage(self, damage):
        if self.is_evading:
            print(f"{self.name} successfully evaded the attack! No damage taken.")
            self.is_evading = False  
            return
        
        if self.is_shielded:
            print(f"{self.name}'s shield absorbed the attack! No damage taken.")
            self.is_shielded = False  
            return

        if self.is_stealthed:
            print(f"{self.name} is hidden in the shadows! The attack completely missed.")
            self.is_stealthed = False  
            return

        self.health -= damage
        print(f"{self.name} takes {damage} damage! Current Health: {max(0, self.health)}/{self.max_health}")

    def heal(self, amount):
        if self.health <= 0:
            print(f"{self.name} cannot heal while defeated!")
            return
        
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} heals for {amount}! Current Health: {self.health}/{self.max_health}")

    def display_stats(self):
        print(f"{self.name} Stats")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Attack Range: {self.attack_min}-{self.attack_max}")


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, max_health=140, attack_min=15, attack_max=25)

    def special_ability_1(self, target):
        print(f"{self.name} uses Power Strike!")
        damage = random.randint(25, 40)
        target.take_damage(damage)

    def special_ability_2(self, target):
        print(f"\n{self.name} lets out a Battle Cry!")
        damage = 20
        target.take_damage(damage)


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=90, max_health=90, attack_min=10, attack_max=30)

    def special_ability_1(self, target):
        print(f"{self.name} casts Fireball!")
        damage = random.randint(35, 45)
        target.take_damage(damage)

    def special_ability_2(self, target):
        print(f"{self.name} casts Spell Shield!")
        self.is_shielded = True


class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=100, max_health=100, attack_min=12, attack_max=28)

    def special_ability_1(self, target):
        print(f"{self.name} uses Quick Shot! Firing two arrows!")
        damage1 = random.randint(10, 18)
        damage2 = random.randint(10, 18)
        target.take_damage(damage1 + damage2)

    def special_ability_2(self, target):
        print(f"{self.name} prepares to Evade the next attack!")
        self.is_evading = True


class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=130, max_health=130, attack_min=14, attack_max=22)

    def special_ability_1(self, target):
        print(f"{self.name} strikes with Holy Strike!")
        damage = random.randint(22, 32)
        target.take_damage(damage)

    def special_ability_2(self, target):
        print(f"{self.name} activates Divine Shield!")
        self.is_shielded = True


# Added the Rogue Class because it's the best class
class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, health=95, max_health=95, attack_min=12, attack_max=22)

    def special_ability_1(self, target):
        # Backstab - Huge damage if hitting from stealth, otherwise normal crit chance
        print(f"{self.name} lunges for a Backstab!")
        if self.is_stealthed:
            damage = random.randint(40, 55)
            print("Critical Hit from the shadows!")
            self.is_stealthed = False #no more stealth
        else:
            damage = random.randint(20, 30)
        target.take_damage(damage)

    def special_ability_2(self, target):
        # Vanish gives stealth to avoid the next attack and set up a backstab
        print(f"{self.name} throws a smoke bomb and vanishes into the shadows!")
        self.is_stealthed = True


# Evil Wizard Class (Boss)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=260, max_health=260, attack_min=15, attack_max=28)
        self.minion = None

    def regenerate(self):
        regen_amount = random.randint(5, 12)
        self.health = min(self.max_health, self.health + regen_amount)
        print(f"{self.name} regenerates {regen_amount} health.")

    # minions must be defeated before you can attack the wizard again
    def summon_minion(self):
        if self.minion is None or self.minion.health <= 0:
            print(f"🔮 {self.name} chants an incantation and summons an Undead Skeleton to protect him!")
            self.minion = Character("Undead Skeleton", health=40, max_health=40, attack_min=8, attack_max=14)
        else:
            print(f"{self.name} tries to summon a minion, but one is already guarding him!")

    # DARK VORTEX
    def cast_dark_vortex(self, target):
        print(f"🌪️ {self.name} channels a massive Dark Vortex!")
        damage = random.randint(30, 45)
        target.take_damage(damage)


# Game Setup and Loop
def main():
    print("Welcome to the Hero vs. Evil Wizard Battle Arena!")
    player_name = input("Enter your hero's name: ")

    print("Choose your character class:")
    print("1. Warrior (High Health, Heavy Hitter)")
    print("2. Mage (Glass Cannon, High Burst/Shield)")
    print("3. Archer (Ranged Multi-strikes, Evasion)")
    print("4. Paladin (Balanced, High Defenses)")
    print("5. Rogue (Stealth mechanics, Critical Backstabs)")
    
    choice = input("Enter choice (1-5): ")
    
    if choice == "1":
        player = Warrior(player_name)
    elif choice == "2":
        player = Mage(player_name)
    elif choice == "3":
        player = Archer(player_name)
    elif choice == "4":
        player = Paladin(player_name)
    elif choice == "5":
        player = Rogue(player_name)
    else:
        print("Invalid choice! Defaulting to Warrior.")
        player = Warrior(player_name)
        
    print(f"✨ You have chosen the path of the {type(player).__name__}! ✨")
    print("Your Special Abilities are:")
    if isinstance(player, Warrior):
        print(" -> Ability 1: Power Strike (Heavy crushing damage)")
        print(" -> Ability 2: Battle Cry (Guaranteed mid-tier damage)")
    elif isinstance(player, Mage):
        print(" -> Ability 1: Fireball (Massive burst magic damage)")
        print(" -> Ability 2: Spell Shield (Absorbs the next incoming attack)")
    elif isinstance(player, Archer):
        print(" -> Ability 1: Quick Shot (Fires two standard arrows at once)")
        print(" -> Ability 2: Evade (Prepares to dodge the next attack)")
    elif isinstance(player, Paladin):
        print(" -> Ability 1: Holy Strike (Reliable bonus radiant damage)")
        print(" -> Ability 2: Divine Shield (Blocks the next incoming attack)")
    elif isinstance(player, Rogue):
        print(" -> Ability 1: Backstab (Massive damage if hitting from stealth)")
        print(" -> Ability 2: Vanish (Enters stealth to dodge and prep a backstab)")

    wizard = EvilWizard("Malakor the Vile")

    print(f"An epic battle begins! {player.name} the Hero vs {wizard.name}!")

    while player.health > 0 and wizard.health > 0:
        # Determine who the player is targeting (Minion must be defeated first if alive)
        active_target = wizard
        if wizard.minion and wizard.minion.health > 0:
            active_target = wizard.minion
            print(f"⚠️ WARNING: An {wizard.minion.name} (HP: {wizard.minion.health}) is blocking your path to the Wizard!")

        wizard.display_stats()
        player.display_stats()

        print("YOUR TURN")
        print(f"1. Attack {active_target.name}")
        print(f"2. Special Ability 1 on {active_target.name}")
        print(f"3. Special Ability 2")
        print("4. Heal")
        print("5. View Detailed Stats")
        
        action = input("Choose an action: ")

        if action == "1":
            player.attack(active_target)
        elif action == "2":
            player.special_ability_1(active_target)
        elif action == "3":
            player.special_ability_2(active_target)
        elif action == "4":
            player.heal(random.randint(20, 35))
        elif action == "5":
            player.display_stats()
            wizard.display_stats()
            if wizard.minion and wizard.minion.health > 0:
                wizard.minion.display_stats()
            continue 
        else:
            print("You stumbled around and missed your chance to act!")

        # Clean up minion if it died this turn
        if wizard.minion and wizard.minion.health <= 0:
            print(f"💀 The {wizard.minion.name} has been destroyed!")
            wizard.minion = None

        # Check if Wizard was defeated before he or his minions can retaliate
        if wizard.health <= 0:
            break

        print("ENEMY TURN")
        wizard.regenerate()

        # randomly decides action
        wizard_action = random.choice(["attack", "ability", "summon"])

        if wizard_action == "summon" and (wizard.minion is None):
            wizard.summon_minion()
        elif wizard_action == "ability":
            wizard.cast_dark_vortex(player)
        else:
            wizard.attack(player)

        # If a minion exists, it gets a small bonus attack too!
        if player.health > 0 and wizard.minion and wizard.minion.health > 0:
            print(f"\nThe {wizard.minion.name} strikes!")
            wizard.minion.attack(player)

    # End Game Conditions
    print("=========================")
    if player.health > 0:
        print(f"🏆 VICTORY! {player.name} has defeated {wizard.name} and saved the realm!")
    else:
        print(f"💀 DEFEAT! {player.name} fell in battle. {wizard.name} rules supreme...")
    print("=========================")

if __name__ == "__main__":
    main()