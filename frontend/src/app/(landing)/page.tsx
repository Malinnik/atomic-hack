'use client';
import { ChangeEvent, useState } from "react";

export default function Home() {

  const [selectedImage, setSelectedImage] = useState<Blob>(new Blob());
  const [isImageSelected, setIsImageSelected] = useState<boolean>(false);
  const [useLabel, setUseLabel] = useState<boolean>(false);
  const [showConf, setShowConf]  = useState<boolean>(false);
  
  const [sended, setSended] = useState<boolean>(false);
  


  const imageChange = (e: ChangeEvent<HTMLInputElement>) => {

    if (e.target.files && e.target.files.length > 0) {
      setSelectedImage(e.target.files[0]);
      setIsImageSelected(true);
    }
  };

  const removeSelectedImage = () => {
    setSelectedImage(new Blob());
    setIsImageSelected(false);

    const element = document.getElementById('get_image_input');
    
    element?.focus();
    element?.classList.remove("clear-input--touched")
    


  };

  const handleUseLabelChange = (e: ChangeEvent<HTMLInputElement>) => {
    setUseLabel(e.target.checked);
  };

  const handleShowConfChange = (e: ChangeEvent<HTMLInputElement>) => {
    setShowConf(e.target.checked);
  };


  const handleSubmit = () => {

    if (!isImageSelected)
      return

    setSended(true);

    let formData = new FormData();

    formData.append('image', selectedImage);
    formData.append('use_label', useLabel.toString());
    formData.append('shof_conf', showConf.toString());

    const result = fetch('/api/v2/test', {
      method: 'POST',
      // headers: {
      //   'Content-Type': 'multipart/form-data',
      // },
      body: formData,
    });

    result.then((response) => response.blob()).then((blob) => {
      setSelectedImage(blob)
      setSended(false);
    });

  };

  return (
    <div className="grid place-items-center h-screen ">
      
      <div className="w-96 rounded overflow-hidden shadow-lg">
        
        <div>
          {!isImageSelected &&
            <input className="block w-full text-sm text-gray-500
            file:me-4 file:py-2 file:px-4
            file:rounded-lg
            file:text-sm file:font-semibold
            hover:file:bg-blue-500 hover:file:text-white
            file:disabled:opacity-50 file:disabled:pointer-events-none
            file:border file:border-blue-500 hover:border-transparent rounded
            file:text-blue-700 file:bg-white" 
            id="get_image_input" type="file" name="image" accept="image/*" onChange={imageChange} />
          }
          {isImageSelected && (
            <>
              <img className="object-cover" src={URL.createObjectURL(selectedImage)} alt="Thumb"  />
            </>
          )}
        </div>

        <div className="mt-4 flex justify-around">
          { !sended && <button onClick={removeSelectedImage} className="inline-block bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded">Сбросить</button>}
          { !sended && <button onClick={handleSubmit} className="inline-block bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded">Проверить</button>}


          { sended && <button disabled onClick={removeSelectedImage} className="inline-block bg-slate-400  text-white font-semibold  py-2 px-4 border   rounded">Сбросить</button>}
          { sended && <button disabled onClick={handleSubmit} className="inline-block bg-slate-400  text-white font-semibold  py-2 px-4 border   rounded">Ожидайте</button>}
        </div>
        
        <div className="">
          <input onChange={handleUseLabelChange} type="checkbox" name="test" id="" /> <label htmlFor="">Отображать название ошибок</label>
          <br />
          <input onChange={handleShowConfChange} type="checkbox" name="test" id="" /> <label htmlFor="">Отображать процент уверенности</label>
          <br /> 
          <label htmlFor="">Вероятность</label><input type="number" min="1" max="100"/>
        </div>
          

      </div>
    </div>
  );
}
