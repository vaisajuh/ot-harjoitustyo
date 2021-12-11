class HandleSession:
    """Luokka, joka vastaa kirjautuneista käyttäjistä
    
    Attributes:
    session: Kirjautuneet käyttäjät tallennetaan listaan
    """

    def __init__(self):
        """Luokan konstruktori, joka luo listan"""
        
        self.session = []

    def add_session(self, user_id):
        """Lisää kirjatuneen käyttäjän id-numeron listaan"""
        
        self.session.append(user_id)

    def get_session(self):
        """Palauttaa viimeksi kirjautuneen käyttäjän id-numeron listasta"""
        
        user_id = self.session[-1]
        return user_id
