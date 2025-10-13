import { Radar } from "react-chartjs-2";
import { Chart, RadialLinearScale, PointElement, LineElement, Filler, Tooltip, Legend } from "chart.js";
Chart.register(RadialLinearScale, PointElement, LineElement, Filler, Tooltip, Legend);

export default function RadarDISC({disc}:{disc:{dominance:number;influence:number;steadiness:number;conformity:number}}){
  const data = { labels:["Dominância","Influência","Estabilidade","Conformidade"], datasets:[{ label:"DISC", data:[disc.dominance,disc.influence,disc.steadiness,disc.conformity], fill:true }]};
  const options = { scales:{ r:{ min:0, max:1 }}} as any;
  return <div className="card"><Radar data={data} options={options}/></div>
}
