from datetime import datetime
import re, os, random, string, shutil


import unittest

def deleting(path, regular,num_thread):
    print "s"


def randstring(path):
    a = string.ascii_letters + string.digits
    name=[random.choice(a) for i in range(5)]
    file_name=""
    for i in name:
        file_name += str(i)
    file_name=file_name+".txt"
    file=open(path+file_name,"w")
    file.close

class tests(unittest.TestCase):
    def setUp(self):
        self.path='/media/70CCDC1FCCDBDE02/temp'
        self.path2='/media/70CCDC1FCCDBDE02/temp2'
        self.path3='/media/70CCDC1FCCDBDE02/temp3'
        self.path4='/media/70CCDC1FCCDBDE02/temp4'
        os.mkdir(self.path,0755)
        shutil.copytree(self.path, self.path2)
        shutil.copytree(self.path, self.path3)
        shutil.copytree(self.path, self.path4)
        for i in range(1000):
            randstring(self.path)
        self.regular=("[A-Z][a-z].*", "[a-z][a-z].*", "[A-Z][A-Z].*", "\d[A-Z].*", "\d[a-z].*","[A-Z]\d.*","[a-z]\d.*")
        self.num_thread=3
        self.num_thread2=10

    def test_kolfile(self):
        for i in range(5):
            deleting(self.path,self.regular[i],self.num_thread)
            print self.regular[0]
            pattern = re.compile(self.regular[i])
            kol_full=0
            kol_match=0
            kol=0
            for names in os.listdir(self.path2):
                if pattern.match(names):
                    kol_match=kol_match+1
                kol_full=kol_full+1
            for names in os.listdir(self.path):
                kol=kol+1
            self.assertEqual(kol, kol_full=kol_match)
            deleting(self.path2,self.regular[i],self.num_thread)

    def test_del(self):
        pattern = re.compile(self.regular[6])
        kol_match=0
        for names in os.listdir(self.path):
            if pattern.match(names):
                kol_match=kol_match+1
        self.assertIs(kol_match,0)

    def test_time(self):
        t = time.time()
        deleting(self.path3,self.regular[5],self.num_thread)
        time1=time.time()-t
        t = time.time()
        deleting(self.path4,self.regular[5],self.num_thread2)
        time2=time.time()-t
        self.assertTrue(time2<time1)

unittest.main()

