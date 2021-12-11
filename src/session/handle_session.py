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
<<<<<<< HEAD
        """Palauttaa viimeksi kirjautuneen käyttäjän id-numeron 
        listasta"""

=======
        """Palauttaa viimeksi kirjautuneen käyttäjän id-numeron listasta"""
        
>>>>>>> 7ddaa855cb7393d5f039f909f178a4568ae5b9ce
        user_id = self.session[-1]
        return user_id
