using System;
using Npgsql;
using StackExchange.Redis;

class Program
{
    static void Main()
    {
        Console.WriteLine("Worker service started...");

        var redis = ConnectionMultiplexer.Connect("redis");
        var db = redis.GetDatabase();

        using var conn = new NpgsqlConnection(
            "Host=db;Username=postgres;Password=postgres;Database=postgres"
        );

        conn.Open();
        Console.WriteLine("Connected to PostgreSQL");

        while (true)
        {
            var vote = db.ListLeftPop("votes");
            if (vote.HasValue)
            {
                Console.WriteLine($"Processing vote: {vote}");
            }

            System.Threading.Thread.Sleep(1000);
        }
    }
}
