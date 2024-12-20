import random

def roll_dice(sides: int) -> int:
    """Roll a dice with the given number of sides."""
    return random.randint(1, sides)

def resolve_attack(attacker, target, weapon):
    """Calculate if the attack hits and apply damage."""
    hit_accuracy = roll_dice(20) + attacker.ACC + weapon["ACC"]
    
    if hit_accuracy >= target.DEF:
        damage = roll_dice(weapon["damage_dice"]) + attacker.STR
        target.HP -= damage
        return f"Hit! {attacker.Name} deals {damage} damage to {target.Name}."
    else:
        return f"Miss! {attacker.Name}'s total accuracy ({hit_accuracy}) < {target.DEF}."
    
def resolve_spell(caster, target, spell, monsters, selected_monster_index):
    """Resolve a spell action. Handles both healing and damaging spells, as well as spell resistance."""
    if caster.MP < spell["mana_cost"]:
        return f"{caster['name']} does not have enough mana to cast {spell['name']}!"

    # Deduct mana
    caster.MP -= spell["mana_cost"]

    if spell.get("effect") == "heal":
        # Healing logic
        heal_amount = roll_dice(spell["damage_dice"]) + caster.INT
        caster.HP = min(100, caster.HP + heal_amount)
        return f"{caster.Name} casts {spell.Name} and heals {heal_amount} HP!"
    else:
        hit_accuracy = roll_dice(20) + caster.ACC + spell["ACC"]

        if hit_accuracy > target.CHA:
            damage = roll_dice(spell["damage_dice"]) + caster.INT
            target.HP -= damage
            return f"Hit! {caster.Name} deals {damage} damage to {target.Name}."
        else:
            return f"Miss! {caster.Name}'s total accuracy ({hit_accuracy}) < {target.DEF}."

def resolve_attack_monster(monster, target):
    hit_accuracy = roll_dice(20) + monster.ACC
    if hit_accuracy >= target.DEF:
        damage = roll_dice(10) + monster.STR
        target.HP -= damage
        return f"{monster.Name} attacks {target.Name} and deals {damage} damage!"
    else:
        return f"Miss! {monster.Name}'s total accuracy ({hit_accuracy}) < {target.DEF}."
