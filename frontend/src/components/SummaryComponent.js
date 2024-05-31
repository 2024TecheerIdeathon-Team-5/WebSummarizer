import React, { useEffect, useState } from "react";

const SummaryComponent = ({ image, titleText, summaryText, url }) => {
  const [imageUrl, setImageUrl] = useState();
  const [title, setTitle] = useState();
  const [summary, setSummary] = useState();

  const [externalUrl, setExternalUrl] = useState();

  // 해당 페이지로 가는 함수
  const handlebutton = () => {
    window.location.href = externalUrl;
  };

  useEffect(() => {
    setImageUrl(image);
    setTitle(titleText);
    setSummary(summaryText);
    setExternalUrl(url);
  });

  return (
    <div className="flex flex-col justify-between w-[289px] h-[356px] rounded-[27px] bg-white border-2 border-primary m-4 p-2">
      <div className="self-start w-full p-0">
        <img src={imageUrl} alt="Loaded Image" className="w-full h-auto" />
      </div>
      <div className="self-center w-full font-sans p-2 text-[21px] font-bold">
        {title}
      </div>
      <div className="self-center w-full font-sans p-2 text-[16px]">
        {summary}
      </div>
      <div className="self-end pr-3">
        <button onClick={handlebutton}>more-{">"}</button>
      </div>
    </div>
  );
};

export default SummaryComponent;
