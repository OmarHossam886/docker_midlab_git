const express = require("express");
const { Pool } = require("pg");

const app = express();

const pool = new Pool({
  host: process.env.DB_HOST || "db",
  user: "postgres",
  password: "postgres",
  database: "postgres"
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
    res.status(500).send("Database error");
  }
});

app.listen(80, () => {
  console.log("Result service running on port 80");
});
