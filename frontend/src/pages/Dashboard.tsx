import Card from "@/components/ui/Card";
import Button from "@/components/ui/Button";
import Badge from "@/components/ui/Badge";
import BigFiveChart from "@/components/charts/BigFiveChart";
import { motion } from "framer-motion";
import { Lightbulb, Activity, Target } from "lucide-react";

const bf = [
  { label: "Abertura", value: 0.78 },
  { label: "Consc.", value: 0.64 },
  { label: "Extroversão", value: 0.51 },
  { label: "Amabilidade", value: 0.72 },
  { label: "Neuroticismo", value: 0.35 },
];

export default function Dashboard(){
  return (
    <>
      <section className="grid gap-2">
        <h1 className="text-3xl font-semibold">Visão Geral</h1>
        <p className="text-slate-600">Painel de resultados psicométricos e insights da organização.</p>
      </section>

      <section className="grid sm:grid-cols-3 gap-4">
        <Card>
          <div className="flex items-center justify-between">
            <div>
              <div className="text-sm text-slate-500">Engajamento</div>
              <div className="text-2xl font-semibold">82%</div>
            </div>
            <Activity className="text-lunno.primary"/>
          </div>
        </Card>
        <Card>
          <div className="flex items-center justify-between">
            <div>
              <div className="text-sm text-slate-500">Coesão de Equipe</div>
              <div className="text-2xl font-semibold">0.71</div>
            </div>
            <Target className="text-lunno.primary"/>
          </div>
        </Card>
        <Card>
          <div className="flex items-center justify-between">
            <div>
              <div className="text-sm text-slate-500">Risco de Conflito</div>
              <div className="text-2xl font-semibold">Baixo</div>
            </div>
            <Lightbulb className="text-lunno.primary"/>
          </div>
        </Card>
      </section>

      <section className="grid lg:grid-cols-2 gap-6">
        <Card>
          <div className="flex items-center justify-between mb-2">
            <h2 className="text-xl font-semibold">Big Five</h2>
            <Badge>perfil atual</Badge>
          </div>
          <BigFiveChart data={bf}/>
        </Card>

        <Card>
          <h2 className="text-xl font-semibold mb-2">Insights</h2>
          <ul className="grid gap-2 text-slate-700">
            <li className="p-3 rounded-lg bg-slate-50 border border-slate-200">• Alta Abertura sugere forte potencial criativo e curiosidade intelectual.</li>
            <li className="p-3 rounded-lg bg-slate-50 border border-slate-200">• Conscienciosidade moderada indica confiabilidade com espaço para otimização de rotinas.</li>
            <li className="p-3 rounded-lg bg-slate-50 border border-slate-200">• Baixo Neuroticismo favorece estabilidade emocional e resiliência.</li>
          </ul>
          <div className="mt-4">
            <Button>Ver Relatórios Detalhados</Button>
          </div>
        </Card>
      </section>

      <motion.section
        initial={{opacity:0, y:10}}
        animate={{opacity:1, y:0}}
        transition={{duration:.4}}
        className="grid gap-2"
      >
        <h2 className="text-xl font-semibold">Próximas Ações</h2>
        <div className="grid md:grid-cols-3 gap-3">
          <div className="p-4 border border-slate-200 rounded-xl bg-white">Workshop de feedback estruturado</div>
          <div className="p-4 border border-slate-200 rounded-xl bg-white">Mentorias focadas em liderança empática</div>
          <div className="p-4 border border-slate-200 rounded-xl bg-white">Trilha de inovação com SJT quinzenal</div>
        </div>
      </motion.section>
    </>
  )
}
