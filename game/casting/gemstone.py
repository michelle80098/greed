from game.casting.actor import Actor

class Gemstone(Actor):
    """
    An item of great worth of no worth. 
    
    The responsibility of an Gemstone provide a message.

    Attributes:
        _message (string): A short description about the gemstone.
    """
    def __init__(self):
        super().__init__()
        self._message = ""
        
    def get_message(self):
        """Gets the gemstone's message.
        
        Returns:
            string: The message.
        """
        
        return self._message
    
    def set_message(self, message):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._message = message