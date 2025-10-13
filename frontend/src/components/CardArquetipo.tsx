export default function CardArquetipo({arch}:{arch:{name:string,motivation:string,fit:string,shadow:string}}){
  return (
    <div className="card">
      <h3 className="text-lg font-semibold">Arquétipo: {arch.name}</h3>
      <p className="mt-2"><b>Motivação:</b> {arch.motivation}</p>
      <p className="mt-1"><b>Ambiente ideal:</b> {arch.fit}</p>
      <p className="mt-1"><b>Sombra:</b> {arch.shadow}</p>
    </div>
  )
}
