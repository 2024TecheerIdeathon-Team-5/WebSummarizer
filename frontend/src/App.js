import Header from "./components/HeaderComponent";
import { Route, Routes } from "react-router-dom";
import MainPage from "./pages/MainPage";
import FolderPage from "./pages/FolderPage";

function App() {
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
