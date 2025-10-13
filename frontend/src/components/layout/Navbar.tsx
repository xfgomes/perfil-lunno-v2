import { User, FileText, BrainCircuit } from "lucide-react";

export default function Navbar(){
  return (
    <header className="sticky top-0 z-30 backdrop-blur bg-white/70 border-b border-slate-200">
      <div className="max-w-7xl mx-auto px-4 py-3 flex items-center gap-3">
        <div className="flex items-center gap-2 text-lunno.ink">
          <BrainCircuit size={22} />
          <span className="font-semibold">Perfil Lunno</span>
          <span className="app-badge">Notion-style</span>
        </div>
        <div className="ml-auto flex items-center gap-4">
          <a href="/relatorio" className="text-sm inline-flex items-center gap-2 text-slate-600 hover:text-slate-900">
            <FileText size={18}/> Relatórios
          </a>
          <button className="inline-flex items-center gap-2 text-slate-600">
            <User size={18}/> Você
          </button>
        </div>
      </div>
    </header>
  )
}
