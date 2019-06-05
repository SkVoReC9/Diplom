import os


def StartConstruct(List_of_blocks):
    #Координаты всех найденных блоков
    SXscr = SYscr = Exscr = EYscr = SXban = SYban = EXban = EYban = SXlow = SYlow = Exlow = EYlow = SXim = SYim = EXim = EYim = SX1ma = SY1ma = EX1ma = EY1ma = 0
    #Переменные для записи в них HTML блоков
    File_Scroll = File_Low_Menu = File_Main_View = File_Image_block = File_Banner = ''
    Path = 'HTMLBlocks\Construct.html'
    #Флаги для проверки больших элементов
    FlagMain = True
    FlagImg = True
    #Запись для каждого блока своих координат и запись из файла HTML кода
    for blocks in List_of_blocks:
        head, name = os.path.split(blocks[4])
        if name == 'Scroll.png':
            SXscr = blocks[0]
            SYscr = blocks[1]
            Exscr = blocks[2]
            EYscr = blocks[3]
            File_Scroll1 = open('HTMLBlocks\Scroll.html','r')
            File_Scroll = File_Scroll1.read()
            File_Scroll1.close()
        elif name == 'Banner.png':
            SXban = blocks[0]
            SYban = blocks[1]
            EXban = blocks[2]
            EYban = blocks[3]
            File_Banner1 = open('HTMLBlocks\Banner.html', 'r')
            File_Banner = File_Banner1.read()
            File_Banner1.close()
        elif name == 'LowerMenu.png':
            SXlow = blocks[0]
            SYlow = blocks[1]
            Exlow = blocks[2]
            EYlow = blocks[3]
            File_Low_Menu1 = open('HTMLBlocks\LowerMenu.html', 'r')
            File_Low_Menu = File_Low_Menu1.read()
            File_Low_Menu1.close()
        elif name == 'ImageBlock.png':
            SXim = blocks[0]
            SYim = blocks[1]
            EXim = blocks[2]
            EYim = blocks[3]
            File_Image_block1 = open('HTMLBlocks\ImageBlock.html', 'r')
            File_Image_block = File_Image_block1.read()
            File_Image_block1.close()
        elif name == '1CMainView.png':
            SX1ma = blocks[0]
            SY1ma = blocks[1]
            EX1ma = blocks[2]
            EY1ma = blocks[3]
            File_Main_View1 = open('HTMLBlocks\MainView.html', 'r')
            File_Main_View = File_Main_View1.read()
            File_Main_View1.close()
    #Проверка на присутствие блоков невошедших в макет
    if(SX1ma > SXim and SY1ma > SYim and EX1ma < EXim and EY1ma < EYim):
        for blocks in List_of_blocks:
            head, name = os.path.split(blocks[4])
            if name == 'ImageBlock.png':
                List_of_blocks.remove(blocks)
            FlagImg = False

    elif(SXim > SX1ma and SYim > SY1ma and EXim < EX1ma and EYim < EX1ma):
        for blocks in List_of_blocks:
            head, name = os.path.split(blocks[4])
            if name == '1CMainView.png':
                List_of_blocks.remove(blocks)
                FlagMain = False

    elif(SY1ma > 300 and EY1ma > 700 and SYim > 300 and EYim > 700):
        for blocks in List_of_blocks:
            head, name = os.path.split(blocks[4])
            if name == '1CMainView.png' or name == 'ImageBlock.png':
                List_of_blocks.remove(blocks)
                FlagImg = False
                FlagMain = False
    #Запись в HTML файл каждый блок HTML
    File_Main = open(Path, 'a+')
    if (FlagMain == True and FlagImg !=True):
        File_Main.write(File_Main_View)
        File_Main.write('\n')
        File_Main.write(File_Low_Menu)
        File_Main.write('\n')
        File_Main.write(File_Banner)
        File_Main.write('\n')
        File_Main.write(File_Scroll)
        File_Main.write('\n')
        File_Main.write('</body>')
        File_Main.write('\n')
        File_Main.write('</html>')
        File_Main.close()
    elif(FlagMain != True and FlagImg == True):
        File_Main.write(File_Image_block)
        File_Main.write('\n')
        File_Main.write(File_Low_Menu)
        File_Main.write('\n')
        File_Main.write(File_Banner)
        File_Main.write('\n')
        File_Main.write(File_Scroll)
        File_Main.write('\n')
        File_Main.write('</body>')
        File_Main.write('\n')
        File_Main.write('</html>')
        File_Main.close()
    elif(FlagMain != True and FlagImg != True):
        File_Main.write(File_Low_Menu)
        File_Main.write('\n')
        File_Main.write(File_Banner)
        File_Main.write('\n')
        File_Main.write(File_Scroll)
        File_Main.write('\n')
        File_Main.write('</body>')
        File_Main.write('\n')
        File_Main.write('</html>')
        File_Main.close()
    return Path


