from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
    
# url = "https://books.goalkicker.com"
# link download https://books.goalkicker.com/XamarinFormsBook/XamarinFormsNotesForProfessionals.pdf

class Write:
    def __init__(self,target,gambar):
        self.title = target
        if target == "TypeScriptBook":
            self.title = "TypeScriptBook2"
        self.gambar = gambar
        self.url = "https://books.goalkicker.com/"
        try:
            self.file = open(f"freeBook/{self.title}.html","a")
        except:
            pass
        print(f"freeBook/{self.title}.html")
    def ParsingHtml(self,url):
        url = f"https://books.goalkicker.com/{url}"
        soup = BeautifulSoup(urlopen(Request(url, headers={"User-Agent":"Mozilla/5.0"}), timeout=10), "lxml")
        return soup
    def Start(self):
        self.WriteHead()
        self.WriteNav()
        self.WriteContent()
        self.WriteFooter()
        self.WriteTutup()
    def WriteHead(self):
        html = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.title}</title>
    <link rel="stylesheet" href="../style.css">
</head>
<body>    
        '''
        self.file.write(html)
    def WriteTutup(self):
        html = """
</body>
</html>
        """
        self.file.write(html)
    def WriteNav(self):
        html = '''
<aside>
        <h1>COCONUT</h1>
        <sup>Big Coriocity!</sup>
    </aside>
    <nav>
        <ul>
            <li>
                <a href="../index.html">
                    <h4>Beranda</h4>
                </a>
            </li>
            <li class="activ">
                <a href="../perpustakaan.html" class="activ">
                    <h4>Perpustakaan</h4>
                </a>
            </li>
            <li>
                <a href="../about.html">
                    <h4>Tentang</h4>
                </a>
            </li>
        </ul>
    </nav>
    <session>
        '''
        self.file.write(html)
    def WriteContent(self):
        link = self.ParsingHtml(self.title).find_all("button")[1].get_attribute_list('onclick')[0]
        ind = link.index("=")
        link = link[ind+1:].replace("'","")
        html = f'''
    <div class="boximg desk">
        <table class="descr">
            <tr>
                <td>
                        <img src="{self.gambar}" alt="" class="tampil">
                        <br>
                        <a href="{self.url}/{self.title}/{link}"><h3>Download <br>{self.title}<h3></a>
                        <br>
        '''
        self.file.write(html)
        data = self.ParsingHtml(self.title).find_all("li")
        for i in range(len(data)):
            html2 = f'''
                <p class="bab">Bab {i+1}:{data[i].get_text()}</p>
            '''
            self.file.write(html2)
        html = '''
                </td>
            </tr>
        </table>
    </div>
        '''
        self.file.write(html)
    def WriteFooter(self):
        html = """
        <footer>
            <aside>
                <h1 onclick="putar()">COCONUT</h1>
                <sup>Big Coriocity!</sup>
            </aside>
            <div class="contentFooter">

                <h3 id="jl">Rekomendasi:</h3>
                <ul class="rekomendasi">
                    <li><a href="freeBook/AlgorithmsBook.html">AlgorithmsBook</a></li>
                    <li><a href="freeBook/GitBook.html">GitBook</a></li>
                    <li><a href="freeBook/LinuxBook.html">LinuxBook</a></li>
                    <li><a href="freeBook/PythonBook.html">PythonBook</a></li>
                </ul>
                <h4 id="jl" class="made"><u>Made By @Uky Coconut 012</u></h4>
            </div>
        </footer>
    </section>
        """
        self.file.write(html)

#Write(target,gambar).Start()



class BuatHtml:
    def __init__(self,url):
        self.url = url
        try:
            self.file = open("test.html","a")
            print("File Ready To Write")
        except:
            print("File Error!")
        self.data = self.ParsingHtml(self.url).find_all("img")
    def ParsingHtml(self,url):
        print("Start get :",self.url)
        soup = BeautifulSoup(urlopen(Request(url, headers={"User-Agent":"Mozilla/5.0"}), timeout=10), "lxml")
        print("Get :",self.url)
        return soup
    def GetUrlImg(self):
        data = []
        data2 = []
        hitung = 0
        print("Mulai Menampung Hasil  :",self.url)
        for isi in self.data:
            if hitung == 0 or hitung == len(self.data)-1:
                hitung += 1
                continue
            else:
                hitung += 1
                data2.append(isi.get_attribute_list('src')[0])
                data.append(f"{self.url}/{isi.get_attribute_list('src')[0]}")
        print("Selesai Menampung :",self.url)
        return data2, data
    def templateTd(self,data):
        print("Mulai Menulis")
        ind = data[0].index('/')
        Write(data[0][0:ind],data[1]).Start()
        print(f"Create Html: {data[0][0:ind]}.html")
        file = open(f"freeBook/{data[0][0:ind]}.html","a")
        tagg = f'''
        <td>
            <div class="boximg">
                <a href="freeBook/{data[0][0:ind]}.html">
                    <img src="{data[1]}" alt="{data[0][0:ind]}"></a>
                    <br>
                    <a href="freeBook/{data[0][0:ind]}.html">
                    <h3 class="tombol">{data[0][0:ind].replace("_"," ")}</h3>
                </a>
            </div>
        </td>
        '''
        print("Selesai Menulis")
        return tagg
    def tulis(self):
        data1, data2 = self.GetUrlImg()
        for i in range(len(data1)):
            self.file.write(self.templateTd([data1[i],data2[i]]))
    
    
BuatHtml("https://books.goalkicker.com").tulis()