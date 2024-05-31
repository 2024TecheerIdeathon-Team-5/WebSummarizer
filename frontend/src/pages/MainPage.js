import React, { useState } from "react";
import addButton from "../assets/images/addButton.svg";
import FolderComponent from "../components/FolderComponent.js";
import SummaryComponent from "../components/SummaryComponent.js";

function MainPage() {
  const [folders, setFolders] = useState([]);

  const handleAddButtonClick = () => {
    const newFolders = [...folders, <FolderComponent key={folders.length} />];
    setFolders(newFolders);
  };

  return (
    <div>
      <div className="flex flex-row p-20 gap-12">
        <div className="mt-4 gap-4">
          <button onClick={handleAddButtonClick}>
            <img src={addButton} alt="폴더 추가" />
          </button>
        </div>
        <div className="flex felx-row gap-4">
          {folders.map((folder) => folder)}
        </div>
      </div>

      <p className="pl-20 pt-10 pb-5 font-sans text-[16px]">분류 없음</p>
      <div className="ml-10">
        <SummaryComponent />
      </div>
    </div>
  );
}

export default MainPage;
