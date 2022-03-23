from game.shared.point import Point

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._total_score = 0
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        collector = cast.get_first_actor("collectors")
        velocity = self._keyboard_service.get_direction()
        collector.set_velocity(velocity) 

        gemstones = cast.get_actors("gemstones")
        for gemstone in gemstones:
            a_velocity = Point(0, 5)
            gemstone.set_velocity(a_velocity)     

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        collector = cast.get_first_actor("collectors")
        gemstones = cast.get_actors("gemstones")

        banner.set_text(f"Score: {self._total_score}")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        collector.move_next(max_x, max_y)
        
        for gemstone in gemstones:
            gemstone.move_next(max_x, max_y)
            if collector.get_position().equals(gemstone.get_position()):
                message = gemstone.get_message()
                banner.set_text(message) 
                if message == '100':
                    self._total_score += 100
                else:
                    self._total_score -= 100

                cast.remove_actor("gemstones", gemstone)   
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()