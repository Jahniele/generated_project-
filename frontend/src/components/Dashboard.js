import React, { useEffect, useState } from "react";
import CustomerTable from "./CustomerTable";

function Dashboard({ user }) {
  const [stats, setStats] = useState({});

  useEffect(() => {
    fetch("http://localhost:5000/api/dashboard/")
      .then(res => res.json())
      .then(data => setStats(data));
  }, []);

  return (
    <div>
      <h1>Welcome {user}</h1>

      <h3>Stats</h3>
      <p>Users: {stats.users}</p>
      <p>Customers: {stats.customers}</p>

      <CustomerTable />
    </div>
  );
}

export default Dashboard;
