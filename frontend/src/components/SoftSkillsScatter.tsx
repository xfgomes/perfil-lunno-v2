import { Scatter } from "react-chartjs-2";
import { Chart, PointElement, LinearScale, Tooltip, Legend } from "chart.js";
Chart.register(PointElement, LinearScale, Tooltip, Legend);

export default function SoftSkillsScatter({skills}:{skills:{potential:Record<string,number>, demonstrated:Record<string,number>}}){
  const labels = Object.keys(skills.potential);
  const points = labels.map(k=>({x: skills.potential[k]||0, y: skills.demonstrated[k]||0, label:k}));
  const data = { datasets:[{ label:"Soft Skills (Potencial x Demonstrado)", data: points as any }] } as any;
  const options = { scales:{ x:{min:0,max:1}, y:{min:0,max:1} }, plugins:{ tooltip:{ callbacks:{ label:(ctx:any)=> `${labels[ctx.dataIndex]}: P=${ctx.parsed.x.toFixed(2)} D=${ctx.parsed.y.toFixed(2)}` }}} } as any;
  return <div className="card"><Scatter data={data} options={options}/></div>
}
