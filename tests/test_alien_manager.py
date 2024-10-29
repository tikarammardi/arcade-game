from app.alien_manager import AlienManager

def test_create_aliens():
    alien_manager = AlienManager()
    alien_manager.create_aliens()
    assert len(alien_manager.aliens) > 0  # Check that aliens were created

def test_all_aliens_defeated():
    alien_manager = AlienManager()
    alien_manager.create_aliens()
    alien_manager.aliens.clear()  # Clear the list to simulate all aliens defeated
    assert alien_manager.all_aliens_defeated() is True

def test_remove_alien():
    alien_manager = AlienManager()
    alien_manager.create_aliens()
    alien_to_remove = alien_manager.aliens[0]
    alien_manager.remove_alien(alien_to_remove)
    assert alien_to_remove not in alien_manager.aliens
