import { useState } from "react";
import "./App.css";
import axios from "axios";

function App() {
  const [msg, setMsg] = useState("");
  const [chat, setChat] = useState([]);
  const [loading, setLoading] = useState(false);

  const enviar = async () => {
    if (!msg.trim()) return;

    const novaMsg = { tipo: "user", texto: msg };
    setChat((prev) => [...prev, novaMsg]);
    setMsg("");
    setLoading(true);

    try {
      const res = await axios.post("http://127.0.0.1:8000/chat", {
        message: msg,
      });

      const resposta = {
        tipo: "bot",
        texto: res.data.response,
      };

      setChat((prev) => [...prev, resposta]);
    } catch (error) {
      console.error("Erro ao chamar API:", error);
      setChat((prev) => [
        ...prev,
        { tipo: "bot", texto: "❌ Erro ao conectar com a API" },
      ]);
    }

    setLoading(false);
  };

  return (
    <div className="container">
      <h1 className="title">🤖 Assistente IA</h1>

      <div className="chat-box">
        {chat.length === 0 && (
          <div className="empty">
            💬 Comece uma conversa com sua IA
          </div>
        )}

        {chat.map((c, i) => (
          <div
            key={i}
            className={`message ${c.tipo === "user" ? "user" : "bot"}`}
          >
            {c.texto}
          </div>
        ))}

        {loading && (
          <div className="message bot typing">
            <span></span>
            <span></span>
            <span></span>
          </div>
        )}
      </div>

      <div className="input-area">
        <input
          value={msg}
          onChange={(e) => setMsg(e.target.value)}
          placeholder="Digite sua mensagem..."
          onKeyDown={(e) => e.key === "Enter" && enviar()}
        />
        <button onClick={enviar}>Enviar</button>
      </div>
    </div>
  );
}

export default App;