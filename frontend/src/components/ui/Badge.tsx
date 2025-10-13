import { ReactNode } from "react";
export default function Badge({children}:{children:ReactNode}){
  return <span className="app-badge">{children}</span>
}
