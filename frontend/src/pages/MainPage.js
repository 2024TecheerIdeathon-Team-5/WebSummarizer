import React, { useState, useEffect } from "react";
import axios from "axios";
import addButton from "../assets/images/addButton.svg";
import FolderComponent from "../components/FolderComponent.js";
import SummaryComponent from "../components/SummaryComponent.js";

function MainPage() {
  const [folders, setFolders] = useState([]);
  const [articles, setArticles] = useState([]);

  axios.defaults.baseURL = "http://localhost:5002";

  const getArticles = async () => {
    axios
      .get("/articles")
      .then((response) => {
        setArticles(response.data.articles);
      })
      .catch((error) => {
        console.error("There was an error!", error);
      });
  };

  useEffect(() => {
    getArticles();
  }, []);

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
        <div className="flex flex-row gap-4">
          {folders.map((folder) => folder)}
        </div>
      </div>

      <p className="pl-20 pt-10 pb-5 font-sans text-[16px]">분류 없음</p>
      <div className="flex flex-row ml-10">
        {articles.map((article, index) => (
          <SummaryComponent
            key={index}
            imageUrl={article.image_url}
            title={article.title}
            summary={article.summary}
            url={article.url}
          />
        ))}
      </div>
    </div>
  );
}

export default MainPage;
