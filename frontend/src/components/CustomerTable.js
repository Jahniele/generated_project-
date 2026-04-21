import React, { useEffect, useState } from "react";

function CustomerTable() {
  const [customers, setCustomers] = useState([]);
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");

  const load = () => {
    fetch("http://localhost:5000/api/customers/")
      .then(res => res.json())
      .then(data => setCustomers(data));
  };

  useEffect(() => {
    load();
  }, []);

  const add = async () => {
    await fetch("http://localhost:5000/api/customers/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, email })
    });
    load();
  };

  return (
    <div>
      <h3>Customers</h3>

      <input placeholder="name" onChange={e => setName(e.target.value)} />
      <input placeholder="email" onChange={e => setEmail(e.target.value)} />
      <button onClick={add}>Add</button>

      <ul>
        {customers.map(c => (
          <li key={c[0]}>{c[1]} - {c[2]}</li>
        ))}
      </ul>
    </div>
  );
}

export default CustomerTable;
