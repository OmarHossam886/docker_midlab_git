const express = require("express");
const { Pool } = require("pg");

const app = express();

const pool = new Pool({
  host: process.env.DB_HOST || "db",
  user: process.env.POSTGRES_USER || "postgres",
  password: process.env.POSTGRES_PASSWORD || "postgres",
  database: process.env.POSTGRES_DB || "postgres",
  port: 5432,
  idleTimeoutMillis: 30000,
  connectionTimeoutMillis: 5000
});

app.get("/", async (req, res) => {
  try {
    const result = await pool.query(
      "SELECT vote, COUNT(*) AS count FROM votes GROUP BY vote"
    );

    let html = "<h2>Voting Results</h2><ul>";
    result.rows.forEach(row => {
      html += `<li>${row.vote}: ${row.count}</li>`;
    });
    html += "</ul>";

    res.send(html);
  } catch (err) {
    console.error("DB error:", err.message);
    res.status(500).send("Database error");
  }
});

app.listen(80, () => {
  console.log("Result service running on port 80");
});
