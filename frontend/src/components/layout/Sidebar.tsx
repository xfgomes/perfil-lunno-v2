import { Home, BarChart3, Users, FileText, Settings } from "lucide-react";
import { NavLink } from "react-router-dom";

const linkBase = "flex items-center gap-2 px-3 py-2 rounded-md text-sm text-slate-600 hover:bg-slate-100";
const linkActive = "bg-slate-100 text-slate-900";

export default function Sidebar(){
  return (
    <aside className="hidden md:block w-60 border-r border-slate-200 bg-white/60">
      <div className="p-3 grid gap-1">
        <NavLink to="/dashboard" className={({isActive})=>`${linkBase} ${isActive?linkActive:""}`}>
          <Home size={18}/> Dashboard
        </NavLink>
        <NavLink to="/relatorio" className={({isActive})=>`${linkBase} ${isActive?linkActive:""}`}>
          <FileText size={18}/> Relatórios
        </NavLink>
        <a className={linkBase} href="#"><BarChart3 size={18}/> Análises</a>
        <a className={linkBase} href="#"><Users size={18}/> Equipes</a>
        <a className={linkBase} href="#"><Settings size={18}/> Configurações</a>
      </div>
    </aside>
  )
}
