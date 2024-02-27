from detectart_teste import ProcessImg

class ImageHandle:
    def __init__(self, x64: str):
        self.x64 = x64
        self.handleImg =  ProcessImg()

    async def findHoles(self):
        print('detect hole')
        return self.handleImg.process(self.x64)