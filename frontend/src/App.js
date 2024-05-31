import Header from "./components/HeaderComponent";
import { Route, Routes } from "react-router-dom";
import MainPage from "./pages/MainPage";
import FolderPage from "./pages/FolderPage";
import axios from "axios";

function App() {
  axios.defaults.withCredentials = true;
  axios.defaults.headers.common["Access-Control-Allow-Origin"] = "*";
  return (
    <div>
      <Header />
      <Routes>
        <Route path="/Main" element={<MainPage />} />
        <Route path="/Folder" element={<FolderPage />} />
      </Routes>
    </div>
  );
}

export default App;
