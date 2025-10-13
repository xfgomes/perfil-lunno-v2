import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Login from "./pages/Login";
import DashboardIndividual from "./pages/DashboardIndividual";
import DashboardOrganizacional from "./pages/DashboardOrganizacional";
import Relatorio from "./pages/Relatorio";

export default function App(){
  return (
    <BrowserRouter>
      <header className="header px-4 py-3 flex gap-6 items-center">
        <div className="font-semibold">Perfil Lunno HUBX</div>
        <nav className="flex gap-4 text-sm">
          <Link to="/individual">Individual</Link>
          <Link to="/organizacional">Organizacional</Link>
          <Link to="/relatorio">Relatório</Link>
        </nav>
      </header>
      <main className="p-6 max-w-6xl mx-auto grid gap-6">
        <Routes>
          <Route path="/" element={<Login/>} />
          <Route path="/individual" element={<DashboardIndividual/>} />
          <Route path="/organizacional" element={<DashboardOrganizacional/>} />
          <Route path="/relatorio" element={<Relatorio/>} />
        </Routes>
      </main>
    </BrowserRouter>
  )
}
