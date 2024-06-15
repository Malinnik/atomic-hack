import logging
import os

from aiohttp import web
from aiohttp_pydantic import PydanticView
import cv2

from common.neuro import process_image


PATH = 'output/'

class GetFile(PydanticView):

    async def post(self):
        data = await self.request.post()
        logging.info(f"{data=}")

        image = data['image']
        filename= image.filename

        image_file = data['image'].file

        content = image_file.read()

        with open(filename, 'wb') as file:
            file.write(content)

        raise web.HTTPFound("/")


class GetFile2(PydanticView):

    async def post(self):
        reader = await self.request.multipart()


        # Get File Content
        field = await reader.next()
        logging.debug(f"{field=}")
        filename = field.filename

        # Save File
        size = 0
        with open(PATH+filename, 'wb') as f:
            while True:
                chunk = await field.read_chunk()  # 8192 bytes by default.
                if not chunk:
                    break
                size += len(chunk)
                f.write(chunk)


        # File Processing
        img = cv2.imread(PATH+filename)
        logging.debug(f"{img=}")
        

        img = await process_image(img, '1.txt')
        
        cv2.imwrite(PATH+filename,  img)

        return web.FileResponse(PATH+filename)

        # response = web.StreamResponse()
        # response.headers['Content-Disposition'] = f'attachment; filename="{filename}"'

        raise web.HTTPFound("/")
        return web.Response(text='{} sized of {} successfully stored'
                             ''.format(filename, size))