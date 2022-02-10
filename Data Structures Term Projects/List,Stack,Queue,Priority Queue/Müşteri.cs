using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proje2
{
    class Müşteri
    {
        private string MüşteriAdı;
        private int ÜrünSayısı;

        public Müşteri(string MüşteriAdı, int ÜrünSayısı) // constructor
        {
            this.MüşteriAdı = MüşteriAdı;
            this.ÜrünSayısı = ÜrünSayısı;
        }

        public int getÜrünSayısı()
        {
            return ÜrünSayısı;
        }

        public void setÜrünSayısı(int sayı)
        {
            ÜrünSayısı = sayı;
        }

        public string getMüşteriAdı()
        {
            return MüşteriAdı;
        }

        public void setMüşteriAdı(string ad)
        {
            MüşteriAdı = ad;
        }

        public override string ToString()
        {
            return "Müşteri Adı: " + MüşteriAdı + "\tÜrün Sayısı: " + ÜrünSayısı;
        }

        
    }
}
