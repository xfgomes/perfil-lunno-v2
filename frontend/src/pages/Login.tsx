import { useState } from "react";
import { api, setAuth } from "../api";

export default function Login(){
  const [email,setEmail]=useState(""); const [password,setPassword]=useState(""); const [msg,setMsg]=useState("");
  async function submit(e:any){ e.preventDefault();
    try{ const {data}=await api.post("/auth/login",{email,password}); setAuth(data.access_token); setMsg("Logado! Vá para o menu acima."); }
    catch(err:any){ setMsg(err?.response?.data?.error||"Falha"); }
  }
  return (
    <div className="max-w-md mx-auto mt-12 card">
      <h1 className="text-xl font-semibold mb-2">Entrar</h1>
      <form onSubmit={submit} className="grid gap-3">
        <input className="border rounded p-2" placeholder="Email" value={email} onChange={e=>setEmail(e.target.value)} />
        <input type="password" className="border rounded p-2" placeholder="Senha" value={password} onChange={e=>setPassword(e.target.value)} />
        <button className="btn-primary">Entrar</button>
        <p className="text-sm text-gray-600">{msg}</p>
      </form>
    </div>
  )
}
