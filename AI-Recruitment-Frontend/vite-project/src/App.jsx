import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";

import MainLayout from "./layouts/MainLayout";

import Dashboard from "./pages/Dashboard";
import ResumeScreening from "./pages/ResumeScreening";

import Interview from "./pages/Interview";
import Reports from "./pages/Reports";
import Settings from "./pages/Settings";

function App() {

  return (

    <BrowserRouter>

      <MainLayout>

        <Routes>

          <Route
            path="/"
            element={<Dashboard />}
          />

          <Route
            path="/resume"
            element={<ResumeScreening />}
          />

          <Route path="/interview" element={<Interview />} />

          <Route path="/reports" element={<Reports />} />

          <Route path="/settings" element={<Settings />} />

        </Routes>

      </MainLayout>

    </BrowserRouter>

  );
}

export default App;