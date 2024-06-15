import logging
import os

from aiohttp import web
from aiohttp_pydantic import PydanticView
import cv2

from common.neuro import predict_image


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
        app = self.request.app

        reader = await self.request.multipart()
        logging.debug(f"{reader=}")

        # Get File Content
        field = await reader.next()
        logging.debug(f"{field=}")
        filename = field.filename
        logging.debug(f"{filename=}")

        # Save File
        size = 0
        with open(PATH+filename, 'wb') as f:
            while True:
                chunk = await field.read_chunk()  # 8192 bytes by default.
                if not chunk:
                    break
                size += len(chunk)
                f.write(chunk)

        use_label = await reader.next()
        use_label = await use_label.json()
        logging.debug(f"{use_label=}")


        show_conf = await reader.next()
        show_conf = await show_conf.json()
        logging.debug(f"{show_conf=}")

        # use_labels = await self.request.post()
        # use_labels = use_labels.get('use_labels', False)


        # File Processing
        img = cv2.imread(PATH+filename)
        # logging.debug(f"{img=}")
        

        img = await predict_image(img, conf=0.25, use_label=use_label, show_conf=show_conf, model=app['model'])
        
        cv2.imwrite(PATH+filename, img)

        return web.FileResponse(PATH+filename)

        # response = web.StreamResponse()
        # response.headers['Content-Disposition'] = f'attachment; filename="{filename}"'