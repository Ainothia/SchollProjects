using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proje2
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.BackgroundColor = ConsoleColor.White;
            Console.Clear();
            Console.ForegroundColor = ConsoleColor.Black;
            string[] MüşteriAdı = { "Ali", "Merve", "Veli", "Gülay", "Okan", "Zekiye","Kemal", "Banu", "İlker", "Songül", "Nuri", "Deniz" };
            int[] ÜrünSayısı = { 8, 11, 16, 5, 15, 14, 19, 3, 18, 17, 13, 15 };

            int lenght = MüşteriAdı.Length;
            int count = 0;
            ArrayList arrayList = new ArrayList();
            int start = 0;
            Random random = new Random();
            while (true)
            {
                int sayı = random.Next(1,5);
                count += sayı; //keeps added musteri number
                List<Müşteri> genlist = new List<Müşteri>();
                for(int i = start; i<count; i++)//adds musteri to the list as many as random number
                {
                    if (i >= lenght) // if i exceeds the number of musteri, loop stops
                        break;
                    genlist.Add(new Müşteri(MüşteriAdı[i], ÜrünSayısı[i]));
                }
                if (genlist.Count == 0) //if generic list is empty, loop stops
                    break;
                start = count;
                arrayList.Add(genlist);
                if (count >= lenght)
                    break;
            }
            int listcount = 1;
            foreach(List<Müşteri> l in arrayList) // prints list
            {
                Console.WriteLine("Liste" + listcount + ": ");
                foreach(Müşteri m in l)
                {
                    Console.WriteLine("Müşteri : " + m);
                }
                listcount++;
            }

            double ortalama = (double)lenght / (double)arrayList.Count;
            Console.WriteLine("ArrayList eleman sayısı : " + arrayList.Count);
            Console.WriteLine("Ortalama eleman sayısı : " + ortalama);
            Console.WriteLine("");
            Console.WriteLine("***************************");
            Console.WriteLine("");
            Console.WriteLine("Stack: ");
            
            Stack stack = new Stack(lenght);
            Queue queue = new Queue(lenght);
            ÖncelikliKuyruk despq = new ÖncelikliKuyruk();
            ÖncelikliKuyruk aspq = new ÖncelikliKuyruk();

            for (int i =  0; i< lenght; i++) // adds object to different kinda structures
            {
                stack.push(new Müşteri(MüşteriAdı[i], ÜrünSayısı[i]));
                despq.insert(new Müşteri(MüşteriAdı[i], ÜrünSayısı[i]));
                queue.insert(new Müşteri(MüşteriAdı[i], ÜrünSayısı[i]));
                aspq.insert(new Müşteri(MüşteriAdı[i], ÜrünSayısı[i]));
            }
            for(int i = 0; i < lenght; i++) // prints stack
                Console.WriteLine(stack.pop());

            Console.WriteLine("");
            Console.WriteLine("***************************");
            Console.WriteLine("");
            Console.WriteLine("Queue: ");

            int islemsüresique = 0;
            for (int i = 0; i < lenght; i++) // prints queue and procces time
            {
                Müşteri dequeue = queue.remove();
                islemsüresique += dequeue.getÜrünSayısı();
                Console.WriteLine(dequeue + "\tİslem süresi: " + islemsüresique);
            }

            Console.WriteLine("");
            Console.WriteLine("***************************");
            Console.WriteLine("");
            Console.WriteLine("Priority Queue Descending: ");
            int islemcount = 0;
            for (int i = 0; i < lenght; i++) // prints descending priority queue and procces time
            {
                Müşteri remove = despq.dpq();
                islemcount += remove.getÜrünSayısı();
                Console.WriteLine(remove + "\tİşlem süresi: " + islemcount);
            }

            Console.WriteLine("");
            Console.WriteLine("***************************");
            Console.WriteLine("");
            Console.WriteLine("Priority Queue Ascending: ");

            int islemcountapq = 0;
            for (int i = 0; i < lenght; i++) // prints ascending priority queue and procces time
            {
                Müşteri removeapq = aspq.apq();
                islemcountapq += removeapq.getÜrünSayısı();
                Console.WriteLine(removeapq + "\tİşlem süresi: " + islemcountapq);
            }

            Console.ReadKey();
        }
    }
}
