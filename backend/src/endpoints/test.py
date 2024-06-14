import logging

from aiohttp import web
from aiohttp_pydantic import PydanticView


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

        # reader.next() will `yield` the fields of your form

        field = await reader.next()
        logging.debug(f"{field=}")
        filename = field.filename
        # You cannot rely on Content-Length if transfer is chunked.
        size = 0
        with open(filename, 'wb') as f:
            while True:
                chunk = await field.read_chunk()  # 8192 bytes by default.
                if not chunk:
                    break
                size += len(chunk)
                f.write(chunk)

        raise web.HTTPFound("/login")
        return web.Response(text='{} sized of {} successfully stored'
                             ''.format(filename, size))