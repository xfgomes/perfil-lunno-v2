import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

type Props = { data: { label: string; value: number }[] }

export default function BigFiveChart({ data }: Props){
  return (
    <div style={{width: "100%", height: 280}}>
      <ResponsiveContainer>
        <BarChart data={data} layout="vertical" margin={{left: 24, right: 24}}>
          <XAxis type="number" domain={[0,1]} hide />
          <YAxis dataKey="label" type="category" width={120} />
          <Tooltip formatter={(v:number)=>Number(v).toFixed(2)} />
          <Bar dataKey="value" radius={[6,6,6,6]} />
        </BarChart>
      </ResponsiveContainer>
    </div>
  )
}
