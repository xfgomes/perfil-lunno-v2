import { Bar } from "react-chartjs-2";
import { Chart, BarElement, CategoryScale, LinearScale, Tooltip, Legend } from "chart.js";
Chart.register(BarElement, CategoryScale, LinearScale, Tooltip, Legend);

export default function BarraBigFive({bf}:{bf:Record<string,number>}){
  const labels = ["Abertura","Consc.","Extroversão","Amabilidade","Neuroticismo"];
  const data = { labels, datasets:[{ label:"Big Five", data:[bf.openness,bf.conscientiousness,bf.extraversion,bf.agreeableness,bf.neuroticism] }]};
  const options = { scales:{ y:{ min:0, max:1 }}} as any;
  return <div className="card"><Bar data={data} options={options}/></div>
}
