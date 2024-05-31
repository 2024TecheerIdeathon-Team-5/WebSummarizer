import Header from "./components/HeaderComponent";
import { Route, Routes } from "react-router-dom";
import MainPage from "./pages/MainPage";

function App() {
  return (
    <div>
      <Header />
      <Routes>
        <Route path="/Main" element={<MainPage />} />
      </Routes>
    </div>
  );
}

export default App;
