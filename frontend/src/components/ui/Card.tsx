import { ReactNode } from "react";
export default function Card({children}:{children:ReactNode}){
  return <div className="app-card">{children}</div>
}
