using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proje1
{
    class Program1
    {
        
        
        public static System.Double[,] point(double width, double height, int n) //Rastgale Nokta Üretimi
        {
            Random random = new Random();
            double[,] nokta = new double[n, 2];
            for (int i = 0; i < n; i++)
            {
                double x = random.NextDouble() * width; //Verilen yatay boyutta nokta üretimi (x)
                double y = random.NextDouble() * height;//Verilen dikey boyutta nokta üretimi (y)
                nokta[i,0] = Math.Round(x,2);
                nokta[i,1] = Math.Round(y,2);
            }
            return nokta;
        }

        public static double uzaklık(double x1, double y1,double x2,double y2) //Euclidean distance func.
        {
            double uzaklık = Math.Sqrt(Math.Pow((x1 - x2), 2.0) + Math.Pow((y1 - y2), 2.0));//xler farkının karesi + yler farkının karesinin karekökü
            uzaklık = Math.Round(uzaklık, 2);
            return uzaklık;
        }
        public static System.Double[,] DM(double[,] nokta) // Uzaklık matrisinin oluşturulma fonksiyonu
        {
            double[,] dm = new double[nokta.GetLength(0), nokta.GetLength(0)]; //Oluşturulan nokta sayısı boyutunda matris.
            for(int i = 0; i < nokta.GetLength(0); i++)
            {
                for (int j = 0; j < nokta.GetLength(0); j++)
                {
                    double distance = uzaklık(nokta[i, 0], nokta[i, 1], nokta[j, 0], nokta[j, 1]);//Oluşturulan noktaların birbirine uzaklıklarının alınması
                    dm[i, j] = distance;
                }
            }
            return dm;
        }

            static void Main(string[] args)
        {
            int height = 100;
            int width = 100;
            int n = 100;

            double[,] nokta = point(width, height, n);
            double[,] dm = DM(nokta);

            Console.WriteLine("x\ty");

            for(int i = 0; i < nokta.GetLength(0); i++)
            {
                for (int j = 0; j < 2; j++)
                {
                    Console.Write(nokta[i, j]+"\t"); //Oluşturulan noktaların x ve y olarak ekrana bastırılması
                }
                Console.WriteLine();
            }
            Console.WriteLine("\t\t\t\tDistance Matrix");
            for(int  i = 0; i < dm.GetLength(1); i++)
            {
                Console.Write("\t" + i);
            }
            Console.WriteLine();
            for (int i = 0; i < dm.GetLength(0); i++)
            {
                Console.Write(i + "\t");
                for (int j = 0; j < dm.GetLength(1); j++)
                {
                    Console.Write(dm[i, j]+"\t"); // Uzaklık matrisi bastırılır.
                }
                Console.WriteLine();
            }
            Console.ReadKey();
        }
    }
}
