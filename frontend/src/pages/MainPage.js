import React, { useState } from "react";
import addButton from "../assets/images/addButton.svg";
import FolderComponent from "../components/FolderComponent.js";
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

function MainPage() {
  const [folders, setFolders] = useState([]);

  const handleAddButtonClick = () => {
    const newFolders = [...folders, <FolderComponent key={folders.length} />];
    setFolders(newFolders);
  };

  // react-slick 설정
  const sliderSettings = {
    dots: true,
    infinite: false,
    speed: 500,
    slidesToShow: 3, // 보여질 슬라이드 개수
    slidesToScroll: 1,
  };

  return (
    <div className="flex flex-row p-20 items-center gap-12">
      <div className="gap-4">
        <button onClick={handleAddButtonClick}>
          <img src={addButton} alt="폴더 추가" />
        </button>
      </div>
      <div className="flex felx-row gap-4">
        <Slider {...sliderSettings}>
          {folders.map((folder, index) => (
            <div key={index}>{folder}</div>
          ))}
        </Slider>
      </div>
    </div>
  );
}

export default MainPage;
