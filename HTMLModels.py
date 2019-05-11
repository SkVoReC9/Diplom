
def StartConstruct(List_of_blocks):
    for blocks in List_of_blocks:
        if blocks[4] == 'IMG\Scroll.png':
            print('Its scroll')
        elif blocks[4] == 'IMG\Banner.png':
            print('Banner')
        elif blocks[4] == 'IMG\LowerMenu.png':
            print('Lower')
        elif blocks[4] == 'IMG\ImageBlock.png':
            print('ImageBlock')
        elif blocks[4] == 'IMG\MainView.png':
            print('Main')
    return
