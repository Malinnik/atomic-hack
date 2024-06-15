'use client';
import { ChangeEvent, useState } from "react";

export default function Home() {

  const [selectedImage, setSelectedImage] = useState<Blob | null>(null);
  const [useLabel, setUseLabel] = useState<boolean>(false);
  const [showConf, setShowConf]  = useState<boolean>(false);
  
  const [sended, setSended] = useState<boolean>(false);
  
  const [showSidebar, setShowSidebar] = useState<boolean>(false);


  const imageChange = (e: ChangeEvent<HTMLInputElement>) => {

    if (e.target.files && e.target.files.length > 0) {
      setSelectedImage(e.target.files[0]);
    }
  };

  const removeSelectedImage = () => {
    setSelectedImage(null);

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

    if (!selectedImage)
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

  const toggleSidebar = () => {
    setShowSidebar(!showSidebar);
  };

  return (
    <div className="grid place-items-center h-screen ">
      
      <div className="w-96 rounded overflow-hidden shadow-lg">
        
        <div>
          {!selectedImage &&
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
          {selectedImage && (
            <>
              <img className="object-cover" src={URL.createObjectURL(selectedImage)} alt="Thumb"  />
            </>
          )}
        </div>

        <div className="mt-4 flex justify-around">
          { !sended && <button onClick={removeSelectedImage} className="inline-block bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded">Сбросить</button>}
          { !sended && <button onClick={handleSubmit} className="inline-block bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded">Проверить</button>}


          { sended && <button disabled onClick={removeSelectedImage} className="inline-block bg-transparent bg-slate-400  text-white font-semibold  py-2 px-4 border   rounded">Сбросить</button>}
          { sended && <button disabled onClick={handleSubmit} className="inline-block bg-transparent bg-slate-400  text-white font-semibold  py-2 px-4 border   rounded">Ожидайте</button>}
        </div>
        
        <div className=" mr-2"> 
          <input onChange={handleUseLabelChange} type="checkbox" name="test" id="" /> <label htmlFor="">Отображать название ошибок</label>
          <br />
          <input onChange={handleShowConfChange} type="checkbox" name="test" id="" /> <label htmlFor="">Отображать процент уверенности</label>
          <br /> 
          <label htmlFor=" " className="border-solid">Вероятность </label><input type="number" min="1" max="100"/>
        </div>
        
        <button onClick={toggleSidebar} className="fixed top-4 left-4 inline-block bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded">Меню</button>

        <div className={`fixed top-0 left-0 h-full sm:w-96 w-screen bg-gray-200 border-2 border-gray-500 text-white transform ${showSidebar ? 'translate-x-0' : '-translate-x-full'} transition-transform duration-300` }>
          <div className="p-4">
            <h2 className="text-xl font-bold mb-4"></h2>
            <button onClick={toggleSidebar} className="absolute top-4 right-4 inline-block bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded">Закрыть</button>
            <div className= "mt-4 text-black overflow-y-auto">
              <div> 
                <p className= "font-bold text-black text-xl text-center">Легенда</p>
                <div> 
                  <h3 className= "text-black my-5">  
                    <p className= " text-blue-500 font-bold">
                      СИНИЙ 
                    </p>  - прилегающие дефекты
                    <p className= "text-red-600 font-bold">
                      КРАСНЫЙ 
                    </p>  - дефекты целостности
                    <p className= " text-green-600 font-bold">
                      ЗЕЛЕНЫЙ 
                    </p>  - дефекты геометрии
                    <p className= " text-violet-600 font-bold">
                      ФИОЛЕТОВЫЙ 
                    </p>  - дефекты постобработки
                    <p className= " text-yellow-500 font-bold">
                      ЖЕЛТЫЙ 
                    </p>  - дефекты невыполнения                    
                  </h3> 
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}