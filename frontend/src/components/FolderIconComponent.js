import React from "react";

const FolderIconComponent = ({ imageUrl }) => {
  return (
    <div
      className="relative w-[83px] h-[83px] rounded-[11px] bg-cover bg-center"
      style={{ backgroundImage: `url(${imageUrl})` }}
    ></div>
  );
};

export default FolderIconComponent;
