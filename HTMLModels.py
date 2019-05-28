import os


def StartConstruct(List_of_blocks):
    for blocks in List_of_blocks:
        head, name = os.path.split(blocks[4])
        if name == 'Scroll.png':
            As = blocks[0]
            Bs = blocks[1]
            print(As, Bs)
        elif name == 'Banner.png':
            AB = blocks[1]
            BB = blocks[2]
        elif name == 'LowerMenu.png':
            AL = blocks[1]
            BL = blocks[2]
        elif name == 'ImageBlock.png':
            AI = blocks[1]
            BI = blocks[2]
        elif name == '1CMainView.png':
            A1 = blocks[1]
            B1 = blocks[2]
    return
