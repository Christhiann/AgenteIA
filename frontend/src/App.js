import { useState } from "react";
import "./App.css";
import axios from "axios";

function App() {
  const [msg, setMsg] = useState("");
  const [cht, setChat] = useState([]);

  const enviar = async () => {
    if (!msg) return;

    const novaMsg = { tipo: "user", texto: msg };
    setChat([...cht, novaMsg]);

    try {
      const res = await axios.post("http://127.0.0.1:8000/chat", {
        message: msg,
      });

      const resposta = {
        tipo: "bot",
        texto: res.data.response,
      };

      // Corrigido: usar o parâmetro correto do callback
      setChat((prev) => [...prev, resposta]);
    } catch (error) {
      console.error("Erro ao chamar API:", error);
      setChat((prev) => [
        ...prev,
        { tipo: "bot", texto: "Erro ao conectar com a API" },
      ]);
    }

    setMsg("");
  };

  return (
    <div className="container">
      <h1>Chat com IA</h1>

      <div className="chat-box">
        {cht.map((c, i) => (
          <div key={i} className={c.tipo}>
            {c.texto}
          </div>
        ))}
      </div>

      <div className="input-area">
        <input
          value={msg}
          onChange={(e) => setMsg(e.target.value)}
          placeholder="Digite sua mensagem..."
        />
        <button onClick={enviar}>Enviar</button>
      </div>
    </div>
  );
}

export default App;