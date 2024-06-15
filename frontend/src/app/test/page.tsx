"use client"

import React, { ChangeEvent, useState } from 'react';
import Image from 'next/image'

interface InputFileProps {
  // You can add any additional props needed
}

export default function InputFile(props: InputFileProps) {
  const [selectedFile, setSelectedFile] = useState<string | null>(null);

  const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];

    if (file) {
      const reader = new FileReader();
      reader.onloadend = () => {
        setSelectedFile(reader.result as string);
      };
      reader.readAsDataURL(file);
    }
  };


  const handleSubmit = () => {

    let formData = new FormData();
    formData.append('image', selectedFile);

    const result = fetch('/api/v2/test', {
      method: 'POST',
      // headers: {
      //   'Content-Type': 'multipart/form-data',
      // },
      body: formData,
    });

    result.then((response) => response.blob()).then((blob) => setSelectedFile(blob));
  };


  return (
    <div className="grid w-full max-w-sm items-center gap-1.5">
      <input type="file" name="image" accept="image/*" onChange={handleFileChange} />
      {selectedFile && (
        <div className="mt-2">
          <Image
            src={selectedFile}
            alt="Preview"
            width={500}
            height={500}
          />
        </div>
      )}
    </div>
  );
}