from game.casting.player import Player


class Gemstone(Player):
    """
    The gems and the stones 
    
    The responsibility of an Gemstones is to move both the gems, the stones, and their vales 

    Attributes:
        gem_value, stone_value
    """
    def __init__(self):
        super().__init__()
        self._pos_value = 100
        self._neg_value = -100
        self._pos_message = "100"
        self._neg_message = "-100"
        
    def get_gem_value(self):
        """Gets the artifact's message.
        
        Returns:
            string: The message.
        """

        self._value = 100
    
    def get_stone_value(self):
        
        self._value = -100
    

    def adjust_value(self, _neg_message, _pos_message):
        
        
        
       
        for value in self._pos_message and self._neg_message:
            if Player.get_position() == _pos_message:
                return self._pos_value
            
            elif Player.get_position() == _neg_message:
                return self._neg_value




    # def set_pos_value(self, ):
    #     """Updates the message to the given one.
        
    #     Args:
    #         message (string): The given message.
    #     """
    #     self._message = message