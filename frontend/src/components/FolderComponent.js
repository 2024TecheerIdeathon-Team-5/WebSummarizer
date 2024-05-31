import React, { useState } from "react";
import deleteButton from "../assets/images/deleteButton.svg";

const FolderComponent = ({ onDelete }) => {
  const [folderName, setFolderName] = useState("");
  const [isEditing, setIsEditing] = useState(true); // 입력 중인지 여부를 나타내는 상태

  const handleInputChange = (event) => {
    setFolderName(event.target.value);
  };

  const handleInputBlur = () => {
    setIsEditing(false);
  };

  const handleInputKeyDown = (event) => {
    if (event.key === "Enter") {
      setIsEditing(false);
    }
  };

  return (
    <div className="flex flex-col">
      <div className="relative w-[289px] h-[156px] rounded-[27px] bg-primary">
        <button
          onClick={onDelete}
          className="absolute top-1 right-2 w-8 h-8 flex items-center justify-center"
        >
          <img src={deleteButton} alt="폴더 삭제" />
        </button>
      </div>
      {isEditing && (
        <input
          type="text"
          className="w-full p-2 bg-transparent border-none outline-none text-center font-sans text-[16px]"
          placeholder="폴더명 입력"
          value={folderName}
          onChange={handleInputChange}
          onBlur={handleInputBlur}
          onKeyDown={handleInputKeyDown}
        />
      )}
      {!isEditing && (
        <div className="mt-2 text-center font-sans text-[16px]">
          {folderName}
        </div>
      )}
    </div>
  );
};

export default FolderComponent;
