import { ReactNode } from "react";
import Navbar from "./Navbar";
import Sidebar from "./Sidebar";

export default function Layout({children}:{children:ReactNode}){
  return (
    <div className="min-h-screen">
      <Navbar/>
      <div className="max-w-7xl mx-auto px-4">
        <div className="grid grid-cols-1 md:grid-cols-[240px_1fr] gap-6 py-6">
          <Sidebar/>
          <main className="grid gap-6">{children}</main>
        </div>
      </div>
    </div>
  )
}
