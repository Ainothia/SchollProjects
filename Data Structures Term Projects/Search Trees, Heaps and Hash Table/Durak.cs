using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proje3
{
    public class Musteri
    {
        private int MusteriID;
        private string KiralamaSaati;

        public Musteri(int MusteriID, string KiralamaSaati)//Constructor Method
        {
            this.MusteriID = MusteriID;
            this.KiralamaSaati = KiralamaSaati;
        }
        //Getter and Setter methods
        public int getMusteriID()
        {
            return MusteriID;
        }

        public void setMusteriID(int MusteriID)
        {
            this.MusteriID = MusteriID;
        }

        public string getKiralamaSaati()
        {
            return KiralamaSaati;
        }

        public void setKiralamaSaati(string KiralamaSaati)
        {
            this.KiralamaSaati = KiralamaSaati;
        }
        public override string ToString()
        {
            return "Musteri ID: " + MusteriID + "\tKiralama Saaati: " + KiralamaSaati+"\n";
        }
    }
    public class Durak
    {
        private string DurakAdı;
        private int BosPark;
        private int TandemBisiklet;
        private int NormalBisiklet;
        public List<Musteri> musteri;

        public Durak(String DurakAdı, int BosPark, int TandemBisiklet, int NormalBisiklet) //Constructor method
        {
            this.DurakAdı = DurakAdı;
            this.BosPark = BosPark;
            this.TandemBisiklet = TandemBisiklet;
            this.NormalBisiklet = NormalBisiklet;
            musteri = new List<Musteri>() ;
        }
        //Getter and Setter methods: 
        public String getDurakAdı()
        {
            return DurakAdı;
        }

        public void setDurakAdı(String DurakAdı)
        {
            this.DurakAdı = DurakAdı;
        }

        public int getBosPark()
        {
            return BosPark;
        }
        public void setBosPark(int BosPark)
        {
            this.BosPark = BosPark;
        }
        public int getTandemBisiklet()
        {
            return TandemBisiklet;
        }
        public void setTandemBisiklet(int TandemBisiklet)
        {
            this.TandemBisiklet = TandemBisiklet;
        }
        public int getNormalBisiklet()
        {
            return NormalBisiklet;
        }

        public void setNormalBisiklet(int NormalBisiklet)
        {
            this.NormalBisiklet = NormalBisiklet;
        }
        public string getMusteri() //gets every element of array musteri.
        {
            string s = "";
            foreach (var m in musteri)
               s += m.ToString();
            return s;
        }        
        public string ToStringHeap()
        {
            return "Durak Adı: " + DurakAdı + "\tBoş Park Sayısı: " + BosPark + "\tTandem Bisiklet Sayısı: " + TandemBisiklet + "\tNormal Bisiklet Sayısı: " + NormalBisiklet;
        }
        public override string ToString()
        {
            return "Durak Adı: " + DurakAdı + "\tBoş Park Sayısı: " + BosPark + "\tTandem Bisiklet Sayısı: " + TandemBisiklet + "\tNormal Bisiklet Sayısı: " + NormalBisiklet + "\n" + getMusteri();
        }

    }
}
