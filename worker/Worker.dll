using System;
using Npgsql;
using StackExchange.Redis;

class Worker
{
    static void Main()
    {
        var redis = ConnectionMultiplexer.Connect("redis");
        var db = redis.GetDatabase();

        var conn = new NpgsqlConnection(
            "Host=db;Username=postgres;Password=postgres;Database=postgres"
        );
        conn.Open();

        Console.WriteLine("Worker started...");

        while (true)
        {
            var vote = db.ListLeftPop("votes");

            if (!vote.IsNull)
            {
                using var cmd = new NpgsqlCommand(
                    "INSERT INTO votes(vote) VALUES (@vote)", conn
                );
                cmd.Parameters.AddWithValue("vote", vote.ToString());
                cmd.ExecuteNonQuery();

                Console.WriteLine($"Processed vote: {vote}");
            }
        }
    }
}
