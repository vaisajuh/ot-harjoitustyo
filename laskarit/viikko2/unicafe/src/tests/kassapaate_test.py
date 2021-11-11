import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_rahamaara_ja_myydyt(self):
        summa = self.kassapaate.kassassa_rahaa
        myyty = self.kassapaate.edulliset + self.kassapaate.maukkaat
        self.assertEqual(summa, 100000)
        self.assertEqual(myyty, 0)
    

    def test_kateisnosto_toimii(self):
        edulliset = self.kassapaate.syo_edullisesti_kateisella(242)
        maukkaat = self.kassapaate.syo_maukkaasti_kateisella(405)
        vaihtoraha = edulliset + maukkaat
        myyty = self.kassapaate.edulliset + self.kassapaate.maukkaat
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100640)
        self.assertEqual(myyty, 2)
        self.assertEqual(vaihtoraha, 7)
    
    def test_maksu_ei_ole_riittava(self):
        edulliset = self.kassapaate.syo_edullisesti_kateisella(239)
        maukkaat = self.kassapaate.syo_maukkaasti_kateisella(399)
        self.assertEqual(edulliset, 239)
        self.assertEqual(maukkaat, 399)
    

    def test_korti_toimii(self):
        tarpeeksi = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        tarpeeksi2 = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(tarpeeksi), "True")
        self.assertEqual(str(tarpeeksi2), "True")
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    

    def test_kortilla_ei_tarpeeksi_rahaa(self):
        self.maksukortti = Maksukortti(10)
        tarpeeksi = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        tarpeeksi2 = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(tarpeeksi), "False")
        self.assertEqual(str(tarpeeksi2), "False")
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    

    def test_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)