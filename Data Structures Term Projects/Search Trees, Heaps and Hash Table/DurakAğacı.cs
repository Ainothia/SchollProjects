using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proje3
{
    class TreeNode
    {
        public Durak data;
        public TreeNode leftChild;
        public TreeNode rightChild;

        public void displayNode()
        {
            Console.WriteLine(data);
        }
        public int Height()
        {
            //return 1 when leaf node is found
            if (this.leftChild== null && this.rightChild == null)
            {
                return 1; //found a leaf node
            }

            int left = 0;
            int right = 0;

            //recursively go through each branch
            if (this.leftChild != null)
                left = this.leftChild.Height();
            if (this.rightChild != null)
                right = this.rightChild.Height();

            //return the greater height of the branch
            if (left > right)
            {
                return (left + 1);
            }
            else
            {
                return (right + 1);
            }
        }
    }
    class DurakAğacı
    {
        private TreeNode root;
        public DurakAğacı()
        {
            root = null;
        }

        public TreeNode getRoot()
        {
            return root;
        }
        public void inOrder(TreeNode localRoot) //prints tree inOrder.
        {
            if (localRoot != null)
            {
                inOrder(localRoot.leftChild);
                localRoot.displayNode();
                inOrder(localRoot.rightChild);
            }
        }
        string s = "";
        public string IDSearch(TreeNode localRoot,int ID) //return Kiralanılan Durak and Kiralama Saati of given ID.
        {
            if (localRoot == null)
                return "Tree is Empty";
            else {
                IDSearch(localRoot.leftChild, ID);
                for (int i = 0; i < localRoot.data.musteri.Count; i++) {
                    if (localRoot.data.musteri[i].getMusteriID() == ID)
                    {
                        s +="Kiralanılan Durak: " + localRoot.data.getDurakAdı() + "\tKiralanılan Saat: " + localRoot.data.musteri[i].getKiralamaSaati() + "\n";
                    }
                }
                IDSearch(localRoot.rightChild, ID);
            }
            if (s.Equals(""))
                return "Müşteri Bisiklet Kiralamamış.";
            Console.WriteLine(s);
            s = "";
            return s;
        }

        public int musteriSayısı = 0;
        public int toplamMusteri = 0;
        Random random = new Random();

        public void MusteriEkle(TreeNode newNode)//inserts new Musteri into the musteri list.
        {           
            musteriSayısı = random.Next(1, 11);
            toplamMusteri += musteriSayısı;
            for (int i = 0; i < musteriSayısı; i++)//adds random number of musteri into list.
            {
                int ID = random.Next(1, 21);//creates random ID.
                string saat = random.Next(0, 24) + ":" + random.Next(0, 60);//creates random time.
                newNode.data.musteri.Add(new Musteri(ID, saat));
            }
        }
        public int Height()//gives the height of tree.
        {
            //if root is null then height is zero
            if (root == null)
            { return 0; }

            return root.Height();
        }
        public void Rent(TreeNode localRoot,string DurakAdı,string ID) //Rents NormalBisiklet from given DurakAdı for given ID.
        {
            if (localRoot == null)
            {
                return;
            }
            Rent(localRoot.leftChild, DurakAdı, ID);//calls left child recursively
            if (localRoot.data.getDurakAdı().Equals(DurakAdı,StringComparison.OrdinalIgnoreCase))//check if given DurakAdı exist in the array.
            {
                if (localRoot.data.getNormalBisiklet() == 0)//check if there is any NormalBisiklet.
                {
                    Console.WriteLine("Durakta Normal Bisiklet Mevcut Değildir.");
                    return;
                }
                localRoot.data.setNormalBisiklet(localRoot.data.getNormalBisiklet() - 1);//Rents a NormalBisiklet for given ID and increase the number of BosPark.
                string saat = random.Next(0, 24) + ":" + random.Next(0, 60);
                localRoot.data.musteri.Add(new Musteri(Convert.ToInt32(ID), saat));
                localRoot.data.setBosPark(localRoot.data.getBosPark()+1);
                localRoot.data.setNormalBisiklet(localRoot.data.getNormalBisiklet() - 1);
            }
            Rent(localRoot.rightChild, DurakAdı, ID);//calls right child recursively
        }
        public void insert(Durak newdata)//insert a new Durak into tree
        {
            TreeNode newNode = new TreeNode();
            if (newdata.getBosPark() <= newdata.getNormalBisiklet() + newdata.getTandemBisiklet())//if BosPark is lower than sum of NormalBisiklet and TandemBisiklet then increase BosPark by length of musteri
                newdata.setBosPark(newdata.getBosPark() + musteriSayısı);
            else // in the other case set BosPark to sum of NormalBisiklet and TandemBisiklet
                newdata.setBosPark(newdata.getNormalBisiklet() + newdata.getTandemBisiklet());
            for (int i = 0; i < musteriSayısı; i++)
            {
                if (newdata.getNormalBisiklet() != 0)
                    newdata.setNormalBisiklet(newdata.getNormalBisiklet() - 1);
                else
                    if (newdata.getTandemBisiklet() == 0)
                {
                    Console.WriteLine(newdata.getDurakAdı() + " Durağında Bisiklet kalmadı.");
                    break;
                }
                else
                    newdata.setTandemBisiklet(newdata.getTandemBisiklet() - 1);
            }
            newNode.data = newdata;
            MusteriEkle(newNode);
            if (root == null)
            {
                root = newNode;
            }
            else//insert element into in rules of binary search tree structure.
            {
                TreeNode current = root;
                TreeNode parent;
                while (true)
                {
                    parent = current;
                    if (string.Compare(newdata.getDurakAdı(), current.data.getDurakAdı()) == -1)
                    {
                        current = current.leftChild;
                        if (current == null)
                        {
                            parent.leftChild = newNode;
                            return;
                        }
                    }
                    else
                    {
                        current = current.rightChild;
                        if (current == null)
                        {
                            parent.rightChild = newNode;
                            return;
                        }
                    }
                }
            }// end else not root
        }// end insert()
    }
}