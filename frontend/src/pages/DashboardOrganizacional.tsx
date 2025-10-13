export default function DashboardOrganizacional(){
  const data = [
    { team:"Marketing", Abertura:0.81, Amabilidade:0.43, Extroversao:0.62 },
    { team:"Engenharia", Abertura:0.55, Amabilidade:0.61, Extroversao:0.38 },
  ];
  return (
    <div className="grid gap-6">
      <h2 className="text-2xl font-semibold">Panorama Organizacional</h2>
      <div className="card overflow-auto">
        <table className="min-w-full text-sm">
          <thead><tr><th className="p-2 text-left">Equipe</th><th className="p-2">Abertura</th><th className="p-2">Amabilidade</th><th className="p-2">Extroversão</th></tr></thead>
          <tbody>
            {data.map((r,i)=>(
              <tr key={i}>
                <td className="p-2 font-medium">{r.team}</td>
                <td className="p-2">{r.Abertura.toFixed(2)}</td>
                <td className="p-2">{r.Amabilidade.toFixed(2)}</td>
                <td className="p-2">{r.Extroversao.toFixed(2)}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <div className="grid md:grid-cols-3 gap-4">
        <div className="card">💡 Potencial criativo alto em Marketing</div>
        <div className="card">⚠️ Risco de conflito (Amabilidade média baixa)</div>
        <div className="card">🚀 Coesão moderada</div>
      </div>
    </div>
  )
}
