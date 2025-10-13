export default function Relatorio(){
  const texto = `Exemplo de relatório narrativo gerado por IA...`;
  return (
    <div className="max-w-3xl mx-auto">
      <h2 className="text-2xl font-semibold mb-4">Relatório Individual</h2>
      <article className="card">
        {texto.split("\n\n").map((p,i)=>(<p key={i} className="mb-3">{p}</p>))}
      </article>
    </div>
  )
}
