import React from "react";
import deleteButton from "../assets/images/deleteButton.svg";

const FolderComponent = ({ onDelete }) => {
  return (
    <div className="relative w-[289px] h-[156px] rounded-[27px] bg-primary">
      <button
        onClick={onDelete}
        className="absolute top-1 right-2 w-8 h-8 flex items-center justify-center"
      >
        <img src={deleteButton} alt="폴더 삭제" />
      </button>
    </div>
  );
};

export default FolderComponent;
