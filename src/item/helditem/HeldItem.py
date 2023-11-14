from src.item.helditem.IHeldItem import IHeldItem
from src.item.Item import Item
from src.item.ItemType import ItemType

class HeldItem(IHeldItem, Item):
    def __init__(self, name: str, item_type:ItemType, effect:dict) -> None:
        super().__init__(name)
        self.itemType = item_type
        self.effect = effect
        
    # Getters
        
    def getItemType(self) -> ItemType:return self.itemType
    def getEffect(self) -> dict:return self.effect
    
    def use(self) -> tuple[ItemType, int]|tuple[ItemType, tuple[str, int]]:
        '''Use the item on the given pokemon
        
        returns:
            tuple[ItemType, int]|tuple[ItemType, tuple[str, int]]: The type of the item and the effect of the item
                ItemType.HEALING: The type of the item and the amount of hp to heal
                ItemType.BOOST_STAT: The type of the item and the stat to boost and the amount to boost
                ItemType.BOOST_ATTACK_TYPE: The type of the item and the attack type to boost and the amount to boost'''
            
        if self.itemType == ItemType.HEALING:
            effect = self.effect.get('healing_amount', 0)
        elif self.itemType == ItemType.BOOST_STAT:
            statToBoost = self.effect.get('stat', None)
            boostAmount = self.effect.get('boost_amount', 0)
            effect = (statToBoost, boostAmount)
        elif self.itemType == ItemType.BOOST_ATTACK_TYPE:
            attackTypeToBoost = self.effect.get('attack_type', None)
            boostAmount = self.effect.get('boost_amount', 0)
            effect = (attackTypeToBoost, boostAmount)
        return (self.itemType, effect)