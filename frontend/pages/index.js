import React, { useState, useEffect } from "react";
import axios from "../services/api";

export default function Home() {
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    axios.get("/transactions").then((res) => setTransactions(res.data));
  }, []);

  return (
    <div>
      <h1>Expense Dashboard</h1>
      <ul>
        {transactions.map((txn, idx) => (
          <li key={idx}>
            {txn.description} - ${txn.amount} ({txn.category})
          </li>
        ))}
      </ul>
    </div>
  );
}
