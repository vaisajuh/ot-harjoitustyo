import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)


    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")
    

    def test_saldo_kasvaa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "saldo: 20.0")
    
    
    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "saldo: 0.0")
    

    def test_saldo_ei_muutu(self):
        self.maksukortti.ota_rahaa(2000)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")
    

    def test_riittavatko_rahat(self):
        boolean = self.maksukortti.ota_rahaa(2000) # x > 10 == False
        self.assertEqual(str(boolean), "False")