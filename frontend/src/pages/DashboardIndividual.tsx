import RadarDISC from "../components/RadarDISC";
import BarraBigFive from "../components/BarraBigFive";
import SoftSkillsScatter from "../components/SoftSkillsScatter";
import CardArquetipo from "../components/CardArquetipo";

export default function DashboardIndividual(){
  const bf = { openness:0.78, conscientiousness:0.64, extraversion:0.51, agreeableness:0.72, neuroticism:0.35 };
  const disc = { dominance:0.7, influence:0.8, steadiness:0.6, conformity:0.5 };
  const skills = { potential:{ Criatividade:0.8, Implementacao:0.6, Comunicacao:0.7, Resiliencia:0.65 }, demonstrated:{ Comunicacao:0.6, ResolucaoProblemas:0.7, Implementacao:0.5 } } as any;
  const arch = { name:"Criador", motivation:"Inovar, expressar, construir soluções", fit:"Autonomia e tolerância ao erro", shadow:"Perfeccionismo" };

  return (
    <div className="grid md:grid-cols-2 gap-6">
      <BarraBigFive bf={bf}/>
      <RadarDISC disc={disc}/>
      <SoftSkillsScatter skills={skills}/>
      <CardArquetipo arch={arch}/>
    </div>
  )
}
