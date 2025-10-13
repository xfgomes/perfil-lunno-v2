import Card from "@/components/ui/Card";

export default function Report(){
  const sections = [
    { title: "Seu Arquétipo", text: "Criador — orientado à inovação, autonomia e construção de soluções originais." },
    { title: "Estilo de Atuação", text: "Equilíbrio entre colaboração e iniciativa própria. Prefere ambientes com espaço para experimentar." },
    { title: "Forças", text: "Aprendizado rápido, curiosidade, pensamento sistêmico, resiliência." },
    { title: "Pontos de Atenção", text: "Risco de dispersão; atenção à priorização e rotinas de acompanhamento." },
    { title: "Plano Acionável", text: "1) Sprint de experimentos quinzenal 2) Revisões semanais 3) Parcerias com perfis de execução forte." }
  ];

  return (
    <div className="grid gap-4">
      <h1 className="text-3xl font-semibold">Relatório Individual</h1>
      <Card>
        <div className="prose max-w-none">
          {sections.map((s,i)=>(
            <section key={i} className="mb-4">
              <h2 className="text-xl font-semibold mb-1">{s.title}</h2>
              <p className="text-slate-700">{s.text}</p>
            </section>
          ))}
        </div>
      </Card>
    </div>
  )
}
