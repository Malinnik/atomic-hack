'use client';
import { ChangeEvent, useState } from "react";

export default function Home() {

  const [selectedImage, setSelectedImage] = useState<Blob | null>(null);

  const imageChange = (e: ChangeEvent<HTMLInputElement>) => {

    // const file = e.target.files?.[0]
  
    // if (file) {
    //   const reader = new FileReader();
    //   reader.onload = () => {
    //     setSelectedImage(reader.result as string)
    //   }
    //   reader.readAsDataURL(file);
    // }

    if (e.target.files && e.target.files.length > 0) {
      setSelectedImage(e.target.files[0]);
    }
  };

  const removeSelectedImage = () => {
    setSelectedImage(null);
  };


  const handleSubmit = () => {

    let formData = new FormData();
    formData.append('image', selectedImage);

    const result = fetch('/api/v2/test', {
      method: 'POST',
      // headers: {
      //   'Content-Type': 'multipart/form-data',
      // },
      body: formData,
    });

    result.then((response) => response.blob()).then((blob) => setSelectedImage(blob));
  };

  return (
    <div className="grid place-items-center h-screen ">
      
      <div className="max-w-sm rounded overflow-hidden shadow-lg">
        
        <form action="/api/v2/test" method="post" accept-charset="utf-8" encType="multipart/form-data">
          <input type="file" name="image" accept="image/*" onChange={imageChange} />
          {selectedImage && (
            <>
              <img src={URL.createObjectURL(selectedImage)} alt="Thumb" />
            </>
          )}
          <div className="grid grid-cols-3 content-between">
            <input className="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded" onClick={removeSelectedImage} type="reset" value="Reset" />
            <input className="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded" type="submit" value="Submit" />
          </div>
        </form>
        <button onClick={handleSubmit} className="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded">Проверка</button>
      </div>
    </div>
  );
}
