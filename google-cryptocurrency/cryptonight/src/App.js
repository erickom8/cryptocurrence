import { useEffect, useState } from "react";
import "./App.css";

export default function App() {
  const [message, setMessage] = useState("");
  const [coins, setCoins] = useState([]);

  useEffect(() => {
    fetch("https://seu-backend.onrender.com/")
      .then((res) => res.json())
      .then((data) => {
        setMessage(data.message);
        setCoins(data.available_coins);
      })
      .catch((err) => console.error("Erro ao buscar API:", err));
  }, []);

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 p-4">
      <h1 className="text-2xl font-bold mb-4">{message}</h1>
      <h2 className="text-lg font-semibold">Moedas disponíveis:</h2>
      <ul className="mt-2">
        {coins.map((coin, index) => (
          <li key={index} className="text-blue-600">{coin}</li>
        ))}
      </ul>
    </div>
  );
}
